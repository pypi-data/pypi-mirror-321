import datetime
import os
import json
import re
import subprocess
import time
import warnings

import requests

from concurrent.futures import ThreadPoolExecutor
from typing import List, Dict, Iterable
from difflib import SequenceMatcher

from bs4 import BeautifulSoup, XMLParsedAsHTMLWarning
from colorama import just_fix_windows_console
from tqdm import tqdm

from .utils import (CACHE_DIR, ACCESS_TOKEN_DIR, CLIENT_ID, CLIENT_SECRET, CLIENT_INFO, AVAILABLE_CLIENTS,
                    YOUTUBE_HEADERS, LOWEST_KEYWORDS, LOW_KEYWORDS, MEDIUM_KEYWORDS, HIGH_KEYWORDS,
                    _format_date, _format_views, format_seconds, formatted_to_seconds, _format_title,
                    _get_chapters, _get_channel_picture, _is_valid_yt_url, _convert_captions, _send_warning_message,
                    _send_info_message, _send_success_message, _process_error, _from_short_number, _combine_av,
                    _filter_numbers, _is_url, VIDEO_EXTS_DOTTED, _send_error_message, BAR_COLOR, DEFAULT_THREADS)
from .out_colors import _dim_cyan


warnings.filterwarnings('ignore', category=XMLParsedAsHTMLWarning)
just_fix_windows_console()


class Video:
    """
    Get data from a YouTube video.

    Attributes
    ----------
    query: str
        A YouTube URL or query to search for.
        To get multiple video data for a query, use the `Search` class instead.
    kwargs: dict (Default parameters)
        get_duration_formatted: bool (True) - Retrieve the duration of the video formatted as HH:MM:SS instead of seconds.
        get_channel_picture: bool (True) - Retrieve the channel picture (slow down by ~0.3s)
        get_thumbnail: bool (True) - Retrieve the thumbnail.
        thumbnail_quality: str ("best") - Quality of the thumbnail to retrieve ("best", "high", "med", "low")
        get_subtitles: bool (True) - Retrieve the subtitles of the video.
        get_chapters: bool (True) - Retrieve the chapters of the video.
        get_stream: bool (True) - Retrieve the stream url.
        get_date: bool (True) - Retrieve publish and upload date.
        get_date_formatted: bool (True) - Format the date to be more readable.
        date_format: str ("eu") - Way to format the date ("eu", "us", "sql", "unix")
        use_login: bool (False) - Login into an account.
        disable_cache: bool (False) - Disable auth cache. Needs login everytime instead.
        ignore_errors: bool (False) - In case of error (not fatal), proceed anyways.
        ignore_warnings: bool (False) - Don't print warnings on screen.
        verbose: bool (True) - Show information/warnings on screen.
        no_retry: bool (False) - Disable retries in case extraction/download fails with the set client.
        client: str ("android_embed") - Client to use. ("android_embed", "android_music", "tv_embed", "ios", "android", "android_creator", "web", "ios_embed")
        ignore_fallback: bool (True) - If innertube fails, ignore 'request' fallback.

    Methods
    -------
    download(path: str = ".", quality: str = "best", keep: bool = False, only_audio: bool = False,
             only_video: bool = False, target_fps: int = -1, target_itag: int = -1, live_duration: int = 10,
             thumbnail: bool = False, preferred_video_format: str = "mp4", preferred_audio_format: str = "mp3",
             overwrite: bool = True, chunk_size: int = 1024*1024, force_ffmpeg: bool = False)
        Downloads an appropriate video/audio stream.

        path: str - Output path.
        quality: str - Quality of the stream (by bitrate): "best", "high", "med", "low", "lowest".
        keep: bool - Keep the audio and video files (in case they exist).
        only_audio: bool - Gets a stream with only audio data.
        only_video: bool - Gets a stream with only video data.
        target_fps: int - Target fps of the video, preferred over bitrate.
        target_itag: int - Target itag of the stream to download.
        live_duration: int - When downloading a livestream, the amount of seconds it should download from now.
        thumbnail: bool - Also download the thumbnail of the video.
        preferred_video_format: str - Video format to download into.
        preferred_audio_format: str - Audio format to download into (for only_audio=True).
        overwrite: bool - Overwrite already existing files.
        chunk_size: int - Stream download chunk size.
        force_ffmpeg: bool - Force the conversion to bytes to be made using ffmpeg, use it for format conversion.
    """
    def __init__(self, query, **kwargs):
        """Make a Video class.

        :param str query:
            A YouTube URL or query to search for.
        :param dict kwargs:
            Extra arguments to parse. Use help(Video) for more info.
        """
        parameters = {
            "get_duration_formatted": True,
            "get_channel_picture": False,
            "get_thumbnail": True,
            "thumbnail_quality": "best",
            "max_comments": 60,
            "get_views_formatted": False,
            "get_subtitles": True,
            "get_chapters": True,
            "get_stream": True,
            "get_date": True,
            "get_date_formatted": True,
            "date_format": "eu",
            "use_login": False,
            "disable_cache": False,
            "ignore_errors": False,
            "ignore_warnings": False,
            "verbose": False,
            "no_retry": False,
            "audio_stream_url": False,
            "client": AVAILABLE_CLIENTS[0],
            "ignore_fallback": True
        }
        invalid_params = []
        for param in kwargs:
            if param not in parameters:
                invalid_params.append(param)
        parameters.update(kwargs)

        self._ignore_errors = parameters.get("ignore_errors")
        self._ignore_warnings = parameters.get("ignore_warnings")
        self._verbose = parameters.get("verbose")
        self._no_retry = parameters.get("no_retry")
        self._ignore_fallback = parameters.get("ignore_fallback")
        self._clients_used = set()
        self._change_client(client=parameters.get("client").lower(), headers=None)
        if invalid_params:
            _send_warning_message(f"The following parameters aren't valid: {', '.join(invalid_params)}", self._ignore_warnings)

        if not query:
            _process_error(er_type="noquery", data={'is_fatal': True},
                           ignore_errors=self._ignore_errors, ignore_warnings=self._ignore_warnings)
        self._query = query.strip()

        self._use_login = parameters.get("use_login")
        self._disable_cache = parameters.get("disable_cache")
        access_token = None
        if parameters.get("use_login"):
            access_token = self._get_token()
        self._headers = self._get_headers(access_token=access_token)

        is_valid_url = _is_valid_yt_url(self._query)

        self.video_id = self._search_query() if is_valid_url[1] is None else is_valid_url[1]
        if self.video_id is None:
            _process_error(er_type="search", data={'query': query, 'is_fatal': True},
                           ignore_errors=self._ignore_errors, ignore_warnings=self._ignore_warnings)
        elif not self.video_id:
            self.url = self._query
        else:
            self.url = "https://www.youtube.com/watch?v="+self.video_id
        self.json = self._extract_video_info()

        if not self.json:
            _process_error(er_type="extract",
                           data={'url': self._query, 'extract_type': 'video info', 'is_fatal': False,
                                 'reason': "Couldn't get json data",
                                 'message': f"Couldn't get json data for {self._query}"},
                           ignore_errors=self._ignore_errors, ignore_warnings=self._ignore_warnings)

        self._max_comments = parameters.get("max_comments", 60)
        self._params = parameters
        self._get_data()

    def _get_data(self):
        parameters = self._params
        couldnt_extract = []
        self.video_info = self.json.get('videoDetails', {})
        if not self.video_info:
            _process_error(er_type="extract",
                                data={'url': self.url, 'reason': '',
                                      'extract_type': 'video details (title, length, ...)',
                                      'message': f"Couldn't extract video details (title, length, ...) for {self.url}",
                                      'is_fatal': False},
                           ignore_errors=self._ignore_errors, ignore_warnings=self._ignore_warnings)
        self.streaming_data = self.json.get('streamingData', {})
        if not self.streaming_data:
            _process_error(er_type="extract",
                                data={'url': self.url, 'reason': '', 'extract_type': 'streaming data',
                                      'message': f"Couldn't extract streaming data for {self.url}", 'is_fatal': False},
                           ignore_errors=self._ignore_errors, ignore_warnings=self._ignore_warnings)
        self.playability_status = self.json.get('playabilityStatus', {})
        if not self.playability_status:
            couldnt_extract.append('playability status')
        _captions = self.json.get('captions', {})
        if not _captions:
            couldnt_extract.append('captions data')
            self._captions_data = {}
        else:
            self._captions_data = _captions.get('playerCaptionsTracklistRenderer', {})
            if not self._captions_data:
                couldnt_extract.append('captions data')
        self._response_context = self.json.get('responseContext', {})
        if not self._response_context:
            couldnt_extract.append('response context')
        self._playback_tracking = self.json.get('playbackTracking', {})
        if not self._playback_tracking:
            couldnt_extract.append('playback tracking')
        self._tracking_params = self.json.get('trackingParams', {})
        if not self._tracking_params:
            couldnt_extract.append('tracking params')
        self._annotations = self.json.get('annotations', {})
        if not self._annotations:
            couldnt_extract.append('annotations')
        self._player_config = self.json.get('playerConfig', {})
        if not self._player_config:
            couldnt_extract.append('player config')
        self._storyboards = self.json.get('storyboards', {})
        if not self._storyboards:
            couldnt_extract.append('storyboards')
        self._microformat = self.json.get('microformat', {})
        if not self._microformat:
            couldnt_extract.append('microformat')
        self._cards = self.json.get('cards', {})
        if not self._cards:
            couldnt_extract.append('cards')
        self._attestation = self.json.get('attestation', {})
        if not self._attestation:
            couldnt_extract.append('attestation')
        self._messages = self.json.get('messages', {})
        if not self._messages:
            couldnt_extract.append('messages')
        self._endscreen = self.json.get('endscreen', {})
        if not self._endscreen:
            couldnt_extract.append('endscreen')
        self._ad_placements = self.json.get('adPlacements', {})
        if not self._ad_placements:
            couldnt_extract.append('ad placements')
        self._ad_breakheartbeat = self.json.get('adBreakHeartbeatParams', {})
        if not self._ad_breakheartbeat:
            couldnt_extract.append('ad break heartbeat params')
        self._framework_updates = self.json.get('frameworkUpdates', {})
        if not self._framework_updates:
            couldnt_extract.append('framework updates')
        if couldnt_extract:
            _send_warning_message(f"Couldn't extract {', '.join(couldnt_extract)} for {self.url}", self._ignore_warnings)

        # vid info
        self.title = self.video_info.get('title')
        self._duration = int(self.video_info.get('lengthSeconds', '0'))
        self.duration = format_seconds(self._duration) if parameters.get("get_duration_formatted") else self._duration
        self.keywords = self.video_info.get('keywords')
        self.channel_id = self.video_info.get('channelId')
        self.channel = self.video_info.get('author')
        self.channel_url = "https://www.youtube.com/channel/" + self.channel_id if self.channel_id else None
        self.channel_picture = _get_channel_picture(self.channel_url) if self.channel_url and parameters.get("get_channel_picture") else None
        self.description = self.video_info.get('shortDescription')
        self.chapters = _get_chapters(self.description) if self.description and parameters.get("get_chapters") else None
        self.thumbnails, self.thumbnail, self.thumbnail_data = None, None, None
        if parameters.get("get_thumbnail"):
            tq = parameters.get("thumbnail_quality").lower()
            self.thumbnails = sorted(self.video_info.get('thumbnail', {}).get('thumbnails', {}), key=lambda x: x.get('width', 0), reverse=True)
            if self.thumbnails:
                if tq in HIGH_KEYWORDS:
                    self.thumbnail_data = self.thumbnails[1] if len(self.thumbnails) > 1 else self.thumbnails[-1]
                elif tq in MEDIUM_KEYWORDS:
                    self.thumbnail_data = self.thumbnails[2] if len(self.thumbnails) > 2 else self.thumbnails[-1]
                elif tq in LOW_KEYWORDS | LOWEST_KEYWORDS:
                    self.thumbnail_data = self.thumbnails[-1]
                else:
                    self.thumbnail_data = self.thumbnails[0]
                self.thumbnail = self.thumbnail_data.get('url')
        views = int(_filter_numbers(self.video_info.get('viewCount', '-1')))
        self.views = _format_views(str(views)) if parameters.get("get_views_formatted") else views
        self.is_live = bool(self.video_info.get('isLive', False))
        self.was_live = bool(self.video_info.get('isLiveContent', False))
        self.streams = None
        self.stream_url = None
        if parameters.get("get_stream"):
            self.stream_url = self._get_stream(only_audio=parameters.get("audio_stream_url")).get('url') if not self.is_live else self._get_stream(_hls=True)
        if parameters.get("get_date"):
            pd = self._microformat.get('playerMicroformatRenderer', {}).get('publishDate')
            ud = self._microformat.get('playerMicroformatRenderer', {}).get('uploadDate')
        else:
            pd, ud = None, None
        date_format = parameters.get("date_format").lower()
        self.publish_date = _format_date(pd, date_format) if pd and parameters.get('get_date_formatted') else pd
        self.upload_date = _format_date(ud, date_format) if ud and parameters.get('get_date_formatted') else ud

        # captions info
        self.subtitles = []
        if parameters.get("get_subtitles"):
            captions_data = self._captions_data.get('captionTracks')
            if captions_data:
                for caption in captions_data:
                    url, language, language_code = caption.get('baseUrl'), caption.get('name'), caption.get(
                        'languageCode')
                    self.subtitles.append({
                        'captions': _convert_captions(url),
                        'language': language.get('simpleText'),
                        'languageCode': language_code
                    })

    def download(self, path: str = ".", quality: str = "best", keep: bool = False, only_audio: bool = False,
                 only_video: bool = False, target_fps: int = -1, target_itag: int = -1, live_duration: int = 10,
                 thumbnail: bool = False, preferred_video_format: str = "mp4", preferred_audio_format: str = "mp3",
                 overwrite: bool = True, chunk_size: int = 1024*1024, force_ffmpeg: bool = False, **kwargs):
        """
        Downloads an appropriate video/audio stream.

        :param str path: Output path. Defaults to the current directory.
        :param str quality: Quality of the stream (by bitrate): "best", "high", "med", "low", "lowest". Defaults to "best".
        :param bool keep: Keep the audio and video files (in case they exist). Defaults to False.
        :param bool only_audio: Gets a stream with only audio data. Defaults to False.
        :param bool only_video: Gets a stream with only video data. Defaults to False.
        :param int target_fps: Target fps of the video, preferred over bitrate. Defaults to -1 (ignore fps, order by bitrate).
        :param int target_itag: Target itag of the stream to download. Defaults to -1 (no specific itag).
        :param int live_duration: When downloading a livestream, the amount of seconds it should download from now. Defaults to 10.
        :param bool thumbnail: Also download the thumbnail of the video. Defaults to False.
        :param str preferred_video_format: Video format to download into. Defaults to "mp4".
        :param str preferred_audio_format: Audio format to download into (for only_audio=True). Defaults to "mp3".
        :param bool overwrite: Overwrite already existing files. Defaults to True.
        :param int chunk_size: Size of the chunks to download. Increase if you're experiencing low speeds, decrease if you want to limit. Defaults to 1024*1024.
        :param bool force_ffmpeg: Force the conversion to bytes to be made using ffmpeg, use it in case of corrupt files. Defaults to False.
        """

        _show_bar = kwargs.get('_show_bar', True)
        _raw_number = kwargs.get('_raw_number', 0)

        dir_path = os.path.abspath(path)
        if not os.path.exists(dir_path):
            os.makedirs(dir_path)
        download_title = _format_title(self.title) if self.title else "download"
        output_path = os.path.join(path, download_title)
        now = datetime.datetime.now().strftime("_%Y-%m-%d_%H-%M-%S_")

        if thumbnail:
            self.download_thumbnail(path=path, overwrite=overwrite, _now=now)

        if self.is_live:
            _send_info_message(f"Downloading {format_seconds(live_duration)} of livestream through hls url", verbose=self._verbose)
            download_path = os.path.join(dir_path, download_title + now + "." + preferred_video_format)
            if _show_bar:
                command = ['ffmpeg', '-progress', '-', '-nostats', '-y', '-i', self.stream_url, '-bsf:a',
                           'aac_adtstoasc', '-vcodec', 'copy', '-c', 'copy', '-crf', '-50', '-t', str(live_duration),
                           download_path]
                with tqdm(desc="Downloading", unit="frames", colour=BAR_COLOR) as pbar:
                    process = subprocess.Popen(command, universal_newlines=True, stderr=subprocess.DEVNULL, stdout=subprocess.PIPE)

                    for lines in iter(process.stdout.readline, ''):
                        for line in lines.split("\n"):
                            line = line.strip()
                            if "frame=" in line:
                                frames = int(float(line.split("=")[1]))
                                pbar.update(abs(pbar.last_print_n-frames))
                                break
            else:
                command = ['ffmpeg', '-loglevel', 'error', '-hide_banner', '-y', '-i', self.stream_url, '-bsf:a',
                           'aac_adtstoasc', '-vcodec', 'copy', '-c', 'copy', '-crf', '-50', '-t', str(live_duration),
                           download_path]
                subprocess.run(command)
            _send_success_message(f"Successfully downloaded `{self.title}` into `{dir_path}`.", verbose=self._verbose)
            return

        check = True
        while check:
            stream = self._get_stream(quality=quality, only_audio=only_audio, only_video=only_video,
                                      target_fps=target_fps, itag=target_itag)
            download_url = stream.get('url')
            response = requests.get(download_url, stream=True, headers=self._headers)
            status = response.status_code

            if status == 200 or self._no_retry:
                break
            else:
                check = self._change_client()
                self.json = self._extract_video_info(silent=True, skip_on_error=True)
                self._get_data()

        if status == 403:
            _process_error(er_type="forbidden", data={'url': self.url, 'is_fatal': False,
                                                      'message': f"Couldn't download '{self.url}' - "
                                                                 f"HTTP <403> Forbidden - You might have reached a "
                                                                 f"ratelimit, try again later or try use_login=False."},
                           ignore_errors=self._ignore_errors, ignore_warnings=self._ignore_warnings)
            return
        elif status != 200:
            _process_error(er_type="download", data={'url': self.url, 'is_fatal': False,
                                         'reason': f'Unsuccessful request - Code <{status}> | {response.reason}'},
                           ignore_errors=self._ignore_errors, ignore_warnings=self._ignore_warnings)
            return
        elif not download_url:
            _process_error(er_type="download", data={'url': self.url, 'is_fatal': False,
                                                     'reason': f"Couldn't find stream url",
                                                     'message': f"Couldn't find stream url for '{self.url}'."},
                           ignore_errors=self._ignore_errors, ignore_warnings=self._ignore_warnings)
            return

        itags = [str(stream.get('itag'))]
        exts = [preferred_audio_format if only_audio else preferred_video_format]
        stream_urls = [download_url]
        total_sizes = [int(response.headers.get('content-length', 0))]
        if not only_video and not only_audio and itags[0] not in {'18', '22'}:
            audio_stream = self._get_stream(quality=quality, only_audio=True, only_video=False, itag=target_itag)
            video_stream = self._get_stream(quality=quality, only_audio=False, only_video=True, target_fps=target_fps, itag=target_itag)
            itags = ["a:"+str(audio_stream.get('itag')), "v:"+str(video_stream.get('itag'))]
            exts = [preferred_audio_format, preferred_video_format]
            stream_urls = [audio_stream.get('url'), video_stream.get('url')]

            audio_response = requests.get(stream_urls[0], stream=True, headers=self._headers)
            video_response = requests.get(stream_urls[1], stream=True, headers=self._headers)

            total_sizes = [int(audio_response.headers.get('content-length', 0)),
                           int(video_response.headers.get('content-length', 0))]

        if os.path.exists(output_path + "." + exts[0]) and overwrite and len(stream_urls) == 1:
            _send_info_message(f"File for `{self.title}` already exists and `overwrite` is enabled, skipping...", self._verbose)
            return

        pl = 's' if len(itags) > 1 else ''
        _send_info_message(f"Downloading stream{pl} - itag{pl}: {'+'.join(itags)}", verbose=self._verbose)
        if len(stream_urls) > 1:
            raw_paths = [os.path.join(path, f"temp_{_raw_number}_{preferred_audio_format}_{itags[0].replace(':', '')}.raw"),
                         os.path.join(path, f"temp_{_raw_number}_{preferred_video_format}_{itags[1].replace(':', '')}.raw")]
        else:
            raw_paths = [os.path.join(path, f"temp_{_raw_number}.raw")]

        data_to_download = []
        for d in zip(stream_urls, exts, itags, total_sizes):
            data_to_download.append((d[0], d[1], d[2], d[3]))

        self._download_streams(download_urls=data_to_download, chunk_size=chunk_size, raw_paths=raw_paths,
                               output_path=output_path, force_ffmpeg=force_ffmpeg, show_bar=_show_bar,
                               _now=now)

        if len(stream_urls) > 1:
            exts2 = [itags[0].replace(":", "")+".", itags[1].replace(":", "")+"."]
            out = output_path+"."+exts[1] if overwrite else output_path+now+"."+exts[1]
            _combine_av(output_path+now+exts2[0]+exts[0], output_path+now+exts2[1]+exts[1], out, verbose=self._verbose)
            if not keep:
                if os.path.exists(output_path+now+exts2[0]+exts[0]):
                    os.remove(output_path+now+exts2[0]+exts[0])
                if os.path.exists(output_path+now+exts2[1]+exts[1]):
                    os.remove(output_path+now+exts2[1]+exts[1])

            _send_success_message(f"Merged audio (itag: {audio_stream.get('itag')}) and video (itag: {video_stream.get('itag')}).", self._verbose)
        else:
            try:
                ffmpeg_str = "_ffmpeg_" if force_ffmpeg else ""
                os.rename(output_path + now + ffmpeg_str + itags[0] + "." + exts[0], output_path + "." + exts[0])
            except:
                pass

        _send_success_message(f"Successfully downloaded `{self.title}` into `{dir_path}`.", verbose=self._verbose)

    def download_thumbnail(self, path: str = ".", image_format: str = "png", overwrite: bool = True, **kwargs):
        if not self.thumbnail_data or not self.thumbnail:
            _process_error(er_type="download", data={'url': self.url, 'is_fatal': False,
                                                     'reason': f"Couldn't find thumbnail data",
                                                     'message': f"Couldn't find thumbnail data for '{self.url}'."},
                           ignore_errors=self._ignore_errors, ignore_warnings=self._ignore_warnings)
            return

        _now = kwargs.get('_now')

        dir_path = os.path.abspath(path)
        download_title = _format_title(self.title) if self.title else "thumbnail"
        size = f"_{self.thumbnail_data.get('width', 0)}x{self.thumbnail_data.get('height', 0)}"
        img_path = os.path.join(dir_path, download_title + size + "." + image_format)
        if os.path.exists(img_path):
            if overwrite:
                _send_info_message(f"Thumbnail file for `{self.title}` already exists and `overwrite` is enabled, skipping...", self._verbose)
                return
            else:
                if _now is None:
                    _now = datetime.datetime.now().strftime("_%Y-%m-%d_%H-%M-%S")
                img_path = os.path.join(dir_path, download_title + size + _now + "." + image_format)
        with open(img_path, "wb") as f:
            f.write(requests.get(self.thumbnail).content)

    def _download_streams(self, download_urls, chunk_size, raw_paths, output_path, force_ffmpeg=False, show_bar=True,
                          _now=''):
        def _download_chunk(url, start, end, session, pbar):
            response_content = session.get(url, headers={'Range': f'bytes={start}-{end}'}, stream=True).content
            if pbar: pbar.update(len(response_content))
            return start, response_content

        i = 0
        for download_url, ext, ext2, total_size in download_urls:
            with open(raw_paths[i], 'wb') as f:
                f.truncate(total_size)

            ranges = [(i, min(i + chunk_size - 1, total_size - 1)) for i in range(0, total_size, chunk_size)]
            pbar = tqdm(total=total_size, unit='B', unit_scale=True, desc="Downloading", colour=BAR_COLOR) if show_bar else None
            with ThreadPoolExecutor(max_workers=8) as executor:
                with requests.Session() as session:
                    futures = [executor.submit(_download_chunk, download_url, start, end, session, pbar) for start, end in ranges]
                    downloaded_data = [future.result() for future in futures]

            self._save_to_file(output_path=output_path, ext=ext, ext2=ext2.replace(":", "")+".", raw_path=raw_paths[i],
                               stream_data=downloaded_data, force_ffmpeg=force_ffmpeg, _now=_now)

            i += 1

    def _save_to_file(self, output_path, ext, ext2='', raw_path=None, stream_data=None, force_ffmpeg=False, _now=''):
        with open(output_path + _now + ext2 + ext, 'wb') as f:
            for start, content in stream_data:
                f.seek(start)
                f.write(content)
        if force_ffmpeg:
            try:
                subprocess.run(['ffmpeg', '-y', '-i', output_path + _now + ext2 + ext, output_path + _now + "_ffmpeg_" + ext2 + ext])
                os.remove(output_path + _now + ext2 + ext)
            except Exception as e:
                _process_error(er_type="generic", data={'url': self.url, 'is_fatal': False, 'error': e,
                                                        'message': f"Error for '{self.url}' - {e}."},
                               ignore_errors=self._ignore_errors, ignore_warnings=self._ignore_warnings)

        if os.path.exists(raw_path):
            os.remove(raw_path)

    def _get_stream(self, quality="best", only_audio=False, only_video=False, target_fps=-1, itag=-1, _hls=False):

        video_formats = audio_formats = ["mp4", "webm"]
        self.streams = streams = self._get_streams()
        if not streams:
            _process_error(er_type='download',
                                data={'url': self.url, 'reason': "No streams available", 'is_fatal': False,
                                      'message': f'No streams available for {self.url}'},
                           ignore_errors=self._ignore_errors, ignore_warnings=self._ignore_warnings)
            return {}
        formats = streams.get('adaptiveFormats') if only_audio or only_video else streams.get('formats')

        if not formats:
            formats = streams.get('adaptiveFormats')
            if not formats:
                st_url = {'url': streams.get('hlsUrl')}
                if st_url.get('url'): return st_url
                _process_error(er_type='download',
                                    data={'url': self.url, 'reason': "Couldn't get formats",
                                          'is_fatal': False, 'message': f"Couldn't get formats for {self.url}"},
                               ignore_errors=self._ignore_errors, ignore_warnings=self._ignore_warnings)
                return {}
        streams_sorted = sorted(formats, key=lambda x: x['bitrate'], reverse=True)

        download_stream = None
        filtered_streams = []
        #excluded_video_itags = {140, 137, 136, 135, 134, 133, 160}
        excluded_video_itags = {}
        excluded_audio_itags = {}
        if _hls:
            return self.streams.get('hlsUrl')
        if itag < 0:
            if only_audio:
                audio_formats = ["audio/" + ext for ext in audio_formats]
                for stream in streams_sorted:
                    mtype = stream.get('mimeType')
                    if not mtype or not mtype.split("; ")[0] in audio_formats or stream.get('itag') in excluded_audio_itags: continue
                    filtered_streams.append(stream)
            else:
                if target_fps and target_fps > 0:
                    streams_sorted = sorted(formats, key=lambda x: (x['fps'] if 'fps' in x else 0, x['bitrate']),
                                            reverse=True)
                video_formats = ["video/" + ext for ext in video_formats]
                fps_set = set()
                for stream in streams_sorted:
                    mtype = stream.get('mimeType')
                    if not mtype or not mtype.split("; ")[0] in video_formats or stream.get('itag') in excluded_video_itags: continue
                    filtered_streams.append(stream)
                    fps_set.add(stream.get('fps'))
                if not filtered_streams:
                    _process_error(er_type='download',
                                   data={'url': self.url, 'reason': "Couldn't get formats",
                                         'is_fatal': False, 'message': f"Couldn't get formats for {self.url}"},
                                   ignore_errors=self._ignore_errors, ignore_warnings=self._ignore_warnings)
                    return {}
                fps = min(fps_set, key=lambda x: abs(x - target_fps))
            stream_index = 0
            formats_length = len(filtered_streams) - 1
            if quality in LOWEST_KEYWORDS:
                stream_index = -1
                if target_fps and target_fps > 0:
                    for i, stream in enumerate(filtered_streams.__reversed__()):
                        stream_fps = stream.get('fps')
                        if not stream_fps:
                            continue
                        if stream_fps == fps:
                            stream_index = i - 1
            elif quality in LOW_KEYWORDS:
                stream_index = formats_length // 4
            elif quality in MEDIUM_KEYWORDS:
                stream_index = formats_length // 2
            elif quality in HIGH_KEYWORDS:
                stream_index = 3 * formats_length // 4
            else:
                if target_fps and target_fps > 0:
                    for i, stream in enumerate(filtered_streams):
                        stream_fps = stream.get('fps')
                        if not stream_fps:
                            continue
                        if stream_fps == fps:
                            stream_index = i - 1
            download_stream = filtered_streams[stream_index]
        else:
            for stream in streams_sorted:
                if stream.get('itag') == itag:
                    download_stream = stream
                    break
            if not download_stream:
                download_stream = streams_sorted[0]
        if not download_stream:
            _process_error(er_type='download',
                                data={'url': self.url, 'reason': "Couldn't get stream",
                                      'is_fatal': False, 'message': f"Couldn't get stream for {self.url}"},
                           ignore_errors=self._ignore_errors, ignore_warnings=self._ignore_warnings)
            return {}
        return download_stream

    def _get_streams(self):
        format_info = {
            'formats': [],
            'adaptiveFormats': [],
            'dashUrl': None,
            'hlsUrl': None
        }

        formats = self.streaming_data.get('formats')
        if formats:
            for format in formats:
                if not format.get('url'):
                    continue
                format_info['formats'].append(format)
        adaptive_formats = self.streaming_data.get('adaptiveFormats')
        if adaptive_formats:
            for format in adaptive_formats:
                if not format.get('url'):
                    continue
                format_info['adaptiveFormats'].append(format)
        dash_url = self.streaming_data.get('dashManifestUrl')
        if dash_url:
            format_info['dashUrl'] = dash_url
        hls_url = self.streaming_data.get('hlsManifestUrl')
        if hls_url:
            format_info['hlsUrl'] = hls_url

        return format_info

    def _get_headers(self, access_token):
        headers = YOUTUBE_HEADERS.copy()
        if self._use_login:
            headers.update({
                'Authorization': f'Bearer {access_token}'
            })
        return headers

    def _get_token(self):
        if not self._disable_cache and os.path.exists(ACCESS_TOKEN_DIR):
            with open(ACCESS_TOKEN_DIR, 'r') as f:
                access_token = json.load(f).get('access_token')
            return access_token

        response = requests.post('https://oauth2.googleapis.com/device/code',
                                 data={'client_id': CLIENT_ID,'scope': 'https://www.googleapis.com/auth/youtube'})

        response_data = response.json()
        _send_info_message("Logging in...", True)
        _send_info_message(f"Open {response_data.get('verification_url')} and use the code {response_data.get('user_code')}", True)
        input(_dim_cyan("[INFO]: Press enter when completed."))

        response = requests.post('https://oauth2.googleapis.com/token',
            data={'client_id': CLIENT_ID, 'client_secret': CLIENT_SECRET, 'device_code': response_data['device_code'], 'grant_type': 'urn:ietf:params:oauth:grant-type:device_code'})
        response_data = response.json()

        return self._write_cache(response_data['access_token'])

    def _write_cache(self, token):
        if not self._disable_cache:
            if not os.path.exists(CACHE_DIR):
                os.mkdir(CACHE_DIR)
            with open(ACCESS_TOKEN_DIR, 'w') as f:
                json.dump({'access_token': token}, f)
        return token

    def _change_client(self, client=None, headers={}):
        if client and not client in self._clients_used:
            self._client = client
        else:
            self._client = None
            for _client in AVAILABLE_CLIENTS:
                if _client not in self._clients_used:
                    self._client = _client
                    break
            if not self._client:
                return False
        self._client_info = CLIENT_INFO[self._client].copy()
        if headers is None:
            self._headers = {}
        self._headers.update(self._client_info['headers'].copy())
        self._clients_used.add(self._client)
        return True

    def _search_query(self):
        url = "https://www.youtube.com/results?search_query=" + self._query.replace(" ", "+")
        html = requests.get(url, headers=self._headers).text

        soup = BeautifulSoup(html, 'html.parser')
        script_tag = soup.find('script', string=re.compile(r'var ytInitialData'))
        if not script_tag:
            return

        try:
            json_text = re.search(r'var ytInitialData = ({.*?});', script_tag.string, re.DOTALL).group(1)
        except:
            _process_error(er_type="search", data={'query': self._query, 'is_fatal': True},
                           ignore_errors=self._ignore_errors, ignore_warnings=self._ignore_warnings)

        keys = ['contents', 'twoColumnSearchResultsRenderer', 'primaryContents', 'sectionListRenderer', 'contents', 0, 'itemSectionRenderer', 'contents']
        try:
            contents = json.loads(json_text)
            for key in keys:
                contents = contents[key]
        except:
            _process_error(er_type="extract",
                                data={'url': self._query, 'extract_type': 'video info', 'is_fatal': True,
                                      'reason': "Couldn't get json data"},
                           ignore_errors=self._ignore_errors, ignore_warnings=self._ignore_warnings)
        for vid_info in contents:
            if 'videoRenderer' in vid_info:
                return vid_info.get('videoRenderer').get('videoId')
        return

    def _extract_video_info(self, silent=False, skip_on_error=False):
        if not silent:
            _send_info_message(f"Trying extraction with {self._client}", verbose=self._verbose)

        payload = self._client_info['payload'].copy()
        payload.update({
            "videoId": self.video_id
        })
        headers = self._headers.copy()
        headers.update({
            'Content-Type': 'application/json',
        })
        headers.update(self._client_info['headers'].copy())

        req = requests.post(f'https://www.youtube.com/youtubei/v1/player?key={self._client_info["api_key"]}',
                            headers=headers, json=payload)
        if req.status_code == 200:
            data = req.json()
        elif not self._ignore_fallback:
            req = requests.get(self.url, headers=headers)

            if req.status_code != 200:
                _process_error(er_type="extract",
                                    data={'url': self.url, 'extract_type': 'video info', 'is_fatal': True,
                                          'reason': f'Unsuccessful request - Code <{req.status_code}> | {req.reason}'},
                           ignore_errors=self._ignore_errors, ignore_warnings=self._ignore_warnings)
            html = req.text
            soup = BeautifulSoup(html, 'html.parser')

            script_tags = soup.find_all("script", string=re.compile('ytInitialPlayerResponse'))
            script_tag = None
            for tag in script_tags:
                if "var ytInitialPlayerResponse = null" not in str(tag):
                    script_tag = tag
                    break
            if not script_tag:
                _process_error(er_type="extract",
                                    data={'url': self.url, 'extract_type': 'video info', 'is_fatal': True,
                                          'reason': f"Couldn't get ytInitialPlayerResponse"},
                           ignore_errors=self._ignore_errors, ignore_warnings=self._ignore_warnings)

            json_text = re.search(r'var ytInitialPlayerResponse = ({.*?});', script_tag.string, re.DOTALL).group(1)
            data = json.loads(json_text)
        else:
            return {}

        tmp_pl = data.get('playabilityStatus')
        playability_status = tmp_pl.get('status') if tmp_pl else None
        if playability_status is None or playability_status == 'ERROR' and not skip_on_error:
            prev = self._client
            check = self._change_client()
            if check and not self._no_retry:
                _send_info_message(f"Extraction failed with {prev}. Retrying with {self._client}", verbose=self._verbose)
                data = self._extract_video_info(silent=True)
            else:
                _process_error(er_type="extract",
                                    data={'url': self.url, 'extract_type': 'video info', 'is_fatal': True,
                                          'reason': 'Video Unavailable (Invalid URL or removed video)'},
                               ignore_errors=self._ignore_errors, ignore_warnings=self._ignore_warnings)
        elif playability_status in {'LOGIN_REQUIRED', 'UNPLAYABLE'} and not skip_on_error:
            prev = self._client
            check = self._change_client(client="tv_embed")
            if check and not self._no_retry:
                _send_info_message(f"Extraction failed with {prev}. Retrying with {self._client}", verbose=self._verbose)
                data = self._extract_video_info(silent=True)
            else:
                reason = tmp_pl.get("reason")
                if not reason:
                    try:
                        reason = tmp_pl.get('errorScreen').get('playerErrorMessageRenderer').get('subreason').get('simpleText')
                    except:
                        reason = "Unknown"
                _process_error(er_type="extract",
                                    data={'url': self.url, 'extract_type': 'video info', 'is_fatal': False,
                                          'reason': f'This video is private - {reason}',
                                          'message': f'Error for {self.url} - This video is private - {reason}'},
                               ignore_errors=self._ignore_errors, ignore_warnings=self._ignore_warnings)
        if 'streamingData' not in data and not self._no_retry:
            prev = self._client
            check = self._change_client()
            if not check:
                return {}

            _send_info_message(f"Extraction failed with {prev}. Retrying with {self._client}", verbose=self._verbose)
            data = self._extract_video_info(silent=True)

        return data

    @property
    def comments(self):
        session = requests.Session()
        req = session.get(self.url, headers=self._headers)
        if req.status_code != 200:
            _process_error(er_type="extract", data={'url': self.url, 'is_fatal': True,
                                                    'extract_type': 'comment contents',
                                                    'reason': f'Unsuccessful request - Code <{req.status_code}> | {req.reason}'},
                           ignore_errors=self._ignore_errors, ignore_warnings=self._ignore_warnings)
        html = req.text

        soup = BeautifulSoup(html, 'html.parser')
        script_tag = soup.find("script", string=re.compile('ytInitialData'))

        json_text = re.search(r'var ytInitialData = ({.*?});', script_tag.string, re.DOTALL).group(1)
        data = json.loads(json_text)
        contents = data.get('contents', {}).get('twoColumnWatchNextResults', {}).get('results', {}).get('results', {}).get('contents', [{}, {}, {}, {}])
        target_id = contents[3].get('itemSectionRenderer', {}).get('targetId')
        ctoken = contents[3].get('itemSectionRenderer', {}).get('contents', [{}])[0].get('continuationItemRenderer', {}).get('continuationEndpoint', {}).get('continuationCommand', {}).get('token')
        comments = []
        i = 1

        while ctoken:
            base_url = "https://www.youtube.com/youtubei/v1/next?key=AIzaSyAO_FJ2SlqU8Q4STEHLGCilw_Y9_11qcW8"
            payload = CLIENT_INFO['web']['payload'].copy()
            payload.update({
                'continuation': ctoken,
                'targetId': target_id
            })
            response = session.post(base_url, headers=CLIENT_INFO['web']['headers'], json=payload)
            if response.status_code != 200:
                _process_error(er_type="extract", data={'url': self.url, 'is_fatal': False,
                                                        'extract_type': 'comment contents',
                                                        'reason': f'Unsuccessful request - Code <{response.status_code}> | {response.reason}',
                                                        'message': f'Unsuccessful request for {self.url} - Code <{response.status_code}> | {response.reason}'},
                               ignore_errors=self._ignore_errors, ignore_warnings=self._ignore_warnings)
            data = response.json()
            comments_data = data.get('frameworkUpdates', {}).get('entityBatchUpdate', {}).get('mutations', [])
            for comment_info in comments_data:
                comment = comment_info.get('payload', {}).get('commentEntityPayload')
                if comment:
                    if i > self._max_comments:
                        return comments
                    owner = comment.get('author')
                    author_id = owner.get('channelId')
                    properties = comment.get('properties')
                    toolbar = comment.get('toolbar')
                    likes = _from_short_number(_filter_numbers(toolbar.get('likeCountNotliked', '0')))
                    dislikes = abs(_from_short_number(_filter_numbers(toolbar.get('likeCountLiked', '0'))) - likes)
                    replies = toolbar.get('replyCount', '0')
                    if not replies: replies = '0'
                    comments.append({
                        "author": owner.get('displayName'), "author_id": author_id,
                        "author_avatar": owner.get('avatarThumbnailUrl'),
                        "author_url": "https://www.youtube.com/channel/" + author_id if author_id else None,
                        "is_verified": owner.get('isVerified'), "text": properties.get('content', {}).get('content'),
                        "likes": likes, "replies": int(_filter_numbers(replies)),
                        "comment_id": properties.get('commentId'),
                        "dislikes": dislikes
                    })

            if not comments:
                break

            def _find_continuation_commands(d, results=None):
                if results is None:
                    results = []

                if isinstance(d, dict):
                    for key, value in d.items():
                        if key == "continuationCommand":
                            results.append(value)
                        else:
                            _find_continuation_commands(value, results)
                elif isinstance(d, list):
                    for item in d:
                        _find_continuation_commands(item, results)

                return results

            try:
                ctoken = _find_continuation_commands(data)[-1].get('token')
            except:
                break
        if not comments:
            _send_warning_message("Couldn't extract comments.", self._ignore_warnings)
        return comments

    @comments.setter
    def comments(self):
        self.comments = None

    def __str__(self):
        return f"`Video` object at {hex(id(self))}, title: {self.title}, url: {self.url}, id: {self.video_id}"

    def __dir__(self):
        """
        Modified dir() to display only common use methods.

        To see the complete dir, use Video().__default_dir__() or dir(Video)
        """
        default_dir = super().__dir__()
        return [attribute for attribute in default_dir if not attribute.startswith("_")]

    def __default_dir__(self):
        return super().__dir__()


class Search:
    """
    Search the given query and fetch the results.
    Automatically get the Video class for each result or only get simple information (title, url, duration, ...).

    Attributes
    ----------
    query: str
        A query to search for
    get_simple: bool (False)
        Get only simplified data of the video (to save time in case the stream/download isn't required)
    use_threads: bool (True)
        Obtain the information/download the videos using threads (parallel processing)
    threads: int (Half of the available threads)
        Amount of threads to use
    download_kwargs: dict (Default parameters)
        The arguments to parse to the `download` method, inherited from `Video.download()`
    kwargs: dict (Default parameters)
        Inherits `Video` kwargs

    Methods
    -------
    download(**kwargs)
        Inherits `Video.download()` arguments
    """
    def __init__(self, query: str, get_simple: bool = False, use_threads: bool = True, threads: int = DEFAULT_THREADS,
                 max_duration: int = -1, max_results: int = -1, retries: int = 5, minimum_results: int = -1,
                 no_headers: bool = False, **kwargs):
        """Make a Search class.

        :param str query:
            A query to search for
        :param bool get_simple:
            Get only simplified data of the video (to save time in case the stream/download isn't required):
            title, video id, url, duration, views, channel name/url/id
        :param bool use_threads:
            Obtain the information/download the videos using threads (parallel processing)
        :param int threads:
            Amount of threads to use
        :param dict download_kwargs:
            The arguments to parse to the `download` method, inherited from `Video.download()`
        :param dict kwargs:
            Inherits `Video` kwargs
        :param int max_duration:
            Max duration of a video, in seconds
        :param int max_results:
            Max amount of videos to fetch from the results
        :param int retries:
            Max amount of retries for a failed search
        :param int minimum_results:
            Minimum amount of videos that should be fetched (else, retry the search)
        :param bool no_headers:
            Disable headers for the request, might make the search slightly faster or "more successful", but also less reliable in some situations.
        """
        kwargs.setdefault('ignore_errors', True)
        kwargs.setdefault('ignore_warnings', True)
        kwargs.setdefault('verbose', False)
        self._ignore_errors = kwargs.get('ignore_errors')
        self._ignore_warnings = kwargs.get('ignore_warnings')
        self._verbose = kwargs.get('verbose')
        self._headers = {
            'Accept-Language': 'en-US,en;q=0.9',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        } if not no_headers else {}
        self._minimum_results = minimum_results
        self._retries = retries

        self._max_dur = max_duration
        self.results = None
        self._query = query.strip()
        _send_info_message(f'Searching for "{self._query}":', self._verbose)
        vids_info = self._search_query()
        self.videos_info = vids_info[:max_results] if max_results > 0 else vids_info
        self.video_urls = list(filter(None, [vid.get('url') for vid in self.videos_info]))
        if not self.video_urls:
            _process_error(er_type="search", data={'query': query, 'is_fatal': True},
                           ignore_errors=self._ignore_errors, ignore_warnings=self._ignore_warnings)

        self._get_simple = get_simple
        self._kwargs = kwargs
        self._download_kwargs = {}
        self._threads = threads
        self._use_threads = use_threads

        if self._get_simple:
            self.results = self.videos_info
        else:
            self.results = Fetch(iterable=self.video_urls, use_threads=self._use_threads, threads=self._threads, **self._kwargs)

        _send_success_message('Successfully fetched info for query "{self._query}"', self._verbose)

    def download(self, **download_kwargs):
        """
        Inherits `Video.download()` arguments
        """
        self._download_kwargs.update(download_kwargs)
        self._download_kwargs.setdefault('_show_bar', False)
        if self.results is None:
            _process_error(er_type="download", data={'url': self._query, 'is_fatal': False,
                                            'reason': f'No results found (have you set get_only_urls=True?)',
                                            'message': f'No results found for {self._query} (have you set get_only_urls=True?)'},
                           ignore_errors=self._ignore_errors, ignore_warnings=self._ignore_warnings)
            return

        Download(self.results, use_threads=self._use_threads, threads=self._threads, **self._download_kwargs)

    def _search_query(self):
        url = "https://www.youtube.com/results?search_query=" + self._query.replace(" ", "+")
        session = requests.Session()
        for i in range(self._retries):
            a = (-5+len(f'Searching for \"{self._query}\":')//2)*'.'
            _send_info_message(f"{a}Attempt #{i + 1}{a}", self._verbose)

            html = session.get(url, headers=self._headers).text
            soup = BeautifulSoup(html, 'html.parser')
            script_tag = soup.find('script', string=re.compile(r'var ytInitialData'))
            if not script_tag:
                continue

            try: json_text = re.search(r'var ytInitialData = ({.*?});', script_tag.string, re.DOTALL).group(1)
            except: continue
            keys = ['contents', 'twoColumnSearchResultsRenderer', 'primaryContents', 'sectionListRenderer', 'contents', 0, 'itemSectionRenderer', 'contents']
            try:
                contents = json.loads(json_text)
                for key in keys:
                    contents = contents[key]
            except:
                continue

            videos_info = []
            for vid in contents:
                if 'videoRenderer' in vid:
                    vid_info = vid.get('videoRenderer')
                    video_id = str(vid_info.get('videoId'))
                    url = "https://www.youtube.com/watch?v="+video_id
                    if url == "https://www.youtube.com/watch?v=None": continue
                    thumbnail, title = vid_info.get('thumbnail', {}).get('thumbnails', [{}])[-1], \
                                       vid_info.get('title', {}).get('runs', [{}])[0].get('text')
                    fduration, views = vid_info.get('lengthText', {}).get('simpleText', '0:00'), _filter_numbers(vid_info.get('viewCountText', {}).get('simpleText', '-1'))
                    duration, fviews = formatted_to_seconds(fduration), _format_views(views)
                    if self._max_dur > 0 and duration > self._max_dur:
                        continue
                    ch = vid_info.get('longBylineText', {}).get('runs', [{}])[0]
                    channel, channel_id = ch.get('text'), \
                                          ch.get('navigationEndpoint', {}).get('browseEndpoint', {}).get('browseId', '')
                    channel_url = "https://www.youtube.com/channel/"+channel_id if channel_id else ''
                    videos_info.append({
                        'title': title, 'video_id': video_id, 'url': url, 'duration': duration, 'fduration': fduration,
                        'views': None if views == '-1' else int(views), 'fviews': fviews, 'channel': channel, 'channel_url': channel_url,
                        'channel_id': channel_id
                    })
            if not videos_info or all((self._minimum_results > 0, len(videos_info) < self._minimum_results)): continue
            return videos_info

        _process_error(er_type="search", data={'query': self._query, 'is_fatal': True},
                       ignore_errors=self._ignore_errors, ignore_warnings=self._ignore_warnings)

    def __str__(self):
        return f"`Search` object at {hex(id(self))}, videos: {len(self.results)}"

    def __dir__(self):
        """
        Modified dir() to display only common use methods.

        To see the complete dir, use Search().__default_dir__() or dir(Search)
        """
        default_dir = super().__dir__()
        return [attribute for attribute in default_dir if not attribute.startswith("_")]

    def __iter__(self):
        return iter(self.results)

    def __len__(self):
        return len(self.results)

    def __getitem__(self, index):
        return self.results[index]

    def __default_dir__(self):
        return super().__dir__()


class Playlist:
    """
    Get data from a YouTube playlist.

    Attributes
    ----------
    url: str
        A YouTube playlist URL.
        Using a video that's part of a list (has &list= on the name) will also work.
    max_length: int (-1)
        Maximum amount of videos to fetch from the playlist.
    max_duration: int (-1)
        Maximum duration a video can have to fetch it.
    use_threads: bool (True)
        Obtain the information/download the videos using threads (parallel processing)
    threads: int (Half of the available threads)
        Amount of threads to use
    format_duration: bool (True)
        Retrieve the duration of the playlist formatted as HH:MM:SS instead of seconds.
    use_login_playlist: bool (False)
        Login to YouTube only to get the video urls of the playlist (for private playlists).
    kwargs: dict (Default parameters)
        Inherits `Video` kwargs

    Methods
    -------
    download(**download_kwargs)
        Download the videos from the playlist. Inherits `Video.download()` method arguments.
    """
    def __init__(self, url, max_length=-1, max_duration=-1, use_threads=True, threads=DEFAULT_THREADS,
                 format_duration=True, use_login_playlist=False, **kwargs):
        kwargs.setdefault('ignore_errors', True)
        kwargs.setdefault('ignore_warnings', True)
        kwargs.setdefault('verbose', False)
        kwargs.setdefault('disable_cache', False)
        self._ignore_errors = kwargs.get("ignore_errors")
        self._ignore_warnings = kwargs.get("ignore_warnings")
        self._verbose = kwargs.get("verbose")
        self._use_threads = use_threads
        self._threads = threads
        self._max_duration = max_duration
        self._max_length = max_length if max_length > 0 else 10000

        self._use_login = use_login_playlist
        self._disable_cache = kwargs.get("disable_cache")
        access_token = None
        if self._use_login:
            access_token = self._get_token()
        self._headers = self._get_headers(access_token=access_token)

        self.url = url
        self.playlist_id = self._extract_playlist_id()
        if not self.playlist_id:
            _process_error(er_type="id", data={'url': self.url, 'is_fatal': True},
                           ignore_errors=self._ignore_errors, ignore_warnings=self._ignore_warnings)
        self.playlist_url = "https://www.youtube.com/playlist?list="+self.playlist_id

        self._playlist_data_info = {}
        self.videos_info = self._extract_videos()
        self.video_urls = [vid.get('url') for vid in self.videos_info]
        self.title = self._playlist_data_info.get('title', {}).get('simpleText')
        self.description = self._playlist_data_info.get('descriptionText', {}).get('simpleText')
        self.length = len(self.video_urls)
        total_length = self._playlist_data_info.get('numVideosText', {}).get('runs', [{}])[0].get('text', '0').replace(',', '')
        self.total_length = int(total_length) if total_length.isnumeric() else 0
        self.views = _filter_numbers(self._playlist_data_info.get('viewCountText', {}).get('simpleText', '-1'))
        dur = sum(vid.get('duration', 0) for vid in self.videos_info)
        self.duration = format_seconds(dur) if format_duration else dur
        ch = self._playlist_data_info.get('ownerText', {}).get('runs', [{}])[0]
        self.channel = ch.get('text', '').replace('by ', '')
        self.channel_id = ch.get('navigationEndpoint', {}).get('browseEndpoint', {}).get('browseId')
        self.channel_url = "https://www.youtube.com/channel/" + self.channel_id if self.channel_id else ''
        self.banner = self._playlist_data_info.get('playlistHeaderBanner', {}).get('heroPlaylistThumbnailRenderer', {}).get('thumbnail', {}).get('thumbnails', [{}])[-1]

        self._kwargs = kwargs
        self._download_kwargs = {}

    def download(self, **download_kwargs):
        """
        Inherits `Video.download()` arguments
        """
        _vids = download_kwargs.get('_vids')
        self._download_kwargs.update(download_kwargs)
        self._download_kwargs.setdefault('_show_bar', False)
        vids = self.videos if not _vids else _vids
        if vids is None:
            _process_error(er_type="download", data={'url': self.url, 'is_fatal': False,
                                                     'reason': f'No videos to download',
                                                     'message': f'No videos to download for {self.url}'},
                           ignore_errors=self._ignore_errors, ignore_warnings=self._ignore_warnings)
            return

        Download(vids, use_threads=self._use_threads, threads=self._threads, **self._download_kwargs)

    @property
    def videos(self):
        return Fetch(iterable=self.video_urls, use_threads=self._use_threads, threads=self._threads, **self._kwargs)

    @videos.setter
    def videos(self):
        self.videos = []

    def _extract_videos(self):
        session = requests.Session()

        req = session.get(self.playlist_url, headers=self._headers)

        if req.status_code != 200:
            _process_error(er_type="extract", data={'url': self.url, 'is_fatal': True,
                                                         'extract_type': 'playlist contents',
                                                         'reason': f'Unsuccessful request - Code <{req.status_code}> | {req.reason}'},
                           ignore_errors=self._ignore_errors, ignore_warnings=self._ignore_warnings)
        html = req.text

        soup = BeautifulSoup(html, 'html.parser')
        script_tag = soup.find("script", string=re.compile('ytInitialData'))

        json_text = re.search(r'var ytInitialData = ({.*?});', script_tag.string, re.DOTALL).group(1)
        data = json.loads(json_text)

        if data.get('alerts', [{}])[0].get('alertRenderer'):
            _process_error(er_type="extract", data={'url': self.playlist_url, 'is_fatal': True,
                                                          'extract_type': 'playlist contents',
                                                          'reason': 'Private or non-existent playlist'},
                           ignore_errors=self._ignore_errors, ignore_warnings=self._ignore_warnings)
        self._playlist_data_info = data.get('header', {}).get('playlistHeaderRenderer', {})
        playlist_contents = data.get('contents', {}).get('twoColumnBrowseResultsRenderer', {}).get('tabs', [{}])[0].get('tabRenderer', {}).get('content', {}).get('sectionListRenderer', {}).get('contents', [{}])[0].get('itemSectionRenderer', {}).get('contents', [{}])[0].get('playlistVideoListRenderer', {}).get('contents', [{}])
        ctoken = playlist_contents[-1].get('continuationItemRenderer', {}).get('continuationEndpoint', {}).get('continuationCommand', {}).get('token')

        videos_info = []
        current_result = 1
        for video in playlist_contents:
            if 'playlistVideoRenderer' in video:
                if current_result > self._max_length:
                    return videos_info
                vid_info = video.get('playlistVideoRenderer', {})

                video_id = vid_info.get('videoId')
                title = vid_info.get('title', {}).get('runs', [{}])[0].get('text')
                url = "https://www.youtube.com/watch?v=" + video_id if video_id else None
                fduration = vid_info.get('lengthText', {}).get('simpleText', '0:00')
                duration = formatted_to_seconds(fduration)
                if self._max_duration > 0 and duration > self._max_duration:
                    _send_info_message(f"Skipped `{title}` - {url}: Exceeds set max duration {format_seconds(self._max_duration)}.", verbose=self._verbose)
                    continue
                thumbnail = vid_info.get('thumbnail', {}).get('thumbnails', [{}])[-1].get('url')
                index = int(vid_info.get('index', {}).get('simpleText', -1))
                ch = vid_info.get('shortBylineText', {}).get('runs', [{}])[0]
                channel, channel_id = ch.get('text'), ch.get('navigationEndpoint', {}).get('browseEndpoint', {}).get('browseId', '')
                channel_url = "https://www.youtube.com/channel/" + channel_id if channel_id else ''
                views_match = re.search(r'(\d{1,3}(?:,\d{3})*) views', vid_info.get('title', {}).get('accessibility', {}).get('accessibilityData', {}).get('label'))
                views = _filter_numbers(views_match.group(1)) if views_match else '-1'
                fviews = _format_views(views)

                vid_dict = {
                    'title': title, 'video_id': video_id, 'url': url, 'duration': duration, 'fduration': fduration,
                    'views': None if views == '-1' else int(views), 'fviews': fviews, 'channel': channel,
                    'channel_url': channel_url, 'channel_id': channel_id, 'index': index, 'thumbnail': thumbnail
                }
                videos_info.append(vid_dict)
                current_result += 1

        while ctoken:
            base_url = "https://www.youtube.com/youtubei/v1/browse?key=AIzaSyAO_FJ2SlqU8Q4STEHLGCilw_Y9_11qcW8"
            payload = CLIENT_INFO['web']['payload'].copy()
            payload.update({
                'continuation': ctoken
            })
            response = session.post(base_url, headers=CLIENT_INFO['web']['headers'], json=payload)
            if response.status_code != 200:
                _process_error(er_type="extract", data={'url': self.url, 'is_fatal': False,
                                                        'extract_type': 'playlist contents',
                                                        'reason': f'Unsuccessful request - Code <{response.status_code}> | {response.reason}',
                                                        'message': f'Unsuccessful request for {self.url} - Code <{response.status_code}> | {response.reason}'},
                           ignore_errors=self._ignore_errors, ignore_warnings=self._ignore_warnings)
                break
            data = response.json()

            next_video_list = data.get('onResponseReceivedActions', [{}])[0].get('appendContinuationItemsAction',
                                                                                 {}).get('continuationItems', [{}])
            ctoken = next_video_list[-1].get('continuationItemRenderer', {}).get('continuationEndpoint', {}).get(
                'continuationCommand', {}).get('token')

            for video in next_video_list:
                if 'playlistVideoRenderer' in video:
                    if current_result > self._max_length:
                        return videos_info
                    vid_info = video.get('playlistVideoRenderer', {})

                    video_id = vid_info.get('videoId')
                    title = vid_info.get('title', {}).get('runs', [{}])[0].get('text')
                    url = "https://www.youtube.com/watch?v=" + video_id if video_id else None

                    fduration = vid_info.get('lengthText', {}).get('simpleText', '0:00')
                    duration = formatted_to_seconds(fduration)
                    if self._max_duration > 0 and duration > self._max_duration:
                        _send_info_message(f"Skipped `{title}` - {url}: Exceeds set max duration {format_seconds(self._max_duration)}.", verbose=self._verbose)
                        continue
                    thumbnail = vid_info.get('thumbnail', {}).get('thumbnails', [{}])[-1].get('url')
                    index = int(vid_info.get('index', {}).get('simpleText', -1))
                    ch = vid_info.get('shortBylineText', {}).get('runs', [{}])[0]
                    channel, channel_id = ch.get('text'), ch.get('navigationEndpoint', {}).get('browseEndpoint', {}).get('browseId', '')
                    channel_url = "https://www.youtube.com/channel/" + channel_id if channel_id else ''
                    views_match = re.search(r'(\d{1,3}(?:,\d{3})*) views',vid_info.get('title', {}).get('accessibility', {}).get('accessibilityData',{}).get('label'))
                    views = _filter_numbers(views_match.group(1)) if views_match else '-1'
                    fviews = _format_views(views)

                    vid_dict = {
                        'title': title, 'video_id': video_id, 'url': url, 'duration': duration, 'fduration': fduration,
                        'views': None if views == '-1' else int(views), 'fviews': fviews, 'channel': channel,
                        'channel_url': channel_url, 'channel_id': channel_id, 'index': index, 'thumbnail': thumbnail
                    }
                    videos_info.append(vid_dict)
                    current_result += 1

        return videos_info

    def _extract_playlist_id(self):
        yt_playlist_match = re.search(r"(?:https?:\/\/(?:www\.|m\.)?youtube\.com\/.*[?&]list=|https?:\/\/youtu\.be\/)([a-zA-Z0-9_-]*)", self.url)
        if yt_playlist_match:
            return yt_playlist_match.group(1)

    def _get_headers(self, access_token):
        if self._use_login: YOUTUBE_HEADERS.update({
                            'Authorization': f'Bearer {access_token}'
                        })
        return YOUTUBE_HEADERS

    def _get_token(self):
        if not self._disable_cache and os.path.exists(ACCESS_TOKEN_DIR):
            with open(ACCESS_TOKEN_DIR, 'r') as f:
                access_token = json.load(f).get('access_token')
            return access_token

        response = requests.post('https://oauth2.googleapis.com/device/code',
                                 data={'client_id': CLIENT_ID,'scope': 'https://www.googleapis.com/auth/youtube'})

        response_data = response.json()
        _send_info_message("Logging in...", True)
        _send_info_message(f"Open {response_data.get('verification_url')} and use the code {response_data.get('user_code')}", True)
        input(_dim_cyan("[INFO]: Press enter when completed."))

        response = requests.post('https://oauth2.googleapis.com/token',
            data={'client_id': CLIENT_ID, 'client_secret': CLIENT_SECRET, 'device_code': response_data['device_code'], 'grant_type': 'urn:ietf:params:oauth:grant-type:device_code'})
        response_data = response.json()

        return self._write_cache(response_data['access_token'])

    def _write_cache(self, token):
        if not self._disable_cache:
            if not os.path.exists(CACHE_DIR):
                os.mkdir(CACHE_DIR)
            with open(ACCESS_TOKEN_DIR, 'w') as f:
                json.dump({'access_token': token}, f)
        return token

    def __str__(self):
        return f"`Playlist` object at {hex(id(self))}, title: {self.title}, url: {self.playlist_url}, id: {self.playlist_id}, videos: {self.length}"

    def __repr__(self):
        return f"`Playlist` object at {hex(id(self))}, title: {self.title}, url: {self.playlist_url}, id: {self.playlist_id}, videos: {self.length}"

    def __dir__(self):
        """
        Modified dir() to display only common use methods.

        To see the complete dir, use Playlist().__default_dir__() or dir(Playlist)
        """
        default_dir = super().__dir__()
        return [attribute for attribute in default_dir if not attribute.startswith("_")]

    def __iter__(self):
        return iter(self.videos_info)

    def __len__(self):
        return self.length

    def __add__(self, other):
        if not isinstance(other, Playlist):
            if isinstance(other, list) or isinstance(other, tuple):
                return self.videos_info + other
            raise TypeError(f"Unsupported operand type(s) for +: 'Playlist' and '{type(other).__name__}'")
        return self.videos_info + other.videos_info

    def __radd__(self, other):
        if not isinstance(other, Playlist):
            if isinstance(other, list) or isinstance(other, tuple):
                return other + self.videos_info
            raise TypeError(f"Unsupported operand type(s) for +: 'Playlist' and '{type(other).__name__}'")
        return other.videos_info + self.videos_info

    def __getitem__(self, index):
        return self.videos_info[index]

    def __setitem__(self, index, value):
        self.videos_info[index] = value

    def __contains__(self, item):
        if isinstance(item, dict):
            return any(item == video for video in self.videos_info) or any(item.get('url') == url for url in self.video_urls)
        return any(item == video['title'] or item == video['url'] or item == video['video_id'] for video in self.videos_info) or any(item == url for url in self.video_urls)

    def append(self, item):
        self.videos_info.append(item)
        self.video_urls.append(item.get('url') if isinstance(item, dict) else item)

    def extend(self, item):
        self.videos_info.extend(item)
        self.video_urls.extend(item.get('url') if isinstance(item, dict) else item)

    def remove(self, item):
        self.videos_info = [video for video in self.videos_info if item not in {video.get('title'), video.get('url'), video.get('video_id')}]
        self.video_urls = [video.get('url') for video in self.videos_info]
        self.length = len(self.video_urls)

    def pop(self, index=-1):
        return self.videos_info.pop(index)

    def clear(self):
        self.videos_info.clear()

    def sort(self, key=None, reverse=False):
        self.videos_info.sort(key=key, reverse=reverse)

    def reverse(self):
        self.videos_info.reverse()

    def __default_dir__(self):
        return super().__dir__()


class Fetch:
    """
    Get information of videos from a list of urls or dicts with video info.
    """
    def __new__(cls, iterable: Iterable[str | Dict], use_threads: bool = True, threads: int = DEFAULT_THREADS, **kwargs) -> List[Video]:
        """
        Get information of videos from a list of urls or dicts with video info.

        :param iterable: List of video URLs or dicts with video info (they need to have a "url" key)
        :param use_threads: Use parallel processing for faster fetching
        :param threads: Amount of threads to use
        :param kwargs: Inherited from `Video` class kwargs
        """
        instance = super().__new__(cls)
        if isinstance(iterable, Playlist):
            vid_urls = iterable.video_urls.copy()
        elif isinstance(iterable, Search):
            vid_urls = iterable.video_urls.copy()
        else:
            vid_urls = [item.get('url') if isinstance(item, dict) else item for item in iterable]
        kwargs.setdefault("ignore_warnings", True)

        if use_threads:
            def _fetch_info(url):
                return Video(url, **kwargs)

            with ThreadPoolExecutor(max_workers=threads) as executor:
                instance.videos = list(executor.map(_fetch_info, vid_urls))
        else:
            instance.videos = []
            for url in vid_urls:
                instance.videos.append(Video(url, **kwargs))

        return instance.videos


class Download:
    """
    Download videos from a list.
    """
    def __init__(self, iterable: Iterable[Video] | Playlist | Search, use_threads: bool = True, threads: int = DEFAULT_THREADS,
                 **download_kwargs) -> None:
        """
        Download videos from a list.

        :param iterable: List of videos to download
        :param use_threads: Use parallel processing to download
        :param threads: Amount of threads to use
        :param download_kwargs: Inherited from `Video` class method `download` args
        """
        if isinstance(iterable, Playlist):
            videos = iterable.videos
        elif isinstance(iterable, Search):
            videos = iterable.results
        else:
            videos = iterable
        if any(not isinstance(x, Video) and not isinstance(x, GenericExtractor) for x in videos):
            _process_error(er_type="download",
                           data={'is_fatal': True, 'url': '', 'reason': 'Invalid video type found. Must be `Video` or `GenericExtractor` class'},
                           ignore_errors=False, ignore_warnings=False)
        self._kwargs = download_kwargs
        self._kwargs.setdefault("_show_bar", False)


        self._pbar = tqdm(total=len(videos), unit='videos', desc="Downloading videos", colour=BAR_COLOR)
        if use_threads:
            with ThreadPoolExecutor(max_workers=threads) as executor:
                executor.map(self._download_vid, videos, [i for i in range(len(videos))])
        else:
            for i, video in enumerate(videos):
                self._download_vid(video, i)

        self._pbar.close()

    def _download_vid(self, video, number):
        try:
            self._kwargs.update({
                "_raw_number": number,
            })
            video.download(**self._kwargs)
            self._pbar.update(1)
        except Exception as e:
            _send_error_message(f"Failed to download `{video.url}`: "+e, False)


class GenericExtractor:
    """
    Try to extract info (focused on stream urls/images) from a site that is not youtube.
    Might get title, id, mosaic (images showing multiple frames of the video as a preview), thumbnail and
    stream url, along with streaming data (all stream urls) and images (all images).

    Attributes
    ----------
    url: str
        The url to extract from
    use_threads: bool (True)
        Check for raw data urls with parallel processing
    threads: int (Half of the available threads)
        Amount of threads to use
    retries: int (1)
        Max amount of retries for a failed request
    ignore_youtube: bool (True)
        Ignore checking if the given url is a query or a youtube url (in case some url is being recognized as a youtube url)
    custom_headers: dict (None)
        Headers to use when making requests
    kwargs: dict (Default parameters)
        Inherits `Video` kwargs + "no_headers" (make the request without headers)

    Methods
    -------
    download(path: str = ".", chunk_size: int = 1024*1024)
        path: str - Output path.
        chunk_size: int - Stream download chunk size.
    """
    def __init__(self, url, use_threads: bool = True, threads: int = DEFAULT_THREADS, retries: int = 1,
                 ignore_youtube: bool = True, custom_headers: dict | None = None, **kwargs):
        """Try to extract some info from an url that is not youtube (focused on stream url/images).

        :param str url:
            The url to extract from
        :param bool use_threads:
            Check for raw data urls with parallel processing
        :param int threads:
            Amount of threads to use
        :param int retries:
            Max amount of retries for a failed request
        :param int ignore_youtube:
            Ignore checking if the given url is a query or a youtube url (in case some url is being recognized as a youtube url)
        :param dict custom_headers:
            Headers to use when making requests
        :param dict kwargs:
            Inherits `Video` kwargs + "no_headers" (make the request without headers)
        """
        self._verbose = kwargs.get("verbose", False)

        if (not _is_url(url) or _is_valid_yt_url(url)[0]) and not ignore_youtube:
            _send_info_message("Youtube URL or query specified, using YT extractor...", self._verbose)
            vid = Video(url, **kwargs)
            for attr in dir(vid):
                if attr == "comments": continue
                setattr(self, attr, getattr(vid, attr))
            return

        self.url = url
        self._threads = threads
        self._use_threads = use_threads
        self._retries = retries
        self._ignore_errors = kwargs.get('ignore_errors', False)
        self._ignore_warnings = kwargs.get('ignore_warnings', False)

        headers = {}
        if custom_headers:
            headers = custom_headers
        elif not kwargs.get('no_headers'):
            headers = {
                'Accept-Language': 'en-US,en;q=0.9',
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36'
            }
        self._headers = headers.copy()

        self.title = None
        self.id = None
        self.stream_url = None
        self.mosaic = None
        self.mosaic_full = None
        self.thumbnail = None
        self.html = ''

        self.streaming_data, self.images, html5player = self._extract_info()

        if html5player is not None:
            self._get_html5player_data(html5player)

        self._parse_info()
        self.stream_url = self.streaming_data[0] if self.streaming_data and not self.stream_url else self.stream_url

    def download(self, path: str = ".", chunk_size: int = 1024*1024, **kwargs):
        """
        Downloads an appropriate video/audio stream.

        Args:
        - path [str]: Output path. Defaults to the current directory.
        - chunk_size [int]: Size of the chunks to download. Increase if you're experiencing low speeds, decrease if you want to limit. Defaults to 1024*1024.
        """
        if not self.stream_url:
            _process_error(er_type="download", data={'url': self.url, 'is_fatal': False,
                                                     'reason': f"Couldn't find stream url"},
                           ignore_errors=self._ignore_errors, ignore_warnings=self._ignore_warnings)
            return

        _show_bar = kwargs.get('_show_bar', True)
        _retries = kwargs.get('_retries', 4)
        _request_interval = kwargs.get('_request_interval', 0.75)

        dir_path = os.path.abspath(path)
        if not os.path.exists(dir_path):
            os.makedirs(dir_path)

        filename = _format_title(self.title)[:200].replace("\n", "").strip()

        if kwargs.get('_raw_number') is not None:
            number = kwargs.get('_raw_number')
            filename = filename + f"_{number}.mp4" if self.title else f"download_{number}.mp4"
        else:
            filename = filename + ".mp4"
        if os.path.exists(os.path.join(path, filename)):
            now = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
            filename = filename.replace(".mp4", f"_{now}.mp4")
        file_path = os.path.join(dir_path, filename)

        if '.m3u8' in self.stream_url or requests.head(self.stream_url).headers.get('Content-Type').lower() in \
                {'application/vnd.apple.mpegurl', 'application/mpegurl', 'application/x-mpegurl'}:
            _send_info_message(f"Downloading m3u8 file", verbose=self._verbose)
            if _show_bar:
                command = ['ffmpeg', '-progress', '-', '-nostats', '-y', '-i', self.stream_url, '-bsf:a',
                           'aac_adtstoasc', '-vcodec', 'copy', '-c', 'copy', '-crf', '-50', file_path]
                with tqdm(desc="Downloading", unit="frames", colour=BAR_COLOR) as pbar:
                    process = subprocess.Popen(command, universal_newlines=True, stderr=subprocess.DEVNULL, stdout=subprocess.PIPE)

                    for lines in iter(process.stdout.readline, ''):
                        for line in lines.split("\n"):
                            line = line.strip()
                            if "frame=" in line:
                                frames = int(float(line.split("=")[1]))
                                pbar.update(abs(pbar.last_print_n-frames))
                                break
            else:
                command = ['ffmpeg', '-loglevel', 'error', '-hide_banner', '-y', '-i', self.stream_url, '-bsf:a',
                           'aac_adtstoasc', '-vcodec', 'copy', '-c', 'copy', '-crf', '-50', file_path]
                subprocess.run(command)
        else:
            for i in range(_retries):
                response = requests.get(self.stream_url, stream=True, headers=self._headers)
                if response.status_code != 429:
                    break
                time.sleep(_request_interval)
                _send_info_message(f"<429> Too many requests, retrying after {_request_interval} seconds...", self._verbose)

            if response.status_code != 200:
                _process_error(er_type="download", data={'url': self.url, 'is_fatal': False,
                                                         'reason': f'Unsuccessful request - Code <{response.status_code}> | {response.reason}',
                                                         'message': f'Unsuccessful request for {self.url} - Code <{response.status_code}> | {response.reason}'},
                               ignore_errors=self._ignore_errors, ignore_warnings=self._ignore_warnings)
                return

            if _show_bar:
                total_size = int(response.headers.get('Content-Length', 0))
                pbar = tqdm(total=total_size, unit='B', unit_scale=True, desc="Downloading", colour=BAR_COLOR)
            with open(file_path, 'wb') as f:
                for chunk in response.iter_content(chunk_size=chunk_size):
                    if chunk:
                        f.write(chunk)
                    if _show_bar:
                        pbar.update(len(chunk))



        _send_success_message(f"Successfully downloaded `{self.title}` into `{dir_path}`.", self._verbose)

    def _parse_info(self):
        if not self.streaming_data:
            _send_warning_message("Couldn't retrieve any stream/download urls", self._ignore_warnings)
        if not self.images:
            _send_warning_message("Couldn't retrieve any image urls", self._ignore_warnings)
        keywords = {1:'main', 2:'master', 3:'mp4', 4:'webm', 5:'3gp', 6:'mp3', 7:'m4a', 8:'wav'}
        self.streaming_data.sort(key=lambda x: (next((k for k in keywords if keywords[k] in x), float('inf')), x))
        keywords_exc = {'thumb'}
        n = len(self.streaming_data)
        for i in range(n):
            if any(k in self.streaming_data[i] for k in keywords_exc):
                self.streaming_data.append(self.streaming_data.pop(i))
            else:
                break

        imgs = [image for image in self.images if not any(k in image for k in {'profile', 'pfp'}) and re.search(r"\d{2,4}x\d{2,4}", image)]
        if imgs:
            self.images = imgs.copy()
            self._sort_images(found_pattern=True)
            self.thumbnail = self.images[0]
        else:
            self._sort_images(found_pattern=False)

        self.streaming_data = list(filter(lambda x: _is_url(x), self.streaming_data))
        self.images = list(filter(lambda x: _is_url(x), self.images))

    def _extract_info(self, data=None):
        session = requests.Session()

        for i in range(self._retries):
            if not data:
                response = session.get(self.url, headers=self._headers)
                if response.status_code != 200: continue

                self.html = html = response.text.replace(r"\/", r"/").replace("quot;", "").replace("amp;", "")
                soup = BeautifulSoup(html, 'html.parser')

                self.title = soup.find('title').text
            else:
                self.html = html = data

            if 'html5player' in html and not data:
                script_tag = soup.find('script', text=lambda text: text and 'html5player' in text)
                return [], [], script_tag.text.strip()
            else:
                all_urls = set(url.replace('//m.', '//www.') for url in re.findall(r'(https?://\S+?(?="|\'|\s))', html))
                urls_set = set(re.sub(r'\b(?:es|en|jp|fr|it|cv|pt|cz|rt|www|pl|nl|de|cn)\.', '', url.split('?lang=')[0]).rstrip(r"\\").rstrip("&") for url in all_urls)

                initial_exclude = {".png", ".jpg", "static", ".js", ".css", ".gif", ".ico", "icon", ".svg", ".html",
                                   "help", "flashplayer", "tabinfo", "terms", "information", "promo", "advertisement",
                                   "trafficjunky", "adblock", "feedback", ".ads", "login", "signup", ".php", "merch"}
                image_words = {".png", ".jpg", ".gif", ".ico", ".svg"}
                image_exclude = {".php", "database", "iqdb", "help", "flashplayer", "tabinfo", "terms", "information",
                                 "promo", "advertisement", "trafficjunky", "adblock", "feedback", ".ads", "login",
                                 "signup", "merch"}
                exclude_words = initial_exclude.copy()
                for element in initial_exclude:
                    if "." in element:
                        element = element.replace(".", "")
                        exclude_words.add(element+"/")
                        exclude_words.add("/"+element)

                urls = list(filter(lambda x: all(ext not in x.lower() for ext in exclude_words)
                                             and len(re.findall(r'https?://', x)) == 1, urls_set))
                image_urls = list(filter(lambda x: any(ext in x.lower() for ext in image_words)
                                                   and all(ext not in x.lower() for ext in image_exclude)
                                                   and len(re.findall(r'https?://', x)) == 1, urls_set))

                key = lambda x: any(keyword in x for keyword in VIDEO_EXTS_DOTTED)
                preferred_urls = list(filter(key, urls))
                rest_urls = [url for url in urls if url not in preferred_urls]

                if not preferred_urls:
                    preferred_urls = rest_urls.copy()

                if self._use_threads:
                    with ThreadPoolExecutor(max_workers=self._threads) as executor:
                        raw_urls = executor.map(self._is_raw, preferred_urls)
                else:
                    raw_urls = []
                    for url in preferred_urls:
                        raw_urls.append(self._is_raw(url))

                return [url[0] for url in raw_urls if url[1]], image_urls, None
        return [], [], None

    def _sort_images(self, found_pattern):
        if not self.images: return
        if found_pattern:
            def _mult(a):
                return int(a[0])*int(a[1])
            self.images.sort(key=lambda s: _mult(re.search(r"\d{2,4}x\d{2,4}", s).group().split('x')), reverse=True)

            return

        keywords = {1: 'preview', 2: 'poster', 3: 'full', 4: '.jpg', 5: '.png', 6: '.gif', 7: '.svg', 8: '.logo',
                    9: '.ico', 10:'php'}
        self.images.sort(key=lambda x: (next((k for k in keywords if keywords[k] in x), float('inf')), x))

        for image in self.images:
            if "mosaic" in image or "mozaique" in image or "mosaique" in image:
                if "full" in image:
                    self.mosaic_full = image
                else:
                    self.mosaic = image
            if self.mosaic_full and self.mosaic: break

        full_images = list(filter(lambda x: any(k in x for k in {"poster", "full", "preview"}), self.images))
        rest_images = [image for image in self.images if image not in full_images]

        self.thumbnail, mimage, mfimage = self.images[0], (None,), (None,)
        if self.mosaic:
            mimage = self._match_string(self.mosaic, full_images)
            if not any(mimage):
                mimage = self._match_string(self.mosaic, rest_images)
        if self.mosaic_full:
            mfimage = self._match_string(self.mosaic_full, full_images)
            if not any(mfimage):
                mfimage = self._match_string(self.mosaic_full, rest_images)

        if all(mimage) and all(mfimage):
            max_val = max((mimage, mfimage), key=lambda x: x[1])
            if max_val[1] > 60: self.thumbnail = max_val[0]
        elif all(mimage):
            self.thumbnail = mimage[0]
        elif all(mfimage):
            self.thumbnail = mfimage[0]

    def _get_html5player_data(self, data):

        for line in data.split("\n"):
            line_check = line.lower().replace("_", "")
            if "title" in line_check and not self.title:
                self.title = next(iter(re.findall(r'["\'](.*?)["\']', line)), None)
            elif any(k in line_check for k in {"videoid", "contentid"}) and not self.id:
                self.id = next(iter(re.findall(r'["\'](.*?)["\']', line)), None)
            elif any(k in line_check for k in {"videourl", "contenturl"}):
                url = next(iter(re.findall(r'["\'](.*?)["\']', line)), None)
                if not self.stream_url: self.stream_url = url
                self.streaming_data.append(url)
            elif any(k in line_check for k in {"hls", "dash"}):
                url = next(iter(re.findall(r'["\'](.*?)["\']', line)), None)
                if not self.stream_url: self.stream_url = url
                self.streaming_data.append(url)
            elif any(k in line_check for k in {"thumb", "thumbnail"}):
                img = next(iter(re.findall(r'["\'](.*?)["\']', line)), None)
                if not self.thumbnail: self.thumbnail = img
                self.images.append(img)
            elif any(k in line_check for k in {"mosaic", "slide"}) and not self.mosaic:
                self.mosaic = next(iter(re.findall(r'["\'](.*?)["\']', line)), None)
                self.images.append(self.mosaic)
            elif any(k in line_check for k in {"mosaicfull", "slidefull", "mosaicbig", "slidebig"}) and not self.mosaic_full:
                self.mosaic_full = next(iter(re.findall(r'["\'](.*?)["\']', line)), None)
                self.images.append(self.mosaic_full)

        if not self.streaming_data or not self.images:
            self.streaming_data, self.images, _ = self._extract_info(self.html)
        self._parse_info()

    @staticmethod
    def _is_raw(url):
        try:
            if any(ext in url for ext in VIDEO_EXTS_DOTTED):
                return url, True

            response = requests.head(url, headers={})
            content_type = response.headers.get('Content-Type', '').lower()

            mime_types = {
                'audio/mpeg', 'audio/wav', 'audio/flac', 'audio/aac', 'audio/ogg', 'audio/mp4', 'audio/m4a', 'video/mp4',
                'video/msvideo', 'video/quicktime', 'video/ms-wmv', 'video/flv', 'video/matroska', 'video/webm',
                'application/vnd.apple.mpegurl', 'application/mpegurl'
            }
            x_mime_types = set(s.replace("/", "/x-") for s in mime_types)

            return url, content_type in mime_types | x_mime_types
        except requests.RequestException:
            return False, False

    @staticmethod
    def _match_string(comp_image, images):
        max_image, max_ratio = max(
            ((image, SequenceMatcher(None, image, comp_image).ratio()) for image in images if image != comp_image),
            key=lambda x: x[1]
        )
        return max_image, max_ratio

    def __str__(self):
        return f"`GenericExtractor` object at {hex(id(self))}, title: {self.title}, url: {self.url}"

    def __dir__(self):
        """
        Modified dir() to display only common use methods.

        To see the complete dir, use GenericExtractor().__default_dir__() or dir(GenericExtractor)
        """
        default_dir = super().__dir__()
        return [attribute for attribute in default_dir if not attribute.startswith("_")]

    def __default_dir__(self):
        return super().__dir__()


class Channel:
    def __init__(self):
        raise NotImplementedError("TODO")


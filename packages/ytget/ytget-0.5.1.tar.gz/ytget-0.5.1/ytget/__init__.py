#######################################################
#              /██                           /██      #
#             | ██                          | ██      #
#  /██   /██ /██████    /██████   /██████  /██████    #
# | ██  | ██|_  ██_/   /██__  ██ /██__  ██|_  ██_/    #
# | ██  | ██  | ██    | ██  \ ██| ████████  | ██      #
# | ██  | ██  | ██ /██| ██  | ██| ██_____/  | ██ /██  #
# |  ███████  |  ████/|  ███████|  ███████  |  ████/  #
#  \____  ██   \___/   \____  ██ \_______/   \___/    #
#  /██  | ██           /██  \ ██                      #
# |  ██████/          |  ██████/                      #
#  \______/            \______/                       #
#######################################################

"""
-----------------|-----------|-----------------
-----------------|---YTGet---|-----------------
-----------------|-----------|-----------------

( Easily get data and download youtube videos )
(    Focused on speed and simplicity.         )

"""
__title__ = "ytget"
__description__ = "Easily get data and download youtube videos. Focused on speed and simplicity."
__url__ = "https://github.com/Coskon/ytget"
__author__ = "Cosk"
__license__ = "MIT"
__version__ = "0.5.1"
__all__ = ["Video", "Search", "Playlist", "Fetch", "Download", "GenericExtractor", "exceptions", "utils"]

from ytget.__main__ import Video, Search, Playlist, Fetch, Download, GenericExtractor

from . import console
from . import exceptions
from . import out_colors
from . import utils

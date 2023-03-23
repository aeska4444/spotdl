"""
Lyrics providers for spotdl_rl.
"""

from spotdl_rl.providers.lyrics.azlyrics import AzLyrics
from spotdl_rl.providers.lyrics.base import LyricsProvider
from spotdl_rl.providers.lyrics.genius import Genius
from spotdl_rl.providers.lyrics.musixmatch import MusixMatch
from spotdl_rl.providers.lyrics.synced import Synced

__all__ = ["AzLyrics", "Genius", "MusixMatch", "Synced", "LyricsProvider"]

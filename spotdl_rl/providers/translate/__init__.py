from spotdl_rl.providers.translate.base import TranslateProvider
from spotdl_rl.providers.translate.lyricstranslate import Lyricstranslate
from spotdl_rl.providers.translate.googletranslate import Googletranslate
from spotdl_rl.providers.translate.animesonglyrics import Animesonglyrics
from spotdl_rl.providers.translate.youtube_subs import YoutubeSbs

__all__ = ["Lyricstranslate", "Googletranslate",
           "Animesonglyrics", "YoutubeSbs", "TranslateProvider"]

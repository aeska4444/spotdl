from typing import List, Optional

from spotdl_rl.providers.translate.base import TranslateProvider
import subprocess
import os

__all__ = ["YoutubeSbs"]


class YoutubeSbs(TranslateProvider):

    def get_translate(self, name: str, artists: List[str], url: str, **kwargs) -> Optional[tuple]:

        comm = 'yt-dlp --skip-download --write-subs ' \
               '--convert-subs lrc --sub-langs en.*,ja ' + url
        process = subprocess.Popen(comm.split(), stdout=subprocess.PIPE)
        output, error = process.communicate()
        try:
            for f in os.listdir():
                if f.endswith('.lrc'):
                    with open(f, encoding='utf-8') as file:
                        if f.endswith('en.lrc'):
                            eng = file.read()
                            print(eng)
                        else:
                            translit = file.read()
                else:
                    translit = None

            [os.remove(i) for i in filter(lambda a: a.endswith(".lrc"), os.listdir())]
            # print(translit, eng)

            return translit, eng
        except Exception:
            return None, None


# YoutubeSbs().get_translate('', [], "https://music.youtube.com/watch?v=tdzsOODJiX8")

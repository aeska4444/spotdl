from spotdl_rl.providers.translate.base import TranslateProvider
from typing import List, Optional

import googletrans

__all__ = ["Googletranslate"]

translator = googletrans.Translator()


class Googletranslate(TranslateProvider):
    @staticmethod
    def translate(lyrics: str, **kwargs) -> Optional[str]:
        return translator.translate(lyrics).text

    @staticmethod
    def romanji(lyrics: str, **kwargs) -> Optional[str]:
        def by_line_trans(line: str):
            t = translator.translate(line)

            if 'origin_pronunciation' in t.extra_data:

                translit = t.extra_data['origin_pronunciation']
            else:
                translit = "".join(filter(lambda a: isinstance(a, str),
                                          t.extra_data['translation'][-1]))
            return translit

        return '\n'.join(map(by_line_trans, lyrics.split('\n')))

    def get_translate(self, name: str, artists: List[str], url=None, **kwargs) -> Optional[str]:
        raise NotImplementedError


# print(Googletranslate().romanji('残酷な天使のように\n少年よ 神話になれ\n♪\n蒼い風がいま\n胸のドアを叩いても\n私だけをただ見つめて'))
# print(Googletranslate().translate('残酷な天使のように\n少年よ 神話になれ\n♪\n蒼い風がいま\n胸のドアを叩いても\n私だけをただ見つめて'))

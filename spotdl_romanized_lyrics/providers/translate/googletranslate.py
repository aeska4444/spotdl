from spotdl_romanized_lyrics.providers.translate.base import TranslateProvider
from typing import List, Optional

import googletrans

translator = googletrans.Translator()


class Googletranslate(TranslateProvider):

    def translate(self, lyrics: str, **kwargs) -> Optional[str]:

        def by_line_trans(line):
            t = translator.translate(line)

            if 'origin_pronunciation' in t.extra_data:
                translit = t.extra_data['origin_pronunciation']
            else:
                translit = "".join(filter(lambda a: isinstance(a, str),
                                          t.extra_data['translation'][-1]))

            text = translit + '\n' + t.text
            return text.strip()

        return '\n'.join(map(by_line_trans, lyrics.split('\n')))

    @staticmethod
    def romanji(lyrics: str, **kwargs) -> Optional[str]:
        return '\n'.join(translator.translate(l).text for l in lyrics.split('\n'))

    def get_translate(self, name: str, artists: List[str], **kwargs) -> Optional[str]:
        raise NotImplementedError

# a = Googletranslate()
# print(a.translate('残酷な天使のように\n少年よ 神話になれ\n♪\n蒼い風がいま\n胸のドアを叩いても\n私だけをただ見つめて'))

# print(t.origin)
# [print(k) for k in t.extra_data]
# print(" ".join(filter(lambda a: a, t.extra_data['translation'][-1])))

from typing import List, Optional

import requests
from bs4 import BeautifulSoup
from spotdl_romanized_lyrics.providers.translate.base import TranslateProvider


class Animesonglyrics(TranslateProvider):

    @staticmethod
    def souper(query):
        url = "https://lyricstranslate.com"
        response = requests.get(
            url + query,
            timeout=10
        )
        return BeautifulSoup(response.text.replace("<br/>", "\n"), "html.parser")

    def get_translate(self, name: str, artists: List[str], **kwargs) -> tuple[
        Optional[str], Optional[bool]]:
        url = "https://www.animesonglyrics.com"
        try:

            artist_str = " ".join(
                artist for artist in artists if artist.lower() not in name.lower()
            )
            name = " ".join(_ for _ in name.split())

            search_response = requests.get(
                url + "/results?",
                params={"q": f"{name}+{artist_str}"},
                timeout=10
            )

            soup = BeautifulSoup(search_response.text.replace("<br/>", "\n"), "html.parser")
            songs = soup.find("div", {"id": "songlist"}).select('span.homesongs')

            for s in songs:
                if name.lower() in s.text.lower():
                    search_response = requests.get(
                        s.a['href'],
                        timeout=10
                    )
                continue

            soup = BeautifulSoup(search_response.text.replace("<br/>", "\n"), "html.parser")
            englishlyrics = soup.select_one('div.englishlyrics')
            romaji = soup.select_one('div.romajilyrics')

            translit, flag = (romaji.get_text('\n'), True,) if romaji else (None, False,)

            eng = englishlyrics.get_text('\n')
            text = '\n'.join(filter(str.strip, translit + '\n' + eng))
            return text, flag,

        except Exception:
            return None, None

    def translate(self, lyrics: str, **kwargs) -> Optional[str]:
        raise NotImplementedError

# a = Animesonglyrics()
# print(a.get_translate('LOST IN PARADISE', ['ALI', 'AKLO']))

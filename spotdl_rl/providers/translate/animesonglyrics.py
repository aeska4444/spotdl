from typing import List, Optional
from Levenshtein import ratio
import re
import requests
from bs4 import BeautifulSoup
from spotdl_rl.providers.translate.base import TranslateProvider

__all__ = ["Animesonglyrics"]


class Animesonglyrics(TranslateProvider):

    def get_translate(self, name: str, artists: List[str], url=None, **kwargs) -> Optional[tuple]:

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

                if ratio(name.lower(),
                         re.findall(r':.+- (.+)',
                                    s.text)[0].lower(),
                         score_cutoff=0.75):
                    search_response = requests.get(
                        s.a['href'],
                        timeout=10
                    )
                    break

            soup = BeautifulSoup(search_response.text.replace("<br/>", "\n"), "html.parser")
            englishlyrics = soup.select_one('div.englishlyrics')
            romaji = soup.select_one('div.romajilyrics')

            translit = romaji.get_text('\n') if romaji else None
            eng = englishlyrics.get_text('\n')
            # print(translit, eng)
            return translit, eng

        except Exception:
            return None, None


# Animesonglyrics().get_translate('kawaki wo ameku', ['minami'])

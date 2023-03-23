from typing import List, Optional

import requests

from bs4 import BeautifulSoup
from spotdl_rl.providers.translate.base import TranslateProvider

__all__ = ["Lyricstranslate"]


class Lyricstranslate(TranslateProvider):

    @staticmethod
    def souper(query):
        url = "https://lyricstranslate.com"
        response = requests.get(
            url + query,
            timeout=10
        )
        return BeautifulSoup(response.text.replace("<br/>", "\n"), "html.parser")

    def get_translate(self, name: str, artists: List[str], url=None, **kwargs) -> Optional[tuple]:

        url = "https://lyricstranslate.com"
        try:

            artist_str = " ".join(
                artist for artist in artists if artist.lower() not in name.lower()
            )
            name = " ".join(_ for _ in name.split())
            search_response = requests.get(
                url + "/en/site-search",
                params={"query": f"{name} {artist_str}"},
                timeout=10
            )

            soup = BeautifulSoup(
                search_response.text.replace("<br/>", "\n"), "html.parser"
            )
            song = soup.select_one('td.ltsearch-songtitle').a['href']
            block = self.souper(song).select_one('div.song-list.grid-item').select(
                'span.song-list-translations-list-languages')

            eng = list(filter(lambda a: a.a.text == 'English', block))[0].a['href']
            eng_containers = self.souper(eng).select_one('div.translate-node-text'). \
                select('div.ltf.direction-ltr')
            eng = " ".join(con.get_text() for con in eng_containers)

            translit = None
            if list(filter(lambda a: a.a.text == 'Transliteration', block)):
                translit = list(filter(lambda a: a.a.text == 'Transliteration', block))[0].a['href']
                # translit_containers = self.souper(translit).select("div#song-body")
                translit_containers = self.souper(translit). \
                    select_one('div.translate-node-text').select('div.ltf.direction-ltr')
                translit = " ".join(con.get_text() for con in translit_containers)
            # print(translit, eng)
            return translit, eng
        except Exception:
            return None, None


# Lyricstranslate().get_translate('カワキヲアメク', ['美波'])

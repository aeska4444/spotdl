"""
Base module for all other lyrics providers.
"""

from typing import List, Optional


class TranslateProvider:
    """
    Base class for all other lyrics providers.
    """

    def get_translate(self, name: str, artists: List[str], **kwargs) -> Optional[str]:
        """
        Returns the lyrics for the given song.

        ### Arguments
        - name: The name of the song.
        - artists: The artists of the song.
        - kwargs: Additional arguments.

        ### Returns
        - The lyrics of the song or None if no lyrics were found.
        """

        raise NotImplementedError

    def translate(self, lyrics: str, **kwargs) -> Optional[str]:
        raise NotImplementedError

    @property
    def name(self) -> str:
        """
        Returns the name of the lyrics provider.
        """

        return self.__class__.__name__




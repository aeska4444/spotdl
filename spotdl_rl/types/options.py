"""
This file contains types for spotdl_rl/downloader/web modules.
Options types have all the fields marked as required.
Settings types have all the fields marked as optional.
"""

from typing import List, Optional, Union

from typing_extensions import TypedDict

__all__ = [
    "SpotifyOptions",
    "DownloaderOptions",
    "WebOptions",
    "spotdl_rlOptions",
    "SpotifyOptionalOptions",
    "DownloaderOptionalOptions",
    "WebOptionalOptions",
    "spotdl_rlOptionalOptions",
]


class SpotifyOptions(TypedDict):
    """
    Options used for initializing the Spotify client.
    """

    client_id: str
    client_secret: str
    auth_token: Optional[str]
    user_auth: bool
    headless: bool
    cache_path: str
    no_cache: bool
    max_retries: int


class DownloaderOptions(TypedDict):
    """
    Options used for initializing the Downloader.
    """
    add_translation: bool
    translate_providers: List[str]

    audio_providers: List[str]
    lyrics_providers: List[str]
    playlist_numbering: bool
    scan_for_songs: bool
    m3u: Optional[str]
    output: str
    overwrite: str
    search_query: Optional[str]
    ffmpeg: str
    bitrate: Optional[Union[str, int]]
    ffmpeg_args: Optional[str]
    format: str
    save_file: Optional[str]
    filter_results: bool
    threads: int
    cookie_file: Optional[str]
    restrict: bool
    print_errors: bool
    sponsor_block: bool
    preload: bool
    archive: Optional[str]
    load_config: bool
    log_level: str
    simple_tui: bool
    fetch_albums: bool
    id3_separator: str
    ytm_data: bool
    add_unavailable: bool
    geo_bypass: bool
    generate_lrc: bool
    force_update_metadata: bool


class WebOptions(TypedDict):
    """
    Options used for initializing the Web server.
    """

    web_use_output_dir: bool
    port: int
    host: str
    keep_alive: bool
    allowed_origins: Optional[List[str]]
    keep_sessions: bool


class spotdl_rlOptions(SpotifyOptions, DownloaderOptions, WebOptions):
    """
    Options used for initializing the spotdl_rl client.
    """


class SpotifyOptionalOptions(TypedDict, total=False):
    """
    Options used for initializing the Spotify client.
    """

    client_id: str
    client_secret: str
    auth_token: Optional[str]
    user_auth: bool
    headless: bool
    cache_path: str
    no_cache: bool
    max_retries: int


class DownloaderOptionalOptions(TypedDict, total=False):
    """
    Options used for initializing the Downloader.
    """

    add_translation: bool
    translate_providers: List[str]

    audio_providers: List[str]
    lyrics_providers: List[str]
    playlist_numbering: bool
    scan_for_songs: bool
    m3u: Optional[str]
    output: str
    overwrite: str
    search_query: Optional[str]
    ffmpeg: str
    bitrate: Optional[Union[str, int]]
    ffmpeg_args: Optional[str]
    format: str
    save_file: Optional[str]
    filter_results: bool
    threads: int
    cookie_file: Optional[str]
    restrict: bool
    print_errors: bool
    sponsor_block: bool
    preload: bool
    archive: Optional[str]
    load_config: bool
    log_level: str
    simple_tui: bool
    fetch_albums: bool
    id3_separator: str
    ytm_data: bool
    add_unavailable: bool
    geo_bypass: bool
    generate_lrc: bool
    force_update_metadata: bool


class WebOptionalOptions(TypedDict, total=False):
    """
    Options used for initializing the Web server.
    """

    web_use_output_dir: bool
    port: int
    host: str
    keep_alive: bool
    allowed_origins: Optional[str]
    keep_sessions: bool


class spotdl_rlOptionalOptions(
    SpotifyOptionalOptions, DownloaderOptionalOptions, WebOptionalOptions
):
    """
    Options used for initializing the spotdl_rl client.
    This type is modified to not require all the fields.
    """

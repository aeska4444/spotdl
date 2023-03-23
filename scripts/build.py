import sys
import os
import ytmusicapi
import PyInstaller.__main__  # type: ignore
from pathlib import Path
from spotdl_rl._version import __version__

locales_path = str((Path(ytmusicapi.__file__).parent / "locales"))

PyInstaller.__main__.run(
    [
        "spotdl_rl/__main__.py",
        "--onefile",
        "--add-data",
        f"{locales_path}{os.pathsep}ytmusicapi/locales",
        "--name",
        f"spotdl_rl-{__version__}-{sys.platform}",
        "--console",
    ]
)

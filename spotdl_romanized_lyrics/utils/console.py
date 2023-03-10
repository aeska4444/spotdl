"""
Module for holding console related actions.
"""

import json

from spotdl_romanized_lyrics.utils.config import DEFAULT_CONFIG, get_config_file
from spotdl_romanized_lyrics.utils.github import check_for_updates as get_update_status
from spotdl_romanized_lyrics.utils.ffmpeg import (
    get_local_ffmpeg,
    is_ffmpeg_installed,
    download_ffmpeg as ffmpeg_download,
)


def generate_config():
    """
    Generate the config file if it doesn't exist
    This is done before the argument parser so it doesn't requires `operation`
    and `query` to be passed.
    """

    config_path = get_config_file()
    if config_path.exists():
        overwrite_config = input("Config file already exists. Overwrite? (y/N): ")

        if overwrite_config.lower() != "y":
            print("Exiting...")
            return None

    with open(config_path, "w", encoding="utf-8") as config_file:
        json.dump(DEFAULT_CONFIG, config_file, indent=4)

    print(f"Config file generated at {config_path}")

    return None


def check_for_updates():
    """
    Check for updates to the current version.
    """

    version_message = get_update_status()

    print(version_message)


def download_ffmpeg():
    """
    Handle ffmpeg download process and print the result.
    """

    if get_local_ffmpeg() is not None or is_ffmpeg_installed():
        overwrite_ffmpeg = input(
            "FFmpeg is already installed. Do you want to overwrite it? (y/N): "
        )

        if overwrite_ffmpeg.lower() == "y":
            local_ffmpeg = ffmpeg_download()

            if local_ffmpeg.is_file():
                print(f"FFmpeg successfully downloaded to {local_ffmpeg.absolute()}")
            else:
                print("FFmpeg download failed")
    else:
        print("Downloading FFmpeg...")
        download_path = ffmpeg_download()

        if download_path.is_file():
            print(f"FFmpeg successfully downloaded to {download_path.absolute()}")
        else:
            print("FFmpeg download failed")


ACTIONS = {
    "--generate-config": generate_config,
    "--check-for-updates": check_for_updates,
    "--download-ffmpeg": download_ffmpeg,
}

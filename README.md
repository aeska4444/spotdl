<!--- mdformat-toc start --slug=github --->

<!---
!!! IF EDITING THE README, ENSURE TO COPY THE WHOLE FILE TO index.md in `/docs/`
--->

<div align="center">

# spotDL v4

Download your Spotify playlists and songs along with album art and metadata


</div>

______________________________________________________________________

**[Read the documentation on ReadTheDocs!](http://spotdl.rtfd.io/)**

______________________________________________________________________

## Prerequisites

- [Visual C++ 2019 redistributable](https://docs.microsoft.com/en-us/cpp/windows/latest-supported-vc-redist?view=msvc-170#visual-studio-2015-2017-2019-and-2022)
  **(on Windows)**
- Python 3.7 or above (added to PATH)

> **_YouTube Music must be available in your country for spotDL to work. This is because we use
> YouTube Music to filter search results. You can check if YouTube Music is available in your
> country, by visiting [YouTube Music](https://music.youtube.com)._**

## Installation

Refer to our [Installation Guide](https://spotdl.rtfd.io/en/latest/installation/) for more
details

- Python (**Recommended**)
  - _spotDL_ can be installed by running `pip install spotdl`.
  > On some systems you might have to change `pip` to `pip3`.



### Installing FFmpeg

If using FFmpeg only for spotDL, you can install FFmpeg to your local directory.
`spotdl --download-ffmpeg` will download FFmpeg to your spotDL installation directory.

We recommend the above option, but if you want to install FFmpeg system-wide,

- [Windows Tutorial](https://windowsloop.com/install-ffmpeg-windows-10/)
- OSX - `brew install ffmpeg`
- Linux - `sudo apt install ffmpeg` or use your distro's package manager

## Usage

To get started right away:

```sh
spotdl download [urls]
```


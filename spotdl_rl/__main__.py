"""
Main module for spotdl_rl. Exports version and main function.
"""

from spotdl_rl._version import __version__
from spotdl_rl.console import console_entry_point

if __name__ == "__main__":
    console_entry_point()

"""
Module for logging
"""

import logging

from rich import get_console
from rich.console import ConsoleRenderable
from rich.logging import RichHandler
from rich.markup import escape
from rich.text import Text
from rich.theme import Theme
from rich.traceback import install

__all__ = [
    "CRITICAL",
    "FATAL",
    "ERROR",
    "WARNING",
    "WARN",
    "INFO",
    "DEBUG",
    "MATCH",
    "NOTSET",
    "init_logging",
    "spotdl_rlFormatter",
    "LEVEL_TO_NAME",
    "NAME_TO_LEVEL",
]

# https://github.com/python/cpython/blob/3.10/Lib/logging/__init__.py
CRITICAL = 50
FATAL = CRITICAL
ERROR = 40
WARNING = 30
WARN = WARNING
INFO = 20
DEBUG = 10
MATCH = 5
NOTSET = 0

LEVEL_TO_NAME = {
    CRITICAL: "CRITICAL",
    ERROR: "ERROR",
    WARNING: "WARNING",
    INFO: "INFO",
    MATCH: "MATCH",
    DEBUG: "DEBUG",
    NOTSET: "NOTSET",
}

NAME_TO_LEVEL = {
    "CRITICAL": CRITICAL,
    "FATAL": FATAL,
    "ERROR": ERROR,
    "WARN": WARNING,
    "WARNING": WARNING,
    "INFO": INFO,
    "MATCH": MATCH,
    "DEBUG": DEBUG,
    "NOTSET": NOTSET,
}

THEME = Theme(
    {
        "bar.back": "grey23",
        "bar.complete": "rgb(165,66,129)",
        "bar.finished": "rgb(114,156,31)",
        "bar.pulse": "rgb(165,66,129)",
        "general": "green",
        "nonimportant": "rgb(40,100,40)",
        "progress.data.speed": "red",
        "progress.description": "none",
        "progress.download": "green",
        "progress.filesize": "green",
        "progress.filesize.total": "green",
        "progress.percentage": "green",
        "progress.remaining": "rgb(40,100,40)",
        "logging.level.debug": "blue",
        "logging.level.info": "green",
        "logging.level.warning": "yellow",
        "logging.level.error": "red",
        "logging.level.critical": "bold red",
    }
)


class spotdl_rlFormatter(logging.Formatter):
    """
    A custom logger for spotdl_rl.
    """

    def format(self, record: logging.LogRecord) -> str:
        """
        Format a log record.
        """

        result = escape(super().format(record))

        msg = result
        if record.levelno == DEBUG:
            msg = f"[blue]{result}"

        if record.levelno == MATCH:
            msg = f"[magenta]{result}"

        if record.levelno == INFO:
            msg = f"[green]{result}"

        if record.levelno == WARNING:
            msg = f"[yellow]{result}"

        if record.levelno == ERROR:
            msg = f"[red]{result}"

        if record.levelno == CRITICAL:
            msg = f"[bold red]{result}"

        return msg


class spotdl_rlHandler(RichHandler):
    """
    A custom logging handler for spotdl_rl.
    In this case, it's just a wrapper around the rich handler.
    To not highlight keywords in info messages
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def render_message(
        self, record: logging.LogRecord, message: str
    ) -> "ConsoleRenderable":
        """Render message text in to Text.

        ### Arguments
        - record: logging Record.
        - message: String containing log message.

        ### Returns
        - ConsoleRenderable: Renderable to display log message.
        """

        use_markup = getattr(record, "markup", self.markup)
        message_text = Text.from_markup(message) if use_markup else Text(message)

        highlighter = getattr(record, "highlighter", self.highlighter)

        # Don't highlight info messages
        if highlighter and record.levelno != INFO:
            message_text = highlighter(message_text)

        if self.keywords is None:
            self.keywords = self.KEYWORDS

        # Don't highlight keywords in info messages
        if self.keywords and record.levelno != INFO:
            message_text.highlight_words(self.keywords, "logging.keyword")

        return message_text


def init_logging(log_level: str):
    """
    Initialize logging for spotdl_rl.

    ### Arguments
    - `console`: The console to use.
    - `log_level`: The log level to use.
    """

    # Don't log too much
    logging.getLogger("requests").setLevel(logging.WARNING)
    logging.getLogger("urllib3").setLevel(logging.WARNING)
    logging.getLogger("spotipy").setLevel(logging.WARNING)
    logging.getLogger("asyncio").setLevel(logging.WARNING)
    logging.getLogger("syncedlyrics").setLevel(logging.WARNING)

    # Create console
    console = get_console()
    console.push_theme(THEME)

    # Add matching level loggers
    logging.addLevelName(MATCH, "MATCH")

    # Create a rich handler
    rich_handler = spotdl_rlHandler(
        show_time=log_level == "DEBUG",
        log_time_format="[%X]",
        omit_repeated_times=False,
        console=console,
        level=log_level,
        markup=True,
        show_path=log_level == "DEBUG",
        show_level=log_level == "DEBUG",
        rich_tracebacks=True,
    )

    msg_format = "%(message)s"
    if log_level == "DEBUG":
        msg_format = "%(threadName)s - %(message)s"

    # Add rich handler to spotdl_rl logger
    rich_handler.setFormatter(spotdl_rlFormatter(msg_format))

    # Create spotdl_rl logger
    spotdl_rl_logger = logging.getLogger("spotdl_rl")

    # Setup spotdl_rl logger
    spotdl_rl_logger.setLevel(log_level)
    spotdl_rl_logger.addHandler(rich_handler)

    # Install rich traceback handler
    install(show_locals=False, extra_lines=1, console=console)

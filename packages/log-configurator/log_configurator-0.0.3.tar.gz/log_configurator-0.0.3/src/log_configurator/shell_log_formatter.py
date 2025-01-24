"""Log formatter that prints colored to shell."""

import logging
from typing import ClassVar, Literal


class ColoredShellLogFormatter(logging.Formatter):
    """Formatter class."""

    SHELL_COLORS: ClassVar = {
        "NONE": "\033[0m",
        "DEBUG": "\033[0m",
        "INFO": "\033[0m",
        "HIGHLIGHT": "\033[36m",
        "WARNING": "\033[33m",
        "ERROR": "\033[31m",
        "CRITICAL": "\033[31m",
    }

    def __init__(
        self,
        colors: dict[str, str],
        fmt: str,
        style: Literal["%", "{"] = "%",
    ) -> None:
        super().__init__(fmt=fmt, style=style)
        self.formatters = {}
        self.default_formatter = logging.Formatter(
            "Requested Formatter not found! - {module}: {message}",
            style=style,
        )
        for loglevel, prefix in colors.items():
            self.formatters[loglevel] = logging.Formatter(
                ColoredShellLogFormatter.colorize(fmt, prefix),
                style=style,
            )

    def format(self, record: logging.LogRecord) -> str:
        """Format the log record."""
        formatter = self.formatters.get(record.levelname, self.default_formatter)
        return formatter.format(record)

    @staticmethod
    def colorize(text: str, color_name: str) -> str:
        """
        Colorize text.

        :param text: Text to colorize
        :param color_name: Color to use, check SHELL_COLORS
        :return: Colorized text
        """
        return color_name + text + ColoredShellLogFormatter.SHELL_COLORS["NONE"]

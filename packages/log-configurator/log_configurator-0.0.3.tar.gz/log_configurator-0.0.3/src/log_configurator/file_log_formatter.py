"""Log formatter that prints uncolored to a file."""

import logging
import re


class UncoloredFileLogFormatter(logging.Formatter):
    """Formatter class."""

    ansi_re = re.compile(r"\x1b\[[0-9;]*m")

    def format(self, record: logging.LogRecord) -> str:
        """Format the log record."""
        formatted = super().format(record)
        return re.sub(UncoloredFileLogFormatter.ansi_re, "", formatted)

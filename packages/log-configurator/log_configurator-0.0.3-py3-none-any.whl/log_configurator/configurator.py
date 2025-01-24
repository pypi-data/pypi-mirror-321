"""
Implements the logging configuration.

Simple configurator for the python logging package that allows simultaneous file and
shell logging.
"""

import logging
import sys
from io import StringIO
from pathlib import Path

from .file_log_formatter import UncoloredFileLogFormatter
from .shell_log_formatter import ColoredShellLogFormatter


def setup_root_logger(
    shell_log_lvl: str = "info",
    file_log_lvl: str = "debug",
    logfile: Path = Path("run.log"),
    *,
    shell_logging: bool = True,
    file_logging: bool = True,
) -> None:
    """
    Set up the root logger, so every created logger inherits the desired configuration.

    :param shell_logging: Enable/disable logging to STDOUT
    :param file_logging: Enable/disable logging to logfile
    :param shell_log_lvl: Severity threshold of shell logging
    :param file_log_lvl: Severity threshold of file logging
    :param logfile: Path to the logfile
    """
    logger = logging.getLogger()
    logging.root.setLevel(logging.NOTSET)

    if shell_logging:
        shell = logging.StreamHandler()
        shell.setLevel(shell_log_lvl.upper())
        color_dict = ColoredShellLogFormatter.SHELL_COLORS
        shell_format = ColoredShellLogFormatter(color_dict, "{message}", style="{")
        shell.setFormatter(shell_format)
        logger.addHandler(shell)

    if file_logging:
        logfile.parent.mkdir(parents=True, exist_ok=True)
        file = logging.FileHandler(logfile, mode="w")
        file.setLevel(file_log_lvl.upper())
        file_format = UncoloredFileLogFormatter(
            "{asctime} - {process} - {name} - {levelname} - {message}",
            style="{",
        )
        file.setFormatter(file_format)
        logger.addHandler(file)


def buffer_log() -> StringIO:
    """
    Buffer log before the setup function has been used.

    Buffered log is formatted by logging.basicConfig, buffered and can be logged after
    the logging
    has been set up.
    :return: Buffer storing the initial log
    """
    buffer = StringIO()
    logging.basicConfig(stream=buffer, level=logging.NOTSET)
    return buffer


def log_subprocess_output(pipe: bytes) -> None:
    """
    Log the output of a subprocess.

    :param pipe: Pipe to the subprocess
    """
    for line in pipe.decode(sys.stdout.encoding).split("\n"):
        # Beispiel: Erkennung und Zuweisung der Log-Ebene
        if line.startswith("CRITICAL"):
            logging.critical("\t%s", line[10:])
        elif line.startswith("ERROR"):
            logging.error("\t%s", line[7:])
        elif line.startswith("WARNING"):
            logging.warning("\t%s", line[9:])
        elif line.startswith("INFO"):
            logging.info("\t%s", line[6:])
        elif line.startswith("DEBUG"):
            logging.debug("\t%s", line[7:])
        else:
            logging.debug("\t%s", line)

import logging
import sys
import time
from typing import Optional

import tqdm

from s3ben.constants import (
    DEFAULT_LOG_DATE_FORMAT,
    DEFAULT_LOG_FORMAT,
    DEFAULT_LOG_FORMAT_DEBUG,
)


class TqdmLoggingHandler(logging.StreamHandler):
    """
    Avoid tqdm progress bar interruption by logger's output to console
    """

    def emit(self, record):
        try:
            msg = self.format(record)
            tqdm.tqdm.write(msg, end=self.terminator)
        except RecursionError:
            raise
        except Exception:  # pylint: disable=broad-except
            self.handleError(record)


def init_logger(
    name: str,
    level: str = "warning",
    log_format: str = None,
    date_format: str = DEFAULT_LOG_DATE_FORMAT,
) -> None:
    """
    Function to initialize logger and all needed parts

    :param str name: logger name to setup
    :param str level: Logging level
    :raises ValueError: If log level doens't exist
    :return: None
    """
    if not logging._checkLevel(level.upper()):
        raise ValueError(f"Log level {level} doesn't exist")
    set_level = logging.getLevelName(level.upper())
    if not log_format:
        log_format = (
            DEFAULT_LOG_FORMAT_DEBUG if level.lower() == "debug" else DEFAULT_LOG_FORMAT
        )
    set_format = logging.Formatter(log_format, datefmt=date_format)
    logger = logging.getLogger(name)
    logger.setLevel(set_level)
    console = TqdmLoggingHandler()
    # console = ProgrsssBarHandler()
    console.setFormatter(set_format)
    console.setLevel(set_level)
    logger.addHandler(console)


class ProgrsssBarHandler(logging.Handler):
    """
    Class to log to console when progress bar is shown
    """

    terminator = "\n"

    def __init__(self, stream=None) -> None:
        logging.Handler.__init__(self)
        self.stream = stream if stream else sys.stderr

    def emit(self, record) -> None:
        """
        Method overide
        """
        try:
            msg = self.format(record)
            self.stream.write("\033[1A")
            # self.stream.write("\x1b[2K")
            self.stream.write(msg)
            self.stream.flush()
            time.sleep(0.5)
            # self.stream.write(self.terminator)
            # self.stream.write("\033[A")
            # self.stream.write(msg + self.terminator)
            # self.stream.flush()

        except (KeyboardInterrupt, SystemExit):
            raise
        except Exception:
            self.handleError(record)

"""The module provides a wrapper to corese library (Software platform for the Semantic Web of Linked Data)"""

from .api import CoreseAPI

all = ['CoreseAPI']

# Read version of the package from the file
# that is in the project rood directory
from pathlib import Path

with open(Path(__file__).parent / "VERSION.txt") as _f:
    __version__ = _f.read().strip()

__version_info__ = tuple([ int(num) for num in __version__.split('.')])

import logging

# Default logging configuration
LOG_LEVEL = logging.INFO
LOG_FILE = 'PyCorese.log'  # Default log file name

def configure_logging(level=None, log_file=None):
    """
    Configures logging for the package. This function can be called to customize logging.

    :param level: The logging level, e.g., logging.DEBUG, logging.INFO. Default is logging.INFO.
    :param log_file: The log file path. If None, logs will only be output to console. Default is None.
    """
    handlers = [logging.StreamHandler()]  # Default handler for console output
    if log_file:
        handlers.append(logging.FileHandler(log_file))  # Add file handler if log_file is specified

    logging.basicConfig(level=level or LOG_LEVEL,
                        format='%(asctime)s - %(levelname)s - %(message)s',
                        handlers=handlers)

# Call the function with default values upon module import
configure_logging(LOG_LEVEL, LOG_FILE)

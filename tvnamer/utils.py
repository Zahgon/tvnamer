#!/usr/bin/env python

"""Utilities for tvnamer, including filename parsing
"""

import datetime
import os
import re
import sys
import shutil
import logging
import platform
import errno

from tvdb_api import Tvdb

import tvnamer
from tvnamer.config import Config
from tvnamer.tvnamer_exceptions import (
    InvalidPath,
    InvalidFilename,
    ShowNotFound,
    DataRetrievalError,
    SeasonNotFound,
    EpisodeNotFound,
    EpisodeNameNotFound,
    ConfigValueError,
    UserAbort,
)

from typing import Any, Dict, List, Optional, Union, Tuple, Pattern


LOG = logging.getLogger(__name__)


def warn(text):
    # type: (str) -> None
    """Displays message to sys.stderr
    """
    pass


def split_extension(filename):
    # type: (str) -> Tuple[str, str]
    pass


def _apply_replacements(cfile, replacements):
    # type: (str, List) -> str
    """Applies custom replacements.

    Argument cfile is string.

    Argument replacements is a list of dicts, with keys "match",
    "replacement", and (optional) "is_regex"
    """
    pass


def make_valid_filename(
    value,
    normalize_unicode=False,
    windows_safe=False,
    custom_blacklist=None,
    replace_with="_",
):
    # type: (str, bool, bool, Optional[str], str) -> str
    """
    Takes a string and makes it into a valid filename.

    normalize_unicode replaces accented characters with ASCII equivalent, and
    removes characters that cannot be converted sensibly to ASCII.

    windows_safe forces Windows-safe filenames, regardless of current platform

    custom_blacklist specifies additional characters that will removed. This
    will not touch the extension separator:

        >>> make_valid_filename("T.est.avi", custom_blacklist=".")
        'T_est.avi'
    """
    pass


def format_episode_numbers(episodenumbers):
    # type: (List[int]) -> str
    """Format episode number(s) into string, using configured values
    """
    pass

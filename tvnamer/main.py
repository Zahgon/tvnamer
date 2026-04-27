#!/usr/bin/env python

"""Main tvnamer utility functionality
"""

import os
import sys
import logging
import warnings

try:
    import readline
except ImportError:
    pass

import json

import tvdb_api
from typing import List, Union, Optional

from tvnamer import cliarg_parser, __version__
from tvnamer.config_defaults import defaults
from tvnamer.config import Config
from .files import FileFinder, FileParser, Renamer, _apply_replacements_input
from .utils import (
    warn,
    format_episode_numbers,
    make_valid_filename,
)
from tvnamer.data import (
    BaseInfo,
    EpisodeInfo,
    DatedEpisodeInfo,
    NoSeasonEpisodeInfo,
)

from tvnamer.tvnamer_exceptions import (
    ShowNotFound,
    SeasonNotFound,
    EpisodeNotFound,
    EpisodeNameNotFound,
    UserAbort,
    InvalidPath,
    NoValidFilesFoundError,
    SkipBehaviourAbort,
    InvalidFilename,
    DataRetrievalError,
)


LOG = logging.getLogger(__name__)


# Key for use in tvnamer only - other keys can easily be registered at https://thetvdb.com/api-information
TVNAMER_API_KEY = "fb51f9b848ffac9750bada89ecba0225"


def get_move_destination(episode):
    # type: (BaseInfo) -> str
    """Constructs the location to move/copy the file
    """
    def wrap_validfname(fname):
        pass
    pass


def do_rename_file(cnamer, new_name):
    # type: (Renamer, str) -> None
    """Renames the file. cnamer should be Renamer instance,
    new_name should be string containing new filename.
    """
    pass


def do_move_file(cnamer, dest_dir=None, dest_filepath=None, get_path_preview=False):
    # type: (Renamer, Optional[str], Optional[str], bool) -> Optional[str]
    """Moves file to dest_dir, or to dest_filepath
    """
    pass


def confirm(question, options, default="y"):
    # type: (str, List[str], str) -> str
    """Takes a question (string), list of options and a default value (used
    when user simply hits enter).
    Asks until valid option is entered.
    """
    pass


def process_file(tvdb_instance, episode):
    # type: (tvdb_api.Tvdb, BaseInfo) -> None
    """Gets episode name, prompts user for input
    """
    pass


def find_files(paths):
    # type: (List[str]) -> List[str]
    """Takes an array of paths, returns all files found
    """
    pass


def tvnamer(paths):
    # type: (List[str]) -> None
    """Main tvnamer function, takes an array of paths, does stuff.
    """
    pass


def main():
    # type: () -> None
    """Parses command line arguments, displays errors from tvnamer in terminal
    """
    pass


if __name__ == "__main__":
    main()

import os
import re
import errno
import shutil
import logging
import datetime
from typing import List, Pattern, Optional

from .config import Config
from .utils import _apply_replacements, warn, split_extension
from .data import BaseInfo, EpisodeInfo, DatedEpisodeInfo, AnimeEpisodeInfo, NoSeasonEpisodeInfo
from .tvnamer_exceptions import ConfigValueError, InvalidFilename, InvalidPath


LOG = logging.getLogger(__name__)


def _apply_replacements_input(cfile):
    # type: (str) -> str
    """Applies custom input filename replacements, wraps _apply_replacements
    """
    pass


def _apply_replacements_fullpath(cfile):
    # type: (str) -> str
    """Applies custom replacements to full path, wraps _apply_replacements
    """
    pass


def _replace_input_series_name(seriesname):
    # type: (str) -> str
    """allow specified replacements of series names

    in cases where default filenames match the wrong series,
    e.g. missing year gives wrong answer, or vice versa

    This helps the TVDB query get the right match.
    """
    pass


def intepret_year(value):
    # type: (str) -> int
    """Handle two-digit years with heuristic-ish guessing

    Assumes 50-99 becomes 1950-1999, and 0-49 becomes 2000-2049

    ..might need to rewrite this function in 2050, but that seems like
    a reasonable limitation
    """
    pass


def _clean_extracted_series_name(seriesname):
    # type: (str) -> str
    """Cleans up series name by removing any . and _
    characters, along with any trailing hyphens.

    Is basically equivalent to replacing all _ and . with a
    space, but handles decimal numbers in string, for example:

    >>> _clean_extracted_series_name("an.example.1.0.test")
    'an example 1.0 test'
    >>> _clean_extracted_series_name("an_example_1.0_test")
    'an example 1.0 test'
    """
    pass


class FileFinder(object):
    """Given a file, it will verify it exists. Given a folder it will descend
    one level into it and return a list of files, unless the recursive argument
    is True, in which case it finds all files contained within the path.

    The with_extension argument is a list of valid extensions, without leading
    spaces. If an empty list (or None) is supplied, no extension checking is
    performed.

    The filename_blacklist argument is a list of regexp strings to match against
    the filename (minus the extension). If a match is found, the file is skipped
    (e.g. for filtering out "sample" files). If [] or None is supplied, no
    filtering is done
    """

    def __init__(
        self, path, with_extension=None, filename_blacklist=None, recursive=False
    ):
        # type: (str, Optional[List[str]], Optional[List[str]], bool) -> None
        self.path = path
        if with_extension is None:
            self.with_extension = [] # type: List[str]
        else:
            self.with_extension = with_extension
        if filename_blacklist is None:
            self.with_blacklist = []
        else:
            self.with_blacklist = filename_blacklist
        self.recursive = recursive

    def find_files(self):
        # type: () -> List[str]
        """Returns list of files found at path
        """
        pass

    def _check_extension(self, fname):
        # type: (str) -> bool
        """Checks if the file extension is blacklisted in valid_extensions
        """
        pass

    def _blacklisted_filename(self, filepath):
        # type: (str) -> bool
        """Checks if the filename (optionally excluding extension)
        matches filename_blacklist

        self.with_blacklist should be a list of strings and/or dicts:

        a string, specifying an exact filename to ignore
        "filename_blacklist": [".DS_Store", "Thumbs.db"],

        a dictionary, where each dict contains:

        Key 'match' - (if the filename matches the pattern, the filename
        is blacklisted)

        Key 'is_regex' - if True, the pattern is treated as a
        regex. If False, simple substring check is used (if
        cur['match'] in filename). Default is False

        Key 'full_path' - if True, full path is checked. If False, only
        filename is checked. Default is False.

        Key 'exclude_extension' - if True, the extension is removed
        from the file before checking. Default is False.
        """
        pass

    def _find_files_in_path(self, startpath):
        # type: (str) -> List[str]
        """Finds files from startpath, could be called recursively
        """
        pass


class FileParser(object):
    """Deals with parsing of filenames
    """

    def __init__(self, path):
        # type: (str) -> None
        self.path = path
        self.compiled_regexs = [] # type: List[Pattern]
        self._compile_regexs()

    def _compile_regexs(self):
        # type: () -> None
        """Takes episode_patterns from config, compiles them all
        into self.compiled_regexs
        """
        pass

    def parse(self):
        # type: () -> BaseInfo
        """Runs path via configured regex, extracting data from groups.
        Returns an EpisodeInfo instance containing extracted data.
        """
        pass


def rename_file(old, new):
    # type: (str, str) -> None
    pass


def copy_file(old, new):
    # type: (str, str) -> None
    pass


def symlink_file(target, name):
    # type: (str, str) -> None
    pass


class Renamer(object):
    """Deals with renaming of files
    """

    def __init__(self, filename):
        # type: (str) -> None
        self.filename = os.path.abspath(filename)

    def new_path(
        self,
        new_path=None, # type: Optional[str]
        new_fullpath=None, # type: Optional[str]
        force=False, # type: bool
        always_copy=False, # type: bool
        always_move=False, # type: bool
        leave_symlink=False, # type: bool
        get_path_preview=False, # type: bool
    ):
        # type: (...) -> Optional[str]
        """Moves the file to a new path.

        If it is on the same partition, it will be moved (unless always_copy is True)
        If it is on a different partition, it will be copied, and the original
        only deleted if always_move is True.
        If the target file already exists, it will raise OSError unless force is True.
        If it was moved, a symlink will be left behind with the original name
        pointing to the file's new destination if leave_symlink is True.
        """
        pass

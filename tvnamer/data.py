import os
import re
import datetime
from abc import ABCMeta, abstractmethod
from typing import Optional, Dict, List, Union, Tuple, Any

import tvdb_api

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
from tvnamer.utils import (
    format_episode_numbers,
    make_valid_filename,
    split_extension,
    _apply_replacements, # FIXME
)


def _replace_output_series_name(seriesname):
    # type: (str) -> str
    """transform TVDB series names

    after matching from TVDB, transform the series name for desired abbreviation, etc.

    This affects the output filename.
    """
    pass



def _apply_replacements_output(cfile):
    # type: (str) -> str
    """Applies custom output filename replacements, wraps _apply_replacements
    """
    pass


def transform_filename(fname):
    # type: (str) -> str

    pass


def format_episode_name(names, join_with, multiep_format):
    # type: (List[str], str, str) -> str
    """
    Takes a list of episode names, formats them into a string.

    If two names are supplied, such as "Pilot (1)" and "Pilot (2)", the
    returned string will be "Pilot (1-2)". Note that the first number
    is not required, for example passing "Pilot" and "Pilot (2)" will
    also result in returning "Pilot (1-2)".

    If two different episode names are found, such as "The first", and
    "Something else" it will return "The first, Something else"
    """
    pass


class BaseInfo(metaclass=ABCMeta):
    """Base class for objects which store information (season, episode number, episode name), and contains
    logic to generate new name for each type of name
    """

    def __init__(
            self,
            filename, # type: Optional[str]
            episodename, # type: Optional[List[str]]
            extra,  # type: Optional[Dict[str, str]]
        ):
        # type: (...) -> None

        self.fullpath = filename
        if filename is not None:
            # Remains untouched, for use when renaming file
            self.originalfilename = os.path.basename(filename) # type: Optional[str]
        else:
            self.originalfilename = None

        self.episodename = episodename

        if extra is None:
            extra = {}
        self.extra = extra

    def fullpath_get(self):
        # type: () -> Optional[str]
        pass

    def fullpath_set(self, value):
        # type: (Optional[str]) -> None
        pass

    fullpath = property(fullpath_get, fullpath_set)

    @property
    def fullfilename(self):
        # type: () -> str
        pass

    @abstractmethod
    def getepdata(self):
        # type: () -> Dict[str, Optional[str]]
        pass

    @abstractmethod
    def number_string(self):
        # type: () -> str
        """Used in UI
        """
        pass

    @abstractmethod
    def sortable_info(self):
        # type: () -> Any
        """Returns a tuple of sortable information
        """
        pass

    def populate_from_tvdb(self, tvdb_instance, force_name=None, series_id=None):
        # mypy: ignore # type: (tvdb_api.Tvdb, Optional[Any], Optional[Any]) -> None
        """Queries the tvdb_api.Tvdb instance for episode name and corrected
        series name.
        If series cannot be found, it will warn the user. If the episode is not
        found, it will use the corrected show name and not set an episode name.
        If the site is unreachable, it will warn the user. If the user aborts
        it will catch tvdb_api's user abort error and raise tvnamer's
        """
        pass

    def format_name(self, epdata):
        # type: (Dict[str, Optional[str]]) -> str
        pass

    def generate_filename(self, preview_orig_filename=False):
        # type: (bool) -> str

        # FIXME: Move this into each subclass - too much hasattr/isinstance

        pass


class EpisodeInfo(BaseInfo):

    def __init__(
        self,
        seriesname,  # type: str
        seasonnumber,  # type: int
        episodenumbers,  # type: List[int]
        episodename=None,  # type: Optional[List[str]]
        filename=None,  # type: Optional[str]
        extra=None,  # type: Optional[Dict[str, str]]
        ):
        # type: (...) -> None

        super(EpisodeInfo, self).__init__(filename=filename, episodename=episodename, extra=extra)

        self.seriesname = seriesname
        self.seasonnumber = seasonnumber
        self.episodenumbers = episodenumbers
        self.episodename = episodename

    def sortable_info(self):
        # type: () -> Tuple[str, int, List[int]]
        """Returns a tuple of sortable information
        """
        pass

    def number_string(self):
        # type: () -> str
        """Used in UI
        """
        pass

    def getepdata(self):
        # type: () -> Dict[str, Optional[str]]
        """
        Uses the following config options:
        filename_with_episode # Filename when episode name is found
        filename_without_episode # Filename when no episode can be found
        episode_single # formatting for a single episode number
        episode_separator # used to join multiple episode numbers
        """
        pass

    def format_name(self, epdata):
        # type: (Dict[str, Optional[str]]) -> str
        pass

    def __repr__(self):
        # type: () -> str
        return "<%s: %r>" % (self.__class__.__name__, self.generate_filename())


class DatedEpisodeInfo(BaseInfo):
    def __init__(
        self,
        seriesname,  # type: str
        episodenumbers,  # type: List[datetime.date]
        episodename=None,  # type: Optional[List[str]]
        filename=None,  # type: Optional[str]
        extra=None,  # type: Optional[Dict[str, str]]
        ):
        # type: (...) -> None

        super(DatedEpisodeInfo, self).__init__(filename=filename, episodename=episodename, extra=extra)

        self.seriesname = seriesname
        self.episodenumbers = episodenumbers


    def sortable_info(self):
        # type: () -> Tuple[str, List[datetime.date]]
        """Returns a tuple of sortable information
        """
        pass

    def number_string(self):
        # type: () -> str
        """Used in UI
        """
        pass

    def getepdata(self):
        # type: () -> Dict[str, Optional[str]]
        # Format episode number into string, or a list

        pass

    def format_name(self, epdata,):
        # type: (Dict[str, Optional[str]]) -> str
        pass


class NoSeasonEpisodeInfo(BaseInfo):
    CFG_KEY_WITH_EP = "filename_with_episode_no_season"
    CFG_KEY_WITHOUT_EP = "filename_without_episode_no_season"

    def __init__(
        self,
        seriesname,  # type: str
        episodenumbers,  # type: List[int]
        episodename=None,  # type: Optional[List[str]]
        filename=None,  # type: Optional[str]
        extra=None,  # type: Optional[Dict[str, str]]
        ):
        # type: (...) -> None

        super(NoSeasonEpisodeInfo, self).__init__(filename=filename, episodename=episodename, extra=extra)
        self.seriesname = seriesname
        self.episodenumbers = episodenumbers
        self.fullpath = filename

    def sortable_info(self):
        # type: () -> Tuple[str, List[int]]
        """Returns a tuple of sortable information
        """
        pass

    def number_string(self):
        # type: () -> str
        """Used in UI
        """
        pass

    def getepdata(self):
        # type: () -> Dict[str, Optional[str]]
        pass

    def format_name(self, epdata):
        # type: (Dict[str, Optional[str]]) -> str
        pass


class AnimeEpisodeInfo(NoSeasonEpisodeInfo):
    CFG_KEY_WITH_EP = "filename_anime_with_episode"
    CFG_KEY_WITHOUT_EP = "filename_anime_without_episode"

    CFG_KEY_WITH_EP_NO_CRC = "filename_anime_with_episode_without_crc"
    CFG_KEY_WITHOUT_EP_NO_CRC = "filename_anime_without_episode_without_crc"

    def format_name(self, epdata):
        # type: (Dict[str, Optional[str]]) -> str
        pass

    def generate_filename(self, preview_orig_filename=False):
        # type: (bool) -> str
        pass

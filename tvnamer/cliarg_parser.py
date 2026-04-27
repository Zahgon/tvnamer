#!/usr/bin/env python

"""Constructs command line argument parser for tvnamer
"""

import optparse
from typing import Any, TYPE_CHECKING

if TYPE_CHECKING:
    from .config_defaults import TypedDefaults


class Group(object):
    """Simple helper context manager to add a group to an OptionParser
    """

    def __init__(self, parser, name):
        # type: (optparse.OptionParser, str) -> None
        self.parser = parser
        self.name = name
        self.group = optparse.OptionGroup(self.parser, name)

    def __enter__(self):
        # type: () -> optparse.OptionGroup
        return self.group

    def __exit__(self, *k, **kw):
        # type: (Any, Any) -> None
        self.parser.add_option_group(self.group)


def get_cli_parser(defaults):
    # type: (TypedDefaults) -> optparse.OptionParser
    pass

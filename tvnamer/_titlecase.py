#!/usr/bin/env python
# -*- coding: utf-8 -*-

# fmt: off

"""
Original Perl version by: John Gruber http://daringfireball.net/ 10 May 2008
Python version by Stuart Colville http://muffinresearch.co.uk
License: http://www.opensource.org/licenses/mit-license.php
"""

import re

__all__ = ['titlecase']
__version__ = '0.5.2'

SMALL = 'a|an|and|as|at|but|by|en|for|if|in|of|on|or|the|to|v\\.?|via|vs\\.?'
PUNCT = r"""!"#$%&'‘()*+,\-./:;?@[\\\]_`{|}~"""

SMALL_WORDS = re.compile(r'^(%s)$' % SMALL, re.I)
INLINE_PERIOD = re.compile(r'[a-z][.][a-z]', re.I)
UC_ELSEWHERE = re.compile(r'[%s]*?[a-zA-Z]+[A-Z]+?' % PUNCT)
CAPFIRST = re.compile(r"^[%s]*?([A-Za-z])" % PUNCT)
SMALL_FIRST = re.compile(r'^([%s]*)(%s)\b' % (PUNCT, SMALL), re.I)
SMALL_LAST = re.compile(r'\b(%s)[%s]?$' % (SMALL, PUNCT), re.I)
SUBPHRASE = re.compile(r'([:.;?!][ ])(%s)' % SMALL)
APOS_SECOND = re.compile(r"^[dol]{1}['‘]{1}[a-z]+$", re.I)
ALL_CAPS = re.compile(r'^[A-Z\s%s]+$' % PUNCT)
UC_INITIALS = re.compile(r"^(?:[A-Z]{1}\.{1}|[A-Z]{1}\.{1}[A-Z]{1})+$")
MAC_MC = re.compile(r"^([Mm]a?c)(\w+)")


def titlecase(text):
    """
    Titlecases input text

    This filter changes all words to Title Caps, and attempts to be clever
    about *un*capitalizing SMALL words like a/an/the in the input.

    The list of "SMALL words" which are not capped comes from
    the New York Times Manual of Style, plus 'vs' and 'v'.

    """
    pass

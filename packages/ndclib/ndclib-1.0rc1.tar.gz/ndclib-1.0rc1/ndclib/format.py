"""This file defines the different valid NDC formats using regex."""

import re
from enum import Enum

from .exceptions import InvalidNDCFormatException


class NDCFormat(Enum):
    """Define a list of NDC formats by their component lengths."""

    _4_4_2 = re.compile(r"^\d{4}\-\d{4}\-\d{2}$")
    _5_3_2 = re.compile(r"^\d{5}\-\d{3}\-\d{2}$")
    _5_4_1 = re.compile(r"^\d{5}\-\d{4}\-\d{1}$")
    _4_6 = re.compile(r"^\d{4}\-\d{6}$")
    _5_5 = re.compile(r"^\d{5}\-\d{5}$")
    _5_4_2 = re.compile(r"^\d{5}\-\d{4}\-\d{2}$")
    _10 = re.compile(r"^\d{10}$")
    _11 = re.compile(r"^\d{11}$")

    @classmethod
    def match(cls, ndc: str):
        """Match to an NDC format for a given input string NDC.

        Raises an InvalidNDCFormatException if the format is not valid.
        """
        for ndc_format in cls:
            if re.match(ndc_format.value, ndc):
                return ndc_format

        raise InvalidNDCFormatException(ndc)

"""
This file defines the different data providers usable by NDC objects to
perform format conversion and other operations. A base class, NDCProvider,
defines functionality. Each subclass should implement the get_ndc_format method,
which takes an unhyphenated, 11-digit NDC and uses the data provider to return
the associated NDCFormat.
"""

import re
from pathlib import Path

import requests

from .exceptions import *
from .format import NDCFormat


__all__ = ["RxNormAPIProvider", "MediSpanProvider"]


class NDCProvider:
    def get_ndc_format(self, ndc11: str) -> NDCFormat:
        """Given an unhyphenated, 11-digit NDC, return an NDCFormat."""
        raise MissingDataProviderException


class RxNormAPIProvider(NDCProvider):
    """A data provider for the RxNorm web API"""

    def __init__(
        self,
        api_base: str = "https://rxnav.nlm.nih.gov/REST/",
        endpoint: str = "ndcproperties.json",
    ):
        self.api_base = api_base
        self.endpoint = endpoint

    def get_ndc_format(self, ndc11: str) -> NDCFormat:
        """Given an unhyphenated, 11-digit NDC, return an NDCFormat.

        If no format can be matched, raise a MissingNDCFormatException.
        """
        data = {"id": ndc11, "ndcstatus": "ALL"}
        api_response = requests.get(self.api_base + self.endpoint, params=data)
        if ndc_properties := api_response.json().get("ndcPropertyList", None):
            ndc10 = ndc_properties["ndcProperty"][0]["ndc10"]
            return NDCFormat.match(ndc10)
        else:
            raise MissingNDCFormatException(ndc11, "Rx Norm Web API")


class MediSpanProvider(NDCProvider):
    """A data provider for the Medi-Span MEDNDC file"""

    def __init__(self, ndc_file: Path = Path.cwd() / "MEDNDC"):
        self.ndc_file = Path(ndc_file)

    @property
    def ndc_file(self):
        return self._ndc_file

    @ndc_file.setter
    def ndc_file(self, ndc_file: Path):
        """Store path to NDC file if it exists and is valid"""
        if ndc_file.is_file() and MediSpanProvider._is_valid_ndc_file(ndc_file):
            self._ndc_file = ndc_file

    @staticmethod
    def _code_to_format(medispan_format_id: int) -> NDCFormat:
        """Convert a Medi-Span format code to an NDCFormat."""
        format_table = {
            1: NDCFormat._4_4_2,
            2: NDCFormat._5_3_2,
            3: NDCFormat._5_4_1,
            4: NDCFormat._4_6,
            5: NDCFormat._5_5,
            6: NDCFormat._5_4_2,
        }
        return format_table[medispan_format_id]

    def get_ndc_format(self, ndc11: str) -> NDCFormat:
        """Given an unhyphenated, 11-digit NDC, return an NDCFormat.

        Each line in MEDNDC starts with an 11-digit NDC. We iterate through each
        line until we match the input NDC. On the matched line, character 53
        corresponds to the 1-digit integer Medi-Span uses to represent the
        NDC format. This is then converted to an NDCFormat using the
        _code_to_format method.

        If no format can be matched, raise a MissingNDCFormatException.
        """
        with open(self._ndc_file, "r") as f:
            for line in f.readlines():
                if line[0:11] == ndc11:
                    format_code = int(line[53])
                    return MediSpanProvider._code_to_format(format_code)

        raise MissingNDCFormatException(ndc11, "Medi-Span MEDNDC File")

    @staticmethod
    def _is_valid_ndc_file(ndc_file: Path) -> bool:
        """Validate the NDC file based on a regex."""
        with open(ndc_file, "r") as f:
            first_line = f.readline()

        # For now, we check if the first line is 128 characters followed by
        # a newline. In the future, we can become more sophisticated.
        line_pattern = re.compile(r"^.{128}\n$")

        if not re.match(line_pattern, first_line):
            return False
        else:
            return True

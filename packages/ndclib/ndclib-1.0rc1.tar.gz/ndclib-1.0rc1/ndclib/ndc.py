"""
This file contains classes representing NDCs. The BaseNDC class is a prototype.
Because conversion and representation of NDCs differs based on NDC format,
subclasses of BaseNDC are used to define behavior in three different cases:

| Input format           | Subclass         |
| ---------------------- | ---------------- |
| 10-digit, hyphenated   | HyphenatedNDC10  |
| 10-digit, unhyphenated | BareNDC10        |
| 11-digit, unhyphenated | NDC11            |

A generic NDC class exists to eliminate the need for format determination ahead
of time. When an NDC object is instantiated, it will automatically convert to
the correct subclass similar to how a pathlib Path converts to WindowsPath or
PosixPath depending on the operating environment.

A data provider is expected when some NDCs must be rendered in formats other
than their original. Set the data_provider class variable to an instance of a
subclass of NDCProvider. If the data_provider is not set, NDC objects can still
be created. We will try to lazily load the NDC format from the external data
provider when required for other functionality (usually, to display an NDC in a
different format). If the provider is not set at that time, we use the RxNorm
web API as the default and try again.
"""

from .exceptions import UndefinedOutputException
from .format import NDCFormat
from .provider import NDCProvider, RxNormAPIProvider


class BaseNDC:
    """A base class for NDCs."""

    _data_provider: NDCProvider = None

    def __init__(self, ndc: str):
        self._ndc = ndc
        self._ndc_format = self._calculate_format()

    def __str__(self):
        return self._ndc

    def __repr__(self):
        return f"{self.__class__.__name__}({self._ndc})"

    def __eq__(self, other):
        return self.ndc11 == other.ndc11

    def _calculate_format(self) -> NDCFormat:
        """Get an NDC format based on the length of its components."""
        raise NotImplementedError()

    def _retry_data_provider(self) -> None:
        """Try to calculate NDC format again if not done on instantiation.

        Some subclasses of BaseNDC require a data provider to be set when
        calculating the NDC format. This will happen automatically if the data
        provider is set before instantiating the NDC class. Otherwise, we
        can perform this calculation lazily using this method.
        """
        if not self._data_provider:
            self.__class__.set_provider()

        if not self._ndc_format:
            self._ndc_format = self._calculate_format()

    @staticmethod
    def set_provider(data_provider: NDCProvider = RxNormAPIProvider()):
        """Set the data provider for all subclasses of BaseNDC.

        If an instance of NDCProvider is not provided, use the RxNormAPIProvider
        as a sane default.
        """
        BaseNDC._data_provider = data_provider

    def to_10(self, hyphenated: bool = True) -> str:
        """Render the NDC as 10 digits, with or without hyphenation."""
        raise NotImplementedError()

    def to_11(self, hyphenated: bool = False) -> str:
        """Render the NDC as 11 digits, with or without hyphenation."""
        raise NotImplementedError()

    @property
    def ndc10(self) -> str:
        return self.to_10()

    @property
    def ndc11(self) -> str:
        return self.to_11()


class HyphenatedNDC10(BaseNDC):
    """Represent a hyphenated, 10-digit NDC."""

    def _calculate_format(self) -> NDCFormat:
        """Get an NDC format based on the length of its components."""
        return NDCFormat.match(self._ndc)

    def to_10(self, hyphenated: bool = True) -> str:
        """Render the NDC as 10 digits, with or without hyphenation."""
        if hyphenated:
            return self._ndc
        else:
            return self._ndc.replace("-", "")

    def to_11(self, hyphenated: bool = False) -> str:
        """Render the NDC as 11 digits, with or without hyphenation."""
        ndc = self._ndc.replace("-", "")
        processor = {
            NDCFormat._4_4_2: lambda n: f"0{n}",
            NDCFormat._5_3_2: lambda n: f"{n[:5]}0{n[5:]}",
            NDCFormat._5_4_1: lambda n: f"{n[:9]}0{n[9:]}",
            NDCFormat._4_6: lambda n: f"0{n}",
            NDCFormat._5_5: lambda n: f"{n[:5]}0{n[5:]}",
        }
        ndc11 = processor[self._ndc_format](ndc)

        upc_formats = [NDCFormat._5_5, NDCFormat._4_6]

        if hyphenated and self._ndc_format in upc_formats:
            raise UndefinedOutputException(self._ndc)
        elif hyphenated:
            return f"{ndc11[0:5]}-{ndc11[5:9]}-{ndc11[9:]}"
        else:
            return ndc11


class BareNDC10(BaseNDC):
    """Represent an unhyphenated, 10-digit NDC."""

    def _calculate_format(self) -> NDCFormat:
        """Get an NDC format based on the length of its components."""
        if self._data_provider:
            for test_ndc in self._calculate_possible_ndc11s():
                try:
                    return self._data_provider.get_ndc_format(test_ndc)
                except Exception:
                    pass

    def _calculate_possible_ndc11s(self) -> list[str]:
        """Calculate possible 11-digit NDCs for a 10-digit unhyphenated input.

        Used to feed to a data provider and determine which is the valid code.
        """
        n = self._ndc
        return [
            f"0{n}",  # 4-4-2
            f"{n[0:5]}0{n[5:]}",  # 5-3-2 or 5-5
            f"{n[0:9]}0{n[9:]}",  # 5-4-1
            f"0{n[0:4]}{n[4:]}",  # 4-6
        ]

    def to_10(self, hyphenated: bool = True) -> str:
        """Render the NDC as 10 digits, with or without hyphenation."""
        self._retry_data_provider()

        processor = {
            NDCFormat._4_4_2: lambda n: f"{n[0:4]}-{n[4:8]}-{n[8:]}",
            NDCFormat._5_3_2: lambda n: f"{n[0:5]}-{n[5:8]}-{n[8:]}",
            NDCFormat._5_4_1: lambda n: f"{n[0:5]}-{n[5:9]}-{n[9:]}",
            NDCFormat._4_6: lambda n: f"{n[0:4]}-{n[4:]}",
            NDCFormat._5_5: lambda n: f"{n[0:5]}-{n[5:]}",
        }
        ndc10 = processor[self._ndc_format](self._ndc)

        if hyphenated:
            return ndc10
        else:
            return ndc10.replace("-", "")

    def to_11(self, hyphenated: bool = False) -> str:
        """Render the NDC as 11 digits, with or without hyphenation."""
        self._retry_data_provider()

        processor = {
            NDCFormat._4_4_2: lambda n: f"0{n}",
            NDCFormat._5_3_2: lambda n: f"{n[:5]}0{n[5:]}",
            NDCFormat._5_4_1: lambda n: f"{n[:9]}0{n[9:]}",
            NDCFormat._4_6: lambda n: f"0{n}",
            NDCFormat._5_5: lambda n: f"{n[:5]}0{n[5:]}",
        }
        ndc11 = processor[self._ndc_format](self._ndc)

        if hyphenated:
            return f"{ndc11[0:5]}-{ndc11[5:9]}-{ndc11[9:]}"
        else:
            return ndc11


class NDC11(BaseNDC):
    """Represent an unhyphenated, 11-digit NDC."""

    def _calculate_format(self) -> NDCFormat:
        """Get an NDC format based on the length of its components."""
        if self._data_provider:
            return self._data_provider.get_ndc_format(self._ndc)

    def to_10(self, hyphenated: bool = True) -> str:
        """Render the NDC as 10 digits, with or without hyphenation."""
        self._retry_data_provider()

        processor = {
            NDCFormat._4_4_2: lambda n: f"{n[1:5]}-{n[5:9]}-{n[9:]}",
            NDCFormat._5_3_2: lambda n: f"{n[0:5]}-{n[6:9]}-{n[9:]}",
            NDCFormat._5_4_1: lambda n: f"{n[0:5]}-{n[5:9]}-{n[10:]}",
            NDCFormat._4_6: lambda n: f"{n[1:5]}-{n[5:]}",
            NDCFormat._5_5: lambda n: f"{n[0:5]}-{n[6:]}",
        }
        ndc10 = processor[self._ndc_format](self._ndc)

        if hyphenated:
            return ndc10
        else:
            return ndc10.replace("-", "")

    def to_11(self, hyphenated: bool = False) -> str:
        """Render the NDC as 11 digits, with or without hyphenation."""
        if hyphenated:
            return f"{self._ndc[0:5]}-{self._ndc[5:9]}-{self._ndc[9:]}"
        else:
            return self._ndc


class NDC(BaseNDC):
    """A generic class for an NDC in any format."""

    def __new__(cls, ndc: str):
        """Determine NDC format and use it to instantiate the right subclass."""
        ndc_format = NDCFormat.match(ndc)
        if ndc_format == NDCFormat._10:
            cls = BareNDC10
        elif ndc_format == NDCFormat._11:
            cls = NDC11
        elif ndc_format == NDCFormat._5_4_2:
            ndc = ndc.replace("-", "")
            cls = NDC11
        else:
            cls = HyphenatedNDC10

        instance = BaseNDC.__new__(cls)
        cls.__init__(instance, ndc)
        return instance

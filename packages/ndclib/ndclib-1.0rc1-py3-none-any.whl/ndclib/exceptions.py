"""This file contains custom exceptions for the NDC package."""


class InvalidNDCFormatException(Exception):
    """The input NDC is not in the correct format."""

    def __init__(self, ndc: str):
        self.ndc = ndc
        self.message = (
            f"The NDC '{self.ndc}' is not in a valid format. It must be 10 or "
            f"11 digits long, optionally with hyphens. Hyphenated NDCs must "
            f"match an FDA-approved format (i.e., 5-4-2, 4-4-2, 5-3-2, or "
            f"5-4-1)."
        )
        super().__init__(self.message)


class MissingNDCFormatException(Exception):
    """The data provider could not determine the format of the provided NDC."""

    def __init__(self, ndc: str, provider: str):
        self.ndc = ndc
        self.provider = provider
        self.message = (
            f"An NDC format could not be determined for NDC '{self.ndc}' using "
            f"the current data provider ({self.provider})."
        )
        super().__init__(self.message)


class MissingDataProviderException(Exception):
    """A data provider was not defined when required."""

    def __init__(self):
        self.message = "A data provider is required for this operation."
        super().__init__(self.message)


class UndefinedOutputException(Exception):
    """The output NDC format is not defined.

    Used when we try to convert a 5-5 or 6-4 input NDC (i.e., UPC) into a
    hyphenated, 11-digit format.
    """

    def __init__(self, ndc: str):
        self.ndc = ndc
        self.message = (
            f"The NDC '{self.ndc}' cannot be rendered in the requested format."
        )
        super().__init__(self.message)

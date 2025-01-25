# NDClib

NDClib is a Python library for representing National Drug Codes (NDCs). Using the library, NDCs can be represented as objects and trivially converted between common output formats (e.g., 10&ndash; and 11&ndash;digit). This eliminates the need to manually convert NDCs from disparate sources into the same format before manipulating or comparing them.

# Requirements

- Python 3.10 or newer

# Installation

```python
pip install ndclib
```

# Usage

## Define an NDC

Any NDC, irrespective of format (10&ndash; or 11&ndash;digit; hyphenated or unhyphenated), can be used to define an NDC object.

```python
from ndclib import NDC

package = NDC("0378-4517-93")
```

## Convert between formats

Once an NDC is defined, the `to_10()` or `to_11()` methods can be called to output the respective formatted strings. By default, the 10-digit format is hyphenated and the 11-digit format is not. Both methods take an optional boolean `hyphenated` parameter that can be used to control the output.

```python
NDC("0378-4517-93").to_11()
# "00378451793"

NDC("00378451793").to_10()
# "0378-4517-93"

NDC("00378451793").to_10(hyphenated=False)
# "0378451793"
```

For convenience, `ndc10` and `ndc11` properties are also available to output the same information as the respective methods using the default hyphenation setting.

```python
NDC("0378-4517-93").ndc11
# "00378451793"

NDC("00378451793").ndc10
# "0378-4517-93"
```

## Check for equality

NDCs objects can be compared for equality using the regular equality operator.

```python
NDC("0378-4517-93") == NDC("00378451793")
# True
```

## Use alternative data sources

If no data provider is explicitly set, NDClib uses the [RxNorm web API](https://lhncbc.nlm.nih.gov/RxNav/APIs/RxNormAPIs.html) to perform any necessary conversions between NDC formats. This may not always be the best option depending on the type of data being processed. For example, it may be important to identify Universal Product Codes (UPCs) in addition to NDCs when performing tasks involving non-drug products treated as if they were medications. Some alternative data providers can also identify UPC codes.

Attempting to process UPC (or any) data not available from the selected provider will result in an exception:

```python
NDC('11822079577').ndc10
# ndclib.exceptions.MissingNDCFormatException: An NDC format could not be determined for NDC '11822079577' using the current data provider (Rx Norm Web API).
```

### Medi-Span

To use the Medi-Span electronic drug file from Wolters Kluwer, extract the `MEDNDC` file and instantiate the `MediSpanProvider` class with a path to the file.

```python
from pathlib import Path
from ndc import MediSpanProvider

medispan = MediSpanProvider(
    Path("/path/to/MEDFPLS/USAENG/DB/MEDNDC")
)
```

Set the NDC provider to the Medi-Span provider.

```python
NDC.set_provider(medispan)
```

From this point on, all NDC objects will use the Medi-Span provider.

```python
NDC('11822079577').ndc10
# '11822-79577'
```

# Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

# License

This software is licensed under the [MIT License](LICENSE).
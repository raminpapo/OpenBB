# Documentation: openbb_platform/extensions/quantitative/openbb_quantitative/helpers.py

## File Metadata
- **Path**: `openbb_platform/extensions/quantitative/openbb_quantitative/helpers.py`
- **Size**: 2,581 characters, 81 lines
- **Words**: 255
- **Extension**: .py
- **Classification**: Text file

## Original Source

```python
"""Helper functions for Quantitative Analysis."""

from typing import TYPE_CHECKING, Union

if TYPE_CHECKING:
    from pandas import DataFrame, Series


# ruff: ignore=S310
def get_fama_raw(start_date: str, end_date: str) -> "DataFrame":
    """Get base Fama French data to calculate risk.

    Returns
    -------
    DataFrame
        A data with fama french model information
    """
    # pylint: disable=import-outside-toplevel
    from io import BytesIO
    from urllib.request import urlopen
    from zipfile import ZipFile

    from pandas import read_csv, to_datetime, to_numeric

    with urlopen(  # nosec  # noqa: S310 SIM117
        "https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/ftp/F-F_Research_Data_Factors_CSV.zip"
    ) as url:
        # Download Zipfile and create pandas DataFrame
        with ZipFile(BytesIO(url.read())) as zipfile:
            with zipfile.open("F-F_Research_Data_Factors.csv") as zip_open:
                df = read_csv(
                    zip_open,
                    header=0,
                    names=["Date", "MKT-RF", "SMB", "HML", "RF"],
                    skiprows=3,
                )

    df = df[df["Date"].apply(lambda x: len(str(x).strip()) == 6)]
    df["Date"] = df["Date"].astype(str) + "01"
    df["Date"] = to_datetime(df["Date"], format="%Y%m%d")
    df["MKT-RF"] = to_numeric(df["MKT-RF"], downcast="float")
    df["SMB"] = to_numeric(df["SMB"], downcast="float")
    df["HML"] = to_numeric(df["HML"], downcast="float")
    df["RF"] = to_numeric(df["RF"], downcast="float")
    df["MKT-RF"] = df["MKT-RF"] / 100
    df["SMB"] = df["SMB"] / 100
    df["HML"] = df["HML"] / 100
    df["RF"] = df["RF"] / 100
    df = df.set_index("Date")

    dt_start_date = to_datetime(start_date, format="%Y-%m-%d")
    if dt_start_date > df.index.max():
        raise ValueError(
            f"Start date '{dt_start_date}' is after the last date available for Fama-French '{df.index[-1]}'"
        )

    df = df.loc[start_date:end_date]  # type: ignore

    return df


def validate_window(input_data: Union["Series", "DataFrame"], window: int) -> None:
    """Validate the window input.

    Parameters
    ----------
    input_data : Union[Series, DataFrame]
        The input data to be validated.
    window : int
        The window to be validated.

    Raises
    ------
    ValueError
        If the window is greater than the input data length.
    """
    if window > len(input_data):
        raise ValueError(
            f"Window '{window}' is greater than the input data length '{len(input_data)}'"
        )

```

## High-Level Overview

Helper functions for Quantitative Analysis.

from typing import TYPE_CHECKING, Union

if TYPE_CHECKING:
from pandas import DataFrame, Series


# ruff: ignore=S310
def get_fama_raw(start_date: str, end_date: str) -> "DataFrame":
Get base Fama French data to calculate risk.

# pylint: disable=import-outside-toplevel
from io import BytesIO
from urllib.request import urlopen
from zipfile import ZipFile

from pandas import read_csv, to_datetime, to_numeric

with urlopen(  # nosec  # noqa: S310 SIM117

## Detailed Structure

### Python File Structure

**Classes** (0):
None

**Functions** (2):
`get_fama_raw`, `validate_window`

**Imports** (12):
`typing`, `TYPE_CHECKING`, `pandas`, `DataFrame`, `io`, `BytesIO`, `urllib.request`, `urlopen`, `zipfile`, `ZipFile`, `pandas`, `read_csv`


## Key Components

No major components extracted.

## Usage & Examples

See source code for usage details.

## Related Files

- `typing`
- `pandas`
- `io`
- `urllib.request`
- `zipfile`
- `pandas`

## Notes
- Generated: 2025-11-18T07:54:36.312584
- Generator: World's Best Repo Book Generator v1.0.0

# Documentation: openbb_platform/obbject_extensions/charting/openbb_charting/core/plotly_ta/ta_helpers.py

## File Metadata
- **Path**: `openbb_platform/obbject_extensions/charting/openbb_charting/core/plotly_ta/ta_helpers.py`
- **Size**: 1,502 characters, 53 lines
- **Words**: 182
- **Extension**: .py
- **Classification**: Text file

## Original Source

```python
"""Helper functions for technical analysis indicators."""

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from pandas import DataFrame


def check_columns(
    data: "DataFrame", high: bool = True, low: bool = True, close: bool = True
) -> str | None:
    """Return the close columns, or None if the dataframe does not have required columns.

    Parameters
    ----------
    data: DataFrame
        The dataframe to check
    high: bool
        Whether to check for high column
    low: bool
        Whether to check for low column
    close: bool
        Whether to check for close column

    Returns
    -------
    Optional[str]
        The name of the close column, none if df is invalid
    """
    # pylint: disable=import-outside-toplevel
    import re

    close_regex = r"(Adj\sClose|adj_close|Close)"
    # pylint: disable=too-many-boolean-expressions
    if (
        (re.findall(r"High", str(data.columns), re.IGNORECASE) is None and high)
        or (re.findall(r"Low", str(data.columns), re.IGNORECASE) is None and low)
        or (close_col := re.findall(close_regex, str(data.columns), re.IGNORECASE))
        is None
        and close
    ):
        raise ValueError(
            " Please make sure that the columns 'High', 'Low', and 'Close' are in the dataframe."
        )

    close_col = [col for col in close_col if col in data.columns]

    # giving priority to the standard close column
    if "close" in close_col:
        return "close"

    return close_col[-1]

```

## High-Level Overview

Helper functions for technical analysis indicators.

from typing import TYPE_CHECKING

if TYPE_CHECKING:
from pandas import DataFrame


def check_columns(
data: "DataFrame", high: bool = True, low: bool = True, close: bool = True
) -> str | None:
Return the close columns, or None if the dataframe does not have required columns.

# pylint: disable=import-outside-toplevel
import re

close_regex = r"(Adj\sClose|adj_close|Close)"
# pylint: disable=too-many-boolean-expressions
if (
(re.findall(r"High", str(data.columns), re.IGNORECASE) is None and high)

## Detailed Structure

### Python File Structure

**Classes** (0):
None

**Functions** (1):
`check_columns`

**Imports** (5):
`typing`, `TYPE_CHECKING`, `pandas`, `DataFrame`, `re`


## Key Components

No major components extracted.

## Usage & Examples

See source code for usage details.

## Related Files

- `typing`
- `pandas`
- `re`

## Notes
- Generated: 2025-11-18T07:54:37.154252
- Generator: World's Best Repo Book Generator v1.0.0

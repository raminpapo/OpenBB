# File Documentation: ta_helpers.py

## Metadata
- **Path**: `openbb_platform/obbject_extensions/charting/openbb_charting/core/plotly_ta/ta_helpers.py`
- **Size**: 1,502 bytes
- **Lines**: 53
- **Category**: python
- **Extension**: .py

---

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



---

## High-Level Overview

This is a **python** file named `ta_helpers.py`.

**Python Module**

- **Functions** (1): check_columns
- **Import Statements**: 3


---

## Detailed Analysis

### Python Code Structure



---

## Related Files

The following files may be related based on imports and references:

**Imported Modules**:
- `DataFrame`
- `TYPE_CHECKING`
- `pandas`
- `re`
- `typing`


---

## Performance & Security Notes

No obvious security concerns detected in static analysis.


---

**Generated**: 2025-11-19T02:16:48.202188Z
**Generator**: World's Best Repo Book Generator v1.0

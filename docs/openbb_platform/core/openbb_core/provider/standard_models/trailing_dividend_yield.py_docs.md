# File Documentation: trailing_dividend_yield.py

## Metadata
- **Path**: `openbb_platform/core/openbb_core/provider/standard_models/trailing_dividend_yield.py`
- **Size**: 909 bytes
- **Lines**: 29
- **Category**: python
- **Extension**: .py

---

## Original Source

```python
"""Trailing Dividend Yield Standard Model."""

from datetime import date as dateType

from openbb_core.provider.abstract.data import Data
from openbb_core.provider.abstract.query_params import QueryParams
from openbb_core.provider.utils.descriptions import (
    DATA_DESCRIPTIONS,
    QUERY_DESCRIPTIONS,
)
from pydantic import Field


class TrailingDivYieldQueryParams(QueryParams):
    """Trailing Dividend Yield Query."""

    symbol: str = Field(description=QUERY_DESCRIPTIONS.get("symbol", ""))
    limit: int | None = Field(
        default=252,
        description=f"{QUERY_DESCRIPTIONS.get('limit', '')} Default is 252, the number of trading days in a year.",
    )


class TrailingDivYieldData(Data):
    """Trailing Dividend Yield Data."""

    date: dateType = Field(description=DATA_DESCRIPTIONS.get("date", ""))
    trailing_dividend_yield: float = Field(description="Trailing dividend yield.")

```



---

## High-Level Overview

This is a **python** file named `trailing_dividend_yield.py`.

**Python Module**

- **Classes** (2): TrailingDivYieldQueryParams, TrailingDivYieldData
- **Import Statements**: 2


---

## Detailed Analysis

### Python Code Structure

#### Classes

- **`TrailingDivYieldQueryParams`**(QueryParams)
- **`TrailingDivYieldData`**(Data)


---

## Related Files

The following files may be related based on imports and references:

**Imported Modules**:
- `Data`
- `Field`
- `QueryParams`
- `date`
- `datetime`
- `openbb_core.provider.abstract.data`
- `openbb_core.provider.abstract.query_params`
- `openbb_core.provider.utils.descriptions`
- `pydantic`


---

## Performance & Security Notes

No obvious security concerns detected in static analysis.


---

**Generated**: 2025-11-19T02:16:46.587233Z
**Generator**: World's Best Repo Book Generator v1.0

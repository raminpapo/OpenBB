# File Documentation: calendar_ipo.py

## Metadata
- **Path**: `openbb_platform/core/openbb_core/provider/standard_models/calendar_ipo.py`
- **Size**: 1,193 bytes
- **Lines**: 42
- **Category**: python
- **Extension**: .py

---

## Original Source

```python
"""IPO Calendar Standard Model."""

from datetime import date as dateType

from openbb_core.provider.abstract.data import Data
from openbb_core.provider.abstract.query_params import QueryParams
from openbb_core.provider.utils.descriptions import (
    DATA_DESCRIPTIONS,
    QUERY_DESCRIPTIONS,
)
from pydantic import Field


class CalendarIpoQueryParams(QueryParams):
    """IPO Calendar Query."""

    symbol: str | None = Field(
        description=QUERY_DESCRIPTIONS.get("symbol", ""), default=None
    )
    start_date: dateType | None = Field(
        description=QUERY_DESCRIPTIONS.get("start_date", ""), default=None
    )
    end_date: dateType | None = Field(
        description=QUERY_DESCRIPTIONS.get("end_date", ""), default=None
    )
    limit: int | None = Field(
        description=QUERY_DESCRIPTIONS.get("limit", ""), default=100
    )


class CalendarIpoData(Data):
    """IPO Calendar Data."""

    symbol: str | None = Field(
        default=None,
        description=DATA_DESCRIPTIONS.get("symbol", ""),
    )
    ipo_date: dateType | None = Field(
        description="The date of the IPO, when the stock first trades on a major exchange.",
        default=None,
    )

```



---

## High-Level Overview

This is a **python** file named `calendar_ipo.py`.

**Python Module**

- **Classes** (2): CalendarIpoQueryParams, CalendarIpoData
- **Import Statements**: 2


---

## Detailed Analysis

### Python Code Structure

#### Classes

- **`CalendarIpoQueryParams`**(QueryParams)
- **`CalendarIpoData`**(Data)


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

**Generated**: 2025-11-19T02:16:46.367800Z
**Generator**: World's Best Repo Book Generator v1.0

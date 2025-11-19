# File Documentation: calendar_splits.py

## Metadata
- **Path**: `openbb_platform/core/openbb_core/provider/standard_models/calendar_splits.py`
- **Size**: 1,015 bytes
- **Lines**: 32
- **Category**: python
- **Extension**: .py

---

## Original Source

```python
"""Calendar Splits Standard Model."""

from datetime import date as dateType

from openbb_core.provider.abstract.data import Data
from openbb_core.provider.abstract.query_params import QueryParams
from openbb_core.provider.utils.descriptions import (
    DATA_DESCRIPTIONS,
    QUERY_DESCRIPTIONS,
)
from pydantic import Field


class CalendarSplitsQueryParams(QueryParams):
    """Calendar Splits Query."""

    start_date: dateType | None = Field(
        description=QUERY_DESCRIPTIONS.get("start_date", ""), default=None
    )
    end_date: dateType | None = Field(
        description=QUERY_DESCRIPTIONS.get("end_date", ""), default=None
    )


class CalendarSplitsData(Data):
    """Calendar Splits Data."""

    date: dateType = Field(description=DATA_DESCRIPTIONS.get("date", ""))
    symbol: str = Field(description=DATA_DESCRIPTIONS.get("symbol", ""))
    numerator: float = Field(description="Numerator of the stock split.")
    denominator: float = Field(description="Denominator of the stock split.")

```



---

## High-Level Overview

This is a **python** file named `calendar_splits.py`.

**Python Module**

- **Classes** (2): CalendarSplitsQueryParams, CalendarSplitsData
- **Import Statements**: 2


---

## Detailed Analysis

### Python Code Structure

#### Classes

- **`CalendarSplitsQueryParams`**(QueryParams)
- **`CalendarSplitsData`**(Data)


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

**Generated**: 2025-11-19T02:16:46.369077Z
**Generator**: World's Best Repo Book Generator v1.0

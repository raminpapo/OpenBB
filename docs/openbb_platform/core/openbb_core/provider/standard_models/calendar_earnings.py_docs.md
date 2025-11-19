# File Documentation: calendar_earnings.py

## Metadata
- **Path**: `openbb_platform/core/openbb_core/provider/standard_models/calendar_earnings.py`
- **Size**: 1,256 bytes
- **Lines**: 39
- **Category**: python
- **Extension**: .py

---

## Original Source

```python
"""Earnings Calendar Standard Model."""

from datetime import date as dateType

from openbb_core.provider.abstract.data import Data
from openbb_core.provider.abstract.query_params import QueryParams
from openbb_core.provider.utils.descriptions import (
    DATA_DESCRIPTIONS,
    QUERY_DESCRIPTIONS,
)
from pydantic import Field


class CalendarEarningsQueryParams(QueryParams):
    """Earnings Calendar Query."""

    start_date: dateType | None = Field(
        default=None, description=QUERY_DESCRIPTIONS.get("start_date", "")
    )
    end_date: dateType | None = Field(
        default=None, description=QUERY_DESCRIPTIONS.get("end_date", "")
    )


class CalendarEarningsData(Data):
    """Earnings Calendar Data."""

    report_date: dateType = Field(description="The date of the earnings report.")
    symbol: str = Field(description=DATA_DESCRIPTIONS.get("symbol", ""))
    name: str | None = Field(description="Name of the entity.", default=None)
    eps_previous: float | None = Field(
        default=None,
        description="The earnings-per-share from the same previously reported period.",
    )
    eps_consensus: float | None = Field(
        default=None,
        description="The analyst conesus earnings-per-share estimate.",
    )

```



---

## High-Level Overview

This is a **python** file named `calendar_earnings.py`.

**Python Module**

- **Classes** (2): CalendarEarningsQueryParams, CalendarEarningsData
- **Import Statements**: 2


---

## Detailed Analysis

### Python Code Structure

#### Classes

- **`CalendarEarningsQueryParams`**(QueryParams)
- **`CalendarEarningsData`**(Data)


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

**Generated**: 2025-11-19T02:16:46.364493Z
**Generator**: World's Best Repo Book Generator v1.0

# File Documentation: calendar_events.py

## Metadata
- **Path**: `openbb_platform/core/openbb_core/provider/standard_models/calendar_events.py`
- **Size**: 929 bytes
- **Lines**: 32
- **Category**: python
- **Extension**: .py

---

## Original Source

```python
"""Company Events Calendar Standard Model."""

from datetime import date as dateType

from openbb_core.provider.abstract.data import Data
from openbb_core.provider.abstract.query_params import QueryParams
from openbb_core.provider.utils.descriptions import (
    DATA_DESCRIPTIONS,
    QUERY_DESCRIPTIONS,
)
from pydantic import Field


class CalendarEventsQueryParams(QueryParams):
    """Company Events Calendar Query."""

    start_date: dateType | None = Field(
        default=None, description=QUERY_DESCRIPTIONS.get("start_date", "")
    )
    end_date: dateType | None = Field(
        default=None, description=QUERY_DESCRIPTIONS.get("end_date", "")
    )


class CalendarEventsData(Data):
    """Company Events Calendar Data."""

    date: dateType = Field(
        description=DATA_DESCRIPTIONS.get("date", "") + " The date of the event."
    )
    symbol: str = Field(description=DATA_DESCRIPTIONS.get("symbol", ""))

```



---

## High-Level Overview

This is a **python** file named `calendar_events.py`.

**Python Module**

- **Classes** (2): CalendarEventsQueryParams, CalendarEventsData
- **Import Statements**: 2


---

## Detailed Analysis

### Python Code Structure

#### Classes

- **`CalendarEventsQueryParams`**(QueryParams)
- **`CalendarEventsData`**(Data)


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

**Generated**: 2025-11-19T02:16:46.366204Z
**Generator**: World's Best Repo Book Generator v1.0

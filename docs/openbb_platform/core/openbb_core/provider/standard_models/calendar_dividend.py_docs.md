# File Documentation: calendar_dividend.py

## Metadata
- **Path**: `openbb_platform/core/openbb_core/provider/standard_models/calendar_dividend.py`
- **Size**: 1,549 bytes
- **Lines**: 48
- **Category**: python
- **Extension**: .py

---

## Original Source

```python
"""Dividend Calendar Standard Model."""

from datetime import date as dateType

from openbb_core.provider.abstract.data import Data
from openbb_core.provider.abstract.query_params import QueryParams
from openbb_core.provider.utils.descriptions import (
    DATA_DESCRIPTIONS,
    QUERY_DESCRIPTIONS,
)
from pydantic import Field


class CalendarDividendQueryParams(QueryParams):
    """Dividend Calendar Query."""

    start_date: dateType | None = Field(
        default=None, description=QUERY_DESCRIPTIONS.get("start_date", "")
    )
    end_date: dateType | None = Field(
        default=None, description=QUERY_DESCRIPTIONS.get("end_date", "")
    )


class CalendarDividendData(Data):
    """Dividend Calendar Data."""

    ex_dividend_date: dateType = Field(
        description="The ex-dividend date - the date on which the stock begins trading without rights to the dividend."
    )
    symbol: str = Field(description=DATA_DESCRIPTIONS.get("symbol", ""))
    amount: float | None = Field(
        default=None, description="The dividend amount per share."
    )
    name: str | None = Field(default=None, description="Name of the entity.")
    record_date: dateType | None = Field(
        default=None,
        description="The record date of ownership for eligibility.",
    )
    payment_date: dateType | None = Field(
        default=None,
        description="The payment date of the dividend.",
    )
    declaration_date: dateType | None = Field(
        default=None,
        description="Declaration date of the dividend.",
    )

```



---

## High-Level Overview

This is a **python** file named `calendar_dividend.py`.

**Python Module**

- **Classes** (2): CalendarDividendQueryParams, CalendarDividendData
- **Import Statements**: 2


---

## Detailed Analysis

### Python Code Structure

#### Classes

- **`CalendarDividendQueryParams`**(QueryParams)
- **`CalendarDividendData`**(Data)


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

**Generated**: 2025-11-19T02:16:46.362950Z
**Generator**: World's Best Repo Book Generator v1.0

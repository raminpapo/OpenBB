# File Documentation: futures_historical.py

## Metadata
- **Path**: `openbb_platform/core/openbb_core/provider/standard_models/futures_historical.py`
- **Size**: 1,819 bytes
- **Lines**: 54
- **Category**: python
- **Extension**: .py

---

## Original Source

```python
"""Futures Historical Price Standard Model."""

from datetime import date, datetime

from dateutil import parser
from openbb_core.provider.abstract.data import Data
from openbb_core.provider.abstract.query_params import QueryParams
from openbb_core.provider.utils.descriptions import (
    DATA_DESCRIPTIONS,
    QUERY_DESCRIPTIONS,
)
from pydantic import Field, field_validator


class FuturesHistoricalQueryParams(QueryParams):
    """Futures Historical Price Query."""

    symbol: str = Field(description=QUERY_DESCRIPTIONS.get("symbol", ""))
    start_date: date | None = Field(
        default=None,
        description=QUERY_DESCRIPTIONS.get("start_date", ""),
    )
    end_date: date | None = Field(
        default=None,
        description=QUERY_DESCRIPTIONS.get("end_date", ""),
    )
    expiration: str | None = Field(
        default=None,
        description="Future expiry date with format YYYY-MM",
    )

    @field_validator("symbol", mode="before", check_fields=False)
    @classmethod
    def to_upper(cls, v: str) -> str:
        """Convert field to uppercase."""
        return v.upper()


class FuturesHistoricalData(Data):
    """Futures Historical Price Data."""

    date: datetime = Field(description=DATA_DESCRIPTIONS.get("date", ""))
    open: float = Field(description=DATA_DESCRIPTIONS.get("open", ""))
    high: float = Field(description=DATA_DESCRIPTIONS.get("high", ""))
    low: float = Field(description=DATA_DESCRIPTIONS.get("low", ""))
    close: float = Field(description=DATA_DESCRIPTIONS.get("close", ""))
    volume: float = Field(description=DATA_DESCRIPTIONS.get("volume", ""))

    @field_validator("symbol", mode="before", check_fields=False)
    @classmethod
    def date_validate(cls, v):
        """Return formatted datetime."""
        return parser.isoparse(str(v))

```



---

## High-Level Overview

This is a **python** file named `futures_historical.py`.

**Python Module**

- **Classes** (2): FuturesHistoricalQueryParams, FuturesHistoricalData
- **Functions** (2): to_upper, date_validate
- **Import Statements**: 2


---

## Detailed Analysis

### Python Code Structure

#### Classes

- **`FuturesHistoricalQueryParams`**(QueryParams)
- **`FuturesHistoricalData`**(Data)

#### Functions

- **`date_validate(cls, v)`**

#### Decorators Used

classmethod, field_validator


---

## Related Files

The following files may be related based on imports and references:

**Imported Modules**:
- `Data`
- `Field`
- `QueryParams`
- `date`
- `datetime`
- `dateutil`
- `openbb_core.provider.abstract.data`
- `openbb_core.provider.abstract.query_params`
- `openbb_core.provider.utils.descriptions`
- `parser`
- `pydantic`


---

## Performance & Security Notes

No obvious security concerns detected in static analysis.


---

**Generated**: 2025-11-19T02:16:46.478262Z
**Generator**: World's Best Repo Book Generator v1.0

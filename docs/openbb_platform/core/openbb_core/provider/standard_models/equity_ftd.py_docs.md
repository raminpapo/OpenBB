# File Documentation: equity_ftd.py

## Metadata
- **Path**: `openbb_platform/core/openbb_core/provider/standard_models/equity_ftd.py`
- **Size**: 1,703 bytes
- **Lines**: 60
- **Category**: python
- **Extension**: .py

---

## Original Source

```python
"""Equity FTD Standard Model."""

from datetime import (
    date as dateType,
    datetime,
)

from openbb_core.provider.abstract.data import Data
from openbb_core.provider.abstract.query_params import QueryParams
from openbb_core.provider.utils.descriptions import (
    DATA_DESCRIPTIONS,
    QUERY_DESCRIPTIONS,
)
from pydantic import Field, field_validator


class EquityFtdQueryParams(QueryParams):
    """Equity FTD Query."""

    symbol: str = Field(description=QUERY_DESCRIPTIONS.get("symbol", ""))

    @field_validator("symbol", mode="before", check_fields=False)
    @classmethod
    def to_upper(cls, v: str):
        """Convert field to uppercase."""
        return v.upper()


class EquityFtdData(Data):
    """Equity FTD Data."""

    settlement_date: dateType | None = Field(
        description="The settlement date of the fail.", default=None
    )
    symbol: str | None = Field(
        description=DATA_DESCRIPTIONS.get("symbol", ""),
        default=None,
    )
    cusip: str | None = Field(
        description="CUSIP of the Security.",
        default=None,
    )
    quantity: int | None = Field(
        description="The number of fails on that settlement date.",
        default=None,
    )
    price: float | None = Field(
        description="The price at the previous closing price from the settlement date.",
        default=None,
    )
    description: str | None = Field(
        description="The description of the Security.",
        default=None,
    )

    @field_validator("settlement_date", mode="before")
    def date_validate(cls, v):  # pylint: disable=E0213
        """Return the date as a datetime object."""
        return datetime.strftime(v, "%Y-%m-%d")

```



---

## High-Level Overview

This is a **python** file named `equity_ftd.py`.

**Python Module**

- **Classes** (2): EquityFtdQueryParams, EquityFtdData
- **Functions** (2): to_upper, date_validate
- **Import Statements**: 2


---

## Detailed Analysis

### Python Code Structure

#### Classes

- **`EquityFtdQueryParams`**(QueryParams)
- **`EquityFtdData`**(Data)

#### Functions

- **`to_upper(cls, v: str)`**
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
- `datetime`
- `openbb_core.provider.abstract.data`
- `openbb_core.provider.abstract.query_params`
- `openbb_core.provider.utils.descriptions`
- `pydantic`


---

## Performance & Security Notes

No obvious security concerns detected in static analysis.


---

**Generated**: 2025-11-19T02:16:46.417370Z
**Generator**: World's Best Repo Book Generator v1.0

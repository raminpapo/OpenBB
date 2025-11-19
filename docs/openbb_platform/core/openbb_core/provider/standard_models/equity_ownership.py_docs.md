# File Documentation: equity_ownership.py

## Metadata
- **Path**: `openbb_platform/core/openbb_core/provider/standard_models/equity_ownership.py`
- **Size**: 1,185 bytes
- **Lines**: 36
- **Category**: python
- **Extension**: .py

---

## Original Source

```python
"""Equity Ownership Standard Model."""

from datetime import date as dateType

from openbb_core.provider.abstract.data import Data
from openbb_core.provider.abstract.query_params import QueryParams
from openbb_core.provider.utils.descriptions import (
    DATA_DESCRIPTIONS,
    QUERY_DESCRIPTIONS,
)
from pydantic import Field, field_validator


class EquityOwnershipQueryParams(QueryParams):
    """Equity Ownership Query."""

    symbol: str = Field(description=QUERY_DESCRIPTIONS.get("symbol", ""))

    @field_validator("symbol", mode="before", check_fields=False)
    @classmethod
    def to_upper(cls, v: str) -> str:
        """Convert field to uppercase."""
        return v.upper()


class EquityOwnershipData(Data):
    """Equity Ownership Data."""

    investor_name: str = Field(description="Investing entity's name.")
    cik: str | None = Field(default=None, description=DATA_DESCRIPTIONS.get("cik", ""))
    date: dateType = Field(
        description=DATA_DESCRIPTIONS.get("date", "") + " For the period ending."
    )
    filing_date: dateType | None = Field(description="Date when reported.")
    symbol: str = Field(description=DATA_DESCRIPTIONS.get("symbol", ""))

```



---

## High-Level Overview

This is a **python** file named `equity_ownership.py`.

**Python Module**

- **Classes** (2): EquityOwnershipQueryParams, EquityOwnershipData
- **Functions** (1): to_upper
- **Import Statements**: 2


---

## Detailed Analysis

### Python Code Structure

#### Classes

- **`EquityOwnershipQueryParams`**(QueryParams)
- **`EquityOwnershipData`**(Data)

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
- `openbb_core.provider.abstract.data`
- `openbb_core.provider.abstract.query_params`
- `openbb_core.provider.utils.descriptions`
- `pydantic`


---

## Performance & Security Notes

No obvious security concerns detected in static analysis.


---

**Generated**: 2025-11-19T02:16:46.424318Z
**Generator**: World's Best Repo Book Generator v1.0

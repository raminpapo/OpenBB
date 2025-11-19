# File Documentation: government_trades.py

## Metadata
- **Path**: `openbb_platform/core/openbb_core/provider/standard_models/government_trades.py`
- **Size**: 1,460 bytes
- **Lines**: 48
- **Category**: python
- **Extension**: .py

---

## Original Source

```python
"""Government Trades Standard Model."""

from datetime import date as dateType
from typing import Literal

from openbb_core.provider.abstract.data import Data
from openbb_core.provider.abstract.query_params import QueryParams
from openbb_core.provider.utils.descriptions import (
    DATA_DESCRIPTIONS,
    QUERY_DESCRIPTIONS,
)
from pydantic import Field, field_validator


class GovernmentTradesQueryParams(QueryParams):
    """Government Trades Query."""

    symbol: str | None = Field(
        default=None, description=QUERY_DESCRIPTIONS.get("symbol", "")
    )
    chamber: Literal["house", "senate", "all"] = Field(
        default="all", description="Government Chamber."
    )
    limit: int | None = Field(
        default=None, description=QUERY_DESCRIPTIONS.get("limit", "")
    )

    @field_validator("symbol", mode="before", check_fields=False)
    @classmethod
    def to_upper(cls, v: str):
        """Convert field to uppercase."""
        return v.upper() if v else None


class GovernmentTradesData(Data):
    """Government Trades data."""

    symbol: str | None = Field(
        default=None, description=DATA_DESCRIPTIONS.get("symbol", "")
    )
    date: dateType = Field(description=DATA_DESCRIPTIONS.get("date", ""))
    transaction_date: dateType | None = Field(
        default=None, description="Date of Transaction."
    )
    representative: str | None = Field(
        default=None, description="Name of Representative."
    )

```



---

## High-Level Overview

This is a **python** file named `government_trades.py`.

**Python Module**

- **Classes** (2): GovernmentTradesQueryParams, GovernmentTradesData
- **Functions** (1): to_upper
- **Import Statements**: 2


---

## Detailed Analysis

### Python Code Structure

#### Classes

- **`GovernmentTradesQueryParams`**(QueryParams)
- **`GovernmentTradesData`**(Data)

#### Functions

- **`to_upper(cls, v: str)`**

#### Decorators Used

classmethod, field_validator


---

## Related Files

The following files may be related based on imports and references:

**Imported Modules**:
- `Data`
- `Field`
- `Literal`
- `QueryParams`
- `date`
- `datetime`
- `openbb_core.provider.abstract.data`
- `openbb_core.provider.abstract.query_params`
- `openbb_core.provider.utils.descriptions`
- `pydantic`
- `typing`


---

## Performance & Security Notes

No obvious security concerns detected in static analysis.


---

**Generated**: 2025-11-19T02:16:46.485584Z
**Generator**: World's Best Repo Book Generator v1.0

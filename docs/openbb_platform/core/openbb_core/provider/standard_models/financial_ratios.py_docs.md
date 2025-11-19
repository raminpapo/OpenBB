# File Documentation: financial_ratios.py

## Metadata
- **Path**: `openbb_platform/core/openbb_core/provider/standard_models/financial_ratios.py`
- **Size**: 1,288 bytes
- **Lines**: 42
- **Category**: python
- **Extension**: .py

---

## Original Source

```python
"""Financial Ratios Standard Model."""

from datetime import date as dateType

from openbb_core.provider.abstract.data import Data
from openbb_core.provider.abstract.query_params import QueryParams
from openbb_core.provider.utils.descriptions import (
    DATA_DESCRIPTIONS,
    QUERY_DESCRIPTIONS,
)
from pydantic import Field, field_validator


class FinancialRatiosQueryParams(QueryParams):
    """Financial Ratios Query."""

    symbol: str = Field(description=QUERY_DESCRIPTIONS.get("symbol", ""))
    limit: int | None = Field(
        default=None, description=QUERY_DESCRIPTIONS.get("limit", "")
    )

    @field_validator("symbol", mode="before", check_fields=False)
    @classmethod
    def to_upper(cls, v: str):
        """Convert field to uppercase."""
        return v.upper()


class FinancialRatiosData(Data):
    """Financial Ratios Standard Model."""

    symbol: str | None = Field(
        default=None, description=DATA_DESCRIPTIONS.get("symbol", "")
    )
    period_ending: dateType | None = Field(
        default=None, description=DATA_DESCRIPTIONS.get("date", "")
    )
    fiscal_period: str | None = Field(
        default=None, description="Period of the financial ratios."
    )
    fiscal_year: int | None = Field(default=None, description="Fiscal year.")

```



---

## High-Level Overview

This is a **python** file named `financial_ratios.py`.

**Python Module**

- **Classes** (2): FinancialRatiosQueryParams, FinancialRatiosData
- **Functions** (1): to_upper
- **Import Statements**: 2


---

## Detailed Analysis

### Python Code Structure

#### Classes

- **`FinancialRatiosQueryParams`**(QueryParams)
- **`FinancialRatiosData`**(Data)

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

**Generated**: 2025-11-19T02:16:46.462119Z
**Generator**: World's Best Repo Book Generator v1.0

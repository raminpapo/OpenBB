# Documentation: openbb_platform/core/openbb_core/provider/standard_models/financial_ratios.py

## File Metadata
- **Path**: `openbb_platform/core/openbb_core/provider/standard_models/financial_ratios.py`
- **Size**: 1,288 characters, 42 lines
- **Words**: 111
- **Extension**: .py
- **Classification**: Text file

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

## High-Level Overview

Financial Ratios Standard Model.

from datetime import date as dateType

from openbb_core.provider.abstract.data import Data
from openbb_core.provider.abstract.query_params import QueryParams
from openbb_core.provider.utils.descriptions import (
DATA_DESCRIPTIONS,
QUERY_DESCRIPTIONS,
)
from pydantic import Field, field_validator


class FinancialRatiosQueryParams(QueryParams):
Financial Ratios Query.
Convert field to uppercase.
return v.upper()


class FinancialRatiosData(Data):

## Detailed Structure

### Python File Structure

**Classes** (2):
`FinancialRatiosQueryParams`, `FinancialRatiosData`

**Functions** (1):
`to_upper`

**Imports** (9):
`datetime`, `date`, `openbb_core.provider.abstract.data`, `Data`, `openbb_core.provider.abstract.query_params`, `QueryParams`, `openbb_core.provider.utils.descriptions`, `pydantic`, `Field`


## Key Components

**Class `FinancialRatiosQueryParams`**: Financial Ratios Query.

**Class `FinancialRatiosData`**: Financial Ratios Standard Model.

## Usage & Examples

See source code for usage details.

## Related Files

- `datetime`
- `openbb_core.provider.abstract.data`
- `openbb_core.provider.abstract.query_params`
- `openbb_core.provider.utils.descriptions`
- `pydantic`

## Notes
- Generated: 2025-11-18T07:54:35.633657
- Generator: World's Best Repo Book Generator v1.0.0

# Documentation: openbb_platform/core/openbb_core/provider/standard_models/equity_ownership.py

## File Metadata
- **Path**: `openbb_platform/core/openbb_core/provider/standard_models/equity_ownership.py`
- **Size**: 1,185 characters, 36 lines
- **Words**: 101
- **Extension**: .py
- **Classification**: Text file

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

## High-Level Overview

Equity Ownership Standard Model.

from datetime import date as dateType

from openbb_core.provider.abstract.data import Data
from openbb_core.provider.abstract.query_params import QueryParams
from openbb_core.provider.utils.descriptions import (
DATA_DESCRIPTIONS,
QUERY_DESCRIPTIONS,
)
from pydantic import Field, field_validator


class EquityOwnershipQueryParams(QueryParams):
Equity Ownership Query.
Convert field to uppercase.
return v.upper()


class EquityOwnershipData(Data):

## Detailed Structure

### Python File Structure

**Classes** (2):
`EquityOwnershipQueryParams`, `EquityOwnershipData`

**Functions** (1):
`to_upper`

**Imports** (9):
`datetime`, `date`, `openbb_core.provider.abstract.data`, `Data`, `openbb_core.provider.abstract.query_params`, `QueryParams`, `openbb_core.provider.utils.descriptions`, `pydantic`, `Field`


## Key Components

**Class `EquityOwnershipQueryParams`**: Equity Ownership Query.

**Class `EquityOwnershipData`**: Equity Ownership Data.

## Usage & Examples

See source code for usage details.

## Related Files

- `datetime`
- `openbb_core.provider.abstract.data`
- `openbb_core.provider.abstract.query_params`
- `openbb_core.provider.utils.descriptions`
- `pydantic`

## Notes
- Generated: 2025-11-18T07:54:35.598340
- Generator: World's Best Repo Book Generator v1.0.0

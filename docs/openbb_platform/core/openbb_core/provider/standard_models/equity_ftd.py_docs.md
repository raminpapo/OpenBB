# Documentation: openbb_platform/core/openbb_core/provider/standard_models/equity_ftd.py

## File Metadata
- **Path**: `openbb_platform/core/openbb_core/provider/standard_models/equity_ftd.py`
- **Size**: 1,703 characters, 60 lines
- **Words**: 164
- **Extension**: .py
- **Classification**: Text file

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

## High-Level Overview

Equity FTD Standard Model.

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
Equity FTD Query.
Convert field to uppercase.
return v.upper()

## Detailed Structure

### Python File Structure

**Classes** (2):
`EquityFtdQueryParams`, `EquityFtdData`

**Functions** (2):
`to_upper`, `date_validate`

**Imports** (9):
`datetime`, `openbb_core.provider.abstract.data`, `Data`, `openbb_core.provider.abstract.query_params`, `QueryParams`, `openbb_core.provider.utils.descriptions`, `pydantic`, `Field`, `the`


## Key Components

**Class `EquityFtdQueryParams`**: Equity FTD Query.

**Class `EquityFtdData`**: Equity FTD Data.

## Usage & Examples

See source code for usage details.

## Related Files

- `datetime`
- `openbb_core.provider.abstract.data`
- `openbb_core.provider.abstract.query_params`
- `openbb_core.provider.utils.descriptions`
- `pydantic`

## Notes
- Generated: 2025-11-18T07:54:35.590881
- Generator: World's Best Repo Book Generator v1.0.0

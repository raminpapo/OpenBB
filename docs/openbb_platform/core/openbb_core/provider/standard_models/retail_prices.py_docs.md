# Documentation: openbb_platform/core/openbb_core/provider/standard_models/retail_prices.py

## File Metadata
- **Path**: `openbb_platform/core/openbb_core/provider/standard_models/retail_prices.py`
- **Size**: 1,509 characters, 55 lines
- **Words**: 135
- **Extension**: .py
- **Classification**: Text file

## Original Source

```python
"""Retail Prices Standard Model."""

from datetime import date as dateType

from openbb_core.provider.abstract.data import Data
from openbb_core.provider.abstract.query_params import QueryParams
from openbb_core.provider.utils.descriptions import (
    DATA_DESCRIPTIONS,
    QUERY_DESCRIPTIONS,
)
from pydantic import Field


class RetailPricesQueryParams(QueryParams):
    """Retail Prices Query."""

    item: str | None = Field(
        default=None,
        description="The item or basket of items to query.",
    )
    country: str = Field(
        description=QUERY_DESCRIPTIONS.get("country", ""),
        default="united_states",
    )
    start_date: dateType | None = Field(
        default=None, description=QUERY_DESCRIPTIONS.get("start_date")
    )
    end_date: dateType | None = Field(
        default=None, description=QUERY_DESCRIPTIONS.get("end_date")
    )


class RetailPricesData(Data):
    """Retail Prices Data."""

    date: dateType | None = Field(
        default=None, description=DATA_DESCRIPTIONS.get("date")
    )
    symbol: str | None = Field(
        default=None,
        description=DATA_DESCRIPTIONS.get("symbol", ""),
    )
    country: str | None = Field(
        default=None,
        description=DATA_DESCRIPTIONS.get("country", ""),
    )
    description: str = Field(
        default=None,
        description="Description of the item.",
    )
    value: float | None = Field(
        default=None,
        description="Price, or change in price, per unit.",
    )

```

## High-Level Overview

Retail Prices Standard Model.

from datetime import date as dateType

from openbb_core.provider.abstract.data import Data
from openbb_core.provider.abstract.query_params import QueryParams
from openbb_core.provider.utils.descriptions import (
DATA_DESCRIPTIONS,
QUERY_DESCRIPTIONS,
)
from pydantic import Field


class RetailPricesQueryParams(QueryParams):
Retail Prices Query.
Retail Prices Data.

date: dateType | None = Field(
default=None, description=DATA_DESCRIPTIONS.get("date")
)

## Detailed Structure

### Python File Structure

**Classes** (2):
`RetailPricesQueryParams`, `RetailPricesData`

**Functions** (0):
None

**Imports** (9):
`datetime`, `date`, `openbb_core.provider.abstract.data`, `Data`, `openbb_core.provider.abstract.query_params`, `QueryParams`, `openbb_core.provider.utils.descriptions`, `pydantic`, `Field`


## Key Components

**Class `RetailPricesQueryParams`**: Retail Prices Query.

**Class `RetailPricesData`**: Retail Prices Data.

## Usage & Examples

See source code for usage details.

## Related Files

- `datetime`
- `openbb_core.provider.abstract.data`
- `openbb_core.provider.abstract.query_params`
- `openbb_core.provider.utils.descriptions`
- `pydantic`

## Notes
- Generated: 2025-11-18T07:54:35.723965
- Generator: World's Best Repo Book Generator v1.0.0

# Documentation: openbb_platform/core/openbb_core/provider/standard_models/commodity_spot_prices.py

## File Metadata
- **Path**: `openbb_platform/core/openbb_core/provider/standard_models/commodity_spot_prices.py`
- **Size**: 1,330 characters, 51 lines
- **Words**: 115
- **Extension**: .py
- **Classification**: Text file

## Original Source

```python
"""Commodity Spot Prices Standard Model."""

from datetime import (
    date as dateType,
)

from openbb_core.provider.abstract.data import Data
from openbb_core.provider.abstract.query_params import QueryParams
from openbb_core.provider.utils.descriptions import (
    DATA_DESCRIPTIONS,
    QUERY_DESCRIPTIONS,
)
from pydantic import Field


class CommoditySpotPricesQueryParams(QueryParams):
    """Commodity Spot Prices Query."""

    start_date: dateType | None = Field(
        default=None,
        description=QUERY_DESCRIPTIONS.get("start_date", ""),
    )
    end_date: dateType | None = Field(
        default=None,
        description=QUERY_DESCRIPTIONS.get("end_date", ""),
    )


class CommoditySpotPricesData(Data):
    """Commodity Spot Prices Data."""

    date: dateType = Field(
        description=DATA_DESCRIPTIONS.get("date", ""),
    )
    symbol: str | None = Field(
        default=None,
        description=DATA_DESCRIPTIONS.get("symbol", ""),
    )
    commodity: str | None = Field(
        default=None,
        description="Commodity name.",
    )
    price: float = Field(
        description="Price of the commodity.",
        json_schema_extra={"x-unit_measurement": "currency"},
    )
    unit: str | None = Field(
        default=None,
        description="Unit of the commodity price.",
    )

```

## High-Level Overview

Commodity Spot Prices Standard Model.

from datetime import (
date as dateType,
)

from openbb_core.provider.abstract.data import Data
from openbb_core.provider.abstract.query_params import QueryParams
from openbb_core.provider.utils.descriptions import (
DATA_DESCRIPTIONS,
QUERY_DESCRIPTIONS,
)
from pydantic import Field


class CommoditySpotPricesQueryParams(QueryParams):
Commodity Spot Prices Query.
Commodity Spot Prices Data.

date: dateType = Field(

## Detailed Structure

### Python File Structure

**Classes** (2):
`CommoditySpotPricesQueryParams`, `CommoditySpotPricesData`

**Functions** (0):
None

**Imports** (8):
`datetime`, `openbb_core.provider.abstract.data`, `Data`, `openbb_core.provider.abstract.query_params`, `QueryParams`, `openbb_core.provider.utils.descriptions`, `pydantic`, `Field`


## Key Components

**Class `CommoditySpotPricesQueryParams`**: Commodity Spot Prices Query.

**Class `CommoditySpotPricesData`**: Commodity Spot Prices Data.

## Usage & Examples

See source code for usage details.

## Related Files

- `datetime`
- `openbb_core.provider.abstract.data`
- `openbb_core.provider.abstract.query_params`
- `openbb_core.provider.utils.descriptions`
- `pydantic`

## Notes
- Generated: 2025-11-18T07:54:35.557792
- Generator: World's Best Repo Book Generator v1.0.0

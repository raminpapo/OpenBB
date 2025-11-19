# File Documentation: commodity_spot_prices.py

## Metadata
- **Path**: `openbb_platform/core/openbb_core/provider/standard_models/commodity_spot_prices.py`
- **Size**: 1,330 bytes
- **Lines**: 51
- **Category**: python
- **Extension**: .py

---

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



---

## High-Level Overview

This is a **python** file named `commodity_spot_prices.py`.

**Python Module**

- **Classes** (2): CommoditySpotPricesQueryParams, CommoditySpotPricesData
- **Import Statements**: 2


---

## Detailed Analysis

### Python Code Structure

#### Classes

- **`CommoditySpotPricesQueryParams`**(QueryParams)
- **`CommoditySpotPricesData`**(Data)


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

**Generated**: 2025-11-19T02:16:46.377595Z
**Generator**: World's Best Repo Book Generator v1.0

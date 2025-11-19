# File Documentation: retail_prices.py

## Metadata
- **Path**: `openbb_platform/core/openbb_core/provider/standard_models/retail_prices.py`
- **Size**: 1,509 bytes
- **Lines**: 55
- **Category**: python
- **Extension**: .py

---

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



---

## High-Level Overview

This is a **python** file named `retail_prices.py`.

**Python Module**

- **Classes** (2): RetailPricesQueryParams, RetailPricesData
- **Import Statements**: 2


---

## Detailed Analysis

### Python Code Structure

#### Classes

- **`RetailPricesQueryParams`**(QueryParams)
- **`RetailPricesData`**(Data)


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

**Generated**: 2025-11-19T02:16:46.556880Z
**Generator**: World's Best Repo Book Generator v1.0

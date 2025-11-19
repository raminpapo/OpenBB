# File Documentation: market_movers.py

## Metadata
- **Path**: `openbb_platform/core/openbb_core/provider/standard_models/market_movers.py`
- **Size**: 799 bytes
- **Lines**: 23
- **Category**: python
- **Extension**: .py

---

## Original Source

```python
"""Market Movers Standard Model."""

from openbb_core.provider.abstract.data import Data
from openbb_core.provider.abstract.query_params import QueryParams
from openbb_core.provider.utils.descriptions import DATA_DESCRIPTIONS
from pydantic import Field


class MarketMoversQueryParams(QueryParams):
    """Market Movers Query."""


class MarketMoversData(Data):
    """Market Movers Data."""

    symbol: str = Field(description=DATA_DESCRIPTIONS.get("symbol", ""))
    name: str | None = Field(
        default=None, description="The name associated with the ticker."
    )
    price: float = Field(description="The last price of the ticker.")
    change: float = Field(description="The change in price from open.")
    change_percent: float = Field(description="The change in percent from open.")

```



---

## High-Level Overview

This is a **python** file named `market_movers.py`.

**Python Module**

- **Classes** (2): MarketMoversQueryParams, MarketMoversData
- **Import Statements**: 1


---

## Detailed Analysis

### Python Code Structure

#### Classes

- **`MarketMoversQueryParams`**(QueryParams)
- **`MarketMoversData`**(Data)


---

## Related Files

The following files may be related based on imports and references:

**Imported Modules**:
- `DATA_DESCRIPTIONS`
- `Data`
- `Field`
- `QueryParams`
- `openbb_core.provider.abstract.data`
- `openbb_core.provider.abstract.query_params`
- `openbb_core.provider.utils.descriptions`
- `pydantic`


---

## Performance & Security Notes

No obvious security concerns detected in static analysis.


---

**Generated**: 2025-11-19T02:16:46.526701Z
**Generator**: World's Best Repo Book Generator v1.0

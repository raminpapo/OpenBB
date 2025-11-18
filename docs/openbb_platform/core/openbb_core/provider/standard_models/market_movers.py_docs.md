# Documentation: openbb_platform/core/openbb_core/provider/standard_models/market_movers.py

## File Metadata
- **Path**: `openbb_platform/core/openbb_core/provider/standard_models/market_movers.py`
- **Size**: 799 characters, 23 lines
- **Words**: 76
- **Extension**: .py
- **Classification**: Text file

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

## High-Level Overview

Market Movers Standard Model.

from openbb_core.provider.abstract.data import Data
from openbb_core.provider.abstract.query_params import QueryParams
from openbb_core.provider.utils.descriptions import DATA_DESCRIPTIONS
from pydantic import Field


class MarketMoversQueryParams(QueryParams):
Market Movers Query.
Market Movers Data.

symbol: str = Field(description=DATA_DESCRIPTIONS.get("symbol", ""))
name: str | None = Field(
default=None, description="The name associated with the ticker."
)
price: float = Field(description="The last price of the ticker.")
change: float = Field(description="The change in price from open.")
change_percent: float = Field(description="The change in percent from open.")


## Detailed Structure

### Python File Structure

**Classes** (2):
`MarketMoversQueryParams`, `MarketMoversData`

**Functions** (0):
None

**Imports** (10):
`openbb_core.provider.abstract.data`, `Data`, `openbb_core.provider.abstract.query_params`, `QueryParams`, `openbb_core.provider.utils.descriptions`, `DATA_DESCRIPTIONS`, `pydantic`, `Field`, `open.`, `open.`


## Key Components

**Class `MarketMoversQueryParams`**: Market Movers Query.

**Class `MarketMoversData`**: Market Movers Data.

## Usage & Examples

See source code for usage details.

## Related Files

- `openbb_core.provider.abstract.data`
- `openbb_core.provider.abstract.query_params`
- `openbb_core.provider.utils.descriptions`
- `pydantic`

## Notes
- Generated: 2025-11-18T07:54:35.696938
- Generator: World's Best Repo Book Generator v1.0.0

# Documentation: openbb_platform/core/openbb_core/provider/standard_models/market_snapshots.py

## File Metadata
- **Path**: `openbb_platform/core/openbb_core/provider/standard_models/market_snapshots.py`
- **Size**: 1,797 characters, 55 lines
- **Words**: 165
- **Extension**: .py
- **Classification**: Text file

## Original Source

```python
"""Market Snapshots Standard Model."""

from openbb_core.provider.abstract.data import Data, ForceInt
from openbb_core.provider.abstract.query_params import QueryParams
from openbb_core.provider.utils.descriptions import DATA_DESCRIPTIONS
from pydantic import Field


class MarketSnapshotsQueryParams(QueryParams):
    """Market Snapshots Query."""


class MarketSnapshotsData(Data):
    """Market Snapshots Data."""

    exchange: str | None = Field(
        description="Exchange the security is listed on.", default=None
    )
    symbol: str = Field(description=DATA_DESCRIPTIONS.get("symbol", ""))
    name: str | None = Field(
        description="Name of the company, fund, or security.", default=None
    )
    open: float | None = Field(
        description=DATA_DESCRIPTIONS.get("open", ""),
        default=None,
    )
    high: float | None = Field(
        description=DATA_DESCRIPTIONS.get("high", ""),
        default=None,
    )
    low: float | None = Field(
        description=DATA_DESCRIPTIONS.get("low", ""),
        default=None,
    )
    close: float | None = Field(
        description=DATA_DESCRIPTIONS.get("close", ""),
        default=None,
    )
    volume: ForceInt | None = Field(
        description=DATA_DESCRIPTIONS.get("volume", ""), default=None
    )
    prev_close: float | None = Field(
        description=DATA_DESCRIPTIONS.get("prev_close", ""),
        default=None,
    )
    change: float | None = Field(
        description="The change in price from the previous close.",
        default=None,
    )
    change_percent: float | None = Field(
        description="The change in price from the previous close, as a normalized percent.",
        default=None,
        json_schema_extra={"x-unit_measurement": "percent", "x-frontend_multiply": 100},
    )

```

## High-Level Overview

Market Snapshots Standard Model.

from openbb_core.provider.abstract.data import Data, ForceInt
from openbb_core.provider.abstract.query_params import QueryParams
from openbb_core.provider.utils.descriptions import DATA_DESCRIPTIONS
from pydantic import Field


class MarketSnapshotsQueryParams(QueryParams):
Market Snapshots Query.
Market Snapshots Data.

exchange: str | None = Field(
description="Exchange the security is listed on.", default=None
)
symbol: str = Field(description=DATA_DESCRIPTIONS.get("symbol", ""))
name: str | None = Field(
description="Name of the company, fund, or security.", default=None
)
open: float | None = Field(

## Detailed Structure

### Python File Structure

**Classes** (2):
`MarketSnapshotsQueryParams`, `MarketSnapshotsData`

**Functions** (0):
None

**Imports** (10):
`openbb_core.provider.abstract.data`, `Data`, `openbb_core.provider.abstract.query_params`, `QueryParams`, `openbb_core.provider.utils.descriptions`, `DATA_DESCRIPTIONS`, `pydantic`, `Field`, `the`, `the`


## Key Components

**Class `MarketSnapshotsQueryParams`**: Market Snapshots Query.

**Class `MarketSnapshotsData`**: Market Snapshots Data.

## Usage & Examples

See source code for usage details.

## Related Files

- `openbb_core.provider.abstract.data`
- `openbb_core.provider.abstract.query_params`
- `openbb_core.provider.utils.descriptions`
- `pydantic`

## Notes
- Generated: 2025-11-18T07:54:35.698046
- Generator: World's Best Repo Book Generator v1.0.0

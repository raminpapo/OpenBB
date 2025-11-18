# Documentation: openbb_platform/core/openbb_core/provider/standard_models/etf_performance.py

## File Metadata
- **Path**: `openbb_platform/core/openbb_core/provider/standard_models/etf_performance.py`
- **Size**: 1,559 characters, 58 lines
- **Words**: 142
- **Extension**: .py
- **Classification**: Text file

## Original Source

```python
"""ETF Performance Standard Model."""

from datetime import date as dateType
from typing import Literal

from openbb_core.provider.abstract.data import Data
from openbb_core.provider.abstract.query_params import QueryParams
from openbb_core.provider.utils.descriptions import (
    DATA_DESCRIPTIONS,
    QUERY_DESCRIPTIONS,
)
from pydantic import Field, field_validator


class ETFPerformanceQueryParams(QueryParams):
    """ETF Performance Query."""

    sort: Literal["asc", "desc"] = Field(
        default="desc",
        description="Sort order. Possible values: 'asc', 'desc'. Default: 'desc'.",
    )
    limit: int = Field(
        default=10,
        description=QUERY_DESCRIPTIONS.get("limit", ""),
    )

    @field_validator("sort", mode="before", check_fields=False)
    @classmethod
    def to_lower(cls, v: str | None) -> str | None:
        """Convert field to lowercase."""
        return v.lower() if v else v


class ETFPerformanceData(Data):
    """ETF Performance Data."""

    symbol: str = Field(
        description=DATA_DESCRIPTIONS.get("symbol", ""),
    )
    name: str = Field(
        description="Name of the entity.",
    )
    last_price: float = Field(
        description="Last price.",
    )
    percent_change: float = Field(
        description="Percent change.",
    )
    net_change: float = Field(
        description="Net change.",
    )
    volume: float = Field(
        description=DATA_DESCRIPTIONS.get("volume", ""),
    )
    date: dateType = Field(
        description=DATA_DESCRIPTIONS.get("date", ""),
    )

```

## High-Level Overview

ETF Performance Standard Model.

from datetime import date as dateType
from typing import Literal

from openbb_core.provider.abstract.data import Data
from openbb_core.provider.abstract.query_params import QueryParams
from openbb_core.provider.utils.descriptions import (
DATA_DESCRIPTIONS,
QUERY_DESCRIPTIONS,
)
from pydantic import Field, field_validator


class ETFPerformanceQueryParams(QueryParams):
ETF Performance Query.
Convert field to lowercase.
return v.lower() if v else v



## Detailed Structure

### Python File Structure

**Classes** (2):
`ETFPerformanceQueryParams`, `ETFPerformanceData`

**Functions** (1):
`to_lower`

**Imports** (11):
`datetime`, `date`, `typing`, `Literal`, `openbb_core.provider.abstract.data`, `Data`, `openbb_core.provider.abstract.query_params`, `QueryParams`, `openbb_core.provider.utils.descriptions`, `pydantic`, `Field`


## Key Components

**Class `ETFPerformanceQueryParams`**: ETF Performance Query.

**Class `ETFPerformanceData`**: ETF Performance Data.

## Usage & Examples

See source code for usage details.

## Related Files

- `datetime`
- `typing`
- `openbb_core.provider.abstract.data`
- `openbb_core.provider.abstract.query_params`
- `openbb_core.provider.utils.descriptions`
- `pydantic`

## Notes
- Generated: 2025-11-18T07:54:35.620771
- Generator: World's Best Repo Book Generator v1.0.0

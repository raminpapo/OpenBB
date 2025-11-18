# Documentation: openbb_platform/core/openbb_core/provider/standard_models/equity_performance.py

## File Metadata
- **Path**: `openbb_platform/core/openbb_core/provider/standard_models/equity_performance.py`
- **Size**: 1,580 characters, 52 lines
- **Words**: 135
- **Extension**: .py
- **Classification**: Text file

## Original Source

```python
"""Equity Performance Standard Model."""

from typing import Literal

from openbb_core.provider.abstract.data import Data
from openbb_core.provider.abstract.query_params import QueryParams
from openbb_core.provider.utils.descriptions import DATA_DESCRIPTIONS
from pydantic import Field, field_validator


class EquityPerformanceQueryParams(QueryParams):
    """Equity Performance Query."""

    sort: Literal["asc", "desc"] = Field(
        default="desc",
        description="Sort order. Possible values: 'asc', 'desc'. Default: 'desc'.",
    )

    @field_validator("sort", mode="before", check_fields=False)
    @classmethod
    def to_lower(cls, v: str | None) -> str | None:
        """Convert field to lowercase."""
        return v.lower() if v else v


class EquityPerformanceData(Data):
    """Equity Performance Data."""

    symbol: str = Field(
        description=DATA_DESCRIPTIONS.get("symbol", ""),
    )
    name: str | None = Field(
        default=None,
        description="Name of the entity.",
    )
    price: float = Field(
        description="Last price.",
        json_schema_extra={"x-unit_measurement": "currency"},
    )
    change: float = Field(
        description="Change in price.",
        json_schema_extra={"x-unit_measurement": "currency"},
    )
    percent_change: float = Field(
        description="Percent change.",
        json_schema_extra={"x-unit_measurement": "percent", "x-frontend_multiply": 100},
    )
    volume: int | float | None = Field(
        default=None,
        description=DATA_DESCRIPTIONS.get("volume", ""),
    )

```

## High-Level Overview

Equity Performance Standard Model.

from typing import Literal

from openbb_core.provider.abstract.data import Data
from openbb_core.provider.abstract.query_params import QueryParams
from openbb_core.provider.utils.descriptions import DATA_DESCRIPTIONS
from pydantic import Field, field_validator


class EquityPerformanceQueryParams(QueryParams):
Equity Performance Query.
Convert field to lowercase.
return v.lower() if v else v


class EquityPerformanceData(Data):
Equity Performance Data.

## Detailed Structure

### Python File Structure

**Classes** (2):
`EquityPerformanceQueryParams`, `EquityPerformanceData`

**Functions** (1):
`to_lower`

**Imports** (10):
`typing`, `Literal`, `openbb_core.provider.abstract.data`, `Data`, `openbb_core.provider.abstract.query_params`, `QueryParams`, `openbb_core.provider.utils.descriptions`, `DATA_DESCRIPTIONS`, `pydantic`, `Field`


## Key Components

**Class `EquityPerformanceQueryParams`**: Equity Performance Query.

**Class `EquityPerformanceData`**: Equity Performance Data.

## Usage & Examples

See source code for usage details.

## Related Files

- `typing`
- `openbb_core.provider.abstract.data`
- `openbb_core.provider.abstract.query_params`
- `openbb_core.provider.utils.descriptions`
- `pydantic`

## Notes
- Generated: 2025-11-18T07:54:35.601214
- Generator: World's Best Repo Book Generator v1.0.0

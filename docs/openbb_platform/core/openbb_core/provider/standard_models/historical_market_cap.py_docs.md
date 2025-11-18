# Documentation: openbb_platform/core/openbb_core/provider/standard_models/historical_market_cap.py

## File Metadata
- **Path**: `openbb_platform/core/openbb_core/provider/standard_models/historical_market_cap.py`
- **Size**: 1,329 characters, 41 lines
- **Words**: 107
- **Extension**: .py
- **Classification**: Text file

## Original Source

```python
"""Historical Market Cap Model."""

from datetime import date as dateType

from openbb_core.provider.abstract.data import Data
from openbb_core.provider.abstract.query_params import QueryParams
from openbb_core.provider.utils.descriptions import (
    DATA_DESCRIPTIONS,
    QUERY_DESCRIPTIONS,
)
from pydantic import Field, field_validator


class HistoricalMarketCapQueryParams(QueryParams):
    """Historical Market Cap Query."""

    symbol: str = Field(description=QUERY_DESCRIPTIONS.get("symbol", ""))
    start_date: dateType | None = Field(
        default=None, description=QUERY_DESCRIPTIONS.get("start_date", "")
    )
    end_date: dateType | None = Field(
        default=None, description=QUERY_DESCRIPTIONS.get("end_date", "")
    )

    @field_validator("symbol", mode="before", check_fields=False)
    @classmethod
    def to_upper(cls, v: str) -> str:
        """Convert field to uppercase."""
        return v.upper()


class HistoricalMarketCapData(Data):
    """Historical Market Cap Data."""

    date: dateType = Field(description=DATA_DESCRIPTIONS.get("date", ""))
    symbol: str = Field(description=DATA_DESCRIPTIONS.get("symbol", ""))
    market_cap: int | float = Field(
        description="Market capitalization of the security.",
        json_schema_extra={"x-unit_measurement": "currency"},
    )

```

## High-Level Overview

Historical Market Cap Model.

from datetime import date as dateType

from openbb_core.provider.abstract.data import Data
from openbb_core.provider.abstract.query_params import QueryParams
from openbb_core.provider.utils.descriptions import (
DATA_DESCRIPTIONS,
QUERY_DESCRIPTIONS,
)
from pydantic import Field, field_validator


class HistoricalMarketCapQueryParams(QueryParams):
Historical Market Cap Query.
Convert field to uppercase.
return v.upper()


class HistoricalMarketCapData(Data):

## Detailed Structure

### Python File Structure

**Classes** (2):
`HistoricalMarketCapQueryParams`, `HistoricalMarketCapData`

**Functions** (1):
`to_upper`

**Imports** (9):
`datetime`, `date`, `openbb_core.provider.abstract.data`, `Data`, `openbb_core.provider.abstract.query_params`, `QueryParams`, `openbb_core.provider.utils.descriptions`, `pydantic`, `Field`


## Key Components

**Class `HistoricalMarketCapQueryParams`**: Historical Market Cap Query.

**Class `HistoricalMarketCapData`**: Historical Market Cap Data.

## Usage & Examples

See source code for usage details.

## Related Files

- `datetime`
- `openbb_core.provider.abstract.data`
- `openbb_core.provider.abstract.query_params`
- `openbb_core.provider.utils.descriptions`
- `pydantic`

## Notes
- Generated: 2025-11-18T07:54:35.665407
- Generator: World's Best Repo Book Generator v1.0.0

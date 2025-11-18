# Documentation: openbb_platform/core/openbb_core/provider/standard_models/share_statistics.py

## File Metadata
- **Path**: `openbb_platform/core/openbb_core/provider/standard_models/share_statistics.py`
- **Size**: 1,525 characters, 48 lines
- **Words**: 139
- **Extension**: .py
- **Classification**: Text file

## Original Source

```python
"""Share Statistics Standard Model."""

from datetime import (
    date as dateType,
    datetime,
)

from openbb_core.provider.abstract.data import Data
from openbb_core.provider.abstract.query_params import QueryParams
from openbb_core.provider.utils.descriptions import (
    DATA_DESCRIPTIONS,
    QUERY_DESCRIPTIONS,
)
from pydantic import Field, field_validator


class ShareStatisticsQueryParams(QueryParams):
    """Share Statistics Query."""

    symbol: str = Field(description=QUERY_DESCRIPTIONS.get("symbol", ""))

    @field_validator("symbol", mode="before", check_fields=False)
    @classmethod
    def to_upper(cls, v: str) -> str:
        """Convert field to uppercase."""
        return v.upper()


class ShareStatisticsData(Data):
    """Share Statistics Data."""

    symbol: str = Field(description=DATA_DESCRIPTIONS.get("symbol", ""))
    date: dateType | datetime | None = Field(
        default=None, description=DATA_DESCRIPTIONS.get("date", "")
    )
    free_float: float | None = Field(
        default=None,
        description="Percentage of unrestricted shares of a publicly-traded company.",
        json_schema_extra={"x-unit_measurement": "percent", "x-frontend_multiply": 100},
    )
    float_shares: int | float | None = Field(
        default=None,
        description="Number of shares available for trading by the general public.",
    )
    outstanding_shares: int | float | None = Field(
        default=None, description="Total number of shares of a publicly-traded company."
    )

```

## High-Level Overview

Share Statistics Standard Model.

from datetime import (
date as dateType,
datetime,
)

from openbb_core.provider.abstract.data import Data
from openbb_core.provider.abstract.query_params import QueryParams
from openbb_core.provider.utils.descriptions import (
DATA_DESCRIPTIONS,
QUERY_DESCRIPTIONS,
)
from pydantic import Field, field_validator


class ShareStatisticsQueryParams(QueryParams):
Share Statistics Query.
Convert field to uppercase.
return v.upper()

## Detailed Structure

### Python File Structure

**Classes** (2):
`ShareStatisticsQueryParams`, `ShareStatisticsData`

**Functions** (1):
`to_upper`

**Imports** (8):
`datetime`, `openbb_core.provider.abstract.data`, `Data`, `openbb_core.provider.abstract.query_params`, `QueryParams`, `openbb_core.provider.utils.descriptions`, `pydantic`, `Field`


## Key Components

**Class `ShareStatisticsQueryParams`**: Share Statistics Query.

**Class `ShareStatisticsData`**: Share Statistics Data.

## Usage & Examples

See source code for usage details.

## Related Files

- `datetime`
- `openbb_core.provider.abstract.data`
- `openbb_core.provider.abstract.query_params`
- `openbb_core.provider.utils.descriptions`
- `pydantic`

## Notes
- Generated: 2025-11-18T07:54:35.736837
- Generator: World's Best Repo Book Generator v1.0.0

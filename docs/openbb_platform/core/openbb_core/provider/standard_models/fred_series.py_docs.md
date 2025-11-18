# Documentation: openbb_platform/core/openbb_core/provider/standard_models/fred_series.py

## File Metadata
- **Path**: `openbb_platform/core/openbb_core/provider/standard_models/fred_series.py`
- **Size**: 1,166 characters, 41 lines
- **Words**: 98
- **Extension**: .py
- **Classification**: Text file

## Original Source

```python
"""FRED Series Standard Model."""

from datetime import date as dateType

from openbb_core.provider.abstract.data import Data
from openbb_core.provider.abstract.query_params import QueryParams
from openbb_core.provider.utils.descriptions import (
    DATA_DESCRIPTIONS,
    QUERY_DESCRIPTIONS,
)
from pydantic import Field, field_validator


class SeriesQueryParams(QueryParams):
    """FRED Series Query."""

    symbol: str = Field(
        description=QUERY_DESCRIPTIONS.get("symbol", ""),
    )
    start_date: dateType | None = Field(
        description=QUERY_DESCRIPTIONS.get("start_date", ""), default=None
    )
    end_date: dateType | None = Field(
        description=QUERY_DESCRIPTIONS.get("end_date", ""), default=None
    )
    limit: int | None = Field(
        description=QUERY_DESCRIPTIONS.get("limit", ""), default=100000
    )

    @field_validator("symbol", mode="before", check_fields=False)
    @classmethod
    def to_upper(cls, v: str) -> str:
        """Convert field to uppercase."""
        return v.upper()


class SeriesData(Data):
    """FRED Series Data."""

    date: dateType = Field(description=DATA_DESCRIPTIONS.get("date", ""))

```

## High-Level Overview

FRED Series Standard Model.

from datetime import date as dateType

from openbb_core.provider.abstract.data import Data
from openbb_core.provider.abstract.query_params import QueryParams
from openbb_core.provider.utils.descriptions import (
DATA_DESCRIPTIONS,
QUERY_DESCRIPTIONS,
)
from pydantic import Field, field_validator


class SeriesQueryParams(QueryParams):
FRED Series Query.
Convert field to uppercase.
return v.upper()


class SeriesData(Data):

## Detailed Structure

### Python File Structure

**Classes** (2):
`SeriesQueryParams`, `SeriesData`

**Functions** (1):
`to_upper`

**Imports** (9):
`datetime`, `date`, `openbb_core.provider.abstract.data`, `Data`, `openbb_core.provider.abstract.query_params`, `QueryParams`, `openbb_core.provider.utils.descriptions`, `pydantic`, `Field`


## Key Components

**Class `SeriesQueryParams`**: FRED Series Query.

**Class `SeriesData`**: FRED Series Data.

## Usage & Examples

See source code for usage details.

## Related Files

- `datetime`
- `openbb_core.provider.abstract.data`
- `openbb_core.provider.abstract.query_params`
- `openbb_core.provider.utils.descriptions`
- `pydantic`

## Notes
- Generated: 2025-11-18T07:54:35.645896
- Generator: World's Best Repo Book Generator v1.0.0

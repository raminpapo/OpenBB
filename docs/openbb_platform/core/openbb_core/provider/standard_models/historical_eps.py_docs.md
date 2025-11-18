# Documentation: openbb_platform/core/openbb_core/provider/standard_models/historical_eps.py

## File Metadata
- **Path**: `openbb_platform/core/openbb_core/provider/standard_models/historical_eps.py`
- **Size**: 1,145 characters, 37 lines
- **Words**: 103
- **Extension**: .py
- **Classification**: Text file

## Original Source

```python
"""Historical EPS Standard Model."""

from datetime import date as dateType

from openbb_core.provider.abstract.data import Data
from openbb_core.provider.abstract.query_params import QueryParams
from openbb_core.provider.utils.descriptions import (
    DATA_DESCRIPTIONS,
    QUERY_DESCRIPTIONS,
)
from pydantic import Field, field_validator


class HistoricalEpsQueryParams(QueryParams):
    """Historical EPS Query."""

    symbol: str = Field(description=QUERY_DESCRIPTIONS.get("symbol", ""))

    @field_validator("symbol", mode="before", check_fields=False)
    @classmethod
    def to_upper(cls, v: str) -> str:
        """Convert field to uppercase."""
        return v.upper()


class HistoricalEpsData(Data):
    """Historical EPS Data."""

    symbol: str = Field(description=DATA_DESCRIPTIONS.get("symbol", ""))
    date: dateType = Field(description=DATA_DESCRIPTIONS.get("date", ""))
    eps_actual: int | float | None = Field(
        default=None, description="Actual EPS from the earnings date."
    )
    eps_estimated: int | float | None = Field(
        default=None, description="Estimated EPS for the earnings date."
    )

```

## High-Level Overview

Historical EPS Standard Model.

from datetime import date as dateType

from openbb_core.provider.abstract.data import Data
from openbb_core.provider.abstract.query_params import QueryParams
from openbb_core.provider.utils.descriptions import (
DATA_DESCRIPTIONS,
QUERY_DESCRIPTIONS,
)
from pydantic import Field, field_validator


class HistoricalEpsQueryParams(QueryParams):
Historical EPS Query.
Convert field to uppercase.
return v.upper()


class HistoricalEpsData(Data):

## Detailed Structure

### Python File Structure

**Classes** (2):
`HistoricalEpsQueryParams`, `HistoricalEpsData`

**Functions** (1):
`to_upper`

**Imports** (10):
`datetime`, `date`, `openbb_core.provider.abstract.data`, `Data`, `openbb_core.provider.abstract.query_params`, `QueryParams`, `openbb_core.provider.utils.descriptions`, `pydantic`, `Field`, `the`


## Key Components

**Class `HistoricalEpsQueryParams`**: Historical EPS Query.

**Class `HistoricalEpsData`**: Historical EPS Data.

## Usage & Examples

See source code for usage details.

## Related Files

- `datetime`
- `openbb_core.provider.abstract.data`
- `openbb_core.provider.abstract.query_params`
- `openbb_core.provider.utils.descriptions`
- `pydantic`

## Notes
- Generated: 2025-11-18T07:54:35.664107
- Generator: World's Best Repo Book Generator v1.0.0

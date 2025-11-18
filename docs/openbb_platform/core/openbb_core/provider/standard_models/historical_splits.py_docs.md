# Documentation: openbb_platform/core/openbb_core/provider/standard_models/historical_splits.py

## File Metadata
- **Path**: `openbb_platform/core/openbb_core/provider/standard_models/historical_splits.py`
- **Size**: 1,169 characters, 42 lines
- **Words**: 100
- **Extension**: .py
- **Classification**: Text file

## Original Source

```python
"""Historical Splits Standard Model."""

from datetime import date as dateType

from openbb_core.provider.abstract.data import Data
from openbb_core.provider.abstract.query_params import QueryParams
from openbb_core.provider.utils.descriptions import (
    DATA_DESCRIPTIONS,
    QUERY_DESCRIPTIONS,
)
from pydantic import Field, field_validator


class HistoricalSplitsQueryParams(QueryParams):
    """Historical Splits Query."""

    symbol: str = Field(description=QUERY_DESCRIPTIONS.get("symbol", ""))

    @field_validator("symbol", mode="before", check_fields=False)
    @classmethod
    def to_upper(cls, v: str) -> str:
        """Convert field to uppercase."""
        return v.upper()


class HistoricalSplitsData(Data):
    """Historical Splits Data."""

    date: dateType = Field(description=DATA_DESCRIPTIONS.get("date", ""))
    numerator: float | None = Field(
        default=None,
        description="Numerator of the split.",
    )
    denominator: float | None = Field(
        default=None,
        description="Denominator of the split.",
    )
    split_ratio: str | None = Field(
        default=None,
        description="Split ratio.",
    )

```

## High-Level Overview

Historical Splits Standard Model.

from datetime import date as dateType

from openbb_core.provider.abstract.data import Data
from openbb_core.provider.abstract.query_params import QueryParams
from openbb_core.provider.utils.descriptions import (
DATA_DESCRIPTIONS,
QUERY_DESCRIPTIONS,
)
from pydantic import Field, field_validator


class HistoricalSplitsQueryParams(QueryParams):
Historical Splits Query.
Convert field to uppercase.
return v.upper()


class HistoricalSplitsData(Data):

## Detailed Structure

### Python File Structure

**Classes** (2):
`HistoricalSplitsQueryParams`, `HistoricalSplitsData`

**Functions** (1):
`to_upper`

**Imports** (9):
`datetime`, `date`, `openbb_core.provider.abstract.data`, `Data`, `openbb_core.provider.abstract.query_params`, `QueryParams`, `openbb_core.provider.utils.descriptions`, `pydantic`, `Field`


## Key Components

**Class `HistoricalSplitsQueryParams`**: Historical Splits Query.

**Class `HistoricalSplitsData`**: Historical Splits Data.

## Usage & Examples

See source code for usage details.

## Related Files

- `datetime`
- `openbb_core.provider.abstract.data`
- `openbb_core.provider.abstract.query_params`
- `openbb_core.provider.utils.descriptions`
- `pydantic`

## Notes
- Generated: 2025-11-18T07:54:35.666737
- Generator: World's Best Repo Book Generator v1.0.0

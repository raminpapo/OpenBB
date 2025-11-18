# Documentation: openbb_platform/core/openbb_core/provider/standard_models/short_volume.py

## File Metadata
- **Path**: `openbb_platform/core/openbb_core/provider/standard_models/short_volume.py`
- **Size**: 1,419 characters, 49 lines
- **Words**: 142
- **Extension**: .py
- **Classification**: Text file

## Original Source

```python
"""Short Volume Standard Model."""

from datetime import date as dateType

from openbb_core.provider.abstract.data import Data
from openbb_core.provider.abstract.query_params import QueryParams
from openbb_core.provider.utils.descriptions import (
    DATA_DESCRIPTIONS,
    QUERY_DESCRIPTIONS,
)
from pydantic import Field


class ShortVolumeQueryParams(QueryParams):
    """Short Volume Query."""

    symbol: str = Field(description=QUERY_DESCRIPTIONS.get("symbol"))


class ShortVolumeData(Data):
    """Short Volume Data."""

    date: dateType | None = Field(
        default=None, description=DATA_DESCRIPTIONS.get("date")
    )

    market: str | None = Field(
        default=None,
        description="Reporting Facility ID. N=NYSE TRF, Q=NASDAQ TRF Carteret, B=NASDAQ TRY Chicago, D=FINRA ADF",
    )

    short_volume: int | None = Field(
        default=None,
        description=(
            "Aggregate reported share volume of executed short sale "
            "and short sale exempt trades during regular trading hours"
        ),
    )

    short_exempt_volume: int | None = Field(
        default=None,
        description="Aggregate reported share volume of executed short sale exempt trades during regular trading hours",
    )

    total_volume: int | None = Field(
        default=None,
        description="Aggregate reported share volume of executed trades during regular trading hours",
    )

```

## High-Level Overview

Short Volume Standard Model.

from datetime import date as dateType

from openbb_core.provider.abstract.data import Data
from openbb_core.provider.abstract.query_params import QueryParams
from openbb_core.provider.utils.descriptions import (
DATA_DESCRIPTIONS,
QUERY_DESCRIPTIONS,
)
from pydantic import Field


class ShortVolumeQueryParams(QueryParams):
Short Volume Query.
Short Volume Data.

date: dateType | None = Field(
default=None, description=DATA_DESCRIPTIONS.get("date")
)

## Detailed Structure

### Python File Structure

**Classes** (2):
`ShortVolumeQueryParams`, `ShortVolumeData`

**Functions** (0):
None

**Imports** (9):
`datetime`, `date`, `openbb_core.provider.abstract.data`, `Data`, `openbb_core.provider.abstract.query_params`, `QueryParams`, `openbb_core.provider.utils.descriptions`, `pydantic`, `Field`


## Key Components

**Class `ShortVolumeQueryParams`**: Short Volume Query.

**Class `ShortVolumeData`**: Short Volume Data.

## Usage & Examples

See source code for usage details.

## Related Files

- `datetime`
- `openbb_core.provider.abstract.data`
- `openbb_core.provider.abstract.query_params`
- `openbb_core.provider.utils.descriptions`
- `pydantic`

## Notes
- Generated: 2025-11-18T07:54:35.739027
- Generator: World's Best Repo Book Generator v1.0.0

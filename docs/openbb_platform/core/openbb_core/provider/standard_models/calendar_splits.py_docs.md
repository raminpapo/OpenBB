# Documentation: openbb_platform/core/openbb_core/provider/standard_models/calendar_splits.py

## File Metadata
- **Path**: `openbb_platform/core/openbb_core/provider/standard_models/calendar_splits.py`
- **Size**: 1,015 characters, 32 lines
- **Words**: 85
- **Extension**: .py
- **Classification**: Text file

## Original Source

```python
"""Calendar Splits Standard Model."""

from datetime import date as dateType

from openbb_core.provider.abstract.data import Data
from openbb_core.provider.abstract.query_params import QueryParams
from openbb_core.provider.utils.descriptions import (
    DATA_DESCRIPTIONS,
    QUERY_DESCRIPTIONS,
)
from pydantic import Field


class CalendarSplitsQueryParams(QueryParams):
    """Calendar Splits Query."""

    start_date: dateType | None = Field(
        description=QUERY_DESCRIPTIONS.get("start_date", ""), default=None
    )
    end_date: dateType | None = Field(
        description=QUERY_DESCRIPTIONS.get("end_date", ""), default=None
    )


class CalendarSplitsData(Data):
    """Calendar Splits Data."""

    date: dateType = Field(description=DATA_DESCRIPTIONS.get("date", ""))
    symbol: str = Field(description=DATA_DESCRIPTIONS.get("symbol", ""))
    numerator: float = Field(description="Numerator of the stock split.")
    denominator: float = Field(description="Denominator of the stock split.")

```

## High-Level Overview

Calendar Splits Standard Model.

from datetime import date as dateType

from openbb_core.provider.abstract.data import Data
from openbb_core.provider.abstract.query_params import QueryParams
from openbb_core.provider.utils.descriptions import (
DATA_DESCRIPTIONS,
QUERY_DESCRIPTIONS,
)
from pydantic import Field


class CalendarSplitsQueryParams(QueryParams):
Calendar Splits Query.
Calendar Splits Data.

date: dateType = Field(description=DATA_DESCRIPTIONS.get("date", ""))
symbol: str = Field(description=DATA_DESCRIPTIONS.get("symbol", ""))
numerator: float = Field(description="Numerator of the stock split.")

## Detailed Structure

### Python File Structure

**Classes** (2):
`CalendarSplitsQueryParams`, `CalendarSplitsData`

**Functions** (0):
None

**Imports** (9):
`datetime`, `date`, `openbb_core.provider.abstract.data`, `Data`, `openbb_core.provider.abstract.query_params`, `QueryParams`, `openbb_core.provider.utils.descriptions`, `pydantic`, `Field`


## Key Components

**Class `CalendarSplitsQueryParams`**: Calendar Splits Query.

**Class `CalendarSplitsData`**: Calendar Splits Data.

## Usage & Examples

See source code for usage details.

## Related Files

- `datetime`
- `openbb_core.provider.abstract.data`
- `openbb_core.provider.abstract.query_params`
- `openbb_core.provider.utils.descriptions`
- `pydantic`

## Notes
- Generated: 2025-11-18T07:54:35.549410
- Generator: World's Best Repo Book Generator v1.0.0

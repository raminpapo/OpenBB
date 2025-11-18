# Documentation: openbb_platform/core/openbb_core/provider/standard_models/calendar_earnings.py

## File Metadata
- **Path**: `openbb_platform/core/openbb_core/provider/standard_models/calendar_earnings.py`
- **Size**: 1,256 characters, 39 lines
- **Words**: 112
- **Extension**: .py
- **Classification**: Text file

## Original Source

```python
"""Earnings Calendar Standard Model."""

from datetime import date as dateType

from openbb_core.provider.abstract.data import Data
from openbb_core.provider.abstract.query_params import QueryParams
from openbb_core.provider.utils.descriptions import (
    DATA_DESCRIPTIONS,
    QUERY_DESCRIPTIONS,
)
from pydantic import Field


class CalendarEarningsQueryParams(QueryParams):
    """Earnings Calendar Query."""

    start_date: dateType | None = Field(
        default=None, description=QUERY_DESCRIPTIONS.get("start_date", "")
    )
    end_date: dateType | None = Field(
        default=None, description=QUERY_DESCRIPTIONS.get("end_date", "")
    )


class CalendarEarningsData(Data):
    """Earnings Calendar Data."""

    report_date: dateType = Field(description="The date of the earnings report.")
    symbol: str = Field(description=DATA_DESCRIPTIONS.get("symbol", ""))
    name: str | None = Field(description="Name of the entity.", default=None)
    eps_previous: float | None = Field(
        default=None,
        description="The earnings-per-share from the same previously reported period.",
    )
    eps_consensus: float | None = Field(
        default=None,
        description="The analyst conesus earnings-per-share estimate.",
    )

```

## High-Level Overview

Earnings Calendar Standard Model.

from datetime import date as dateType

from openbb_core.provider.abstract.data import Data
from openbb_core.provider.abstract.query_params import QueryParams
from openbb_core.provider.utils.descriptions import (
DATA_DESCRIPTIONS,
QUERY_DESCRIPTIONS,
)
from pydantic import Field


class CalendarEarningsQueryParams(QueryParams):
Earnings Calendar Query.
Earnings Calendar Data.

report_date: dateType = Field(description="The date of the earnings report.")
symbol: str = Field(description=DATA_DESCRIPTIONS.get("symbol", ""))
name: str | None = Field(description="Name of the entity.", default=None)

## Detailed Structure

### Python File Structure

**Classes** (2):
`CalendarEarningsQueryParams`, `CalendarEarningsData`

**Functions** (0):
None

**Imports** (10):
`datetime`, `date`, `openbb_core.provider.abstract.data`, `Data`, `openbb_core.provider.abstract.query_params`, `QueryParams`, `openbb_core.provider.utils.descriptions`, `pydantic`, `Field`, `the`


## Key Components

**Class `CalendarEarningsQueryParams`**: Earnings Calendar Query.

**Class `CalendarEarningsData`**: Earnings Calendar Data.

## Usage & Examples

See source code for usage details.

## Related Files

- `datetime`
- `openbb_core.provider.abstract.data`
- `openbb_core.provider.abstract.query_params`
- `openbb_core.provider.utils.descriptions`
- `pydantic`

## Notes
- Generated: 2025-11-18T07:54:35.545528
- Generator: World's Best Repo Book Generator v1.0.0

# Documentation: openbb_platform/core/openbb_core/provider/standard_models/calendar_events.py

## File Metadata
- **Path**: `openbb_platform/core/openbb_core/provider/standard_models/calendar_events.py`
- **Size**: 929 characters, 32 lines
- **Words**: 81
- **Extension**: .py
- **Classification**: Text file

## Original Source

```python
"""Company Events Calendar Standard Model."""

from datetime import date as dateType

from openbb_core.provider.abstract.data import Data
from openbb_core.provider.abstract.query_params import QueryParams
from openbb_core.provider.utils.descriptions import (
    DATA_DESCRIPTIONS,
    QUERY_DESCRIPTIONS,
)
from pydantic import Field


class CalendarEventsQueryParams(QueryParams):
    """Company Events Calendar Query."""

    start_date: dateType | None = Field(
        default=None, description=QUERY_DESCRIPTIONS.get("start_date", "")
    )
    end_date: dateType | None = Field(
        default=None, description=QUERY_DESCRIPTIONS.get("end_date", "")
    )


class CalendarEventsData(Data):
    """Company Events Calendar Data."""

    date: dateType = Field(
        description=DATA_DESCRIPTIONS.get("date", "") + " The date of the event."
    )
    symbol: str = Field(description=DATA_DESCRIPTIONS.get("symbol", ""))

```

## High-Level Overview

Company Events Calendar Standard Model.

from datetime import date as dateType

from openbb_core.provider.abstract.data import Data
from openbb_core.provider.abstract.query_params import QueryParams
from openbb_core.provider.utils.descriptions import (
DATA_DESCRIPTIONS,
QUERY_DESCRIPTIONS,
)
from pydantic import Field


class CalendarEventsQueryParams(QueryParams):
Company Events Calendar Query.
Company Events Calendar Data.

date: dateType = Field(
description=DATA_DESCRIPTIONS.get("date", "") + " The date of the event."
)

## Detailed Structure

### Python File Structure

**Classes** (2):
`CalendarEventsQueryParams`, `CalendarEventsData`

**Functions** (0):
None

**Imports** (9):
`datetime`, `date`, `openbb_core.provider.abstract.data`, `Data`, `openbb_core.provider.abstract.query_params`, `QueryParams`, `openbb_core.provider.utils.descriptions`, `pydantic`, `Field`


## Key Components

**Class `CalendarEventsQueryParams`**: Company Events Calendar Query.

**Class `CalendarEventsData`**: Company Events Calendar Data.

## Usage & Examples

See source code for usage details.

## Related Files

- `datetime`
- `openbb_core.provider.abstract.data`
- `openbb_core.provider.abstract.query_params`
- `openbb_core.provider.utils.descriptions`
- `pydantic`

## Notes
- Generated: 2025-11-18T07:54:35.546791
- Generator: World's Best Repo Book Generator v1.0.0

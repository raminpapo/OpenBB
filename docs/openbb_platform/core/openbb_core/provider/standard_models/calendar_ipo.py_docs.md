# Documentation: openbb_platform/core/openbb_core/provider/standard_models/calendar_ipo.py

## File Metadata
- **Path**: `openbb_platform/core/openbb_core/provider/standard_models/calendar_ipo.py`
- **Size**: 1,193 characters, 42 lines
- **Words**: 111
- **Extension**: .py
- **Classification**: Text file

## Original Source

```python
"""IPO Calendar Standard Model."""

from datetime import date as dateType

from openbb_core.provider.abstract.data import Data
from openbb_core.provider.abstract.query_params import QueryParams
from openbb_core.provider.utils.descriptions import (
    DATA_DESCRIPTIONS,
    QUERY_DESCRIPTIONS,
)
from pydantic import Field


class CalendarIpoQueryParams(QueryParams):
    """IPO Calendar Query."""

    symbol: str | None = Field(
        description=QUERY_DESCRIPTIONS.get("symbol", ""), default=None
    )
    start_date: dateType | None = Field(
        description=QUERY_DESCRIPTIONS.get("start_date", ""), default=None
    )
    end_date: dateType | None = Field(
        description=QUERY_DESCRIPTIONS.get("end_date", ""), default=None
    )
    limit: int | None = Field(
        description=QUERY_DESCRIPTIONS.get("limit", ""), default=100
    )


class CalendarIpoData(Data):
    """IPO Calendar Data."""

    symbol: str | None = Field(
        default=None,
        description=DATA_DESCRIPTIONS.get("symbol", ""),
    )
    ipo_date: dateType | None = Field(
        description="The date of the IPO, when the stock first trades on a major exchange.",
        default=None,
    )

```

## High-Level Overview

IPO Calendar Standard Model.

from datetime import date as dateType

from openbb_core.provider.abstract.data import Data
from openbb_core.provider.abstract.query_params import QueryParams
from openbb_core.provider.utils.descriptions import (
DATA_DESCRIPTIONS,
QUERY_DESCRIPTIONS,
)
from pydantic import Field


class CalendarIpoQueryParams(QueryParams):
IPO Calendar Query.
IPO Calendar Data.

symbol: str | None = Field(
default=None,
description=DATA_DESCRIPTIONS.get("symbol", ""),

## Detailed Structure

### Python File Structure

**Classes** (2):
`CalendarIpoQueryParams`, `CalendarIpoData`

**Functions** (0):
None

**Imports** (9):
`datetime`, `date`, `openbb_core.provider.abstract.data`, `Data`, `openbb_core.provider.abstract.query_params`, `QueryParams`, `openbb_core.provider.utils.descriptions`, `pydantic`, `Field`


## Key Components

**Class `CalendarIpoQueryParams`**: IPO Calendar Query.

**Class `CalendarIpoData`**: IPO Calendar Data.

## Usage & Examples

See source code for usage details.

## Related Files

- `datetime`
- `openbb_core.provider.abstract.data`
- `openbb_core.provider.abstract.query_params`
- `openbb_core.provider.utils.descriptions`
- `pydantic`

## Notes
- Generated: 2025-11-18T07:54:35.548060
- Generator: World's Best Repo Book Generator v1.0.0

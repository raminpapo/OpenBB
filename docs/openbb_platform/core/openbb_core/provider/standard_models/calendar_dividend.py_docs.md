# Documentation: openbb_platform/core/openbb_core/provider/standard_models/calendar_dividend.py

## File Metadata
- **Path**: `openbb_platform/core/openbb_core/provider/standard_models/calendar_dividend.py`
- **Size**: 1,549 characters, 48 lines
- **Words**: 151
- **Extension**: .py
- **Classification**: Text file

## Original Source

```python
"""Dividend Calendar Standard Model."""

from datetime import date as dateType

from openbb_core.provider.abstract.data import Data
from openbb_core.provider.abstract.query_params import QueryParams
from openbb_core.provider.utils.descriptions import (
    DATA_DESCRIPTIONS,
    QUERY_DESCRIPTIONS,
)
from pydantic import Field


class CalendarDividendQueryParams(QueryParams):
    """Dividend Calendar Query."""

    start_date: dateType | None = Field(
        default=None, description=QUERY_DESCRIPTIONS.get("start_date", "")
    )
    end_date: dateType | None = Field(
        default=None, description=QUERY_DESCRIPTIONS.get("end_date", "")
    )


class CalendarDividendData(Data):
    """Dividend Calendar Data."""

    ex_dividend_date: dateType = Field(
        description="The ex-dividend date - the date on which the stock begins trading without rights to the dividend."
    )
    symbol: str = Field(description=DATA_DESCRIPTIONS.get("symbol", ""))
    amount: float | None = Field(
        default=None, description="The dividend amount per share."
    )
    name: str | None = Field(default=None, description="Name of the entity.")
    record_date: dateType | None = Field(
        default=None,
        description="The record date of ownership for eligibility.",
    )
    payment_date: dateType | None = Field(
        default=None,
        description="The payment date of the dividend.",
    )
    declaration_date: dateType | None = Field(
        default=None,
        description="Declaration date of the dividend.",
    )

```

## High-Level Overview

Dividend Calendar Standard Model.

from datetime import date as dateType

from openbb_core.provider.abstract.data import Data
from openbb_core.provider.abstract.query_params import QueryParams
from openbb_core.provider.utils.descriptions import (
DATA_DESCRIPTIONS,
QUERY_DESCRIPTIONS,
)
from pydantic import Field


class CalendarDividendQueryParams(QueryParams):
Dividend Calendar Query.
Dividend Calendar Data.

ex_dividend_date: dateType = Field(
description="The ex-dividend date - the date on which the stock begins trading without rights to the dividend."
)

## Detailed Structure

### Python File Structure

**Classes** (2):
`CalendarDividendQueryParams`, `CalendarDividendData`

**Functions** (0):
None

**Imports** (9):
`datetime`, `date`, `openbb_core.provider.abstract.data`, `Data`, `openbb_core.provider.abstract.query_params`, `QueryParams`, `openbb_core.provider.utils.descriptions`, `pydantic`, `Field`


## Key Components

**Class `CalendarDividendQueryParams`**: Dividend Calendar Query.

**Class `CalendarDividendData`**: Dividend Calendar Data.

## Usage & Examples

See source code for usage details.

## Related Files

- `datetime`
- `openbb_core.provider.abstract.data`
- `openbb_core.provider.abstract.query_params`
- `openbb_core.provider.utils.descriptions`
- `pydantic`

## Notes
- Generated: 2025-11-18T07:54:35.544236
- Generator: World's Best Repo Book Generator v1.0.0

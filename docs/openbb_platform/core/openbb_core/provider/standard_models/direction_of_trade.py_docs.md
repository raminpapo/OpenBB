# Documentation: openbb_platform/core/openbb_core/provider/standard_models/direction_of_trade.py

## File Metadata
- **Path**: `openbb_platform/core/openbb_core/provider/standard_models/direction_of_trade.py`
- **Size**: 2,344 characters, 66 lines
- **Words**: 232
- **Extension**: .py
- **Classification**: Text file

## Original Source

```python
"""Direction Of Trade Standard Model."""

from datetime import date as dateType
from typing import Literal

from openbb_core.provider.abstract.data import Data
from openbb_core.provider.abstract.query_params import QueryParams
from openbb_core.provider.utils.descriptions import (
    DATA_DESCRIPTIONS,
    QUERY_DESCRIPTIONS,
)
from pydantic import Field


class DirectionOfTradeQueryParams(QueryParams):
    """Direction Of Trade Query."""

    __json_schema_extra__ = {
        "direction": {
            "choices": ["exports", "imports", "balance", "all"],
        },
        "frequency": {
            "choices": ["month", "quarter", "annual"],
        },
    }

    country: str | None = Field(
        default=None,
        description=QUERY_DESCRIPTIONS.get("country", "")
        + " None is an equiavlent to 'all'. If 'all' is used, the counterpart field cannot be 'all'.",
    )
    counterpart: str | None = Field(
        default=None,
        description="Counterpart country to the trade. None is an equiavlent to 'all'."
        + " If 'all' is used, the country field cannot be 'all'.",
    )
    direction: Literal["exports", "imports", "balance", "all"] = Field(
        default="balance",
        description="Trade direction. Use 'all' to get all data for this dimension.",
    )
    start_date: dateType | None = Field(
        default=None, description=QUERY_DESCRIPTIONS.get("start_date", "")
    )
    end_date: dateType | None = Field(
        default=None, description=QUERY_DESCRIPTIONS.get("end_date", "")
    )
    frequency: Literal["month", "quarter", "annual"] = Field(
        default="month", description=QUERY_DESCRIPTIONS.get("frequency", "")
    )


class DirectionOfTradeData(Data):
    """Direction Of Trade Data."""

    date: dateType = Field(description=DATA_DESCRIPTIONS.get("date", ""))
    symbol: str | None = Field(
        default=None, description=DATA_DESCRIPTIONS.get("symbol", "")
    )
    country: str = Field(description=DATA_DESCRIPTIONS.get("country", ""))
    counterpart: str = Field(description="Counterpart country or region to the trade.")
    title: str | None = Field(
        default=None, description="Title corresponding to the symbol."
    )
    value: float = Field(description="Trade value.")
    scale: str | None = Field(default=None, description="Scale of the value.")

```

## High-Level Overview

Direction Of Trade Standard Model.

from datetime import date as dateType
from typing import Literal

from openbb_core.provider.abstract.data import Data
from openbb_core.provider.abstract.query_params import QueryParams
from openbb_core.provider.utils.descriptions import (
DATA_DESCRIPTIONS,
QUERY_DESCRIPTIONS,
)
from pydantic import Field


class DirectionOfTradeQueryParams(QueryParams):
Direction Of Trade Query.

## Detailed Structure

### Python File Structure

**Classes** (2):
`DirectionOfTradeQueryParams`, `DirectionOfTradeData`

**Functions** (0):
None

**Imports** (11):
`datetime`, `date`, `typing`, `Literal`, `openbb_core.provider.abstract.data`, `Data`, `openbb_core.provider.abstract.query_params`, `QueryParams`, `openbb_core.provider.utils.descriptions`, `pydantic`, `Field`


## Key Components

**Class `DirectionOfTradeQueryParams`**: Direction Of Trade Query.

**Class `DirectionOfTradeData`**: Direction Of Trade Data.

## Usage & Examples

See source code for usage details.

## Related Files

- `datetime`
- `typing`
- `openbb_core.provider.abstract.data`
- `openbb_core.provider.abstract.query_params`
- `openbb_core.provider.utils.descriptions`
- `pydantic`

## Notes
- Generated: 2025-11-18T07:54:35.581167
- Generator: World's Best Repo Book Generator v1.0.0

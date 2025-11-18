# Documentation: openbb_platform/core/openbb_core/provider/standard_models/futures_historical.py

## File Metadata
- **Path**: `openbb_platform/core/openbb_core/provider/standard_models/futures_historical.py`
- **Size**: 1,819 characters, 54 lines
- **Words**: 143
- **Extension**: .py
- **Classification**: Text file

## Original Source

```python
"""Futures Historical Price Standard Model."""

from datetime import date, datetime

from dateutil import parser
from openbb_core.provider.abstract.data import Data
from openbb_core.provider.abstract.query_params import QueryParams
from openbb_core.provider.utils.descriptions import (
    DATA_DESCRIPTIONS,
    QUERY_DESCRIPTIONS,
)
from pydantic import Field, field_validator


class FuturesHistoricalQueryParams(QueryParams):
    """Futures Historical Price Query."""

    symbol: str = Field(description=QUERY_DESCRIPTIONS.get("symbol", ""))
    start_date: date | None = Field(
        default=None,
        description=QUERY_DESCRIPTIONS.get("start_date", ""),
    )
    end_date: date | None = Field(
        default=None,
        description=QUERY_DESCRIPTIONS.get("end_date", ""),
    )
    expiration: str | None = Field(
        default=None,
        description="Future expiry date with format YYYY-MM",
    )

    @field_validator("symbol", mode="before", check_fields=False)
    @classmethod
    def to_upper(cls, v: str) -> str:
        """Convert field to uppercase."""
        return v.upper()


class FuturesHistoricalData(Data):
    """Futures Historical Price Data."""

    date: datetime = Field(description=DATA_DESCRIPTIONS.get("date", ""))
    open: float = Field(description=DATA_DESCRIPTIONS.get("open", ""))
    high: float = Field(description=DATA_DESCRIPTIONS.get("high", ""))
    low: float = Field(description=DATA_DESCRIPTIONS.get("low", ""))
    close: float = Field(description=DATA_DESCRIPTIONS.get("close", ""))
    volume: float = Field(description=DATA_DESCRIPTIONS.get("volume", ""))

    @field_validator("symbol", mode="before", check_fields=False)
    @classmethod
    def date_validate(cls, v):
        """Return formatted datetime."""
        return parser.isoparse(str(v))

```

## High-Level Overview

Futures Historical Price Standard Model.

from datetime import date, datetime

from dateutil import parser
from openbb_core.provider.abstract.data import Data
from openbb_core.provider.abstract.query_params import QueryParams
from openbb_core.provider.utils.descriptions import (
DATA_DESCRIPTIONS,
QUERY_DESCRIPTIONS,
)
from pydantic import Field, field_validator


class FuturesHistoricalQueryParams(QueryParams):
Futures Historical Price Query.
Convert field to uppercase.
return v.upper()



## Detailed Structure

### Python File Structure

**Classes** (2):
`FuturesHistoricalQueryParams`, `FuturesHistoricalData`

**Functions** (2):
`to_upper`, `date_validate`

**Imports** (11):
`datetime`, `date`, `dateutil`, `parser`, `openbb_core.provider.abstract.data`, `Data`, `openbb_core.provider.abstract.query_params`, `QueryParams`, `openbb_core.provider.utils.descriptions`, `pydantic`, `Field`


## Key Components

**Class `FuturesHistoricalQueryParams`**: Futures Historical Price Query.

**Class `FuturesHistoricalData`**: Futures Historical Price Data.

## Usage & Examples

See source code for usage details.

## Related Files

- `datetime`
- `dateutil`
- `openbb_core.provider.abstract.data`
- `openbb_core.provider.abstract.query_params`
- `openbb_core.provider.utils.descriptions`
- `pydantic`

## Notes
- Generated: 2025-11-18T07:54:35.648747
- Generator: World's Best Repo Book Generator v1.0.0

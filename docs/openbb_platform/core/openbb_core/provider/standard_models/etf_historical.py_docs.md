# Documentation: openbb_platform/core/openbb_core/provider/standard_models/etf_historical.py

## File Metadata
- **Path**: `openbb_platform/core/openbb_core/provider/standard_models/etf_historical.py`
- **Size**: 1,915 characters, 56 lines
- **Words**: 155
- **Extension**: .py
- **Classification**: Text file

## Original Source

```python
"""ETF Historical Price Standard Model."""

from datetime import (
    date as dateType,
    datetime,
)

from dateutil import parser
from openbb_core.provider.abstract.data import Data
from openbb_core.provider.abstract.query_params import QueryParams
from openbb_core.provider.utils.descriptions import (
    DATA_DESCRIPTIONS,
    QUERY_DESCRIPTIONS,
)
from pydantic import Field, NonNegativeInt, PositiveFloat, field_validator


class EtfHistoricalQueryParams(QueryParams):
    """ETF Historical Price Query."""

    symbol: str = Field(description=QUERY_DESCRIPTIONS.get("symbol", "") + " (ETF)")
    start_date: dateType | None = Field(
        default=None,
        description=QUERY_DESCRIPTIONS.get("start_date", ""),
    )
    end_date: dateType | None = Field(
        default=None,
        description=QUERY_DESCRIPTIONS.get("end_date", ""),
    )

    @field_validator("symbol", mode="before", check_fields=False)
    @classmethod
    def to_upper(cls, v: str) -> str:
        """Convert field to uppercase and remove '-'."""
        return v.upper()


class EtfHistoricalData(Data):
    """ETF Historical Price Data."""

    date: dateType | datetime = Field(description=DATA_DESCRIPTIONS.get("date", ""))
    open: PositiveFloat = Field(description=DATA_DESCRIPTIONS.get("open", ""))
    high: PositiveFloat = Field(description=DATA_DESCRIPTIONS.get("high", ""))
    low: PositiveFloat = Field(description=DATA_DESCRIPTIONS.get("low", ""))
    close: PositiveFloat = Field(description=DATA_DESCRIPTIONS.get("close", ""))
    volume: NonNegativeInt | None = Field(
        description=DATA_DESCRIPTIONS.get("volume", "")
    )

    @field_validator("date", mode="before", check_fields=False)
    def date_validate(cls, v):  # pylint: disable=E0213
        """Return formatted datetime."""
        if ":" in str(v):
            return parser.isoparse(str(v))
        return parser.parse(str(v)).date()

```

## High-Level Overview

ETF Historical Price Standard Model.

from datetime import (
date as dateType,
datetime,
)

from dateutil import parser
from openbb_core.provider.abstract.data import Data
from openbb_core.provider.abstract.query_params import QueryParams
from openbb_core.provider.utils.descriptions import (
DATA_DESCRIPTIONS,
QUERY_DESCRIPTIONS,
)
from pydantic import Field, NonNegativeInt, PositiveFloat, field_validator


class EtfHistoricalQueryParams(QueryParams):
ETF Historical Price Query.
Convert field to uppercase and remove '-'.

## Detailed Structure

### Python File Structure

**Classes** (2):
`EtfHistoricalQueryParams`, `EtfHistoricalData`

**Functions** (2):
`to_upper`, `date_validate`

**Imports** (10):
`datetime`, `dateutil`, `parser`, `openbb_core.provider.abstract.data`, `Data`, `openbb_core.provider.abstract.query_params`, `QueryParams`, `openbb_core.provider.utils.descriptions`, `pydantic`, `Field`


## Key Components

**Class `EtfHistoricalQueryParams`**: ETF Historical Price Query.

**Class `EtfHistoricalData`**: ETF Historical Price Data.

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
- Generated: 2025-11-18T07:54:35.615492
- Generator: World's Best Repo Book Generator v1.0.0

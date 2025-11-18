# Documentation: openbb_platform/core/openbb_core/provider/standard_models/currency_historical.py

## File Metadata
- **Path**: `openbb_platform/core/openbb_core/provider/standard_models/currency_historical.py`
- **Size**: 2,332 characters, 70 lines
- **Words**: 202
- **Extension**: .py
- **Classification**: Text file

## Original Source

```python
"""Currency Historical Price Standard Model."""

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
from pydantic import Field, field_validator


class CurrencyHistoricalQueryParams(QueryParams):
    """Currency Historical Price Query."""

    symbol: str = Field(
        description=QUERY_DESCRIPTIONS.get("symbol", "")
        + " Can use CURR1-CURR2 or CURR1CURR2 format."
    )
    start_date: dateType | None = Field(
        default=None,
        description=QUERY_DESCRIPTIONS.get("start_date", ""),
    )
    end_date: dateType | None = Field(
        default=None,
        description=QUERY_DESCRIPTIONS.get("end_date", ""),
    )

    @field_validator("symbol", mode="before", check_fields=False)
    def validate_symbol(cls, v: str | list[str] | set[str]):  # pylint: disable=E0213
        """Convert field to uppercase and remove '-'."""
        if isinstance(v, str):
            return v.upper().replace("-", "")
        return ",".join([symbol.upper().replace("-", "") for symbol in list(v)])


class CurrencyHistoricalData(Data):
    """Currency Historical Price Data."""

    date: dateType | datetime = Field(description=DATA_DESCRIPTIONS.get("date", ""))
    open: float | None = Field(
        default=None, description=DATA_DESCRIPTIONS.get("open", "")
    )
    high: float | None = Field(
        default=None, description=DATA_DESCRIPTIONS.get("high", "")
    )
    low: float | None = Field(
        default=None, description=DATA_DESCRIPTIONS.get("low", "")
    )
    close: float = Field(description=DATA_DESCRIPTIONS.get("close", ""))
    volume: float | None = Field(
        description=DATA_DESCRIPTIONS.get("volume", ""), default=None
    )
    vwap: float | None = Field(
        description=DATA_DESCRIPTIONS.get("vwap", ""), default=None
    )

    @field_validator("date", mode="before", check_fields=False)
    @classmethod
    def date_validate(cls, v):  # pylint: disable=E0213
        """Return formatted datetime."""
        if ":" in str(v):
            return parser.isoparse(str(v))
        return parser.parse(str(v)).date()

```

## High-Level Overview

Currency Historical Price Standard Model.

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
from pydantic import Field, field_validator


class CurrencyHistoricalQueryParams(QueryParams):
Currency Historical Price Query.
Convert field to uppercase and remove '-'.

## Detailed Structure

### Python File Structure

**Classes** (2):
`CurrencyHistoricalQueryParams`, `CurrencyHistoricalData`

**Functions** (2):
`validate_symbol`, `date_validate`

**Imports** (10):
`datetime`, `dateutil`, `parser`, `openbb_core.provider.abstract.data`, `Data`, `openbb_core.provider.abstract.query_params`, `QueryParams`, `openbb_core.provider.utils.descriptions`, `pydantic`, `Field`


## Key Components

**Class `CurrencyHistoricalQueryParams`**: Currency Historical Price Query.

**Class `CurrencyHistoricalData`**: Currency Historical Price Data.

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
- Generated: 2025-11-18T07:54:35.574813
- Generator: World's Best Repo Book Generator v1.0.0

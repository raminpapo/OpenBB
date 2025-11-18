# Documentation: openbb_platform/core/openbb_core/provider/standard_models/crypto_historical.py

## File Metadata
- **Path**: `openbb_platform/core/openbb_core/provider/standard_models/crypto_historical.py`
- **Size**: 2,083 characters, 66 lines
- **Words**: 174
- **Extension**: .py
- **Classification**: Text file

## Original Source

```python
"""Crypto Historical Price Standard Model."""

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


class CryptoHistoricalQueryParams(QueryParams):
    """Crypto Historical Price Query."""

    symbol: str = Field(description=QUERY_DESCRIPTIONS.get("symbol", ""))
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
    def _to_upper(cls, v):
        """Convert field to uppercase and remove '-'."""
        return str(v).upper()


class CryptoHistoricalData(Data):
    """Crypto Historical Price Data."""

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
        default=None, description=DATA_DESCRIPTIONS.get("volume", "")
    )
    vwap: float | None = Field(
        default=None, description=DATA_DESCRIPTIONS.get("vwap", "")
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

Crypto Historical Price Standard Model.

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


class CryptoHistoricalQueryParams(QueryParams):
Crypto Historical Price Query.
Convert field to uppercase and remove '-'.

## Detailed Structure

### Python File Structure

**Classes** (2):
`CryptoHistoricalQueryParams`, `CryptoHistoricalData`

**Functions** (2):
`_to_upper`, `date_validate`

**Imports** (10):
`datetime`, `dateutil`, `parser`, `openbb_core.provider.abstract.data`, `Data`, `openbb_core.provider.abstract.query_params`, `QueryParams`, `openbb_core.provider.utils.descriptions`, `pydantic`, `Field`


## Key Components

**Class `CryptoHistoricalQueryParams`**: Crypto Historical Price Query.

**Class `CryptoHistoricalData`**: Crypto Historical Price Data.

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
- Generated: 2025-11-18T07:54:35.572105
- Generator: World's Best Repo Book Generator v1.0.0

# Documentation: openbb_platform/core/openbb_core/provider/standard_models/historical_dividends.py

## File Metadata
- **Path**: `openbb_platform/core/openbb_core/provider/standard_models/historical_dividends.py`
- **Size**: 1,367 characters, 42 lines
- **Words**: 121
- **Extension**: .py
- **Classification**: Text file

## Original Source

```python
"""Historical Dividends Standard Model."""

from datetime import date as dateType

from openbb_core.provider.abstract.data import Data
from openbb_core.provider.abstract.query_params import QueryParams
from openbb_core.provider.utils.descriptions import (
    DATA_DESCRIPTIONS,
    QUERY_DESCRIPTIONS,
)
from pydantic import Field, field_validator


class HistoricalDividendsQueryParams(QueryParams):
    """Historical Dividends Query."""

    symbol: str = Field(description=QUERY_DESCRIPTIONS.get("symbol", ""))
    start_date: dateType | None = Field(
        default=None, description=QUERY_DESCRIPTIONS.get("start_date", "")
    )
    end_date: dateType | None = Field(
        default=None, description=QUERY_DESCRIPTIONS.get("end_date", "")
    )

    @field_validator("symbol", mode="before", check_fields=False)
    @classmethod
    def to_upper(cls, v: str) -> str:
        """Convert field to uppercase."""
        return v.upper()


class HistoricalDividendsData(Data):
    """Historical Dividends Data."""

    symbol: str | None = Field(
        default=None, description=DATA_DESCRIPTIONS.get("symbol", "")
    )
    ex_dividend_date: dateType = Field(
        description="The ex-dividend date - the date on which the stock begins trading without rights to the dividend."
    )
    amount: float = Field(description="The dividend amount per share.")

```

## High-Level Overview

Historical Dividends Standard Model.

from datetime import date as dateType

from openbb_core.provider.abstract.data import Data
from openbb_core.provider.abstract.query_params import QueryParams
from openbb_core.provider.utils.descriptions import (
DATA_DESCRIPTIONS,
QUERY_DESCRIPTIONS,
)
from pydantic import Field, field_validator


class HistoricalDividendsQueryParams(QueryParams):
Historical Dividends Query.
Convert field to uppercase.
return v.upper()


class HistoricalDividendsData(Data):

## Detailed Structure

### Python File Structure

**Classes** (2):
`HistoricalDividendsQueryParams`, `HistoricalDividendsData`

**Functions** (1):
`to_upper`

**Imports** (9):
`datetime`, `date`, `openbb_core.provider.abstract.data`, `Data`, `openbb_core.provider.abstract.query_params`, `QueryParams`, `openbb_core.provider.utils.descriptions`, `pydantic`, `Field`


## Key Components

**Class `HistoricalDividendsQueryParams`**: Historical Dividends Query.

**Class `HistoricalDividendsData`**: Historical Dividends Data.

## Usage & Examples

See source code for usage details.

## Related Files

- `datetime`
- `openbb_core.provider.abstract.data`
- `openbb_core.provider.abstract.query_params`
- `openbb_core.provider.utils.descriptions`
- `pydantic`

## Notes
- Generated: 2025-11-18T07:54:35.661250
- Generator: World's Best Repo Book Generator v1.0.0

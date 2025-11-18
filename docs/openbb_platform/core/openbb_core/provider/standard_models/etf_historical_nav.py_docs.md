# Documentation: openbb_platform/core/openbb_core/provider/standard_models/etf_historical_nav.py

## File Metadata
- **Path**: `openbb_platform/core/openbb_core/provider/standard_models/etf_historical_nav.py`
- **Size**: 870 characters, 31 lines
- **Words**: 76
- **Extension**: .py
- **Classification**: Text file

## Original Source

```python
"""ETF Historical NAV model."""

from datetime import date as dateType

from openbb_core.provider.abstract.data import Data
from openbb_core.provider.abstract.query_params import QueryParams
from openbb_core.provider.utils.descriptions import (
    DATA_DESCRIPTIONS,
    QUERY_DESCRIPTIONS,
)
from pydantic import Field, field_validator


class EtfHistoricalNavQueryParams(QueryParams):
    """ETF Historical NAV Query."""

    symbol: str = Field(description=QUERY_DESCRIPTIONS.get("symbol", ""))

    @field_validator("symbol")
    @classmethod
    def to_upper(cls, v: str) -> str:
        """Convert field to uppercase."""
        return v.upper()


class EtfHistoricalNavData(Data):
    """ETF Historical NAV Data."""

    date: dateType = Field(description=DATA_DESCRIPTIONS.get("date", ""))
    nav: float = Field(description="The net asset value on the date.")

```

## High-Level Overview

ETF Historical NAV model.

from datetime import date as dateType

from openbb_core.provider.abstract.data import Data
from openbb_core.provider.abstract.query_params import QueryParams
from openbb_core.provider.utils.descriptions import (
DATA_DESCRIPTIONS,
QUERY_DESCRIPTIONS,
)
from pydantic import Field, field_validator


class EtfHistoricalNavQueryParams(QueryParams):
ETF Historical NAV Query.
Convert field to uppercase.
return v.upper()


class EtfHistoricalNavData(Data):

## Detailed Structure

### Python File Structure

**Classes** (2):
`EtfHistoricalNavQueryParams`, `EtfHistoricalNavData`

**Functions** (1):
`to_upper`

**Imports** (9):
`datetime`, `date`, `openbb_core.provider.abstract.data`, `Data`, `openbb_core.provider.abstract.query_params`, `QueryParams`, `openbb_core.provider.utils.descriptions`, `pydantic`, `Field`


## Key Components

**Class `EtfHistoricalNavQueryParams`**: ETF Historical NAV Query.

**Class `EtfHistoricalNavData`**: ETF Historical NAV Data.

## Usage & Examples

See source code for usage details.

## Related Files

- `datetime`
- `openbb_core.provider.abstract.data`
- `openbb_core.provider.abstract.query_params`
- `openbb_core.provider.utils.descriptions`
- `pydantic`

## Notes
- Generated: 2025-11-18T07:54:35.616859
- Generator: World's Best Repo Book Generator v1.0.0

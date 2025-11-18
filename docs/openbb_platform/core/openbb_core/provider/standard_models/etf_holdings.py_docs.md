# Documentation: openbb_platform/core/openbb_core/provider/standard_models/etf_holdings.py

## File Metadata
- **Path**: `openbb_platform/core/openbb_core/provider/standard_models/etf_holdings.py`
- **Size**: 886 characters, 34 lines
- **Words**: 78
- **Extension**: .py
- **Classification**: Text file

## Original Source

```python
"""ETF Holdings Standard Model."""

from openbb_core.provider.abstract.data import Data
from openbb_core.provider.abstract.query_params import QueryParams
from openbb_core.provider.utils.descriptions import (
    DATA_DESCRIPTIONS,
    QUERY_DESCRIPTIONS,
)
from pydantic import Field, field_validator


class EtfHoldingsQueryParams(QueryParams):
    """ETF Holdings Query."""

    symbol: str = Field(description=QUERY_DESCRIPTIONS.get("symbol", "") + " (ETF)")

    @field_validator("symbol")
    @classmethod
    def to_upper(cls, v: str) -> str:
        """Convert field to uppercase."""
        return v.upper()


class EtfHoldingsData(Data):
    """ETF Holdings Data."""

    symbol: str | None = Field(
        default=None, description=DATA_DESCRIPTIONS.get("symbol", "")
    )
    name: str | None = Field(
        default=None,
        description="Name of the asset.",
    )

```

## High-Level Overview

ETF Holdings Standard Model.

from openbb_core.provider.abstract.data import Data
from openbb_core.provider.abstract.query_params import QueryParams
from openbb_core.provider.utils.descriptions import (
DATA_DESCRIPTIONS,
QUERY_DESCRIPTIONS,
)
from pydantic import Field, field_validator


class EtfHoldingsQueryParams(QueryParams):
ETF Holdings Query.
Convert field to uppercase.
return v.upper()


class EtfHoldingsData(Data):
ETF Holdings Data.

## Detailed Structure

### Python File Structure

**Classes** (2):
`EtfHoldingsQueryParams`, `EtfHoldingsData`

**Functions** (1):
`to_upper`

**Imports** (7):
`openbb_core.provider.abstract.data`, `Data`, `openbb_core.provider.abstract.query_params`, `QueryParams`, `openbb_core.provider.utils.descriptions`, `pydantic`, `Field`


## Key Components

**Class `EtfHoldingsQueryParams`**: ETF Holdings Query.

**Class `EtfHoldingsData`**: ETF Holdings Data.

## Usage & Examples

See source code for usage details.

## Related Files

- `openbb_core.provider.abstract.data`
- `openbb_core.provider.abstract.query_params`
- `openbb_core.provider.utils.descriptions`
- `pydantic`

## Notes
- Generated: 2025-11-18T07:54:35.618182
- Generator: World's Best Repo Book Generator v1.0.0

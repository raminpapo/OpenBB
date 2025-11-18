# Documentation: openbb_platform/core/openbb_core/provider/standard_models/equity_peers.py

## File Metadata
- **Path**: `openbb_platform/core/openbb_core/provider/standard_models/equity_peers.py`
- **Size**: 775 characters, 28 lines
- **Words**: 60
- **Extension**: .py
- **Classification**: Text file

## Original Source

```python
"""Equity Peers Standard Model."""

from openbb_core.provider.abstract.data import Data
from openbb_core.provider.abstract.query_params import QueryParams
from openbb_core.provider.utils.descriptions import (
    DATA_DESCRIPTIONS,
    QUERY_DESCRIPTIONS,
)
from pydantic import Field, field_validator


class EquityPeersQueryParams(QueryParams):
    """Equity Peers Query."""

    symbol: str = Field(description=QUERY_DESCRIPTIONS.get("symbol", ""))

    @field_validator("symbol", mode="before", check_fields=False)
    @classmethod
    def to_upper(cls, v: str) -> str:
        """Convert field to uppercase."""
        return v.upper()


class EquityPeersData(Data):
    """Equity Peers Data."""

    symbol: str = Field(description=DATA_DESCRIPTIONS.get("symbol", ""))

```

## High-Level Overview

Equity Peers Standard Model.

from openbb_core.provider.abstract.data import Data
from openbb_core.provider.abstract.query_params import QueryParams
from openbb_core.provider.utils.descriptions import (
DATA_DESCRIPTIONS,
QUERY_DESCRIPTIONS,
)
from pydantic import Field, field_validator


class EquityPeersQueryParams(QueryParams):
Equity Peers Query.
Convert field to uppercase.
return v.upper()


class EquityPeersData(Data):
Equity Peers Data.

## Detailed Structure

### Python File Structure

**Classes** (2):
`EquityPeersQueryParams`, `EquityPeersData`

**Functions** (1):
`to_upper`

**Imports** (7):
`openbb_core.provider.abstract.data`, `Data`, `openbb_core.provider.abstract.query_params`, `QueryParams`, `openbb_core.provider.utils.descriptions`, `pydantic`, `Field`


## Key Components

**Class `EquityPeersQueryParams`**: Equity Peers Query.

**Class `EquityPeersData`**: Equity Peers Data.

## Usage & Examples

See source code for usage details.

## Related Files

- `openbb_core.provider.abstract.data`
- `openbb_core.provider.abstract.query_params`
- `openbb_core.provider.utils.descriptions`
- `pydantic`

## Notes
- Generated: 2025-11-18T07:54:35.599957
- Generator: World's Best Repo Book Generator v1.0.0

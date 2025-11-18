# Documentation: openbb_platform/core/openbb_core/provider/standard_models/equity_screener.py

## File Metadata
- **Path**: `openbb_platform/core/openbb_core/provider/standard_models/equity_screener.py`
- **Size**: 555 characters, 18 lines
- **Words**: 45
- **Extension**: .py
- **Classification**: Text file

## Original Source

```python
"""Equity Screener Standard Model."""

from openbb_core.provider.abstract.data import Data
from openbb_core.provider.abstract.query_params import QueryParams
from openbb_core.provider.utils.descriptions import DATA_DESCRIPTIONS
from pydantic import Field


class EquityScreenerQueryParams(QueryParams):
    """Equity Screener Query."""


class EquityScreenerData(Data):
    """Equity Screener Data."""

    symbol: str = Field(description=DATA_DESCRIPTIONS.get("symbol", ""))
    name: str | None = Field(default=None, description="Name of the company.")

```

## High-Level Overview

Equity Screener Standard Model.

from openbb_core.provider.abstract.data import Data
from openbb_core.provider.abstract.query_params import QueryParams
from openbb_core.provider.utils.descriptions import DATA_DESCRIPTIONS
from pydantic import Field


class EquityScreenerQueryParams(QueryParams):
Equity Screener Query.
Equity Screener Data.

symbol: str = Field(description=DATA_DESCRIPTIONS.get("symbol", ""))
name: str | None = Field(default=None, description="Name of the company.")


## Detailed Structure

### Python File Structure

**Classes** (2):
`EquityScreenerQueryParams`, `EquityScreenerData`

**Functions** (0):
None

**Imports** (8):
`openbb_core.provider.abstract.data`, `Data`, `openbb_core.provider.abstract.query_params`, `QueryParams`, `openbb_core.provider.utils.descriptions`, `DATA_DESCRIPTIONS`, `pydantic`, `Field`


## Key Components

**Class `EquityScreenerQueryParams`**: Equity Screener Query.

**Class `EquityScreenerData`**: Equity Screener Data.

## Usage & Examples

See source code for usage details.

## Related Files

- `openbb_core.provider.abstract.data`
- `openbb_core.provider.abstract.query_params`
- `openbb_core.provider.utils.descriptions`
- `pydantic`

## Notes
- Generated: 2025-11-18T07:54:35.604761
- Generator: World's Best Repo Book Generator v1.0.0

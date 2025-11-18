# Documentation: openbb_platform/core/openbb_core/provider/standard_models/equity_search.py

## File Metadata
- **Path**: `openbb_platform/core/openbb_core/provider/standard_models/equity_search.py`
- **Size**: 753 characters, 25 lines
- **Words**: 68
- **Extension**: .py
- **Classification**: Text file

## Original Source

```python
"""Equity Search Standard Model."""

from openbb_core.provider.abstract.data import Data
from openbb_core.provider.abstract.query_params import QueryParams
from openbb_core.provider.utils.descriptions import DATA_DESCRIPTIONS
from pydantic import Field


class EquitySearchQueryParams(QueryParams):
    """Equity Search Query."""

    query: str = Field(description="Search query.", default="")
    is_symbol: bool = Field(
        description="Whether to search by ticker symbol.", default=False
    )


class EquitySearchData(Data):
    """Equity Search Data."""

    symbol: str | None = Field(
        default=None, description=DATA_DESCRIPTIONS.get("symbol", "")
    )
    name: str | None = Field(default=None, description="Name of the company.")

```

## High-Level Overview

Equity Search Standard Model.

from openbb_core.provider.abstract.data import Data
from openbb_core.provider.abstract.query_params import QueryParams
from openbb_core.provider.utils.descriptions import DATA_DESCRIPTIONS
from pydantic import Field


class EquitySearchQueryParams(QueryParams):
Equity Search Query.
Equity Search Data.

symbol: str | None = Field(
default=None, description=DATA_DESCRIPTIONS.get("symbol", "")
)
name: str | None = Field(default=None, description="Name of the company.")


## Detailed Structure

### Python File Structure

**Classes** (2):
`EquitySearchQueryParams`, `EquitySearchData`

**Functions** (0):
None

**Imports** (8):
`openbb_core.provider.abstract.data`, `Data`, `openbb_core.provider.abstract.query_params`, `QueryParams`, `openbb_core.provider.utils.descriptions`, `DATA_DESCRIPTIONS`, `pydantic`, `Field`


## Key Components

**Class `EquitySearchQueryParams`**: Equity Search Query.

**Class `EquitySearchData`**: Equity Search Data.

## Usage & Examples

See source code for usage details.

## Related Files

- `openbb_core.provider.abstract.data`
- `openbb_core.provider.abstract.query_params`
- `openbb_core.provider.utils.descriptions`
- `pydantic`

## Notes
- Generated: 2025-11-18T07:54:35.605950
- Generator: World's Best Repo Book Generator v1.0.0

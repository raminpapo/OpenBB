# Documentation: openbb_platform/core/openbb_core/provider/standard_models/currency_pairs.py

## File Metadata
- **Path**: `openbb_platform/core/openbb_core/provider/standard_models/currency_pairs.py`
- **Size**: 696 characters, 22 lines
- **Words**: 63
- **Extension**: .py
- **Classification**: Text file

## Original Source

```python
"""Currency Available Pairs Standard Model."""

from openbb_core.provider.abstract.data import Data
from openbb_core.provider.abstract.query_params import QueryParams
from openbb_core.provider.utils.descriptions import DATA_DESCRIPTIONS
from pydantic import Field


class CurrencyPairsQueryParams(QueryParams):
    """Currency Available Pairs Query."""

    query: str | None = Field(
        default=None, description="Query to search for currency pairs."
    )


class CurrencyPairsData(Data):
    """Currency Available Pairs Data."""

    symbol: str = Field(description=DATA_DESCRIPTIONS.get("symbol", ""))
    name: str | None = Field(default=None, description="Name of the currency pair.")

```

## High-Level Overview

Currency Available Pairs Standard Model.

from openbb_core.provider.abstract.data import Data
from openbb_core.provider.abstract.query_params import QueryParams
from openbb_core.provider.utils.descriptions import DATA_DESCRIPTIONS
from pydantic import Field


class CurrencyPairsQueryParams(QueryParams):
Currency Available Pairs Query.
Currency Available Pairs Data.

symbol: str = Field(description=DATA_DESCRIPTIONS.get("symbol", ""))
name: str | None = Field(default=None, description="Name of the currency pair.")


## Detailed Structure

### Python File Structure

**Classes** (2):
`CurrencyPairsQueryParams`, `CurrencyPairsData`

**Functions** (0):
None

**Imports** (8):
`openbb_core.provider.abstract.data`, `Data`, `openbb_core.provider.abstract.query_params`, `QueryParams`, `openbb_core.provider.utils.descriptions`, `DATA_DESCRIPTIONS`, `pydantic`, `Field`


## Key Components

**Class `CurrencyPairsQueryParams`**: Currency Available Pairs Query.

**Class `CurrencyPairsData`**: Currency Available Pairs Data.

## Usage & Examples

See source code for usage details.

## Related Files

- `openbb_core.provider.abstract.data`
- `openbb_core.provider.abstract.query_params`
- `openbb_core.provider.utils.descriptions`
- `pydantic`

## Notes
- Generated: 2025-11-18T07:54:35.576142
- Generator: World's Best Repo Book Generator v1.0.0

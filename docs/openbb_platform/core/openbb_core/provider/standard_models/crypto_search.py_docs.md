# Documentation: openbb_platform/core/openbb_core/provider/standard_models/crypto_search.py

## File Metadata
- **Path**: `openbb_platform/core/openbb_core/provider/standard_models/crypto_search.py`
- **Size**: 632 characters, 20 lines
- **Words**: 56
- **Extension**: .py
- **Classification**: Text file

## Original Source

```python
"""Crypto Search Standard Model."""

from openbb_core.provider.abstract.data import Data
from openbb_core.provider.abstract.query_params import QueryParams
from openbb_core.provider.utils.descriptions import DATA_DESCRIPTIONS
from pydantic import Field


class CryptoSearchQueryParams(QueryParams):
    """Crypto Search Query."""

    query: str | None = Field(description="Search query.", default=None)


class CryptoSearchData(Data):
    """Crypto Search Data."""

    symbol: str = Field(description=DATA_DESCRIPTIONS.get("symbol", "") + " (Crypto)")
    name: str | None = Field(description="Name of the crypto.", default=None)

```

## High-Level Overview

Crypto Search Standard Model.

from openbb_core.provider.abstract.data import Data
from openbb_core.provider.abstract.query_params import QueryParams
from openbb_core.provider.utils.descriptions import DATA_DESCRIPTIONS
from pydantic import Field


class CryptoSearchQueryParams(QueryParams):
Crypto Search Query.
Crypto Search Data.

symbol: str = Field(description=DATA_DESCRIPTIONS.get("symbol", "") + " (Crypto)")
name: str | None = Field(description="Name of the crypto.", default=None)


## Detailed Structure

### Python File Structure

**Classes** (2):
`CryptoSearchQueryParams`, `CryptoSearchData`

**Functions** (0):
None

**Imports** (8):
`openbb_core.provider.abstract.data`, `Data`, `openbb_core.provider.abstract.query_params`, `QueryParams`, `openbb_core.provider.utils.descriptions`, `DATA_DESCRIPTIONS`, `pydantic`, `Field`


## Key Components

**Class `CryptoSearchQueryParams`**: Crypto Search Query.

**Class `CryptoSearchData`**: Crypto Search Data.

## Usage & Examples

See source code for usage details.

## Related Files

- `openbb_core.provider.abstract.data`
- `openbb_core.provider.abstract.query_params`
- `openbb_core.provider.utils.descriptions`
- `pydantic`

## Notes
- Generated: 2025-11-18T07:54:35.573470
- Generator: World's Best Repo Book Generator v1.0.0

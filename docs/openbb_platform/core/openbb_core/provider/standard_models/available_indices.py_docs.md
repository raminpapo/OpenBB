# Documentation: openbb_platform/core/openbb_core/provider/standard_models/available_indices.py

## File Metadata
- **Path**: `openbb_platform/core/openbb_core/provider/standard_models/available_indices.py`
- **Size**: 891 characters, 31 lines
- **Words**: 86
- **Extension**: .py
- **Classification**: Text file

## Original Source

```python
"""Available Indices Standard Model."""

from openbb_core.provider.abstract.data import Data
from openbb_core.provider.abstract.query_params import QueryParams
from openbb_core.provider.utils.descriptions import (
    DATA_DESCRIPTIONS,
)
from pydantic import Field


class AvailableIndicesQueryParams(QueryParams):
    """Available Indices Query."""


class AvailableIndicesData(Data):
    """Available Indices Data.

    Returns the list of available indices from a provider.
    """

    symbol: str = Field(description=DATA_DESCRIPTIONS.get("symbol", ""))
    name: str | None = Field(
        default=None, description=DATA_DESCRIPTIONS.get("name", "")
    )
    exchange: str | None = Field(
        default=None, description="Stock exchange where the index is listed."
    )
    currency: str | None = Field(
        default=None, description="Currency the index is traded in."
    )

```

## High-Level Overview

Available Indices Standard Model.

from openbb_core.provider.abstract.data import Data
from openbb_core.provider.abstract.query_params import QueryParams
from openbb_core.provider.utils.descriptions import (
DATA_DESCRIPTIONS,
)
from pydantic import Field


class AvailableIndicesQueryParams(QueryParams):
Available Indices Query.
Available Indices Data.

Returns the list of available indices from a provider.


## Detailed Structure

### Python File Structure

**Classes** (2):
`AvailableIndicesQueryParams`, `AvailableIndicesData`

**Functions** (0):
None

**Imports** (8):
`openbb_core.provider.abstract.data`, `Data`, `openbb_core.provider.abstract.query_params`, `QueryParams`, `openbb_core.provider.utils.descriptions`, `pydantic`, `Field`, `a`


## Key Components

**Class `AvailableIndicesQueryParams`**: Available Indices Query.

**Class `AvailableIndicesData`**: Available Indices Data.

    Returns the list of available indices from a provider.

## Usage & Examples

See source code for usage details.

## Related Files

- `openbb_core.provider.abstract.data`
- `openbb_core.provider.abstract.query_params`
- `openbb_core.provider.utils.descriptions`
- `pydantic`

## Notes
- Generated: 2025-11-18T07:54:35.528851
- Generator: World's Best Repo Book Generator v1.0.0

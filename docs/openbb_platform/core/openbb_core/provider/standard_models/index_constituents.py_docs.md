# Documentation: openbb_platform/core/openbb_core/provider/standard_models/index_constituents.py

## File Metadata
- **Path**: `openbb_platform/core/openbb_core/provider/standard_models/index_constituents.py`
- **Size**: 882 characters, 31 lines
- **Words**: 72
- **Extension**: .py
- **Classification**: Text file

## Original Source

```python
"""Index Constituents Standard Model."""

from openbb_core.provider.abstract.data import Data
from openbb_core.provider.abstract.query_params import QueryParams
from openbb_core.provider.utils.descriptions import (
    DATA_DESCRIPTIONS,
    QUERY_DESCRIPTIONS,
)
from pydantic import Field, field_validator


class IndexConstituentsQueryParams(QueryParams):
    """Index Constituents Query."""

    symbol: str = Field(description=QUERY_DESCRIPTIONS.get("symbol", ""))

    @classmethod
    @field_validator("symbol")
    def _to_upper(cls, v):
        """Convert the symbol to uppercase."""
        return v.upper()


class IndexConstituentsData(Data):
    """Index Constituents Data."""

    symbol: str = Field(description=DATA_DESCRIPTIONS.get("symbol", ""))
    name: str | None = Field(
        default=None, description="Name of the constituent company in the index."
    )

```

## High-Level Overview

Index Constituents Standard Model.

from openbb_core.provider.abstract.data import Data
from openbb_core.provider.abstract.query_params import QueryParams
from openbb_core.provider.utils.descriptions import (
DATA_DESCRIPTIONS,
QUERY_DESCRIPTIONS,
)
from pydantic import Field, field_validator


class IndexConstituentsQueryParams(QueryParams):
Index Constituents Query.
Convert the symbol to uppercase.
return v.upper()


class IndexConstituentsData(Data):
Index Constituents Data.

## Detailed Structure

### Python File Structure

**Classes** (2):
`IndexConstituentsQueryParams`, `IndexConstituentsData`

**Functions** (1):
`_to_upper`

**Imports** (7):
`openbb_core.provider.abstract.data`, `Data`, `openbb_core.provider.abstract.query_params`, `QueryParams`, `openbb_core.provider.utils.descriptions`, `pydantic`, `Field`


## Key Components

**Class `IndexConstituentsQueryParams`**: Index Constituents Query.

**Class `IndexConstituentsData`**: Index Constituents Data.

## Usage & Examples

See source code for usage details.

## Related Files

- `openbb_core.provider.abstract.data`
- `openbb_core.provider.abstract.query_params`
- `openbb_core.provider.utils.descriptions`
- `pydantic`

## Notes
- Generated: 2025-11-18T07:54:35.671704
- Generator: World's Best Repo Book Generator v1.0.0

# Documentation: openbb_platform/core/openbb_core/provider/standard_models/index_search.py

## File Metadata
- **Path**: `openbb_platform/core/openbb_core/provider/standard_models/index_search.py`
- **Size**: 690 characters, 23 lines
- **Words**: 60
- **Extension**: .py
- **Classification**: Text file

## Original Source

```python
"""Index Search Standard Model."""

from openbb_core.provider.abstract.data import Data
from openbb_core.provider.abstract.query_params import QueryParams
from openbb_core.provider.utils.descriptions import DATA_DESCRIPTIONS
from pydantic import Field


class IndexSearchQueryParams(QueryParams):
    """Index Search Query."""

    query: str = Field(description="Search query.", default="")
    is_symbol: bool = Field(
        description="Whether to search by ticker symbol.", default=False
    )


class IndexSearchData(Data):
    """Index Search Data."""

    symbol: str = Field(description=DATA_DESCRIPTIONS.get("symbol", ""))
    name: str = Field(description="Name of the index.")

```

## High-Level Overview

Index Search Standard Model.

from openbb_core.provider.abstract.data import Data
from openbb_core.provider.abstract.query_params import QueryParams
from openbb_core.provider.utils.descriptions import DATA_DESCRIPTIONS
from pydantic import Field


class IndexSearchQueryParams(QueryParams):
Index Search Query.
Index Search Data.

symbol: str = Field(description=DATA_DESCRIPTIONS.get("symbol", ""))
name: str = Field(description="Name of the index.")


## Detailed Structure

### Python File Structure

**Classes** (2):
`IndexSearchQueryParams`, `IndexSearchData`

**Functions** (0):
None

**Imports** (8):
`openbb_core.provider.abstract.data`, `Data`, `openbb_core.provider.abstract.query_params`, `QueryParams`, `openbb_core.provider.utils.descriptions`, `DATA_DESCRIPTIONS`, `pydantic`, `Field`


## Key Components

**Class `IndexSearchQueryParams`**: Index Search Query.

**Class `IndexSearchData`**: Index Search Data.

## Usage & Examples

See source code for usage details.

## Related Files

- `openbb_core.provider.abstract.data`
- `openbb_core.provider.abstract.query_params`
- `openbb_core.provider.utils.descriptions`
- `pydantic`

## Notes
- Generated: 2025-11-18T07:54:35.675644
- Generator: World's Best Repo Book Generator v1.0.0

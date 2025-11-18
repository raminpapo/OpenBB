# Documentation: openbb_platform/core/openbb_core/provider/standard_models/etf_search.py

## File Metadata
- **Path**: `openbb_platform/core/openbb_core/provider/standard_models/etf_search.py`
- **Size**: 608 characters, 20 lines
- **Words**: 55
- **Extension**: .py
- **Classification**: Text file

## Original Source

```python
"""ETF Search Standard Model."""

from openbb_core.provider.abstract.data import Data
from openbb_core.provider.abstract.query_params import QueryParams
from openbb_core.provider.utils.descriptions import DATA_DESCRIPTIONS
from pydantic import Field


class EtfSearchQueryParams(QueryParams):
    """ETF Search Query."""

    query: str | None = Field(description="Search query.", default="")


class EtfSearchData(Data):
    """ETF Search Data."""

    symbol: str = Field(description=DATA_DESCRIPTIONS.get("symbol", "") + "(ETF)")
    name: str | None = Field(description="Name of the ETF.", default=None)

```

## High-Level Overview

ETF Search Standard Model.

from openbb_core.provider.abstract.data import Data
from openbb_core.provider.abstract.query_params import QueryParams
from openbb_core.provider.utils.descriptions import DATA_DESCRIPTIONS
from pydantic import Field


class EtfSearchQueryParams(QueryParams):
ETF Search Query.
ETF Search Data.

symbol: str = Field(description=DATA_DESCRIPTIONS.get("symbol", "") + "(ETF)")
name: str | None = Field(description="Name of the ETF.", default=None)


## Detailed Structure

### Python File Structure

**Classes** (2):
`EtfSearchQueryParams`, `EtfSearchData`

**Functions** (0):
None

**Imports** (8):
`openbb_core.provider.abstract.data`, `Data`, `openbb_core.provider.abstract.query_params`, `QueryParams`, `openbb_core.provider.utils.descriptions`, `DATA_DESCRIPTIONS`, `pydantic`, `Field`


## Key Components

**Class `EtfSearchQueryParams`**: ETF Search Query.

**Class `EtfSearchData`**: ETF Search Data.

## Usage & Examples

See source code for usage details.

## Related Files

- `openbb_core.provider.abstract.data`
- `openbb_core.provider.abstract.query_params`
- `openbb_core.provider.utils.descriptions`
- `pydantic`

## Notes
- Generated: 2025-11-18T07:54:35.622068
- Generator: World's Best Repo Book Generator v1.0.0

# Documentation: openbb_platform/core/openbb_core/provider/standard_models/futures_info.py

## File Metadata
- **Path**: `openbb_platform/core/openbb_core/provider/standard_models/futures_info.py`
- **Size**: 547 characters, 19 lines
- **Words**: 47
- **Extension**: .py
- **Classification**: Text file

## Original Source

```python
"""Futures Info Standard Model."""

from openbb_core.provider.abstract.data import Data
from openbb_core.provider.abstract.query_params import QueryParams
from openbb_core.provider.utils.descriptions import DATA_DESCRIPTIONS
from pydantic import Field


class FuturesInfoQueryParams(QueryParams):
    """Futures Info Query."""

    # leaving this empty to let the provider create custom symbol docstrings.


class FuturesInfoData(Data):
    """Futures Instruments Data."""

    symbol: str = Field(description=DATA_DESCRIPTIONS.get("symbol", ""))

```

## High-Level Overview

Futures Info Standard Model.

from openbb_core.provider.abstract.data import Data
from openbb_core.provider.abstract.query_params import QueryParams
from openbb_core.provider.utils.descriptions import DATA_DESCRIPTIONS
from pydantic import Field


class FuturesInfoQueryParams(QueryParams):
Futures Info Query.
leaving this empty to let the provider create custom symbol docstrings.
Futures Instruments Data.

symbol: str = Field(description=DATA_DESCRIPTIONS.get("symbol", ""))


## Detailed Structure

### Python File Structure

**Classes** (2):
`FuturesInfoQueryParams`, `FuturesInfoData`

**Functions** (0):
None

**Imports** (8):
`openbb_core.provider.abstract.data`, `Data`, `openbb_core.provider.abstract.query_params`, `QueryParams`, `openbb_core.provider.utils.descriptions`, `DATA_DESCRIPTIONS`, `pydantic`, `Field`


## Key Components

**Class `FuturesInfoQueryParams`**: Futures Info Query.

**Class `FuturesInfoData`**: Futures Instruments Data.

## Usage & Examples

See source code for usage details.

## Related Files

- `openbb_core.provider.abstract.data`
- `openbb_core.provider.abstract.query_params`
- `openbb_core.provider.utils.descriptions`
- `pydantic`

## Notes
- Generated: 2025-11-18T07:54:35.650186
- Generator: World's Best Repo Book Generator v1.0.0

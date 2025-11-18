# Documentation: openbb_platform/core/openbb_core/provider/standard_models/cot_search.py

## File Metadata
- **Path**: `openbb_platform/core/openbb_core/provider/standard_models/cot_search.py`
- **Size**: 1,087 characters, 30 lines
- **Words**: 110
- **Extension**: .py
- **Classification**: Text file

## Original Source

```python
"""Commitment of Traders Reports Search Standard Model."""

from openbb_core.provider.abstract.data import Data
from openbb_core.provider.abstract.query_params import QueryParams
from openbb_core.provider.utils.descriptions import DATA_DESCRIPTIONS
from pydantic import Field


class CotSearchQueryParams(QueryParams):
    """Commitment of Traders Reports Search Query."""

    query: str = Field(description="Search query.", default="")


class CotSearchData(Data):
    """Commitment of Traders Reports Search Data."""

    code: str = Field(description="CFTC market contract code of the report.")
    name: str = Field(description="Name of the underlying asset.")
    category: str | None = Field(
        default=None, description="Category of the underlying asset."
    )
    subcategory: str | None = Field(
        default=None, description="Subcategory of the underlying asset."
    )
    units: str | None = Field(default=None, description="The units for one contract.")
    symbol: str | None = Field(
        default=None, description=DATA_DESCRIPTIONS.get("symbol", "")
    )

```

## High-Level Overview

Commitment of Traders Reports Search Standard Model.

from openbb_core.provider.abstract.data import Data
from openbb_core.provider.abstract.query_params import QueryParams
from openbb_core.provider.utils.descriptions import DATA_DESCRIPTIONS
from pydantic import Field


class CotSearchQueryParams(QueryParams):
Commitment of Traders Reports Search Query.
Commitment of Traders Reports Search Data.

code: str = Field(description="CFTC market contract code of the report.")
name: str = Field(description="Name of the underlying asset.")
category: str | None = Field(
default=None, description="Category of the underlying asset."
)
subcategory: str | None = Field(
default=None, description="Subcategory of the underlying asset."
)

## Detailed Structure

### Python File Structure

**Classes** (2):
`CotSearchQueryParams`, `CotSearchData`

**Functions** (0):
None

**Imports** (8):
`openbb_core.provider.abstract.data`, `Data`, `openbb_core.provider.abstract.query_params`, `QueryParams`, `openbb_core.provider.utils.descriptions`, `DATA_DESCRIPTIONS`, `pydantic`, `Field`


## Key Components

**Class `CotSearchQueryParams`**: Commitment of Traders Reports Search Query.

**Class `CotSearchData`**: Commitment of Traders Reports Search Data.

## Usage & Examples

See source code for usage details.

## Related Files

- `openbb_core.provider.abstract.data`
- `openbb_core.provider.abstract.query_params`
- `openbb_core.provider.utils.descriptions`
- `pydantic`

## Notes
- Generated: 2025-11-18T07:54:35.568438
- Generator: World's Best Repo Book Generator v1.0.0

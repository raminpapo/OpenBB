# Documentation: openbb_platform/core/openbb_core/provider/standard_models/index_info.py

## File Metadata
- **Path**: `openbb_platform/core/openbb_core/provider/standard_models/index_info.py`
- **Size**: 1,250 characters, 41 lines
- **Words**: 121
- **Extension**: .py
- **Classification**: Text file

## Original Source

```python
"""Index Info Standard Model."""

from openbb_core.provider.abstract.data import Data
from openbb_core.provider.abstract.query_params import QueryParams
from openbb_core.provider.utils.descriptions import (
    DATA_DESCRIPTIONS,
    QUERY_DESCRIPTIONS,
)
from pydantic import Field, field_validator


class IndexInfoQueryParams(QueryParams):
    """Index Info Query."""

    symbol: str = Field(description=QUERY_DESCRIPTIONS.get("symbol", ""))

    @field_validator("symbol")
    @classmethod
    def to_upper(cls, v: str) -> str:
        """Convert field to uppercase."""
        return v.upper()


class IndexInfoData(Data):
    """Index Info Data."""

    symbol: str = Field(description=DATA_DESCRIPTIONS.get("symbol", ""))
    name: str = Field(description="The name of the index.")
    description: str | None = Field(
        description="The short description of the index.", default=None
    )
    methodology: str | None = Field(
        description="URL to the methodology document.", default=None
    )
    factsheet: str | None = Field(
        description="URL to the factsheet document.", default=None
    )
    num_constituents: int | None = Field(
        description="The number of constituents in the index.", default=None
    )

```

## High-Level Overview

Index Info Standard Model.

from openbb_core.provider.abstract.data import Data
from openbb_core.provider.abstract.query_params import QueryParams
from openbb_core.provider.utils.descriptions import (
DATA_DESCRIPTIONS,
QUERY_DESCRIPTIONS,
)
from pydantic import Field, field_validator


class IndexInfoQueryParams(QueryParams):
Index Info Query.
Convert field to uppercase.
return v.upper()


class IndexInfoData(Data):
Index Info Data.

## Detailed Structure

### Python File Structure

**Classes** (2):
`IndexInfoQueryParams`, `IndexInfoData`

**Functions** (1):
`to_upper`

**Imports** (7):
`openbb_core.provider.abstract.data`, `Data`, `openbb_core.provider.abstract.query_params`, `QueryParams`, `openbb_core.provider.utils.descriptions`, `pydantic`, `Field`


## Key Components

**Class `IndexInfoQueryParams`**: Index Info Query.

**Class `IndexInfoData`**: Index Info Data.

## Usage & Examples

See source code for usage details.

## Related Files

- `openbb_core.provider.abstract.data`
- `openbb_core.provider.abstract.query_params`
- `openbb_core.provider.utils.descriptions`
- `pydantic`

## Notes
- Generated: 2025-11-18T07:54:35.674233
- Generator: World's Best Repo Book Generator v1.0.0

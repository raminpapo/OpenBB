# Documentation: openbb_platform/core/openbb_core/provider/standard_models/index_sectors.py

## File Metadata
- **Path**: `openbb_platform/core/openbb_core/provider/standard_models/index_sectors.py`
- **Size**: 776 characters, 26 lines
- **Words**: 67
- **Extension**: .py
- **Classification**: Text file

## Original Source

```python
"""Index Sectors Standard Model."""

from openbb_core.provider.abstract.data import Data
from openbb_core.provider.abstract.query_params import QueryParams
from openbb_core.provider.utils.descriptions import QUERY_DESCRIPTIONS
from pydantic import Field, field_validator


class IndexSectorsQueryParams(QueryParams):
    """Index Sectors Query."""

    symbol: str = Field(description=QUERY_DESCRIPTIONS.get("symbol", ""))

    @field_validator("symbol")
    @classmethod
    def to_upper(cls, v: str) -> str:
        """Convert field to uppercase."""
        return v.upper()


class IndexSectorsData(Data):
    """Index Sectors Data."""

    sector: str = Field(description="The sector name.")
    weight: float = Field(description="The weight of the sector in the index.")

```

## High-Level Overview

Index Sectors Standard Model.

from openbb_core.provider.abstract.data import Data
from openbb_core.provider.abstract.query_params import QueryParams
from openbb_core.provider.utils.descriptions import QUERY_DESCRIPTIONS
from pydantic import Field, field_validator


class IndexSectorsQueryParams(QueryParams):
Index Sectors Query.
Convert field to uppercase.
return v.upper()


class IndexSectorsData(Data):
Index Sectors Data.

## Detailed Structure

### Python File Structure

**Classes** (2):
`IndexSectorsQueryParams`, `IndexSectorsData`

**Functions** (1):
`to_upper`

**Imports** (8):
`openbb_core.provider.abstract.data`, `Data`, `openbb_core.provider.abstract.query_params`, `QueryParams`, `openbb_core.provider.utils.descriptions`, `QUERY_DESCRIPTIONS`, `pydantic`, `Field`


## Key Components

**Class `IndexSectorsQueryParams`**: Index Sectors Query.

**Class `IndexSectorsData`**: Index Sectors Data.

## Usage & Examples

See source code for usage details.

## Related Files

- `openbb_core.provider.abstract.data`
- `openbb_core.provider.abstract.query_params`
- `openbb_core.provider.utils.descriptions`
- `pydantic`

## Notes
- Generated: 2025-11-18T07:54:35.676883
- Generator: World's Best Repo Book Generator v1.0.0

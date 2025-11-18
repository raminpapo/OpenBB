# Documentation: openbb_platform/core/openbb_core/provider/standard_models/cik_map.py

## File Metadata
- **Path**: `openbb_platform/core/openbb_core/provider/standard_models/cik_map.py`
- **Size**: 783 characters, 30 lines
- **Words**: 65
- **Extension**: .py
- **Classification**: Text file

## Original Source

```python
"""Cik Map Standard Model."""

from openbb_core.provider.abstract.data import Data
from openbb_core.provider.abstract.query_params import QueryParams
from openbb_core.provider.utils.descriptions import (
    DATA_DESCRIPTIONS,
    QUERY_DESCRIPTIONS,
)
from pydantic import Field, field_validator


class CikMapQueryParams(QueryParams):
    """CikMap Query."""

    symbol: str = Field(description=QUERY_DESCRIPTIONS.get("symbol", ""))

    @field_validator("symbol", mode="before", check_fields=False)
    @classmethod
    def to_upper(cls, v: str) -> str:
        """Convert field to uppercase."""
        return v.upper()


class CikMapData(Data):
    """CikMap Data."""

    cik: str | int | None = Field(
        default=None, description=DATA_DESCRIPTIONS.get("cik", "")
    )

```

## High-Level Overview

Cik Map Standard Model.

from openbb_core.provider.abstract.data import Data
from openbb_core.provider.abstract.query_params import QueryParams
from openbb_core.provider.utils.descriptions import (
DATA_DESCRIPTIONS,
QUERY_DESCRIPTIONS,
)
from pydantic import Field, field_validator


class CikMapQueryParams(QueryParams):
CikMap Query.
Convert field to uppercase.
return v.upper()


class CikMapData(Data):
CikMap Data.

## Detailed Structure

### Python File Structure

**Classes** (2):
`CikMapQueryParams`, `CikMapData`

**Functions** (1):
`to_upper`

**Imports** (7):
`openbb_core.provider.abstract.data`, `Data`, `openbb_core.provider.abstract.query_params`, `QueryParams`, `openbb_core.provider.utils.descriptions`, `pydantic`, `Field`


## Key Components

**Class `CikMapQueryParams`**: CikMap Query.

**Class `CikMapData`**: CikMap Data.

## Usage & Examples

See source code for usage details.

## Related Files

- `openbb_core.provider.abstract.data`
- `openbb_core.provider.abstract.query_params`
- `openbb_core.provider.utils.descriptions`
- `pydantic`

## Notes
- Generated: 2025-11-18T07:54:35.555180
- Generator: World's Best Repo Book Generator v1.0.0

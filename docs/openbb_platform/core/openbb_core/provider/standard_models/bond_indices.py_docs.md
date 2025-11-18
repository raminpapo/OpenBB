# Documentation: openbb_platform/core/openbb_core/provider/standard_models/bond_indices.py

## File Metadata
- **Path**: `openbb_platform/core/openbb_core/provider/standard_models/bond_indices.py`
- **Size**: 1,559 characters, 52 lines
- **Words**: 138
- **Extension**: .py
- **Classification**: Text file

## Original Source

```python
"""Bond Indices Standard Model."""

from datetime import (
    date as dateType,
)
from typing import Literal

from openbb_core.provider.abstract.data import Data
from openbb_core.provider.abstract.query_params import QueryParams
from openbb_core.provider.utils.descriptions import (
    DATA_DESCRIPTIONS,
    QUERY_DESCRIPTIONS,
)
from pydantic import Field, field_validator


class BondIndicesQueryParams(QueryParams):
    """Bond Indices Query."""

    start_date: dateType | None = Field(
        default=None,
        description=QUERY_DESCRIPTIONS.get("start_date", ""),
    )
    end_date: dateType | None = Field(
        default=None,
        description=QUERY_DESCRIPTIONS.get("end_date", ""),
    )
    index_type: Literal["yield", "yield_to_worst", "total_return", "oas"] = Field(
        default="yield",
        description="The type of series. OAS is the option-adjusted spread. Default is yield.",
        json_schema_extra={
            "choices": ["yield", "yield_to_worst", "total_return", "oas"]
        },
    )

    @field_validator("index_type", mode="before", check_fields=False)
    @classmethod
    def to_lower(cls, v: str | None) -> str | None:
        """Convert field to lowercase."""
        return v.lower() if v else v


class BondIndicesData(Data):
    """Bond Indices Data."""

    date: dateType = Field(description=DATA_DESCRIPTIONS.get("date", ""))
    symbol: str | None = Field(
        default=None,
        description=DATA_DESCRIPTIONS.get("symbol", ""),
    )
    value: float = Field(description="Index values.")

```

## High-Level Overview

Bond Indices Standard Model.

from datetime import (
date as dateType,
)
from typing import Literal

from openbb_core.provider.abstract.data import Data
from openbb_core.provider.abstract.query_params import QueryParams
from openbb_core.provider.utils.descriptions import (
DATA_DESCRIPTIONS,
QUERY_DESCRIPTIONS,
)
from pydantic import Field, field_validator


class BondIndicesQueryParams(QueryParams):
Bond Indices Query.
Convert field to lowercase.
return v.lower() if v else v

## Detailed Structure

### Python File Structure

**Classes** (2):
`BondIndicesQueryParams`, `BondIndicesData`

**Functions** (1):
`to_lower`

**Imports** (10):
`datetime`, `typing`, `Literal`, `openbb_core.provider.abstract.data`, `Data`, `openbb_core.provider.abstract.query_params`, `QueryParams`, `openbb_core.provider.utils.descriptions`, `pydantic`, `Field`


## Key Components

**Class `BondIndicesQueryParams`**: Bond Indices Query.

**Class `BondIndicesData`**: Bond Indices Data.

## Usage & Examples

See source code for usage details.

## Related Files

- `datetime`
- `typing`
- `openbb_core.provider.abstract.data`
- `openbb_core.provider.abstract.query_params`
- `openbb_core.provider.utils.descriptions`
- `pydantic`

## Notes
- Generated: 2025-11-18T07:54:35.538530
- Generator: World's Best Repo Book Generator v1.0.0

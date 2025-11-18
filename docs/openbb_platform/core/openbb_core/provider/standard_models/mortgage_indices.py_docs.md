# Documentation: openbb_platform/core/openbb_core/provider/standard_models/mortgage_indices.py

## File Metadata
- **Path**: `openbb_platform/core/openbb_core/provider/standard_models/mortgage_indices.py`
- **Size**: 1,197 characters, 45 lines
- **Words**: 99
- **Extension**: .py
- **Classification**: Text file

## Original Source

```python
"""Mortgage Indices Standard Model."""

from datetime import (
    date as dateType,
)

from openbb_core.provider.abstract.data import Data
from openbb_core.provider.abstract.query_params import QueryParams
from openbb_core.provider.utils.descriptions import (
    DATA_DESCRIPTIONS,
    QUERY_DESCRIPTIONS,
)
from pydantic import Field


class MortgageIndicesQueryParams(QueryParams):
    """Mortgage Indices Query."""

    start_date: dateType | None = Field(
        default=None,
        description=QUERY_DESCRIPTIONS.get("start_date", ""),
    )
    end_date: dateType | None = Field(
        default=None,
        description=QUERY_DESCRIPTIONS.get("end_date", ""),
    )


class MortgageIndicesData(Data):
    """Mortgage Indices Data."""

    date: dateType = Field(description=DATA_DESCRIPTIONS.get("date", ""))
    symbol: str | None = Field(
        default=None,
        description=DATA_DESCRIPTIONS.get("symbol", ""),
    )
    name: str | None = Field(
        default=None,
        description="Name of the index.",
    )
    rate: float = Field(
        description="Mortgage rate.",
        json_schema_extra={"x-unit_measurement": "percent", "x-frontend_multiply": 100},
    )

```

## High-Level Overview

Mortgage Indices Standard Model.

from datetime import (
date as dateType,
)

from openbb_core.provider.abstract.data import Data
from openbb_core.provider.abstract.query_params import QueryParams
from openbb_core.provider.utils.descriptions import (
DATA_DESCRIPTIONS,
QUERY_DESCRIPTIONS,
)
from pydantic import Field


class MortgageIndicesQueryParams(QueryParams):
Mortgage Indices Query.
Mortgage Indices Data.

date: dateType = Field(description=DATA_DESCRIPTIONS.get("date", ""))

## Detailed Structure

### Python File Structure

**Classes** (2):
`MortgageIndicesQueryParams`, `MortgageIndicesData`

**Functions** (0):
None

**Imports** (8):
`datetime`, `openbb_core.provider.abstract.data`, `Data`, `openbb_core.provider.abstract.query_params`, `QueryParams`, `openbb_core.provider.utils.descriptions`, `pydantic`, `Field`


## Key Components

**Class `MortgageIndicesQueryParams`**: Mortgage Indices Query.

**Class `MortgageIndicesData`**: Mortgage Indices Data.

## Usage & Examples

See source code for usage details.

## Related Files

- `datetime`
- `openbb_core.provider.abstract.data`
- `openbb_core.provider.abstract.query_params`
- `openbb_core.provider.utils.descriptions`
- `pydantic`

## Notes
- Generated: 2025-11-18T07:54:35.700634
- Generator: World's Best Repo Book Generator v1.0.0

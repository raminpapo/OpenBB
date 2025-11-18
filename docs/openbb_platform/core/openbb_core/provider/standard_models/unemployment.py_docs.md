# Documentation: openbb_platform/core/openbb_core/provider/standard_models/unemployment.py

## File Metadata
- **Path**: `openbb_platform/core/openbb_core/provider/standard_models/unemployment.py`
- **Size**: 1,528 characters, 50 lines
- **Words**: 122
- **Extension**: .py
- **Classification**: Text file

## Original Source

```python
"""Unemployment Standard Model."""

from datetime import date as dateType
from typing import Literal

from openbb_core.provider.abstract.data import Data
from openbb_core.provider.abstract.query_params import QueryParams
from openbb_core.provider.utils.descriptions import (
    DATA_DESCRIPTIONS,
    QUERY_DESCRIPTIONS,
)
from pydantic import Field


class UnemploymentQueryParams(QueryParams):
    """Unemployment Query."""

    country: str = Field(
        description=QUERY_DESCRIPTIONS.get("country", ""),
        default="united_states",
    )
    frequency: Literal["monthly", "quarter", "annual"] = Field(
        description=QUERY_DESCRIPTIONS.get("frequency", ""),
        default="monthly",
        json_schema_extra={"choices": ["monthly", "quarter", "annual"]},
    )
    start_date: dateType | None = Field(
        default=None, description=QUERY_DESCRIPTIONS.get("start_date")
    )
    end_date: dateType | None = Field(
        default=None, description=QUERY_DESCRIPTIONS.get("end_date")
    )


class UnemploymentData(Data):
    """Unemployment Data."""

    date: dateType | None = Field(
        default=None, description=DATA_DESCRIPTIONS.get("date")
    )
    country: str | None = Field(
        default=None,
        description="Country for which unemployment rate is given",
    )
    value: float | None = Field(
        default=None,
        description="Unemployment rate, as a normalized percent.",
        json_schema_extra={"x-unit_measurement": "percent", "x-frontend_multiply": 100},
    )

```

## High-Level Overview

Unemployment Standard Model.

from datetime import date as dateType
from typing import Literal

from openbb_core.provider.abstract.data import Data
from openbb_core.provider.abstract.query_params import QueryParams
from openbb_core.provider.utils.descriptions import (
DATA_DESCRIPTIONS,
QUERY_DESCRIPTIONS,
)
from pydantic import Field


class UnemploymentQueryParams(QueryParams):
Unemployment Query.
Unemployment Data.

date: dateType | None = Field(
default=None, description=DATA_DESCRIPTIONS.get("date")

## Detailed Structure

### Python File Structure

**Classes** (2):
`UnemploymentQueryParams`, `UnemploymentData`

**Functions** (0):
None

**Imports** (11):
`datetime`, `date`, `typing`, `Literal`, `openbb_core.provider.abstract.data`, `Data`, `openbb_core.provider.abstract.query_params`, `QueryParams`, `openbb_core.provider.utils.descriptions`, `pydantic`, `Field`


## Key Components

**Class `UnemploymentQueryParams`**: Unemployment Query.

**Class `UnemploymentData`**: Unemployment Data.

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
- Generated: 2025-11-18T07:54:35.760025
- Generator: World's Best Repo Book Generator v1.0.0

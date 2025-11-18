# Documentation: openbb_platform/core/openbb_core/provider/standard_models/ameribor.py

## File Metadata
- **Path**: `openbb_platform/core/openbb_core/provider/standard_models/ameribor.py`
- **Size**: 1,214 characters, 43 lines
- **Words**: 102
- **Extension**: .py
- **Classification**: Text file

## Original Source

```python
"""AMERIBOR Standard Model."""

from datetime import date as dateType

from openbb_core.provider.abstract.data import Data
from openbb_core.provider.abstract.query_params import QueryParams
from openbb_core.provider.utils.descriptions import (
    DATA_DESCRIPTIONS,
    QUERY_DESCRIPTIONS,
)
from pydantic import Field


class AmeriborQueryParams(QueryParams):
    """AMERIBOR Query."""

    start_date: dateType | None = Field(
        default=None,
        description=QUERY_DESCRIPTIONS.get("start_date", ""),
    )
    end_date: dateType | None = Field(
        default=None,
        description=QUERY_DESCRIPTIONS.get("end_date", ""),
    )


class AmeriborData(Data):
    """AMERIBOR Data."""

    date: dateType = Field(description=DATA_DESCRIPTIONS.get("date", ""))
    symbol: str | None = Field(
        default=None, description=DATA_DESCRIPTIONS.get("symbol", "")
    )
    maturity: str = Field(description="Maturity length of the item.")
    rate: float = Field(
        description="Interest rate.",
        json_schema_extra={"x-unit_measurement": "percent", "x-frontend_multiply": 100},
    )
    title: str | None = Field(
        default=None,
        description="Title of the series.",
    )

```

## High-Level Overview

AMERIBOR Standard Model.

from datetime import date as dateType

from openbb_core.provider.abstract.data import Data
from openbb_core.provider.abstract.query_params import QueryParams
from openbb_core.provider.utils.descriptions import (
DATA_DESCRIPTIONS,
QUERY_DESCRIPTIONS,
)
from pydantic import Field


class AmeriborQueryParams(QueryParams):
AMERIBOR Query.
AMERIBOR Data.

date: dateType = Field(description=DATA_DESCRIPTIONS.get("date", ""))
symbol: str | None = Field(
default=None, description=DATA_DESCRIPTIONS.get("symbol", "")

## Detailed Structure

### Python File Structure

**Classes** (2):
`AmeriborQueryParams`, `AmeriborData`

**Functions** (0):
None

**Imports** (9):
`datetime`, `date`, `openbb_core.provider.abstract.data`, `Data`, `openbb_core.provider.abstract.query_params`, `QueryParams`, `openbb_core.provider.utils.descriptions`, `pydantic`, `Field`


## Key Components

**Class `AmeriborQueryParams`**: AMERIBOR Query.

**Class `AmeriborData`**: AMERIBOR Data.

## Usage & Examples

See source code for usage details.

## Related Files

- `datetime`
- `openbb_core.provider.abstract.data`
- `openbb_core.provider.abstract.query_params`
- `openbb_core.provider.utils.descriptions`
- `pydantic`

## Notes
- Generated: 2025-11-18T07:54:35.523353
- Generator: World's Best Repo Book Generator v1.0.0

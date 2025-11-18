# Documentation: openbb_platform/core/openbb_core/provider/standard_models/tips_yields.py

## File Metadata
- **Path**: `openbb_platform/core/openbb_core/provider/standard_models/tips_yields.py`
- **Size**: 1,370 characters, 48 lines
- **Words**: 119
- **Extension**: .py
- **Classification**: Text file

## Original Source

```python
"""TIPS (Treasury Inflation-Protected Securities) Yields Standard Model."""

from datetime import date as dateType

from openbb_core.provider.abstract.data import Data
from openbb_core.provider.abstract.query_params import QueryParams
from openbb_core.provider.utils.descriptions import (
    DATA_DESCRIPTIONS,
    QUERY_DESCRIPTIONS,
)
from pydantic import Field


class TipsYieldsQueryParams(QueryParams):
    """TIPS Yields Query."""

    start_date: dateType | None = Field(
        default=None,
        description=QUERY_DESCRIPTIONS.get("start_date", ""),
    )
    end_date: dateType | None = Field(
        default=None,
        description=QUERY_DESCRIPTIONS.get("end_date", ""),
    )


class TipsYieldsData(Data):
    """TIPS Yields Data."""

    date: dateType = Field(description=DATA_DESCRIPTIONS.get("date", ""))
    symbol: str | None = Field(
        default=None,
        description=DATA_DESCRIPTIONS.get("symbol", ""),
    )
    due: dateType | None = Field(
        default=None,
        description="The due date (maturation date) of the security.",
    )
    name: str | None = Field(
        default=None,
        description="The name of the security.",
    )
    value: float = Field(
        default=None,
        description="The yield value.",
        json_schema_extra={"x-unit_measurement": "percent", "x-frontend_multiply": 100},
    )

```

## High-Level Overview

TIPS (Treasury Inflation-Protected Securities) Yields Standard Model.

from datetime import date as dateType

from openbb_core.provider.abstract.data import Data
from openbb_core.provider.abstract.query_params import QueryParams
from openbb_core.provider.utils.descriptions import (
DATA_DESCRIPTIONS,
QUERY_DESCRIPTIONS,
)
from pydantic import Field


class TipsYieldsQueryParams(QueryParams):
TIPS Yields Query.
TIPS Yields Data.

date: dateType = Field(description=DATA_DESCRIPTIONS.get("date", ""))
symbol: str | None = Field(
default=None,

## Detailed Structure

### Python File Structure

**Classes** (2):
`TipsYieldsQueryParams`, `TipsYieldsData`

**Functions** (0):
None

**Imports** (9):
`datetime`, `date`, `openbb_core.provider.abstract.data`, `Data`, `openbb_core.provider.abstract.query_params`, `QueryParams`, `openbb_core.provider.utils.descriptions`, `pydantic`, `Field`


## Key Components

**Class `TipsYieldsQueryParams`**: TIPS Yields Query.

**Class `TipsYieldsData`**: TIPS Yields Data.

## Usage & Examples

See source code for usage details.

## Related Files

- `datetime`
- `openbb_core.provider.abstract.data`
- `openbb_core.provider.abstract.query_params`
- `openbb_core.provider.utils.descriptions`
- `pydantic`

## Notes
- Generated: 2025-11-18T07:54:35.749092
- Generator: World's Best Repo Book Generator v1.0.0

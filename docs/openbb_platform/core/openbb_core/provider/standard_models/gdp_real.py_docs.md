# Documentation: openbb_platform/core/openbb_core/provider/standard_models/gdp_real.py

## File Metadata
- **Path**: `openbb_platform/core/openbb_core/provider/standard_models/gdp_real.py`
- **Size**: 960 characters, 35 lines
- **Words**: 90
- **Extension**: .py
- **Classification**: Text file

## Original Source

```python
"""Real GDP Standard Model."""

from datetime import date as dateType

from openbb_core.provider.abstract.data import Data
from openbb_core.provider.abstract.query_params import QueryParams
from openbb_core.provider.utils.descriptions import (
    DATA_DESCRIPTIONS,
    QUERY_DESCRIPTIONS,
)
from pydantic import Field


class GdpRealQueryParams(QueryParams):
    """Real GDP Query."""

    start_date: dateType | None = Field(
        default=None, description=QUERY_DESCRIPTIONS.get("start_date")
    )
    end_date: dateType | None = Field(
        default=None, description=QUERY_DESCRIPTIONS.get("end_date")
    )


class GdpRealData(Data):
    """Real GDP Data."""

    date: dateType = Field(description=DATA_DESCRIPTIONS.get("date"))
    country: str = Field(
        default=None, description="The country represented by the Real GDP value."
    )
    value: int | float = Field(
        description="Real GDP value for the country and date.",
    )

```

## High-Level Overview

Real GDP Standard Model.

from datetime import date as dateType

from openbb_core.provider.abstract.data import Data
from openbb_core.provider.abstract.query_params import QueryParams
from openbb_core.provider.utils.descriptions import (
DATA_DESCRIPTIONS,
QUERY_DESCRIPTIONS,
)
from pydantic import Field


class GdpRealQueryParams(QueryParams):
Real GDP Query.
Real GDP Data.

date: dateType = Field(description=DATA_DESCRIPTIONS.get("date"))
country: str = Field(
default=None, description="The country represented by the Real GDP value."

## Detailed Structure

### Python File Structure

**Classes** (2):
`GdpRealQueryParams`, `GdpRealData`

**Functions** (0):
None

**Imports** (9):
`datetime`, `date`, `openbb_core.provider.abstract.data`, `Data`, `openbb_core.provider.abstract.query_params`, `QueryParams`, `openbb_core.provider.utils.descriptions`, `pydantic`, `Field`


## Key Components

**Class `GdpRealQueryParams`**: Real GDP Query.

**Class `GdpRealData`**: Real GDP Data.

## Usage & Examples

See source code for usage details.

## Related Files

- `datetime`
- `openbb_core.provider.abstract.data`
- `openbb_core.provider.abstract.query_params`
- `openbb_core.provider.utils.descriptions`
- `pydantic`

## Notes
- Generated: 2025-11-18T07:54:35.655331
- Generator: World's Best Repo Book Generator v1.0.0

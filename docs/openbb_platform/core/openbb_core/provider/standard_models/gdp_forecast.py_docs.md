# Documentation: openbb_platform/core/openbb_core/provider/standard_models/gdp_forecast.py

## File Metadata
- **Path**: `openbb_platform/core/openbb_core/provider/standard_models/gdp_forecast.py`
- **Size**: 941 characters, 33 lines
- **Words**: 80
- **Extension**: .py
- **Classification**: Text file

## Original Source

```python
"""Forecast GDP Standard Model."""

from datetime import date as dateType

from openbb_core.provider.abstract.data import Data
from openbb_core.provider.abstract.query_params import QueryParams
from openbb_core.provider.utils.descriptions import (
    DATA_DESCRIPTIONS,
    QUERY_DESCRIPTIONS,
)
from pydantic import Field


class GdpForecastQueryParams(QueryParams):
    """Forecast GDP Query."""

    start_date: dateType | None = Field(
        default=None, description=QUERY_DESCRIPTIONS.get("start_date")
    )
    end_date: dateType | None = Field(
        default=None, description=QUERY_DESCRIPTIONS.get("end_date")
    )


class GdpForecastData(Data):
    """Forecast GDP Data."""

    date: dateType = Field(description=DATA_DESCRIPTIONS.get("date"))
    country: str = Field(description=DATA_DESCRIPTIONS.get("country"))
    value: int | float = Field(
        description="Forecasted GDP value for the country and date."
    )

```

## High-Level Overview

Forecast GDP Standard Model.

from datetime import date as dateType

from openbb_core.provider.abstract.data import Data
from openbb_core.provider.abstract.query_params import QueryParams
from openbb_core.provider.utils.descriptions import (
DATA_DESCRIPTIONS,
QUERY_DESCRIPTIONS,
)
from pydantic import Field


class GdpForecastQueryParams(QueryParams):
Forecast GDP Query.
Forecast GDP Data.

date: dateType = Field(description=DATA_DESCRIPTIONS.get("date"))
country: str = Field(description=DATA_DESCRIPTIONS.get("country"))
value: int | float = Field(

## Detailed Structure

### Python File Structure

**Classes** (2):
`GdpForecastQueryParams`, `GdpForecastData`

**Functions** (0):
None

**Imports** (9):
`datetime`, `date`, `openbb_core.provider.abstract.data`, `Data`, `openbb_core.provider.abstract.query_params`, `QueryParams`, `openbb_core.provider.utils.descriptions`, `pydantic`, `Field`


## Key Components

**Class `GdpForecastQueryParams`**: Forecast GDP Query.

**Class `GdpForecastData`**: Forecast GDP Data.

## Usage & Examples

See source code for usage details.

## Related Files

- `datetime`
- `openbb_core.provider.abstract.data`
- `openbb_core.provider.abstract.query_params`
- `openbb_core.provider.utils.descriptions`
- `pydantic`

## Notes
- Generated: 2025-11-18T07:54:35.652800
- Generator: World's Best Repo Book Generator v1.0.0

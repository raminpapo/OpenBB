# File Documentation: gdp_forecast.py

## Metadata
- **Path**: `openbb_platform/core/openbb_core/provider/standard_models/gdp_forecast.py`
- **Size**: 941 bytes
- **Lines**: 33
- **Category**: python
- **Extension**: .py

---

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



---

## High-Level Overview

This is a **python** file named `gdp_forecast.py`.

**Python Module**

- **Classes** (2): GdpForecastQueryParams, GdpForecastData
- **Import Statements**: 2


---

## Detailed Analysis

### Python Code Structure

#### Classes

- **`GdpForecastQueryParams`**(QueryParams)
- **`GdpForecastData`**(Data)


---

## Related Files

The following files may be related based on imports and references:

**Imported Modules**:
- `Data`
- `Field`
- `QueryParams`
- `date`
- `datetime`
- `openbb_core.provider.abstract.data`
- `openbb_core.provider.abstract.query_params`
- `openbb_core.provider.utils.descriptions`
- `pydantic`


---

## Performance & Security Notes

No obvious security concerns detected in static analysis.


---

**Generated**: 2025-11-19T02:16:46.481886Z
**Generator**: World's Best Repo Book Generator v1.0

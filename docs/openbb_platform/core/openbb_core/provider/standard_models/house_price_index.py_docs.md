# File Documentation: house_price_index.py

## Metadata
- **Path**: `openbb_platform/core/openbb_core/provider/standard_models/house_price_index.py`
- **Size**: 1,744 bytes
- **Lines**: 55
- **Category**: python
- **Extension**: .py

---

## Original Source

```python
"""House Price Index Standard Model."""

from datetime import date as dateType
from typing import Literal

from openbb_core.provider.abstract.data import Data
from openbb_core.provider.abstract.query_params import QueryParams
from openbb_core.provider.utils.descriptions import (
    DATA_DESCRIPTIONS,
    QUERY_DESCRIPTIONS,
)
from pydantic import Field


class HousePriceIndexQueryParams(QueryParams):
    """House Price Index Query."""

    country: str = Field(
        description=QUERY_DESCRIPTIONS.get("country", ""),
        default="united_states",
    )
    frequency: Literal["monthly", "quarter", "annual"] = Field(
        description=QUERY_DESCRIPTIONS.get("frequency", ""),
        default="quarter",
        json_schema_extra={"choices": ["monthly", "quarter", "annual"]},
    )
    transform: Literal["index", "yoy", "period"] = Field(
        description="Transformation of the CPI data. Period represents the change since previous."
        + " Defaults to change from one year ago (yoy).",
        default="index",
        json_schema_extra={"choices": ["index", "yoy", "period"]},
    )
    start_date: dateType | None = Field(
        default=None, description=QUERY_DESCRIPTIONS.get("start_date")
    )
    end_date: dateType | None = Field(
        default=None, description=QUERY_DESCRIPTIONS.get("end_date")
    )


class HousePriceIndexData(Data):
    """House Price Index Data."""

    date: dateType | None = Field(
        default=None, description=DATA_DESCRIPTIONS.get("date")
    )
    country: str | None = Field(
        default=None,
        description=DATA_DESCRIPTIONS.get("country", ""),
    )
    value: float | None = Field(
        default=None,
        description="Share price index value.",
    )

```



---

## High-Level Overview

This is a **python** file named `house_price_index.py`.

**Python Module**

- **Classes** (2): HousePriceIndexQueryParams, HousePriceIndexData
- **Import Statements**: 2


---

## Detailed Analysis

### Python Code Structure

#### Classes

- **`HousePriceIndexQueryParams`**(QueryParams)
- **`HousePriceIndexData`**(Data)


---

## Related Files

The following files may be related based on imports and references:

**Imported Modules**:
- `Data`
- `Field`
- `Literal`
- `QueryParams`
- `date`
- `datetime`
- `openbb_core.provider.abstract.data`
- `openbb_core.provider.abstract.query_params`
- `openbb_core.provider.utils.descriptions`
- `pydantic`
- `typing`


---

## Performance & Security Notes

No obvious security concerns detected in static analysis.


---

**Generated**: 2025-11-19T02:16:46.496247Z
**Generator**: World's Best Repo Book Generator v1.0

# File Documentation: etf_performance.py

## Metadata
- **Path**: `openbb_platform/core/openbb_core/provider/standard_models/etf_performance.py`
- **Size**: 1,559 bytes
- **Lines**: 58
- **Category**: python
- **Extension**: .py

---

## Original Source

```python
"""ETF Performance Standard Model."""

from datetime import date as dateType
from typing import Literal

from openbb_core.provider.abstract.data import Data
from openbb_core.provider.abstract.query_params import QueryParams
from openbb_core.provider.utils.descriptions import (
    DATA_DESCRIPTIONS,
    QUERY_DESCRIPTIONS,
)
from pydantic import Field, field_validator


class ETFPerformanceQueryParams(QueryParams):
    """ETF Performance Query."""

    sort: Literal["asc", "desc"] = Field(
        default="desc",
        description="Sort order. Possible values: 'asc', 'desc'. Default: 'desc'.",
    )
    limit: int = Field(
        default=10,
        description=QUERY_DESCRIPTIONS.get("limit", ""),
    )

    @field_validator("sort", mode="before", check_fields=False)
    @classmethod
    def to_lower(cls, v: str | None) -> str | None:
        """Convert field to lowercase."""
        return v.lower() if v else v


class ETFPerformanceData(Data):
    """ETF Performance Data."""

    symbol: str = Field(
        description=DATA_DESCRIPTIONS.get("symbol", ""),
    )
    name: str = Field(
        description="Name of the entity.",
    )
    last_price: float = Field(
        description="Last price.",
    )
    percent_change: float = Field(
        description="Percent change.",
    )
    net_change: float = Field(
        description="Net change.",
    )
    volume: float = Field(
        description=DATA_DESCRIPTIONS.get("volume", ""),
    )
    date: dateType = Field(
        description=DATA_DESCRIPTIONS.get("date", ""),
    )

```



---

## High-Level Overview

This is a **python** file named `etf_performance.py`.

**Python Module**

- **Classes** (2): ETFPerformanceQueryParams, ETFPerformanceData
- **Functions** (1): to_lower
- **Import Statements**: 2


---

## Detailed Analysis

### Python Code Structure

#### Classes

- **`ETFPerformanceQueryParams`**(QueryParams)
- **`ETFPerformanceData`**(Data)

#### Decorators Used

classmethod, field_validator


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

**Generated**: 2025-11-19T02:16:46.447532Z
**Generator**: World's Best Repo Book Generator v1.0

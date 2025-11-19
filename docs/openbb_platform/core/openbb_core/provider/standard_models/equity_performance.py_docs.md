# File Documentation: equity_performance.py

## Metadata
- **Path**: `openbb_platform/core/openbb_core/provider/standard_models/equity_performance.py`
- **Size**: 1,580 bytes
- **Lines**: 52
- **Category**: python
- **Extension**: .py

---

## Original Source

```python
"""Equity Performance Standard Model."""

from typing import Literal

from openbb_core.provider.abstract.data import Data
from openbb_core.provider.abstract.query_params import QueryParams
from openbb_core.provider.utils.descriptions import DATA_DESCRIPTIONS
from pydantic import Field, field_validator


class EquityPerformanceQueryParams(QueryParams):
    """Equity Performance Query."""

    sort: Literal["asc", "desc"] = Field(
        default="desc",
        description="Sort order. Possible values: 'asc', 'desc'. Default: 'desc'.",
    )

    @field_validator("sort", mode="before", check_fields=False)
    @classmethod
    def to_lower(cls, v: str | None) -> str | None:
        """Convert field to lowercase."""
        return v.lower() if v else v


class EquityPerformanceData(Data):
    """Equity Performance Data."""

    symbol: str = Field(
        description=DATA_DESCRIPTIONS.get("symbol", ""),
    )
    name: str | None = Field(
        default=None,
        description="Name of the entity.",
    )
    price: float = Field(
        description="Last price.",
        json_schema_extra={"x-unit_measurement": "currency"},
    )
    change: float = Field(
        description="Change in price.",
        json_schema_extra={"x-unit_measurement": "currency"},
    )
    percent_change: float = Field(
        description="Percent change.",
        json_schema_extra={"x-unit_measurement": "percent", "x-frontend_multiply": 100},
    )
    volume: int | float | None = Field(
        default=None,
        description=DATA_DESCRIPTIONS.get("volume", ""),
    )

```



---

## High-Level Overview

This is a **python** file named `equity_performance.py`.

**Python Module**

- **Classes** (2): EquityPerformanceQueryParams, EquityPerformanceData
- **Functions** (1): to_lower
- **Import Statements**: 1


---

## Detailed Analysis

### Python Code Structure

#### Classes

- **`EquityPerformanceQueryParams`**(QueryParams)
- **`EquityPerformanceData`**(Data)

#### Decorators Used

classmethod, field_validator


---

## Related Files

The following files may be related based on imports and references:

**Imported Modules**:
- `DATA_DESCRIPTIONS`
- `Data`
- `Field`
- `Literal`
- `QueryParams`
- `openbb_core.provider.abstract.data`
- `openbb_core.provider.abstract.query_params`
- `openbb_core.provider.utils.descriptions`
- `pydantic`
- `typing`


---

## Performance & Security Notes

No obvious security concerns detected in static analysis.


---

**Generated**: 2025-11-19T02:16:46.426827Z
**Generator**: World's Best Repo Book Generator v1.0

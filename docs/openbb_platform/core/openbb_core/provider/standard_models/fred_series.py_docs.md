# File Documentation: fred_series.py

## Metadata
- **Path**: `openbb_platform/core/openbb_core/provider/standard_models/fred_series.py`
- **Size**: 1,166 bytes
- **Lines**: 41
- **Category**: python
- **Extension**: .py

---

## Original Source

```python
"""FRED Series Standard Model."""

from datetime import date as dateType

from openbb_core.provider.abstract.data import Data
from openbb_core.provider.abstract.query_params import QueryParams
from openbb_core.provider.utils.descriptions import (
    DATA_DESCRIPTIONS,
    QUERY_DESCRIPTIONS,
)
from pydantic import Field, field_validator


class SeriesQueryParams(QueryParams):
    """FRED Series Query."""

    symbol: str = Field(
        description=QUERY_DESCRIPTIONS.get("symbol", ""),
    )
    start_date: dateType | None = Field(
        description=QUERY_DESCRIPTIONS.get("start_date", ""), default=None
    )
    end_date: dateType | None = Field(
        description=QUERY_DESCRIPTIONS.get("end_date", ""), default=None
    )
    limit: int | None = Field(
        description=QUERY_DESCRIPTIONS.get("limit", ""), default=100000
    )

    @field_validator("symbol", mode="before", check_fields=False)
    @classmethod
    def to_upper(cls, v: str) -> str:
        """Convert field to uppercase."""
        return v.upper()


class SeriesData(Data):
    """FRED Series Data."""

    date: dateType = Field(description=DATA_DESCRIPTIONS.get("date", ""))

```



---

## High-Level Overview

This is a **python** file named `fred_series.py`.

**Python Module**

- **Classes** (2): SeriesQueryParams, SeriesData
- **Functions** (1): to_upper
- **Import Statements**: 2


---

## Detailed Analysis

### Python Code Structure

#### Classes

- **`SeriesQueryParams`**(QueryParams)
- **`SeriesData`**(Data)

#### Decorators Used

classmethod, field_validator


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

**Generated**: 2025-11-19T02:16:46.474849Z
**Generator**: World's Best Repo Book Generator v1.0

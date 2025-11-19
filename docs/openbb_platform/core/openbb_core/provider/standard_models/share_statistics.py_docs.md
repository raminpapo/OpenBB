# File Documentation: share_statistics.py

## Metadata
- **Path**: `openbb_platform/core/openbb_core/provider/standard_models/share_statistics.py`
- **Size**: 1,525 bytes
- **Lines**: 48
- **Category**: python
- **Extension**: .py

---

## Original Source

```python
"""Share Statistics Standard Model."""

from datetime import (
    date as dateType,
    datetime,
)

from openbb_core.provider.abstract.data import Data
from openbb_core.provider.abstract.query_params import QueryParams
from openbb_core.provider.utils.descriptions import (
    DATA_DESCRIPTIONS,
    QUERY_DESCRIPTIONS,
)
from pydantic import Field, field_validator


class ShareStatisticsQueryParams(QueryParams):
    """Share Statistics Query."""

    symbol: str = Field(description=QUERY_DESCRIPTIONS.get("symbol", ""))

    @field_validator("symbol", mode="before", check_fields=False)
    @classmethod
    def to_upper(cls, v: str) -> str:
        """Convert field to uppercase."""
        return v.upper()


class ShareStatisticsData(Data):
    """Share Statistics Data."""

    symbol: str = Field(description=DATA_DESCRIPTIONS.get("symbol", ""))
    date: dateType | datetime | None = Field(
        default=None, description=DATA_DESCRIPTIONS.get("date", "")
    )
    free_float: float | None = Field(
        default=None,
        description="Percentage of unrestricted shares of a publicly-traded company.",
        json_schema_extra={"x-unit_measurement": "percent", "x-frontend_multiply": 100},
    )
    float_shares: int | float | None = Field(
        default=None,
        description="Number of shares available for trading by the general public.",
    )
    outstanding_shares: int | float | None = Field(
        default=None, description="Total number of shares of a publicly-traded company."
    )

```



---

## High-Level Overview

This is a **python** file named `share_statistics.py`.

**Python Module**

- **Classes** (2): ShareStatisticsQueryParams, ShareStatisticsData
- **Functions** (1): to_upper
- **Import Statements**: 2


---

## Detailed Analysis

### Python Code Structure

#### Classes

- **`ShareStatisticsQueryParams`**(QueryParams)
- **`ShareStatisticsData`**(Data)

#### Decorators Used

classmethod, field_validator


---

## Related Files

The following files may be related based on imports and references:

**Imported Modules**:
- `Data`
- `Field`
- `QueryParams`
- `datetime`
- `openbb_core.provider.abstract.data`
- `openbb_core.provider.abstract.query_params`
- `openbb_core.provider.utils.descriptions`
- `pydantic`


---

## Performance & Security Notes

No obvious security concerns detected in static analysis.


---

**Generated**: 2025-11-19T02:16:46.569974Z
**Generator**: World's Best Repo Book Generator v1.0

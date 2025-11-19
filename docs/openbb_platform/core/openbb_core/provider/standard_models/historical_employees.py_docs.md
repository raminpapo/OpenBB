# File Documentation: historical_employees.py

## Metadata
- **Path**: `openbb_platform/core/openbb_core/provider/standard_models/historical_employees.py`
- **Size**: 1,275 bytes
- **Lines**: 40
- **Category**: python
- **Extension**: .py

---

## Original Source

```python
"""Historical Employees Standard Model."""

from datetime import date as dateType

from openbb_core.provider.abstract.data import Data
from openbb_core.provider.abstract.query_params import QueryParams
from openbb_core.provider.utils.descriptions import (
    DATA_DESCRIPTIONS,
    QUERY_DESCRIPTIONS,
)
from pydantic import Field, field_validator


class HistoricalEmployeesQueryParams(QueryParams):
    """Historical Employees Query."""

    symbol: str = Field(description=QUERY_DESCRIPTIONS.get("symbol", ""))
    start_date: dateType | None = Field(
        default=None, description=QUERY_DESCRIPTIONS.get("start_date", "")
    )
    end_date: dateType | None = Field(
        default=None, description=QUERY_DESCRIPTIONS.get("end_date", "")
    )

    @field_validator("symbol", mode="before", check_fields=False)
    @classmethod
    def to_upper(cls, v: str) -> str:
        """Convert field to uppercase."""
        return v.upper()


class HistoricalEmployeesData(Data):
    """Historical Employees Data."""

    date: dateType = Field(description=DATA_DESCRIPTIONS.get("date", ""))
    symbol: str | None = Field(
        default=None, description=DATA_DESCRIPTIONS.get("symbol", "")
    )
    employees: int = Field(description="Reported number of employees.")

```



---

## High-Level Overview

This is a **python** file named `historical_employees.py`.

**Python Module**

- **Classes** (2): HistoricalEmployeesQueryParams, HistoricalEmployeesData
- **Functions** (1): to_upper
- **Import Statements**: 2


---

## Detailed Analysis

### Python Code Structure

#### Classes

- **`HistoricalEmployeesQueryParams`**(QueryParams)
- **`HistoricalEmployeesData`**(Data)

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

**Generated**: 2025-11-19T02:16:46.490944Z
**Generator**: World's Best Repo Book Generator v1.0

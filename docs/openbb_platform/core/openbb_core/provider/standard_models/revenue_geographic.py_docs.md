# File Documentation: revenue_geographic.py

## Metadata
- **Path**: `openbb_platform/core/openbb_core/provider/standard_models/revenue_geographic.py`
- **Size**: 1,512 bytes
- **Lines**: 44
- **Category**: python
- **Extension**: .py

---

## Original Source

```python
"""Revenue by Geographic Segments Standard Model."""

from datetime import date as dateType

from openbb_core.provider.abstract.data import Data
from openbb_core.provider.abstract.query_params import QueryParams
from openbb_core.provider.utils.descriptions import QUERY_DESCRIPTIONS
from pydantic import Field, field_validator


class RevenueGeographicQueryParams(QueryParams):
    """Revenue by Geographic Segments Query."""

    symbol: str = Field(description=QUERY_DESCRIPTIONS.get("symbol", ""))

    @field_validator("symbol", mode="before", check_fields=False)
    @classmethod
    def to_upper(cls, v: str):
        """Convert field to uppercase."""
        return v.upper()


class RevenueGeographicData(Data):
    """Revenue by Geographic Segments Data."""

    period_ending: dateType = Field(description="The end date of the reporting period.")
    fiscal_period: str | None = Field(
        default=None, description="The fiscal period of the reporting period."
    )
    fiscal_year: int | None = Field(
        default=None, description="The fiscal year of the reporting period."
    )
    filing_date: dateType | None = Field(
        default=None, description="The filing date of the report."
    )
    region: str | None = Field(
        default=None,
        description="The region represented by the revenue data.",
    )
    revenue: int | float = Field(
        description="The total revenue attributed to the region.",
        json_schema_extra={"x-unit_measurement": "currency"},
    )

```



---

## High-Level Overview

This is a **python** file named `revenue_geographic.py`.

**Python Module**

- **Classes** (2): RevenueGeographicQueryParams, RevenueGeographicData
- **Functions** (1): to_upper
- **Import Statements**: 1


---

## Detailed Analysis

### Python Code Structure

#### Classes

- **`RevenueGeographicQueryParams`**(QueryParams)
- **`RevenueGeographicData`**(Data)

#### Functions

- **`to_upper(cls, v: str)`**

#### Decorators Used

classmethod, field_validator


---

## Related Files

The following files may be related based on imports and references:

**Imported Modules**:
- `Data`
- `Field`
- `QUERY_DESCRIPTIONS`
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

**Generated**: 2025-11-19T02:16:46.559950Z
**Generator**: World's Best Repo Book Generator v1.0

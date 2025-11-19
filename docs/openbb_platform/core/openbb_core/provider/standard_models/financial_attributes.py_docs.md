# File Documentation: financial_attributes.py

## Metadata
- **Path**: `openbb_platform/core/openbb_core/provider/standard_models/financial_attributes.py`
- **Size**: 1,721 bytes
- **Lines**: 49
- **Category**: python
- **Extension**: .py

---

## Original Source

```python
"""Financial Attributes Standard Model."""

from datetime import date as dateType
from typing import Literal

from openbb_core.provider.abstract.data import Data
from openbb_core.provider.abstract.query_params import QueryParams
from openbb_core.provider.utils.descriptions import (
    DATA_DESCRIPTIONS,
    QUERY_DESCRIPTIONS,
)
from pydantic import Field, field_validator


class FinancialAttributesQueryParams(QueryParams):
    """Financial Attributes Query."""

    symbol: str = Field(description=QUERY_DESCRIPTIONS.get("symbol"))
    tag: str = Field(description=QUERY_DESCRIPTIONS.get("tag"))
    period: Literal["annual", "quarter"] | None = Field(
        default="annual", description=QUERY_DESCRIPTIONS.get("period")
    )
    limit: int | None = Field(default=1000, description=QUERY_DESCRIPTIONS.get("limit"))
    type: str | None = Field(
        default=None, description="Filter by type, when applicable."
    )
    start_date: dateType | None = Field(
        default=None, description=QUERY_DESCRIPTIONS.get("start_date")
    )
    end_date: dateType | None = Field(
        default=None, description=QUERY_DESCRIPTIONS.get("end_date")
    )
    sort: Literal["asc", "desc"] | None = Field(
        default="desc", description="Sort order."
    )

    @field_validator("period", "sort", mode="before", check_fields=False)
    @classmethod
    def to_lower(cls, v: str | None) -> str | None:
        """Convert field to lowercase."""
        return v.lower() if v else v


class FinancialAttributesData(Data):
    """Financial Attributes Data."""

    date: dateType = Field(description=DATA_DESCRIPTIONS.get("date"))
    value: float | None = Field(default=None, description="The value of the data.")

```



---

## High-Level Overview

This is a **python** file named `financial_attributes.py`.

**Python Module**

- **Classes** (2): FinancialAttributesQueryParams, FinancialAttributesData
- **Functions** (1): to_lower
- **Import Statements**: 2


---

## Detailed Analysis

### Python Code Structure

#### Classes

- **`FinancialAttributesQueryParams`**(QueryParams)
- **`FinancialAttributesData`**(Data)

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

**Generated**: 2025-11-19T02:16:46.460777Z
**Generator**: World's Best Repo Book Generator v1.0

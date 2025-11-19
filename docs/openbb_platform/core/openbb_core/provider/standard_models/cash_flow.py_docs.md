# File Documentation: cash_flow.py

## Metadata
- **Path**: `openbb_platform/core/openbb_core/provider/standard_models/cash_flow.py`
- **Size**: 1,186 bytes
- **Lines**: 36
- **Category**: python
- **Extension**: .py

---

## Original Source

```python
"""Cash Flow Statement Standard Model."""

from datetime import date as dateType

from openbb_core.provider.abstract.data import Data
from openbb_core.provider.abstract.query_params import QueryParams
from openbb_core.provider.utils.descriptions import QUERY_DESCRIPTIONS
from pydantic import Field, NonNegativeInt, field_validator


class CashFlowStatementQueryParams(QueryParams):
    """Cash Flow Statement Query."""

    symbol: str = Field(description=QUERY_DESCRIPTIONS.get("symbol", ""))
    limit: NonNegativeInt | None = Field(
        default=5, description=QUERY_DESCRIPTIONS.get("limit", "")
    )

    @field_validator("symbol", mode="before", check_fields=False)
    @classmethod
    def to_upper(cls, v: str):
        """Convert field to uppercase."""
        return v.upper()


class CashFlowStatementData(Data):
    """Cash Flow Statement Data."""

    period_ending: dateType = Field(description="The end date of the reporting period.")
    fiscal_period: str | None = Field(
        description="The fiscal period of the report.", default=None
    )
    fiscal_year: int | None = Field(
        description="The fiscal year of the fiscal period.", default=None
    )

```



---

## High-Level Overview

This is a **python** file named `cash_flow.py`.

**Python Module**

- **Classes** (2): CashFlowStatementQueryParams, CashFlowStatementData
- **Functions** (1): to_upper
- **Import Statements**: 1


---

## Detailed Analysis

### Python Code Structure

#### Classes

- **`CashFlowStatementQueryParams`**(QueryParams)
- **`CashFlowStatementData`**(Data)

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

**Generated**: 2025-11-19T02:16:46.370450Z
**Generator**: World's Best Repo Book Generator v1.0

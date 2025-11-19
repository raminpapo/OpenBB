# File Documentation: cash_flow_growth.py

## Metadata
- **Path**: `openbb_platform/core/openbb_core/provider/standard_models/cash_flow_growth.py`
- **Size**: 1,202 bytes
- **Lines**: 36
- **Category**: python
- **Extension**: .py

---

## Original Source

```python
"""Cash Flow Statement Growth Standard Model."""

from datetime import date as dateType

from openbb_core.provider.abstract.data import Data
from openbb_core.provider.abstract.query_params import QueryParams
from openbb_core.provider.utils.descriptions import QUERY_DESCRIPTIONS
from pydantic import Field, field_validator


class CashFlowStatementGrowthQueryParams(QueryParams):
    """Cash Flow Statement Growth Query."""

    symbol: str = Field(description=QUERY_DESCRIPTIONS.get("symbol", ""))
    limit: int | None = Field(
        default=None, description=QUERY_DESCRIPTIONS.get("limit", "")
    )

    @field_validator("symbol", mode="before", check_fields=False)
    @classmethod
    def to_upper(cls, v: str) -> str:
        """Convert field to uppercase."""
        return v.upper()


class CashFlowStatementGrowthData(Data):
    """Cash Flow Statement Growth Data."""

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

This is a **python** file named `cash_flow_growth.py`.

**Python Module**

- **Classes** (2): CashFlowStatementGrowthQueryParams, CashFlowStatementGrowthData
- **Functions** (1): to_upper
- **Import Statements**: 1


---

## Detailed Analysis

### Python Code Structure

#### Classes

- **`CashFlowStatementGrowthQueryParams`**(QueryParams)
- **`CashFlowStatementGrowthData`**(Data)

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

**Generated**: 2025-11-19T02:16:46.372025Z
**Generator**: World's Best Repo Book Generator v1.0

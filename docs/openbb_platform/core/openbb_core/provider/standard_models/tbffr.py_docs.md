# File Documentation: tbffr.py

## Metadata
- **Path**: `openbb_platform/core/openbb_core/provider/standard_models/tbffr.py`
- **Size**: 1,298 bytes
- **Lines**: 45
- **Category**: python
- **Extension**: .py

---

## Original Source

```python
"""Selected Treasury Bill Standard Model."""

from datetime import (
    date as dateType,
)
from typing import Literal

from openbb_core.provider.abstract.data import Data
from openbb_core.provider.abstract.query_params import QueryParams
from openbb_core.provider.utils.descriptions import (
    DATA_DESCRIPTIONS,
    QUERY_DESCRIPTIONS,
)
from pydantic import Field, field_validator


class SelectedTreasuryBillQueryParams(QueryParams):
    """Selected Treasury Bill Query."""

    start_date: dateType | None = Field(
        default=None,
        description=QUERY_DESCRIPTIONS.get("start_date", ""),
    )
    end_date: dateType | None = Field(
        default=None,
        description=QUERY_DESCRIPTIONS.get("end_date", ""),
    )
    maturity: Literal["3m", "6m"] | None = Field(
        default="3m",
        description="The maturity",
    )

    @field_validator("maturity", mode="before", check_fields=False)
    @classmethod
    def to_lower(cls, v: str | None) -> str | None:
        """Convert field to lowercase."""
        return v.lower() if v else v


class SelectedTreasuryBillData(Data):
    """Selected Treasury Bill Data."""

    date: dateType = Field(description=DATA_DESCRIPTIONS.get("date", ""))
    rate: float | None = Field(description="SelectedTreasuryBill Rate.")

```



---

## High-Level Overview

This is a **python** file named `tbffr.py`.

**Python Module**

- **Classes** (2): SelectedTreasuryBillQueryParams, SelectedTreasuryBillData
- **Functions** (1): to_lower
- **Import Statements**: 2


---

## Detailed Analysis

### Python Code Structure

#### Classes

- **`SelectedTreasuryBillQueryParams`**(QueryParams)
- **`SelectedTreasuryBillData`**(Data)

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

**Generated**: 2025-11-19T02:16:46.582201Z
**Generator**: World's Best Repo Book Generator v1.0

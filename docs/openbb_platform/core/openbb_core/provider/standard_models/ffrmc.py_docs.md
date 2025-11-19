# File Documentation: ffrmc.py

## Metadata
- **Path**: `openbb_platform/core/openbb_core/provider/standard_models/ffrmc.py`
- **Size**: 1,396 bytes
- **Lines**: 45
- **Category**: python
- **Extension**: .py

---

## Original Source

```python
"""Selected Treasury Constant Maturity Standard Model."""

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


class SelectedTreasuryConstantMaturityQueryParams(QueryParams):
    """Selected Treasury Constant Maturity Query."""

    start_date: dateType | None = Field(
        default=None,
        description=QUERY_DESCRIPTIONS.get("start_date", ""),
    )
    end_date: dateType | None = Field(
        default=None,
        description=QUERY_DESCRIPTIONS.get("end_date", ""),
    )
    maturity: Literal["10y", "5y", "1y", "6m", "3m"] | None = Field(
        default="10y",
        description="The maturity",
    )

    @field_validator("maturity", mode="before", check_fields=False)
    @classmethod
    def to_lower(cls, v: str | None) -> str | None:
        """Convert field to lowercase."""
        return v.lower() if v else v


class SelectedTreasuryConstantMaturityData(Data):
    """Selected Treasury Constant Maturity Data."""

    date: dateType = Field(description=DATA_DESCRIPTIONS.get("date", ""))
    rate: float | None = Field(description="Selected Treasury Constant Maturity Rate.")

```



---

## High-Level Overview

This is a **python** file named `ffrmc.py`.

**Python Module**

- **Classes** (2): SelectedTreasuryConstantMaturityQueryParams, SelectedTreasuryConstantMaturityData
- **Functions** (1): to_lower
- **Import Statements**: 2


---

## Detailed Analysis

### Python Code Structure

#### Classes

- **`SelectedTreasuryConstantMaturityQueryParams`**(QueryParams)
- **`SelectedTreasuryConstantMaturityData`**(Data)

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

**Generated**: 2025-11-19T02:16:46.459489Z
**Generator**: World's Best Repo Book Generator v1.0

# File Documentation: forward_pe_estimates.py

## Metadata
- **Path**: `openbb_platform/core/openbb_core/provider/standard_models/forward_pe_estimates.py`
- **Size**: 1,594 bytes
- **Lines**: 52
- **Category**: python
- **Extension**: .py

---

## Original Source

```python
"""Forward PE Estimates Standard Model."""

from openbb_core.provider.abstract.data import Data
from openbb_core.provider.abstract.query_params import QueryParams
from openbb_core.provider.utils.descriptions import (
    DATA_DESCRIPTIONS,
    QUERY_DESCRIPTIONS,
)
from pydantic import Field, field_validator


class ForwardPeEstimatesQueryParams(QueryParams):
    """Forward PE Estimates Query Parameters."""

    symbol: str | None = Field(
        default=None,
        description=QUERY_DESCRIPTIONS["symbol"],
    )

    @field_validator("symbol", mode="before", check_fields=False)
    @classmethod
    def to_upper(cls, v):
        """Convert field to uppercase."""
        return v.upper() if v else None


class ForwardPeEstimatesData(Data):
    """Forward PE Estimates Data."""

    symbol: str = Field(description=DATA_DESCRIPTIONS.get("symbol", ""))
    name: str | None = Field(default=None, description="Name of the entity.")
    year1: float | None = Field(
        default=None,
        description="Estimated PE ratio for the next fiscal year.",
    )
    year2: float | None = Field(
        default=None,
        description="Estimated PE ratio two fiscal years from now.",
    )
    year3: float | None = Field(
        default=None,
        description="Estimated PE ratio three fiscal years from now.",
    )
    year4: float | None = Field(
        default=None,
        description="Estimated PE ratio four fiscal years from now.",
    )
    year5: float | None = Field(
        default=None,
        description="Estimated PE ratio five fiscal years from now.",
    )

```



---

## High-Level Overview

This is a **python** file named `forward_pe_estimates.py`.

**Python Module**

- **Classes** (2): ForwardPeEstimatesQueryParams, ForwardPeEstimatesData
- **Functions** (1): to_upper
- **Import Statements**: 2


---

## Detailed Analysis

### Python Code Structure

#### Classes

- **`ForwardPeEstimatesQueryParams`**(QueryParams)
- **`ForwardPeEstimatesData`**(Data)

#### Functions

- **`to_upper(cls, v)`**

#### Decorators Used

classmethod, field_validator


---

## Related Files

The following files may be related based on imports and references:

**Imported Modules**:
- `Data`
- `Field`
- `QueryParams`
- `openbb_core.provider.abstract.data`
- `openbb_core.provider.abstract.query_params`
- `openbb_core.provider.utils.descriptions`
- `pydantic`


---

## Performance & Security Notes

No obvious security concerns detected in static analysis.


---

**Generated**: 2025-11-19T02:16:46.468847Z
**Generator**: World's Best Repo Book Generator v1.0

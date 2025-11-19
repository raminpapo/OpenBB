# File Documentation: forward_eps_estimates.py

## Metadata
- **Path**: `openbb_platform/core/openbb_core/provider/standard_models/forward_eps_estimates.py`
- **Size**: 2,256 bytes
- **Lines**: 66
- **Category**: python
- **Extension**: .py

---

## Original Source

```python
"""Forward EPS Estimates Standard Model."""

from datetime import date as dateType

from openbb_core.provider.abstract.data import Data
from openbb_core.provider.abstract.query_params import QueryParams
from openbb_core.provider.utils.descriptions import (
    DATA_DESCRIPTIONS,
    QUERY_DESCRIPTIONS,
)
from pydantic import Field, field_validator


class ForwardEpsEstimatesQueryParams(QueryParams):
    """Forward EPS Estimates Query Parameters."""

    symbol: str | None = Field(
        default=None,
        description=QUERY_DESCRIPTIONS["symbol"],
    )

    @field_validator("symbol", mode="before", check_fields=False)
    @classmethod
    def to_upper(cls, v):
        """Convert field to uppercase."""
        return v.upper() if v else None


class ForwardEpsEstimatesData(Data):
    """Forward EPS Estimates Data."""

    symbol: str = Field(description=DATA_DESCRIPTIONS.get("symbol", ""))
    name: str | None = Field(default=None, description="Name of the entity.")
    date: dateType = Field(description=DATA_DESCRIPTIONS.get("date", ""))
    fiscal_year: int | None = Field(
        default=None, description="Fiscal year for the estimate."
    )
    fiscal_period: str | None = Field(
        default=None, description="Fiscal quarter for the estimate."
    )
    calendar_year: int | None = Field(
        default=None, description="Calendar year for the estimate."
    )
    calendar_period: str | None = Field(
        default=None, description="Calendar quarter for the estimate."
    )
    low_estimate: float | None = Field(
        default=None, description="Estimated EPS low for the period."
    )
    high_estimate: float | None = Field(
        default=None, description="Estimated EPS high for the period."
    )
    mean: float | None = Field(
        default=None, description="Estimated EPS mean for the period."
    )
    median: float | None = Field(
        default=None, description="Estimated EPS median for the period."
    )
    standard_deviation: float | None = Field(
        default=None, description="Estimated EPS standard deviation for the period."
    )
    number_of_analysts: int | None = Field(
        default=None,
        description="Number of analysts providing estimates for the period.",
    )

```



---

## High-Level Overview

This is a **python** file named `forward_eps_estimates.py`.

**Python Module**

- **Classes** (2): ForwardEpsEstimatesQueryParams, ForwardEpsEstimatesData
- **Functions** (1): to_upper
- **Import Statements**: 2


---

## Detailed Analysis

### Python Code Structure

#### Classes

- **`ForwardEpsEstimatesQueryParams`**(QueryParams)
- **`ForwardEpsEstimatesData`**(Data)

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

**Generated**: 2025-11-19T02:16:46.467006Z
**Generator**: World's Best Repo Book Generator v1.0

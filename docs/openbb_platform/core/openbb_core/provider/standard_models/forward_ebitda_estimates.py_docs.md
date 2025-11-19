# File Documentation: forward_ebitda_estimates.py

## Metadata
- **Path**: `openbb_platform/core/openbb_core/provider/standard_models/forward_ebitda_estimates.py`
- **Size**: 2,523 bytes
- **Lines**: 74
- **Category**: python
- **Extension**: .py

---

## Original Source

```python
"""Forward EBITDA Estimates Standard Model."""

from datetime import date as dateType

from openbb_core.provider.abstract.data import Data, ForceInt
from openbb_core.provider.abstract.query_params import QueryParams
from openbb_core.provider.utils.descriptions import (
    DATA_DESCRIPTIONS,
    QUERY_DESCRIPTIONS,
)
from pydantic import Field, field_validator


class ForwardEbitdaEstimatesQueryParams(QueryParams):
    """Forward EBITDA Estimates Query Parameters."""

    symbol: str | None = Field(
        default=None,
        description=QUERY_DESCRIPTIONS["symbol"],
    )

    @field_validator("symbol", mode="before", check_fields=False)
    @classmethod
    def to_upper(cls, v):
        """Convert field to uppercase."""
        return v.upper() if v else None


class ForwardEbitdaEstimatesData(Data):
    """Forward EBITDA Estimates Data."""

    symbol: str = Field(description=DATA_DESCRIPTIONS.get("symbol", ""))
    name: str | None = Field(default=None, description="Name of the entity.")
    last_updated: dateType | None = Field(
        default=None,
        description="The date of the last update.",
    )
    period_ending: dateType | None = Field(
        default=None,
        description="The end date of the reporting period.",
    )
    fiscal_year: int | None = Field(
        default=None, description="Fiscal year for the estimate."
    )
    fiscal_period: str | None = Field(
        default=None, description="Fiscal quarter for the estimate."
    )
    calendar_year: int | None = Field(
        default=None, description="Calendar year for the estimate."
    )
    calendar_period: int | str | None = Field(
        default=None, description="Calendar quarter for the estimate."
    )
    low_estimate: ForceInt | None = Field(
        default=None, description="The EBITDA estimate low for the period."
    )
    high_estimate: ForceInt | None = Field(
        default=None, description="The EBITDA estimate high for the period."
    )
    mean: ForceInt | None = Field(
        default=None, description="The EBITDA estimate mean for the period."
    )
    median: ForceInt | None = Field(
        default=None, description="The EBITDA estimate median for the period."
    )
    standard_deviation: ForceInt | None = Field(
        default=None,
        description="The EBITDA estimate standard deviation for the period.",
    )
    number_of_analysts: int | None = Field(
        default=None,
        description="Number of analysts providing estimates for the period.",
    )

```



---

## High-Level Overview

This is a **python** file named `forward_ebitda_estimates.py`.

**Python Module**

- **Classes** (2): ForwardEbitdaEstimatesQueryParams, ForwardEbitdaEstimatesData
- **Functions** (1): to_upper
- **Import Statements**: 2


---

## Detailed Analysis

### Python Code Structure

#### Classes

- **`ForwardEbitdaEstimatesQueryParams`**(QueryParams)
- **`ForwardEbitdaEstimatesData`**(Data)

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

**Generated**: 2025-11-19T02:16:46.465415Z
**Generator**: World's Best Repo Book Generator v1.0

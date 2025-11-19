# File Documentation: analyst_estimates.py

## Metadata
- **Path**: `openbb_platform/core/openbb_core/provider/standard_models/analyst_estimates.py`
- **Size**: 3,337 bytes
- **Lines**: 91
- **Category**: python
- **Extension**: .py

---

## Original Source

```python
"""Analyst Estimates Standard Model."""

from datetime import date as dateType

from openbb_core.provider.abstract.data import Data, ForceInt
from openbb_core.provider.abstract.query_params import QueryParams
from openbb_core.provider.utils.descriptions import (
    DATA_DESCRIPTIONS,
    QUERY_DESCRIPTIONS,
)
from pydantic import Field, field_validator


class AnalystEstimatesQueryParams(QueryParams):
    """Analyst Estimates Query."""

    symbol: str = Field(description=QUERY_DESCRIPTIONS.get("symbol", ""))

    @field_validator("symbol", mode="before", check_fields=False)
    @classmethod
    def to_upper(cls, v: str) -> str:
        """Convert field to uppercase."""
        return v.upper()


class AnalystEstimatesData(Data):
    """Analyst Estimates data."""

    symbol: str = Field(description=DATA_DESCRIPTIONS.get("symbol", ""))
    date: dateType = Field(description=DATA_DESCRIPTIONS.get("date", ""))
    estimated_revenue_low: ForceInt | None = Field(
        default=None, description="Estimated revenue low."
    )
    estimated_revenue_high: ForceInt | None = Field(
        default=None, description="Estimated revenue high."
    )
    estimated_revenue_avg: ForceInt | None = Field(
        default=None, description="Estimated revenue average."
    )
    estimated_sga_expense_low: ForceInt | None = Field(
        default=None, description="Estimated SGA expense low."
    )
    estimated_sga_expense_high: ForceInt | None = Field(
        default=None, description="Estimated SGA expense high."
    )
    estimated_sga_expense_avg: ForceInt | None = Field(
        default=None, description="Estimated SGA expense average."
    )
    estimated_ebitda_low: ForceInt | None = Field(
        default=None, description="Estimated EBITDA low."
    )
    estimated_ebitda_high: ForceInt | None = Field(
        default=None, description="Estimated EBITDA high."
    )
    estimated_ebitda_avg: ForceInt | None = Field(
        default=None, description="Estimated EBITDA average."
    )
    estimated_ebit_low: ForceInt | None = Field(
        default=None, description="Estimated EBIT low."
    )
    estimated_ebit_high: ForceInt | None = Field(
        default=None, description="Estimated EBIT high."
    )
    estimated_ebit_avg: ForceInt | None = Field(
        default=None, description="Estimated EBIT average."
    )
    estimated_net_income_low: ForceInt | None = Field(
        default=None, description="Estimated net income low."
    )
    estimated_net_income_high: ForceInt | None = Field(
        default=None, description="Estimated net income high."
    )
    estimated_net_income_avg: ForceInt | None = Field(
        default=None, description="Estimated net income average."
    )
    estimated_eps_avg: float | None = Field(
        default=None, description="Estimated EPS average."
    )
    estimated_eps_high: float | None = Field(
        default=None, description="Estimated EPS high."
    )
    estimated_eps_low: float | None = Field(
        default=None, description="Estimated EPS low."
    )
    number_analyst_estimated_revenue: ForceInt | None = Field(
        default=None, description="Number of analysts who estimated revenue."
    )
    number_analysts_estimated_eps: ForceInt | None = Field(
        default=None, description="Number of analysts who estimated EPS."
    )

```



---

## High-Level Overview

This is a **python** file named `analyst_estimates.py`.

**Python Module**

- **Classes** (2): AnalystEstimatesQueryParams, AnalystEstimatesData
- **Functions** (1): to_upper
- **Import Statements**: 2


---

## Detailed Analysis

### Python Code Structure

#### Classes

- **`AnalystEstimatesQueryParams`**(QueryParams)
- **`AnalystEstimatesData`**(Data)

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

**Generated**: 2025-11-19T02:16:46.340616Z
**Generator**: World's Best Repo Book Generator v1.0

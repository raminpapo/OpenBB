# File Documentation: reported_financials.py

## Metadata
- **Path**: `openbb_platform/core/openbb_core/provider/standard_models/reported_financials.py`
- **Size**: 2,295 bytes
- **Lines**: 69
- **Category**: python
- **Extension**: .py

---

## Original Source

```python
"""Reported Financials."""

from datetime import date as dateType

from openbb_core.provider.abstract.data import Data
from openbb_core.provider.abstract.query_params import QueryParams
from openbb_core.provider.utils.descriptions import (
    QUERY_DESCRIPTIONS,
)
from pydantic import Field, field_validator, model_validator


class ReportedFinancialsQueryParams(QueryParams):
    """Reported Financials Query Params."""

    symbol: str = Field(description=QUERY_DESCRIPTIONS.get("symbol", ""))
    period: str = Field(
        default="annual", description=QUERY_DESCRIPTIONS.get("period", "")
    )
    statement_type: str = Field(
        default="balance",
        description="The type of financial statement - i.e, balance, income, cash.",
    )
    limit: int | None = Field(
        default=100,
        description=(
            QUERY_DESCRIPTIONS.get("limit", "")
            + " Although the response object contains multiple results,"
            + " because of the variance in the fields, year-to-year and quarter-to-quarter,"
            + " it is recommended to view results in small chunks."
        ),
    )

    @field_validator("symbol", mode="before", check_fields=False)
    @classmethod
    def to_upper(cls, v: str):
        """Convert field to uppercase."""
        return v.upper()

    @field_validator("period", "statement_type", mode="before", check_fields=False)
    @classmethod
    def to_lower(cls, v: str | None) -> str | None:
        """Convert field to lowercase."""
        return v.lower() if v else v


class ReportedFinancialsData(Data):
    """Reported Financials Data."""

    period_ending: dateType = Field(
        description="The ending date of the reporting period."
    )
    fiscal_period: str = Field(
        description="The fiscal period of the report (e.g. FY, Q1, etc.)."
    )
    fiscal_year: int | None = Field(
        description="The fiscal year of the fiscal period.", default=None
    )

    @model_validator(mode="before")
    @classmethod
    def replace_zero(cls, values):  # pylint: disable=no-self-argument
        """Check for zero values and replace with None."""
        return (
            {k: None if v == 0 else v for k, v in values.items()}
            if isinstance(values, dict)
            else values
        )

```



---

## High-Level Overview

This is a **python** file named `reported_financials.py`.

**Python Module**

- **Classes** (2): ReportedFinancialsQueryParams, ReportedFinancialsData
- **Functions** (3): to_upper, to_lower, replace_zero
- **Import Statements**: 2


---

## Detailed Analysis

### Python Code Structure

#### Classes

- **`ReportedFinancialsQueryParams`**(QueryParams)
- **`ReportedFinancialsData`**(Data)

#### Functions

- **`to_upper(cls, v: str)`**
- **`replace_zero(cls, values)`**

#### Decorators Used

classmethod, field_validator, model_validator


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

**Generated**: 2025-11-19T02:16:46.555362Z
**Generator**: World's Best Repo Book Generator v1.0

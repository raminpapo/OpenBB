# Documentation: openbb_platform/core/openbb_core/provider/standard_models/executive_compensation.py

## File Metadata
- **Path**: `openbb_platform/core/openbb_core/provider/standard_models/executive_compensation.py`
- **Size**: 2,019 characters, 50 lines
- **Words**: 194
- **Extension**: .py
- **Classification**: Text file

## Original Source

```python
"""Executive Compensation Standard Model."""

from datetime import date as dateType

from openbb_core.provider.abstract.data import Data
from openbb_core.provider.abstract.query_params import QueryParams
from openbb_core.provider.utils.descriptions import (
    DATA_DESCRIPTIONS,
    QUERY_DESCRIPTIONS,
)
from pydantic import Field, field_validator


class ExecutiveCompensationQueryParams(QueryParams):
    """Executive Compensation Query."""

    symbol: str = Field(description=QUERY_DESCRIPTIONS.get("symbol", ""))

    @field_validator("symbol", mode="before", check_fields=False)
    @classmethod
    def to_upper(cls, v: str) -> str:
        """Convert field to uppercase."""
        return v.upper()


class ExecutiveCompensationData(Data):
    """Executive Compensation Data."""

    symbol: str = Field(description=DATA_DESCRIPTIONS.get("symbol", ""))
    cik: str | None = Field(default=None, description=DATA_DESCRIPTIONS.get("cik", ""))
    report_date: dateType | None = Field(
        default=None, description="Date of reported compensation."
    )
    company_name: str | None = Field(
        default=None, description="The name of the company."
    )
    executive: str | None = Field(default=None, description="Name and position.")
    year: int | None = Field(default=None, description="Year of the compensation.")
    salary: int | float | None = Field(default=None, description="Base salary.")
    bonus: int | float | None = Field(default=None, description="Bonus payments.")
    stock_award: int | float | None = Field(default=None, description="Stock awards.")
    option_award: int | float | None = Field(default=None, description="Option awards.")
    incentive_plan_compensation: int | float | None = Field(
        default=None, description="Incentive plan compensation."
    )
    all_other_compensation: int | float | None = Field(
        default=None, description="All other compensation."
    )
    total: int | float | None = Field(default=None, description="Total compensation.")

```

## High-Level Overview

Executive Compensation Standard Model.

from datetime import date as dateType

from openbb_core.provider.abstract.data import Data
from openbb_core.provider.abstract.query_params import QueryParams
from openbb_core.provider.utils.descriptions import (
DATA_DESCRIPTIONS,
QUERY_DESCRIPTIONS,
)
from pydantic import Field, field_validator


class ExecutiveCompensationQueryParams(QueryParams):
Executive Compensation Query.
Convert field to uppercase.
return v.upper()


class ExecutiveCompensationData(Data):

## Detailed Structure

### Python File Structure

**Classes** (2):
`ExecutiveCompensationQueryParams`, `ExecutiveCompensationData`

**Functions** (1):
`to_upper`

**Imports** (9):
`datetime`, `date`, `openbb_core.provider.abstract.data`, `Data`, `openbb_core.provider.abstract.query_params`, `QueryParams`, `openbb_core.provider.utils.descriptions`, `pydantic`, `Field`


## Key Components

**Class `ExecutiveCompensationQueryParams`**: Executive Compensation Query.

**Class `ExecutiveCompensationData`**: Executive Compensation Data.

## Usage & Examples

See source code for usage details.

## Related Files

- `datetime`
- `openbb_core.provider.abstract.data`
- `openbb_core.provider.abstract.query_params`
- `openbb_core.provider.utils.descriptions`
- `pydantic`

## Notes
- Generated: 2025-11-18T07:54:35.625732
- Generator: World's Best Repo Book Generator v1.0.0

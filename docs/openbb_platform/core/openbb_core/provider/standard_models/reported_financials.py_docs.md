# Documentation: openbb_platform/core/openbb_core/provider/standard_models/reported_financials.py

## File Metadata
- **Path**: `openbb_platform/core/openbb_core/provider/standard_models/reported_financials.py`
- **Size**: 2,295 characters, 69 lines
- **Words**: 230
- **Extension**: .py
- **Classification**: Text file

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

## High-Level Overview

Reported Financials.

from datetime import date as dateType

from openbb_core.provider.abstract.data import Data
from openbb_core.provider.abstract.query_params import QueryParams
from openbb_core.provider.utils.descriptions import (
QUERY_DESCRIPTIONS,
)
from pydantic import Field, field_validator, model_validator


class ReportedFinancialsQueryParams(QueryParams):
Reported Financials Query Params.
Convert field to uppercase.
return v.upper()

@field_validator("period", "statement_type", mode="before", check_fields=False)
@classmethod
def to_lower(cls, v: str | None) -> str | None:

## Detailed Structure

### Python File Structure

**Classes** (2):
`ReportedFinancialsQueryParams`, `ReportedFinancialsData`

**Functions** (3):
`to_upper`, `to_lower`, `replace_zero`

**Imports** (9):
`datetime`, `date`, `openbb_core.provider.abstract.data`, `Data`, `openbb_core.provider.abstract.query_params`, `QueryParams`, `openbb_core.provider.utils.descriptions`, `pydantic`, `Field`


## Key Components

**Class `ReportedFinancialsQueryParams`**: Reported Financials Query Params.

**Class `ReportedFinancialsData`**: Reported Financials Data.

## Usage & Examples

See source code for usage details.

## Related Files

- `datetime`
- `openbb_core.provider.abstract.data`
- `openbb_core.provider.abstract.query_params`
- `openbb_core.provider.utils.descriptions`
- `pydantic`

## Notes
- Generated: 2025-11-18T07:54:35.722719
- Generator: World's Best Repo Book Generator v1.0.0

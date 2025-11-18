# Documentation: openbb_platform/core/openbb_core/provider/standard_models/forward_ebitda_estimates.py

## File Metadata
- **Path**: `openbb_platform/core/openbb_core/provider/standard_models/forward_ebitda_estimates.py`
- **Size**: 2,523 characters, 74 lines
- **Words**: 261
- **Extension**: .py
- **Classification**: Text file

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

## High-Level Overview

Forward EBITDA Estimates Standard Model.

from datetime import date as dateType

from openbb_core.provider.abstract.data import Data, ForceInt
from openbb_core.provider.abstract.query_params import QueryParams
from openbb_core.provider.utils.descriptions import (
DATA_DESCRIPTIONS,
QUERY_DESCRIPTIONS,
)
from pydantic import Field, field_validator


class ForwardEbitdaEstimatesQueryParams(QueryParams):
Forward EBITDA Estimates Query Parameters.
Convert field to uppercase.
return v.upper() if v else None


class ForwardEbitdaEstimatesData(Data):

## Detailed Structure

### Python File Structure

**Classes** (2):
`ForwardEbitdaEstimatesQueryParams`, `ForwardEbitdaEstimatesData`

**Functions** (1):
`to_upper`

**Imports** (9):
`datetime`, `date`, `openbb_core.provider.abstract.data`, `Data`, `openbb_core.provider.abstract.query_params`, `QueryParams`, `openbb_core.provider.utils.descriptions`, `pydantic`, `Field`


## Key Components

**Class `ForwardEbitdaEstimatesQueryParams`**: Forward EBITDA Estimates Query Parameters.

**Class `ForwardEbitdaEstimatesData`**: Forward EBITDA Estimates Data.

## Usage & Examples

See source code for usage details.

## Related Files

- `datetime`
- `openbb_core.provider.abstract.data`
- `openbb_core.provider.abstract.query_params`
- `openbb_core.provider.utils.descriptions`
- `pydantic`

## Notes
- Generated: 2025-11-18T07:54:35.636854
- Generator: World's Best Repo Book Generator v1.0.0

# Documentation: openbb_platform/core/openbb_core/provider/standard_models/country_interest_rates.py

## File Metadata
- **Path**: `openbb_platform/core/openbb_core/provider/standard_models/country_interest_rates.py`
- **Size**: 1,265 characters, 42 lines
- **Words**: 102
- **Extension**: .py
- **Classification**: Text file

## Original Source

```python
"""Country Interest Rates Standard Model."""

from datetime import date as dateType

from openbb_core.provider.abstract.data import Data
from openbb_core.provider.abstract.query_params import QueryParams
from openbb_core.provider.utils.descriptions import (
    DATA_DESCRIPTIONS,
    QUERY_DESCRIPTIONS,
)
from pydantic import Field


class CountryInterestRatesQueryParams(QueryParams):
    """Country Interest Rates Query."""

    country: str = Field(
        default="united_states",
        description=QUERY_DESCRIPTIONS.get("country"),
    )
    start_date: dateType | None = Field(
        default=None, description=QUERY_DESCRIPTIONS.get("start_date")
    )
    end_date: dateType | None = Field(
        default=None, description=QUERY_DESCRIPTIONS.get("end_date")
    )


class CountryInterestRatesData(Data):
    """Country Interest Rates Data."""

    date: dateType = Field(default=None, description=DATA_DESCRIPTIONS.get("date"))
    value: float = Field(
        default=None,
        description="The interest rate value.",
        json_schema_extra={"x-unit_measurment": "percent", "x-frontend_multiply": 100},
    )
    country: str | None = Field(
        default=None,
        description="Country for which the interest rate is given.",
    )

```

## High-Level Overview

Country Interest Rates Standard Model.

from datetime import date as dateType

from openbb_core.provider.abstract.data import Data
from openbb_core.provider.abstract.query_params import QueryParams
from openbb_core.provider.utils.descriptions import (
DATA_DESCRIPTIONS,
QUERY_DESCRIPTIONS,
)
from pydantic import Field


class CountryInterestRatesQueryParams(QueryParams):
Country Interest Rates Query.
Country Interest Rates Data.

date: dateType = Field(default=None, description=DATA_DESCRIPTIONS.get("date"))
value: float = Field(
default=None,

## Detailed Structure

### Python File Structure

**Classes** (2):
`CountryInterestRatesQueryParams`, `CountryInterestRatesData`

**Functions** (0):
None

**Imports** (9):
`datetime`, `date`, `openbb_core.provider.abstract.data`, `Data`, `openbb_core.provider.abstract.query_params`, `QueryParams`, `openbb_core.provider.utils.descriptions`, `pydantic`, `Field`


## Key Components

**Class `CountryInterestRatesQueryParams`**: Country Interest Rates Query.

**Class `CountryInterestRatesData`**: Country Interest Rates Data.

## Usage & Examples

See source code for usage details.

## Related Files

- `datetime`
- `openbb_core.provider.abstract.data`
- `openbb_core.provider.abstract.query_params`
- `openbb_core.provider.utils.descriptions`
- `pydantic`

## Notes
- Generated: 2025-11-18T07:54:35.569601
- Generator: World's Best Repo Book Generator v1.0.0

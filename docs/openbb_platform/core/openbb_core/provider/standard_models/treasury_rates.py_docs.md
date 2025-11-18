# Documentation: openbb_platform/core/openbb_core/provider/standard_models/treasury_rates.py

## File Metadata
- **Path**: `openbb_platform/core/openbb_core/provider/standard_models/treasury_rates.py`
- **Size**: 3,452 characters, 96 lines
- **Words**: 287
- **Extension**: .py
- **Classification**: Text file

## Original Source

```python
"""Treasury Rates Standard Model."""

from datetime import date as dateType

from openbb_core.provider.abstract.data import Data
from openbb_core.provider.abstract.query_params import QueryParams
from openbb_core.provider.utils.descriptions import (
    DATA_DESCRIPTIONS,
    QUERY_DESCRIPTIONS,
)
from pydantic import Field


class TreasuryRatesQueryParams(QueryParams):
    """Treasury Rates Query."""

    start_date: dateType | None = Field(
        default=None,
        description=QUERY_DESCRIPTIONS.get("start_date", ""),
    )
    end_date: dateType | None = Field(
        default=None,
        description=QUERY_DESCRIPTIONS.get("end_date", ""),
    )


class TreasuryRatesData(Data):
    """Treasury Rates Data. All fields are expressed as a normalized percent - 1% = 0.01."""

    date: dateType = Field(description=DATA_DESCRIPTIONS.get("date", ""))
    week_4: float | None = Field(
        default=None,
        description="4 week Treasury bills rate (secondary market).",
        json_schema_extra={"x-unit_measurement": "percent", "x-frontend_multiply": 100},
    )
    month_1: float | None = Field(
        description="1 month Treasury rate.",
        default=None,
        json_schema_extra={"x-unit_measurement": "percent", "x-frontend_multiply": 100},
    )
    month_2: float | None = Field(
        description="2 month Treasury rate.",
        default=None,
        json_schema_extra={"x-unit_measurement": "percent", "x-frontend_multiply": 100},
    )
    month_3: float | None = Field(
        description="3 month Treasury rate.",
        default=None,
        json_schema_extra={"x-unit_measurement": "percent", "x-frontend_multiply": 100},
    )
    month_6: float | None = Field(
        description="6 month Treasury rate.",
        default=None,
        json_schema_extra={"x-unit_measurement": "percent", "x-frontend_multiply": 100},
    )
    year_1: float | None = Field(
        description="1 year Treasury rate.",
        default=None,
        json_schema_extra={"x-unit_measurement": "percent", "x-frontend_multiply": 100},
    )
    year_2: float | None = Field(
        description="2 year Treasury rate.",
        default=None,
        json_schema_extra={"x-unit_measurement": "percent", "x-frontend_multiply": 100},
    )
    year_3: float | None = Field(
        description="3 year Treasury rate.",
        default=None,
        json_schema_extra={"x-unit_measurement": "percent", "x-frontend_multiply": 100},
    )
    year_5: float | None = Field(
        description="5 year Treasury rate.",
        default=None,
        json_schema_extra={"x-unit_measurement": "percent", "x-frontend_multiply": 100},
    )
    year_7: float | None = Field(
        description="7 year Treasury rate.",
        default=None,
        json_schema_extra={"x-unit_measurement": "percent", "x-frontend_multiply": 100},
    )
    year_10: float | None = Field(
        description="10 year Treasury rate.",
        default=None,
        json_schema_extra={"x-unit_measurement": "percent", "x-frontend_multiply": 100},
    )
    year_20: float | None = Field(
        description="20 year Treasury rate.",
        default=None,
        json_schema_extra={"x-unit_measurement": "percent", "x-frontend_multiply": 100},
    )
    year_30: float | None = Field(
        description="30 year Treasury rate.",
        default=None,
        json_schema_extra={"x-unit_measurement": "percent", "x-frontend_multiply": 100},
    )

```

## High-Level Overview

Treasury Rates Standard Model.

from datetime import date as dateType

from openbb_core.provider.abstract.data import Data
from openbb_core.provider.abstract.query_params import QueryParams
from openbb_core.provider.utils.descriptions import (
DATA_DESCRIPTIONS,
QUERY_DESCRIPTIONS,
)
from pydantic import Field


class TreasuryRatesQueryParams(QueryParams):
Treasury Rates Query.
Treasury Rates Data. All fields are expressed as a normalized percent - 1% = 0.01.

date: dateType = Field(description=DATA_DESCRIPTIONS.get("date", ""))
week_4: float | None = Field(
default=None,

## Detailed Structure

### Python File Structure

**Classes** (2):
`TreasuryRatesQueryParams`, `TreasuryRatesData`

**Functions** (0):
None

**Imports** (9):
`datetime`, `date`, `openbb_core.provider.abstract.data`, `Data`, `openbb_core.provider.abstract.query_params`, `QueryParams`, `openbb_core.provider.utils.descriptions`, `pydantic`, `Field`


## Key Components

**Class `TreasuryRatesQueryParams`**: Treasury Rates Query.

**Class `TreasuryRatesData`**: Treasury Rates Data. All fields are expressed as a normalized percent - 1% = 0.01.

## Usage & Examples

See source code for usage details.

## Related Files

- `datetime`
- `openbb_core.provider.abstract.data`
- `openbb_core.provider.abstract.query_params`
- `openbb_core.provider.utils.descriptions`
- `pydantic`

## Notes
- Generated: 2025-11-18T07:54:35.758638
- Generator: World's Best Repo Book Generator v1.0.0

# Documentation: openbb_platform/core/openbb_core/provider/standard_models/euro_short_term_rate.py

## File Metadata
- **Path**: `openbb_platform/core/openbb_core/provider/standard_models/euro_short_term_rate.py`
- **Size**: 2,197 characters, 66 lines
- **Words**: 186
- **Extension**: .py
- **Classification**: Text file

## Original Source

```python
"""Euro Short Term Rate Standard Model."""

from datetime import date as dateType

from openbb_core.provider.abstract.data import Data
from openbb_core.provider.abstract.query_params import QueryParams
from openbb_core.provider.utils.descriptions import (
    DATA_DESCRIPTIONS,
    QUERY_DESCRIPTIONS,
)
from pydantic import Field


class EuroShortTermRateQueryParams(QueryParams):
    """Euro Short Term Rate Query."""

    start_date: dateType | None = Field(
        default=None,
        description=QUERY_DESCRIPTIONS.get("start_date", ""),
    )
    end_date: dateType | None = Field(
        default=None,
        description=QUERY_DESCRIPTIONS.get("end_date", ""),
    )


class EuroShortTermRateData(Data):
    """Euro Short Term Rate Data."""

    date: dateType = Field(description=DATA_DESCRIPTIONS.get("date", ""))
    rate: float = Field(
        description="Volume-weighted trimmed mean rate.",
        json_schema_extra={"x-unit_measurement": "percent", "x-frontend_multiply": 100},
    )
    percentile_25: float | None = Field(
        default=None,
        description="Rate at 25th percentile of volume.",
        json_schema_extra={"x-unit_measurement": "percent", "x-frontend_multiply": 100},
    )
    percentile_75: float | None = Field(
        default=None,
        description="Rate at 75th percentile of volume.",
        json_schema_extra={"x-unit_measurement": "percent", "x-frontend_multiply": 100},
    )
    volume: float | None = Field(
        default=None,
        description=DATA_DESCRIPTIONS.get("volume", "") + " (Millions of €EUR).",
        json_schema_extra={
            "x-unit_measurement": "currency",
            "x-frontend_multiply": 1e6,
        },
    )
    transactions: int | None = Field(
        default=None,
        description="Number of transactions.",
    )
    number_of_banks: int | None = Field(
        default=None,
        description="Number of active banks.",
    )
    large_bank_share_of_volume: float | None = Field(
        default=None,
        description="The percent of volume attributable to the 5 largest active banks.",
        json_schema_extra={"x-unit_measurement": "percent", "x-frontend_multiply": 100},
    )

```

## High-Level Overview

Euro Short Term Rate Standard Model.

from datetime import date as dateType

from openbb_core.provider.abstract.data import Data
from openbb_core.provider.abstract.query_params import QueryParams
from openbb_core.provider.utils.descriptions import (
DATA_DESCRIPTIONS,
QUERY_DESCRIPTIONS,
)
from pydantic import Field


class EuroShortTermRateQueryParams(QueryParams):
Euro Short Term Rate Query.
Euro Short Term Rate Data.

date: dateType = Field(description=DATA_DESCRIPTIONS.get("date", ""))
rate: float = Field(
description="Volume-weighted trimmed mean rate.",

## Detailed Structure

### Python File Structure

**Classes** (2):
`EuroShortTermRateQueryParams`, `EuroShortTermRateData`

**Functions** (0):
None

**Imports** (9):
`datetime`, `date`, `openbb_core.provider.abstract.data`, `Data`, `openbb_core.provider.abstract.query_params`, `QueryParams`, `openbb_core.provider.utils.descriptions`, `pydantic`, `Field`


## Key Components

**Class `EuroShortTermRateQueryParams`**: Euro Short Term Rate Query.

**Class `EuroShortTermRateData`**: Euro Short Term Rate Data.

## Usage & Examples

See source code for usage details.

## Related Files

- `datetime`
- `openbb_core.provider.abstract.data`
- `openbb_core.provider.abstract.query_params`
- `openbb_core.provider.utils.descriptions`
- `pydantic`

## Notes
- Generated: 2025-11-18T07:54:35.624389
- Generator: World's Best Repo Book Generator v1.0.0

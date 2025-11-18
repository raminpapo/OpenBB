# Documentation: openbb_platform/core/openbb_core/provider/standard_models/revenue_geographic.py

## File Metadata
- **Path**: `openbb_platform/core/openbb_core/provider/standard_models/revenue_geographic.py`
- **Size**: 1,512 characters, 44 lines
- **Words**: 147
- **Extension**: .py
- **Classification**: Text file

## Original Source

```python
"""Revenue by Geographic Segments Standard Model."""

from datetime import date as dateType

from openbb_core.provider.abstract.data import Data
from openbb_core.provider.abstract.query_params import QueryParams
from openbb_core.provider.utils.descriptions import QUERY_DESCRIPTIONS
from pydantic import Field, field_validator


class RevenueGeographicQueryParams(QueryParams):
    """Revenue by Geographic Segments Query."""

    symbol: str = Field(description=QUERY_DESCRIPTIONS.get("symbol", ""))

    @field_validator("symbol", mode="before", check_fields=False)
    @classmethod
    def to_upper(cls, v: str):
        """Convert field to uppercase."""
        return v.upper()


class RevenueGeographicData(Data):
    """Revenue by Geographic Segments Data."""

    period_ending: dateType = Field(description="The end date of the reporting period.")
    fiscal_period: str | None = Field(
        default=None, description="The fiscal period of the reporting period."
    )
    fiscal_year: int | None = Field(
        default=None, description="The fiscal year of the reporting period."
    )
    filing_date: dateType | None = Field(
        default=None, description="The filing date of the report."
    )
    region: str | None = Field(
        default=None,
        description="The region represented by the revenue data.",
    )
    revenue: int | float = Field(
        description="The total revenue attributed to the region.",
        json_schema_extra={"x-unit_measurement": "currency"},
    )

```

## High-Level Overview

Revenue by Geographic Segments Standard Model.

from datetime import date as dateType

from openbb_core.provider.abstract.data import Data
from openbb_core.provider.abstract.query_params import QueryParams
from openbb_core.provider.utils.descriptions import QUERY_DESCRIPTIONS
from pydantic import Field, field_validator


class RevenueGeographicQueryParams(QueryParams):
Revenue by Geographic Segments Query.
Convert field to uppercase.
return v.upper()


class RevenueGeographicData(Data):
Revenue by Geographic Segments Data.

## Detailed Structure

### Python File Structure

**Classes** (2):
`RevenueGeographicQueryParams`, `RevenueGeographicData`

**Functions** (1):
`to_upper`

**Imports** (10):
`datetime`, `date`, `openbb_core.provider.abstract.data`, `Data`, `openbb_core.provider.abstract.query_params`, `QueryParams`, `openbb_core.provider.utils.descriptions`, `QUERY_DESCRIPTIONS`, `pydantic`, `Field`


## Key Components

**Class `RevenueGeographicQueryParams`**: Revenue by Geographic Segments Query.

**Class `RevenueGeographicData`**: Revenue by Geographic Segments Data.

## Usage & Examples

See source code for usage details.

## Related Files

- `datetime`
- `openbb_core.provider.abstract.data`
- `openbb_core.provider.abstract.query_params`
- `openbb_core.provider.utils.descriptions`
- `pydantic`

## Notes
- Generated: 2025-11-18T07:54:35.726632
- Generator: World's Best Repo Book Generator v1.0.0

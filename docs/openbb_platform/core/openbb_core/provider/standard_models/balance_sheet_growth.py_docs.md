# Documentation: openbb_platform/core/openbb_core/provider/standard_models/balance_sheet_growth.py

## File Metadata
- **Path**: `openbb_platform/core/openbb_core/provider/standard_models/balance_sheet_growth.py`
- **Size**: 1,197 characters, 36 lines
- **Words**: 111
- **Extension**: .py
- **Classification**: Text file

## Original Source

```python
"""Balance Sheet Statement Growth Standard Model."""

from datetime import date as dateType

from openbb_core.provider.abstract.data import Data
from openbb_core.provider.abstract.query_params import QueryParams
from openbb_core.provider.utils.descriptions import QUERY_DESCRIPTIONS
from pydantic import Field, field_validator


class BalanceSheetGrowthQueryParams(QueryParams):
    """Balance Sheet Statement Growth Query."""

    symbol: str = Field(description=QUERY_DESCRIPTIONS.get("symbol", ""))
    limit: int | None = Field(
        default=None, description=QUERY_DESCRIPTIONS.get("limit", "")
    )

    @field_validator("symbol", mode="before", check_fields=False)
    @classmethod
    def to_upper(cls, v: str):
        """Convert field to uppercase."""
        return v.upper()


class BalanceSheetGrowthData(Data):
    """Balance Sheet Statement Growth Data."""

    period_ending: dateType = Field(description="The end date of the reporting period.")
    fiscal_period: str | None = Field(
        description="The fiscal period of the report.", default=None
    )
    fiscal_year: int | None = Field(
        description="The fiscal year of the fiscal period.", default=None
    )

```

## High-Level Overview

Balance Sheet Statement Growth Standard Model.

from datetime import date as dateType

from openbb_core.provider.abstract.data import Data
from openbb_core.provider.abstract.query_params import QueryParams
from openbb_core.provider.utils.descriptions import QUERY_DESCRIPTIONS
from pydantic import Field, field_validator


class BalanceSheetGrowthQueryParams(QueryParams):
Balance Sheet Statement Growth Query.
Convert field to uppercase.
return v.upper()


class BalanceSheetGrowthData(Data):
Balance Sheet Statement Growth Data.

## Detailed Structure

### Python File Structure

**Classes** (2):
`BalanceSheetGrowthQueryParams`, `BalanceSheetGrowthData`

**Functions** (1):
`to_upper`

**Imports** (10):
`datetime`, `date`, `openbb_core.provider.abstract.data`, `Data`, `openbb_core.provider.abstract.query_params`, `QueryParams`, `openbb_core.provider.utils.descriptions`, `QUERY_DESCRIPTIONS`, `pydantic`, `Field`


## Key Components

**Class `BalanceSheetGrowthQueryParams`**: Balance Sheet Statement Growth Query.

**Class `BalanceSheetGrowthData`**: Balance Sheet Statement Growth Data.

## Usage & Examples

See source code for usage details.

## Related Files

- `datetime`
- `openbb_core.provider.abstract.data`
- `openbb_core.provider.abstract.query_params`
- `openbb_core.provider.utils.descriptions`
- `pydantic`

## Notes
- Generated: 2025-11-18T07:54:35.534493
- Generator: World's Best Repo Book Generator v1.0.0

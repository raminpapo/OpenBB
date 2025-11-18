# Documentation: openbb_platform/core/openbb_core/provider/standard_models/balance_sheet.py

## File Metadata
- **Path**: `openbb_platform/core/openbb_core/provider/standard_models/balance_sheet.py`
- **Size**: 1,170 characters, 38 lines
- **Words**: 108
- **Extension**: .py
- **Classification**: Text file

## Original Source

```python
"""Balance Sheet Standard Model."""

from datetime import date as dateType

from openbb_core.provider.abstract.data import Data
from openbb_core.provider.abstract.query_params import QueryParams
from openbb_core.provider.utils.descriptions import (
    QUERY_DESCRIPTIONS,
)
from pydantic import Field, NonNegativeInt, field_validator


class BalanceSheetQueryParams(QueryParams):
    """Balance Sheet Query."""

    symbol: str = Field(description=QUERY_DESCRIPTIONS.get("symbol", ""))
    limit: NonNegativeInt | None = Field(
        default=None, description=QUERY_DESCRIPTIONS.get("limit", "")
    )

    @field_validator("symbol", mode="before", check_fields=False)
    @classmethod
    def to_upper(cls, v: str):
        """Convert field to uppercase."""
        return v.upper()


class BalanceSheetData(Data):
    """Balance Sheet Data."""

    period_ending: dateType = Field(description="The end date of the reporting period.")
    fiscal_period: str | None = Field(
        description="The fiscal period of the report.", default=None
    )
    fiscal_year: int | None = Field(
        description="The fiscal year of the fiscal period.", default=None
    )

```

## High-Level Overview

Balance Sheet Standard Model.

from datetime import date as dateType

from openbb_core.provider.abstract.data import Data
from openbb_core.provider.abstract.query_params import QueryParams
from openbb_core.provider.utils.descriptions import (
QUERY_DESCRIPTIONS,
)
from pydantic import Field, NonNegativeInt, field_validator


class BalanceSheetQueryParams(QueryParams):
Balance Sheet Query.
Convert field to uppercase.
return v.upper()


class BalanceSheetData(Data):
Balance Sheet Data.

## Detailed Structure

### Python File Structure

**Classes** (2):
`BalanceSheetQueryParams`, `BalanceSheetData`

**Functions** (1):
`to_upper`

**Imports** (9):
`datetime`, `date`, `openbb_core.provider.abstract.data`, `Data`, `openbb_core.provider.abstract.query_params`, `QueryParams`, `openbb_core.provider.utils.descriptions`, `pydantic`, `Field`


## Key Components

**Class `BalanceSheetQueryParams`**: Balance Sheet Query.

**Class `BalanceSheetData`**: Balance Sheet Data.

## Usage & Examples

See source code for usage details.

## Related Files

- `datetime`
- `openbb_core.provider.abstract.data`
- `openbb_core.provider.abstract.query_params`
- `openbb_core.provider.utils.descriptions`
- `pydantic`

## Notes
- Generated: 2025-11-18T07:54:35.533218
- Generator: World's Best Repo Book Generator v1.0.0

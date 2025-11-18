# Documentation: openbb_platform/core/openbb_core/provider/standard_models/historical_employees.py

## File Metadata
- **Path**: `openbb_platform/core/openbb_core/provider/standard_models/historical_employees.py`
- **Size**: 1,275 characters, 40 lines
- **Words**: 103
- **Extension**: .py
- **Classification**: Text file

## Original Source

```python
"""Historical Employees Standard Model."""

from datetime import date as dateType

from openbb_core.provider.abstract.data import Data
from openbb_core.provider.abstract.query_params import QueryParams
from openbb_core.provider.utils.descriptions import (
    DATA_DESCRIPTIONS,
    QUERY_DESCRIPTIONS,
)
from pydantic import Field, field_validator


class HistoricalEmployeesQueryParams(QueryParams):
    """Historical Employees Query."""

    symbol: str = Field(description=QUERY_DESCRIPTIONS.get("symbol", ""))
    start_date: dateType | None = Field(
        default=None, description=QUERY_DESCRIPTIONS.get("start_date", "")
    )
    end_date: dateType | None = Field(
        default=None, description=QUERY_DESCRIPTIONS.get("end_date", "")
    )

    @field_validator("symbol", mode="before", check_fields=False)
    @classmethod
    def to_upper(cls, v: str) -> str:
        """Convert field to uppercase."""
        return v.upper()


class HistoricalEmployeesData(Data):
    """Historical Employees Data."""

    date: dateType = Field(description=DATA_DESCRIPTIONS.get("date", ""))
    symbol: str | None = Field(
        default=None, description=DATA_DESCRIPTIONS.get("symbol", "")
    )
    employees: int = Field(description="Reported number of employees.")

```

## High-Level Overview

Historical Employees Standard Model.

from datetime import date as dateType

from openbb_core.provider.abstract.data import Data
from openbb_core.provider.abstract.query_params import QueryParams
from openbb_core.provider.utils.descriptions import (
DATA_DESCRIPTIONS,
QUERY_DESCRIPTIONS,
)
from pydantic import Field, field_validator


class HistoricalEmployeesQueryParams(QueryParams):
Historical Employees Query.
Convert field to uppercase.
return v.upper()


class HistoricalEmployeesData(Data):

## Detailed Structure

### Python File Structure

**Classes** (2):
`HistoricalEmployeesQueryParams`, `HistoricalEmployeesData`

**Functions** (1):
`to_upper`

**Imports** (9):
`datetime`, `date`, `openbb_core.provider.abstract.data`, `Data`, `openbb_core.provider.abstract.query_params`, `QueryParams`, `openbb_core.provider.utils.descriptions`, `pydantic`, `Field`


## Key Components

**Class `HistoricalEmployeesQueryParams`**: Historical Employees Query.

**Class `HistoricalEmployeesData`**: Historical Employees Data.

## Usage & Examples

See source code for usage details.

## Related Files

- `datetime`
- `openbb_core.provider.abstract.data`
- `openbb_core.provider.abstract.query_params`
- `openbb_core.provider.utils.descriptions`
- `pydantic`

## Notes
- Generated: 2025-11-18T07:54:35.662781
- Generator: World's Best Repo Book Generator v1.0.0

# Documentation: openbb_platform/core/openbb_core/provider/standard_models/non_farm_payrolls.py

## File Metadata
- **Path**: `openbb_platform/core/openbb_core/provider/standard_models/non_farm_payrolls.py`
- **Size**: 869 characters, 30 lines
- **Words**: 73
- **Extension**: .py
- **Classification**: Text file

## Original Source

```python
"""NonFarm Payrolls Standard Model."""

from datetime import date as dateType

from openbb_core.provider.abstract.data import Data
from openbb_core.provider.abstract.query_params import QueryParams
from openbb_core.provider.utils.descriptions import (
    DATA_DESCRIPTIONS,
    QUERY_DESCRIPTIONS,
)
from pydantic import Field


class NonFarmPayrollsQueryParams(QueryParams):
    """NonFarm Payrolls Query."""

    date: dateType | str | None = Field(
        default=None,
        description=QUERY_DESCRIPTIONS.get("date", "")
        + " Default is the latest report.",
    )


class NonFarmPayrollsData(Data):
    """NonFarm Payrolls Data."""

    date: dateType = Field(description=DATA_DESCRIPTIONS.get("date", ""))
    symbol: str = Field(description=DATA_DESCRIPTIONS.get("symbol", ""))
    value: float = Field(description=DATA_DESCRIPTIONS.get("value", ""))

```

## High-Level Overview

NonFarm Payrolls Standard Model.

from datetime import date as dateType

from openbb_core.provider.abstract.data import Data
from openbb_core.provider.abstract.query_params import QueryParams
from openbb_core.provider.utils.descriptions import (
DATA_DESCRIPTIONS,
QUERY_DESCRIPTIONS,
)
from pydantic import Field


class NonFarmPayrollsQueryParams(QueryParams):
NonFarm Payrolls Query.
NonFarm Payrolls Data.

date: dateType = Field(description=DATA_DESCRIPTIONS.get("date", ""))
symbol: str = Field(description=DATA_DESCRIPTIONS.get("symbol", ""))
value: float = Field(description=DATA_DESCRIPTIONS.get("value", ""))

## Detailed Structure

### Python File Structure

**Classes** (2):
`NonFarmPayrollsQueryParams`, `NonFarmPayrollsData`

**Functions** (0):
None

**Imports** (9):
`datetime`, `date`, `openbb_core.provider.abstract.data`, `Data`, `openbb_core.provider.abstract.query_params`, `QueryParams`, `openbb_core.provider.utils.descriptions`, `pydantic`, `Field`


## Key Components

**Class `NonFarmPayrollsQueryParams`**: NonFarm Payrolls Query.

**Class `NonFarmPayrollsData`**: NonFarm Payrolls Data.

## Usage & Examples

See source code for usage details.

## Related Files

- `datetime`
- `openbb_core.provider.abstract.data`
- `openbb_core.provider.abstract.query_params`
- `openbb_core.provider.utils.descriptions`
- `pydantic`

## Notes
- Generated: 2025-11-18T07:54:35.701739
- Generator: World's Best Repo Book Generator v1.0.0

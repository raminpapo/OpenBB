# Documentation: openbb_platform/core/openbb_core/provider/standard_models/economic_indicators.py

## File Metadata
- **Path**: `openbb_platform/core/openbb_core/provider/standard_models/economic_indicators.py`
- **Size**: 1,458 characters, 46 lines
- **Words**: 136
- **Extension**: .py
- **Classification**: Text file

## Original Source

```python
"""Economic Indicators Standard Model."""

from datetime import date as dateType

from openbb_core.provider.abstract.data import Data
from openbb_core.provider.abstract.query_params import QueryParams
from openbb_core.provider.utils.descriptions import (
    DATA_DESCRIPTIONS,
    QUERY_DESCRIPTIONS,
)
from pydantic import Field


class EconomicIndicatorsQueryParams(QueryParams):
    """Economic Indicators Query."""

    country: str | None = Field(
        default=None,
        description=QUERY_DESCRIPTIONS.get("country", "")
        + " The country represented by the indicator, if available.",
    )
    start_date: dateType | None = Field(
        description=QUERY_DESCRIPTIONS.get("start_date", ""), default=None
    )
    end_date: dateType | None = Field(
        description=QUERY_DESCRIPTIONS.get("end_date", ""), default=None
    )


class EconomicIndicatorsData(Data):
    """Economic Indicators Data."""

    date: dateType = Field(description=DATA_DESCRIPTIONS.get("date", ""))
    symbol_root: str | None = Field(
        default=None, description="The root symbol for the indicator (e.g. GDP)."
    )
    symbol: str | None = Field(
        default=None, description=DATA_DESCRIPTIONS.get("symbol", "")
    )
    country: str | None = Field(
        default=None, description="The country represented by the data."
    )
    value: int | float | None = Field(
        default=None, description=DATA_DESCRIPTIONS.get("value", "")
    )

```

## High-Level Overview

Economic Indicators Standard Model.

from datetime import date as dateType

from openbb_core.provider.abstract.data import Data
from openbb_core.provider.abstract.query_params import QueryParams
from openbb_core.provider.utils.descriptions import (
DATA_DESCRIPTIONS,
QUERY_DESCRIPTIONS,
)
from pydantic import Field


class EconomicIndicatorsQueryParams(QueryParams):
Economic Indicators Query.
Economic Indicators Data.

date: dateType = Field(description=DATA_DESCRIPTIONS.get("date", ""))
symbol_root: str | None = Field(
default=None, description="The root symbol for the indicator (e.g. GDP)."

## Detailed Structure

### Python File Structure

**Classes** (2):
`EconomicIndicatorsQueryParams`, `EconomicIndicatorsData`

**Functions** (0):
None

**Imports** (9):
`datetime`, `date`, `openbb_core.provider.abstract.data`, `Data`, `openbb_core.provider.abstract.query_params`, `QueryParams`, `openbb_core.provider.utils.descriptions`, `pydantic`, `Field`


## Key Components

**Class `EconomicIndicatorsQueryParams`**: Economic Indicators Query.

**Class `EconomicIndicatorsData`**: Economic Indicators Data.

## Usage & Examples

See source code for usage details.

## Related Files

- `datetime`
- `openbb_core.provider.abstract.data`
- `openbb_core.provider.abstract.query_params`
- `openbb_core.provider.utils.descriptions`
- `pydantic`

## Notes
- Generated: 2025-11-18T07:54:35.589422
- Generator: World's Best Repo Book Generator v1.0.0

# Documentation: openbb_platform/core/openbb_core/provider/standard_models/house_price_index.py

## File Metadata
- **Path**: `openbb_platform/core/openbb_core/provider/standard_models/house_price_index.py`
- **Size**: 1,744 characters, 55 lines
- **Words**: 150
- **Extension**: .py
- **Classification**: Text file

## Original Source

```python
"""House Price Index Standard Model."""

from datetime import date as dateType
from typing import Literal

from openbb_core.provider.abstract.data import Data
from openbb_core.provider.abstract.query_params import QueryParams
from openbb_core.provider.utils.descriptions import (
    DATA_DESCRIPTIONS,
    QUERY_DESCRIPTIONS,
)
from pydantic import Field


class HousePriceIndexQueryParams(QueryParams):
    """House Price Index Query."""

    country: str = Field(
        description=QUERY_DESCRIPTIONS.get("country", ""),
        default="united_states",
    )
    frequency: Literal["monthly", "quarter", "annual"] = Field(
        description=QUERY_DESCRIPTIONS.get("frequency", ""),
        default="quarter",
        json_schema_extra={"choices": ["monthly", "quarter", "annual"]},
    )
    transform: Literal["index", "yoy", "period"] = Field(
        description="Transformation of the CPI data. Period represents the change since previous."
        + " Defaults to change from one year ago (yoy).",
        default="index",
        json_schema_extra={"choices": ["index", "yoy", "period"]},
    )
    start_date: dateType | None = Field(
        default=None, description=QUERY_DESCRIPTIONS.get("start_date")
    )
    end_date: dateType | None = Field(
        default=None, description=QUERY_DESCRIPTIONS.get("end_date")
    )


class HousePriceIndexData(Data):
    """House Price Index Data."""

    date: dateType | None = Field(
        default=None, description=DATA_DESCRIPTIONS.get("date")
    )
    country: str | None = Field(
        default=None,
        description=DATA_DESCRIPTIONS.get("country", ""),
    )
    value: float | None = Field(
        default=None,
        description="Share price index value.",
    )

```

## High-Level Overview

House Price Index Standard Model.

from datetime import date as dateType
from typing import Literal

from openbb_core.provider.abstract.data import Data
from openbb_core.provider.abstract.query_params import QueryParams
from openbb_core.provider.utils.descriptions import (
DATA_DESCRIPTIONS,
QUERY_DESCRIPTIONS,
)
from pydantic import Field


class HousePriceIndexQueryParams(QueryParams):
House Price Index Query.
House Price Index Data.

date: dateType | None = Field(
default=None, description=DATA_DESCRIPTIONS.get("date")

## Detailed Structure

### Python File Structure

**Classes** (2):
`HousePriceIndexQueryParams`, `HousePriceIndexData`

**Functions** (0):
None

**Imports** (12):
`datetime`, `date`, `typing`, `Literal`, `openbb_core.provider.abstract.data`, `Data`, `openbb_core.provider.abstract.query_params`, `QueryParams`, `openbb_core.provider.utils.descriptions`, `pydantic`, `Field`, `one`


## Key Components

**Class `HousePriceIndexQueryParams`**: House Price Index Query.

**Class `HousePriceIndexData`**: House Price Index Data.

## Usage & Examples

See source code for usage details.

## Related Files

- `datetime`
- `typing`
- `openbb_core.provider.abstract.data`
- `openbb_core.provider.abstract.query_params`
- `openbb_core.provider.utils.descriptions`
- `pydantic`

## Notes
- Generated: 2025-11-18T07:54:35.668067
- Generator: World's Best Repo Book Generator v1.0.0

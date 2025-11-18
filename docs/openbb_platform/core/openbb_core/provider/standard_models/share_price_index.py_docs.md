# Documentation: openbb_platform/core/openbb_core/provider/standard_models/share_price_index.py

## File Metadata
- **Path**: `openbb_platform/core/openbb_core/provider/standard_models/share_price_index.py`
- **Size**: 1,431 characters, 49 lines
- **Words**: 117
- **Extension**: .py
- **Classification**: Text file

## Original Source

```python
"""Share Price Index Standard Model."""

from datetime import date as dateType
from typing import Literal

from openbb_core.provider.abstract.data import Data
from openbb_core.provider.abstract.query_params import QueryParams
from openbb_core.provider.utils.descriptions import (
    DATA_DESCRIPTIONS,
    QUERY_DESCRIPTIONS,
)
from pydantic import Field


class SharePriceIndexQueryParams(QueryParams):
    """Share Price Index Query."""

    country: str = Field(
        description=QUERY_DESCRIPTIONS.get("country", ""),
        default="united_states",
    )
    frequency: Literal["monthly", "quarter", "annual"] = Field(
        description=QUERY_DESCRIPTIONS.get("frequency", ""),
        default="monthly",
        json_schema_extra={"choices": ["monthly", "quarter", "annual"]},
    )
    start_date: dateType | None = Field(
        default=None, description=QUERY_DESCRIPTIONS.get("start_date")
    )
    end_date: dateType | None = Field(
        default=None, description=QUERY_DESCRIPTIONS.get("end_date")
    )


class SharePriceIndexData(Data):
    """Share Price Index Data."""

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

Share Price Index Standard Model.

from datetime import date as dateType
from typing import Literal

from openbb_core.provider.abstract.data import Data
from openbb_core.provider.abstract.query_params import QueryParams
from openbb_core.provider.utils.descriptions import (
DATA_DESCRIPTIONS,
QUERY_DESCRIPTIONS,
)
from pydantic import Field


class SharePriceIndexQueryParams(QueryParams):
Share Price Index Query.
Share Price Index Data.

date: dateType | None = Field(
default=None, description=DATA_DESCRIPTIONS.get("date")

## Detailed Structure

### Python File Structure

**Classes** (2):
`SharePriceIndexQueryParams`, `SharePriceIndexData`

**Functions** (0):
None

**Imports** (11):
`datetime`, `date`, `typing`, `Literal`, `openbb_core.provider.abstract.data`, `Data`, `openbb_core.provider.abstract.query_params`, `QueryParams`, `openbb_core.provider.utils.descriptions`, `pydantic`, `Field`


## Key Components

**Class `SharePriceIndexQueryParams`**: Share Price Index Query.

**Class `SharePriceIndexData`**: Share Price Index Data.

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
- Generated: 2025-11-18T07:54:35.735614
- Generator: World's Best Repo Book Generator v1.0.0

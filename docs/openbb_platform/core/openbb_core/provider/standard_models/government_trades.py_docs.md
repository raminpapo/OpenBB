# Documentation: openbb_platform/core/openbb_core/provider/standard_models/government_trades.py

## File Metadata
- **Path**: `openbb_platform/core/openbb_core/provider/standard_models/government_trades.py`
- **Size**: 1,460 characters, 48 lines
- **Words**: 129
- **Extension**: .py
- **Classification**: Text file

## Original Source

```python
"""Government Trades Standard Model."""

from datetime import date as dateType
from typing import Literal

from openbb_core.provider.abstract.data import Data
from openbb_core.provider.abstract.query_params import QueryParams
from openbb_core.provider.utils.descriptions import (
    DATA_DESCRIPTIONS,
    QUERY_DESCRIPTIONS,
)
from pydantic import Field, field_validator


class GovernmentTradesQueryParams(QueryParams):
    """Government Trades Query."""

    symbol: str | None = Field(
        default=None, description=QUERY_DESCRIPTIONS.get("symbol", "")
    )
    chamber: Literal["house", "senate", "all"] = Field(
        default="all", description="Government Chamber."
    )
    limit: int | None = Field(
        default=None, description=QUERY_DESCRIPTIONS.get("limit", "")
    )

    @field_validator("symbol", mode="before", check_fields=False)
    @classmethod
    def to_upper(cls, v: str):
        """Convert field to uppercase."""
        return v.upper() if v else None


class GovernmentTradesData(Data):
    """Government Trades data."""

    symbol: str | None = Field(
        default=None, description=DATA_DESCRIPTIONS.get("symbol", "")
    )
    date: dateType = Field(description=DATA_DESCRIPTIONS.get("date", ""))
    transaction_date: dateType | None = Field(
        default=None, description="Date of Transaction."
    )
    representative: str | None = Field(
        default=None, description="Name of Representative."
    )

```

## High-Level Overview

Government Trades Standard Model.

from datetime import date as dateType
from typing import Literal

from openbb_core.provider.abstract.data import Data
from openbb_core.provider.abstract.query_params import QueryParams
from openbb_core.provider.utils.descriptions import (
DATA_DESCRIPTIONS,
QUERY_DESCRIPTIONS,
)
from pydantic import Field, field_validator


class GovernmentTradesQueryParams(QueryParams):
Government Trades Query.
Convert field to uppercase.
return v.upper() if v else None



## Detailed Structure

### Python File Structure

**Classes** (2):
`GovernmentTradesQueryParams`, `GovernmentTradesData`

**Functions** (1):
`to_upper`

**Imports** (11):
`datetime`, `date`, `typing`, `Literal`, `openbb_core.provider.abstract.data`, `Data`, `openbb_core.provider.abstract.query_params`, `QueryParams`, `openbb_core.provider.utils.descriptions`, `pydantic`, `Field`


## Key Components

**Class `GovernmentTradesQueryParams`**: Government Trades Query.

**Class `GovernmentTradesData`**: Government Trades data.

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
- Generated: 2025-11-18T07:54:35.656554
- Generator: World's Best Repo Book Generator v1.0.0

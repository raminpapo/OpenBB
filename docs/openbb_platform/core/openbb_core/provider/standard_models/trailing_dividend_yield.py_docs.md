# Documentation: openbb_platform/core/openbb_core/provider/standard_models/trailing_dividend_yield.py

## File Metadata
- **Path**: `openbb_platform/core/openbb_core/provider/standard_models/trailing_dividend_yield.py`
- **Size**: 909 characters, 29 lines
- **Words**: 79
- **Extension**: .py
- **Classification**: Text file

## Original Source

```python
"""Trailing Dividend Yield Standard Model."""

from datetime import date as dateType

from openbb_core.provider.abstract.data import Data
from openbb_core.provider.abstract.query_params import QueryParams
from openbb_core.provider.utils.descriptions import (
    DATA_DESCRIPTIONS,
    QUERY_DESCRIPTIONS,
)
from pydantic import Field


class TrailingDivYieldQueryParams(QueryParams):
    """Trailing Dividend Yield Query."""

    symbol: str = Field(description=QUERY_DESCRIPTIONS.get("symbol", ""))
    limit: int | None = Field(
        default=252,
        description=f"{QUERY_DESCRIPTIONS.get('limit', '')} Default is 252, the number of trading days in a year.",
    )


class TrailingDivYieldData(Data):
    """Trailing Dividend Yield Data."""

    date: dateType = Field(description=DATA_DESCRIPTIONS.get("date", ""))
    trailing_dividend_yield: float = Field(description="Trailing dividend yield.")

```

## High-Level Overview

Trailing Dividend Yield Standard Model.

from datetime import date as dateType

from openbb_core.provider.abstract.data import Data
from openbb_core.provider.abstract.query_params import QueryParams
from openbb_core.provider.utils.descriptions import (
DATA_DESCRIPTIONS,
QUERY_DESCRIPTIONS,
)
from pydantic import Field


class TrailingDivYieldQueryParams(QueryParams):
Trailing Dividend Yield Query.
Trailing Dividend Yield Data.

date: dateType = Field(description=DATA_DESCRIPTIONS.get("date", ""))
trailing_dividend_yield: float = Field(description="Trailing dividend yield.")


## Detailed Structure

### Python File Structure

**Classes** (2):
`TrailingDivYieldQueryParams`, `TrailingDivYieldData`

**Functions** (0):
None

**Imports** (9):
`datetime`, `date`, `openbb_core.provider.abstract.data`, `Data`, `openbb_core.provider.abstract.query_params`, `QueryParams`, `openbb_core.provider.utils.descriptions`, `pydantic`, `Field`


## Key Components

**Class `TrailingDivYieldQueryParams`**: Trailing Dividend Yield Query.

**Class `TrailingDivYieldData`**: Trailing Dividend Yield Data.

## Usage & Examples

See source code for usage details.

## Related Files

- `datetime`
- `openbb_core.provider.abstract.data`
- `openbb_core.provider.abstract.query_params`
- `openbb_core.provider.utils.descriptions`
- `pydantic`

## Notes
- Generated: 2025-11-18T07:54:35.752831
- Generator: World's Best Repo Book Generator v1.0.0

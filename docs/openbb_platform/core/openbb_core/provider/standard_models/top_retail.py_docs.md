# Documentation: openbb_platform/core/openbb_core/provider/standard_models/top_retail.py

## File Metadata
- **Path**: `openbb_platform/core/openbb_core/provider/standard_models/top_retail.py`
- **Size**: 874 characters, 29 lines
- **Words**: 79
- **Extension**: .py
- **Classification**: Text file

## Original Source

```python
"""Top Retail Standard Model."""

from datetime import date as DateType

from openbb_core.provider.abstract.data import Data
from openbb_core.provider.abstract.query_params import QueryParams
from openbb_core.provider.utils.descriptions import (
    DATA_DESCRIPTIONS,
    QUERY_DESCRIPTIONS,
)
from pydantic import Field


class TopRetailQueryParams(QueryParams):
    """Top Retail Search Query."""

    limit: int = Field(description=QUERY_DESCRIPTIONS.get("limit", ""), default=5)


class TopRetailData(Data):
    """Top Retail Search Data."""

    date: DateType = Field(description=DATA_DESCRIPTIONS.get("date", ""))
    symbol: str = Field(description=DATA_DESCRIPTIONS.get("symbol", ""))
    activity: float = Field(description="Activity of the symbol.")
    sentiment: float = Field(
        description="Sentiment of the symbol. 1 is bullish, -1 is bearish."
    )

```

## High-Level Overview

Top Retail Standard Model.

from datetime import date as DateType

from openbb_core.provider.abstract.data import Data
from openbb_core.provider.abstract.query_params import QueryParams
from openbb_core.provider.utils.descriptions import (
DATA_DESCRIPTIONS,
QUERY_DESCRIPTIONS,
)
from pydantic import Field


class TopRetailQueryParams(QueryParams):
Top Retail Search Query.
Top Retail Search Data.

date: DateType = Field(description=DATA_DESCRIPTIONS.get("date", ""))
symbol: str = Field(description=DATA_DESCRIPTIONS.get("symbol", ""))
activity: float = Field(description="Activity of the symbol.")

## Detailed Structure

### Python File Structure

**Classes** (2):
`TopRetailQueryParams`, `TopRetailData`

**Functions** (0):
None

**Imports** (9):
`datetime`, `date`, `openbb_core.provider.abstract.data`, `Data`, `openbb_core.provider.abstract.query_params`, `QueryParams`, `openbb_core.provider.utils.descriptions`, `pydantic`, `Field`


## Key Components

**Class `TopRetailQueryParams`**: Top Retail Search Query.

**Class `TopRetailData`**: Top Retail Search Data.

## Usage & Examples

See source code for usage details.

## Related Files

- `datetime`
- `openbb_core.provider.abstract.data`
- `openbb_core.provider.abstract.query_params`
- `openbb_core.provider.utils.descriptions`
- `pydantic`

## Notes
- Generated: 2025-11-18T07:54:35.751648
- Generator: World's Best Repo Book Generator v1.0.0

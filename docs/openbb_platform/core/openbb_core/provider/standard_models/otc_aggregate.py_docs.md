# Documentation: openbb_platform/core/openbb_core/provider/standard_models/otc_aggregate.py

## File Metadata
- **Path**: `openbb_platform/core/openbb_core/provider/standard_models/otc_aggregate.py`
- **Size**: 986 characters, 32 lines
- **Words**: 103
- **Extension**: .py
- **Classification**: Text file

## Original Source

```python
"""OTC Aggregate Standard Model."""

from datetime import date as dateType

from openbb_core.provider.abstract.data import Data
from openbb_core.provider.abstract.query_params import QueryParams
from openbb_core.provider.utils.descriptions import QUERY_DESCRIPTIONS
from pydantic import Field


class OTCAggregateQueryParams(QueryParams):
    """OTC Aggregate Query."""

    symbol: str | None = Field(
        description=QUERY_DESCRIPTIONS.get("symbol", ""),
        default=None,
    )


class OTCAggregateData(Data):
    """OTC Aggregate Data."""

    update_date: dateType = Field(
        description="Most recent date on which total trades is updated based on data received from each ATS/OTC."
    )
    share_quantity: float = Field(
        description="Aggregate weekly total number of shares reported by each ATS for the Symbol."
    )
    trade_quantity: float = Field(
        description="Aggregate weekly total number of trades reported by each ATS for the Symbol"
    )

```

## High-Level Overview

OTC Aggregate Standard Model.

from datetime import date as dateType

from openbb_core.provider.abstract.data import Data
from openbb_core.provider.abstract.query_params import QueryParams
from openbb_core.provider.utils.descriptions import QUERY_DESCRIPTIONS
from pydantic import Field


class OTCAggregateQueryParams(QueryParams):
OTC Aggregate Query.
OTC Aggregate Data.

update_date: dateType = Field(
description="Most recent date on which total trades is updated based on data received from each ATS/OTC."
)
share_quantity: float = Field(
description="Aggregate weekly total number of shares reported by each ATS for the Symbol."
)

## Detailed Structure

### Python File Structure

**Classes** (2):
`OTCAggregateQueryParams`, `OTCAggregateData`

**Functions** (0):
None

**Imports** (11):
`datetime`, `date`, `openbb_core.provider.abstract.data`, `Data`, `openbb_core.provider.abstract.query_params`, `QueryParams`, `openbb_core.provider.utils.descriptions`, `QUERY_DESCRIPTIONS`, `pydantic`, `Field`, `each`


## Key Components

**Class `OTCAggregateQueryParams`**: OTC Aggregate Query.

**Class `OTCAggregateData`**: OTC Aggregate Data.

## Usage & Examples

See source code for usage details.

## Related Files

- `datetime`
- `openbb_core.provider.abstract.data`
- `openbb_core.provider.abstract.query_params`
- `openbb_core.provider.utils.descriptions`
- `pydantic`

## Notes
- Generated: 2025-11-18T07:54:35.710192
- Generator: World's Best Repo Book Generator v1.0.0

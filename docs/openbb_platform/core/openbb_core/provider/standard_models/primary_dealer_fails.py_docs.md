# Documentation: openbb_platform/core/openbb_core/provider/standard_models/primary_dealer_fails.py

## File Metadata
- **Path**: `openbb_platform/core/openbb_core/provider/standard_models/primary_dealer_fails.py`
- **Size**: 895 characters, 32 lines
- **Words**: 74
- **Extension**: .py
- **Classification**: Text file

## Original Source

```python
"""Primray Dealer Fails Standard Model."""

from datetime import (
    date as dateType,
)

from openbb_core.provider.abstract.data import Data
from openbb_core.provider.abstract.query_params import QueryParams
from openbb_core.provider.utils.descriptions import (
    DATA_DESCRIPTIONS,
    QUERY_DESCRIPTIONS,
)
from pydantic import Field


class PrimaryDealerFailsQueryParams(QueryParams):
    """Primary Dealer Fails Query."""

    start_date: dateType | None = Field(
        default=None, description=QUERY_DESCRIPTIONS.get("start_date", "")
    )
    end_date: dateType | None = Field(
        default=None, description=QUERY_DESCRIPTIONS.get("end_date", "")
    )


class PrimaryDealerFailsData(Data):
    """Primary Dealer Fails Data."""

    date: dateType = Field(description=DATA_DESCRIPTIONS.get("date", ""))
    symbol: str = Field(description=DATA_DESCRIPTIONS.get("symbol", ""))

```

## High-Level Overview

Primray Dealer Fails Standard Model.

from datetime import (
date as dateType,
)

from openbb_core.provider.abstract.data import Data
from openbb_core.provider.abstract.query_params import QueryParams
from openbb_core.provider.utils.descriptions import (
DATA_DESCRIPTIONS,
QUERY_DESCRIPTIONS,
)
from pydantic import Field


class PrimaryDealerFailsQueryParams(QueryParams):
Primary Dealer Fails Query.
Primary Dealer Fails Data.

date: dateType = Field(description=DATA_DESCRIPTIONS.get("date", ""))

## Detailed Structure

### Python File Structure

**Classes** (2):
`PrimaryDealerFailsQueryParams`, `PrimaryDealerFailsData`

**Functions** (0):
None

**Imports** (8):
`datetime`, `openbb_core.provider.abstract.data`, `Data`, `openbb_core.provider.abstract.query_params`, `QueryParams`, `openbb_core.provider.utils.descriptions`, `pydantic`, `Field`


## Key Components

**Class `PrimaryDealerFailsQueryParams`**: Primary Dealer Fails Query.

**Class `PrimaryDealerFailsData`**: Primary Dealer Fails Data.

## Usage & Examples

See source code for usage details.

## Related Files

- `datetime`
- `openbb_core.provider.abstract.data`
- `openbb_core.provider.abstract.query_params`
- `openbb_core.provider.utils.descriptions`
- `pydantic`

## Notes
- Generated: 2025-11-18T07:54:35.719159
- Generator: World's Best Repo Book Generator v1.0.0

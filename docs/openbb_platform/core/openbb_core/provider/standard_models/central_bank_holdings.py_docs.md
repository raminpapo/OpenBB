# Documentation: openbb_platform/core/openbb_core/provider/standard_models/central_bank_holdings.py

## File Metadata
- **Path**: `openbb_platform/core/openbb_core/provider/standard_models/central_bank_holdings.py`
- **Size**: 706 characters, 29 lines
- **Words**: 59
- **Extension**: .py
- **Classification**: Text file

## Original Source

```python
"""Central Bank Holdings Standard Model."""

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


class CentralBankHoldingsQueryParams(QueryParams):
    """Central Bank Holdings Query."""

    date: dateType | None = Field(
        default=None,
        description=QUERY_DESCRIPTIONS.get("date", ""),
    )


class CentralBankHoldingsData(Data):
    """Central Bank Holdings Data."""

    date: dateType = Field(description=DATA_DESCRIPTIONS.get("date", ""))

```

## High-Level Overview

Central Bank Holdings Standard Model.

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


class CentralBankHoldingsQueryParams(QueryParams):
Central Bank Holdings Query.
Central Bank Holdings Data.

date: dateType = Field(description=DATA_DESCRIPTIONS.get("date", ""))

## Detailed Structure

### Python File Structure

**Classes** (2):
`CentralBankHoldingsQueryParams`, `CentralBankHoldingsData`

**Functions** (0):
None

**Imports** (8):
`datetime`, `openbb_core.provider.abstract.data`, `Data`, `openbb_core.provider.abstract.query_params`, `QueryParams`, `openbb_core.provider.utils.descriptions`, `pydantic`, `Field`


## Key Components

**Class `CentralBankHoldingsQueryParams`**: Central Bank Holdings Query.

**Class `CentralBankHoldingsData`**: Central Bank Holdings Data.

## Usage & Examples

See source code for usage details.

## Related Files

- `datetime`
- `openbb_core.provider.abstract.data`
- `openbb_core.provider.abstract.query_params`
- `openbb_core.provider.utils.descriptions`
- `pydantic`

## Notes
- Generated: 2025-11-18T07:54:35.553793
- Generator: World's Best Repo Book Generator v1.0.0

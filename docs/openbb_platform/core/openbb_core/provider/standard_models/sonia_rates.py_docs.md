# Documentation: openbb_platform/core/openbb_core/provider/standard_models/sonia_rates.py

## File Metadata
- **Path**: `openbb_platform/core/openbb_core/provider/standard_models/sonia_rates.py`
- **Size**: 818 characters, 32 lines
- **Words**: 68
- **Extension**: .py
- **Classification**: Text file

## Original Source

```python
"""SONIA Standard Model."""

from datetime import date as dateType

from openbb_core.provider.abstract.data import Data
from openbb_core.provider.abstract.query_params import QueryParams
from openbb_core.provider.utils.descriptions import (
    DATA_DESCRIPTIONS,
    QUERY_DESCRIPTIONS,
)
from pydantic import Field


class SONIAQueryParams(QueryParams):
    """SONIA Query."""

    start_date: dateType | None = Field(
        default=None,
        description=QUERY_DESCRIPTIONS.get("start_date", ""),
    )
    end_date: dateType | None = Field(
        default=None,
        description=QUERY_DESCRIPTIONS.get("end_date", ""),
    )


class SONIAData(Data):
    """SONIA Data."""

    date: dateType = Field(description=DATA_DESCRIPTIONS.get("date", ""))
    rate: float | None = Field(description="SONIA rate.")

```

## High-Level Overview

SONIA Standard Model.

from datetime import date as dateType

from openbb_core.provider.abstract.data import Data
from openbb_core.provider.abstract.query_params import QueryParams
from openbb_core.provider.utils.descriptions import (
DATA_DESCRIPTIONS,
QUERY_DESCRIPTIONS,
)
from pydantic import Field


class SONIAQueryParams(QueryParams):
SONIA Query.
SONIA Data.

date: dateType = Field(description=DATA_DESCRIPTIONS.get("date", ""))
rate: float | None = Field(description="SONIA rate.")


## Detailed Structure

### Python File Structure

**Classes** (2):
`SONIAQueryParams`, `SONIAData`

**Functions** (0):
None

**Imports** (9):
`datetime`, `date`, `openbb_core.provider.abstract.data`, `Data`, `openbb_core.provider.abstract.query_params`, `QueryParams`, `openbb_core.provider.utils.descriptions`, `pydantic`, `Field`


## Key Components

**Class `SONIAQueryParams`**: SONIA Query.

**Class `SONIAData`**: SONIA Data.

## Usage & Examples

See source code for usage details.

## Related Files

- `datetime`
- `openbb_core.provider.abstract.data`
- `openbb_core.provider.abstract.query_params`
- `openbb_core.provider.utils.descriptions`
- `pydantic`

## Notes
- Generated: 2025-11-18T07:54:35.741195
- Generator: World's Best Repo Book Generator v1.0.0

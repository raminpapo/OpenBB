# Documentation: openbb_platform/core/openbb_core/provider/standard_models/port_volume.py

## File Metadata
- **Path**: `openbb_platform/core/openbb_core/provider/standard_models/port_volume.py`
- **Size**: 1,028 characters, 34 lines
- **Words**: 94
- **Extension**: .py
- **Classification**: Text file

## Original Source

```python
"""Port Volume Standard Model."""

from datetime import date as dateType

from openbb_core.provider.abstract.data import Data
from openbb_core.provider.abstract.query_params import QueryParams
from openbb_core.provider.utils.descriptions import (
    DATA_DESCRIPTIONS,
    QUERY_DESCRIPTIONS,
)
from pydantic import Field


class PortVolumeQueryParams(QueryParams):
    """Port Volume Query."""

    start_date: dateType | None = Field(
        default=None, description=QUERY_DESCRIPTIONS.get("start_date", "")
    )
    end_date: dateType | None = Field(
        default=None, description=QUERY_DESCRIPTIONS.get("end_date", "")
    )


class PortVolumeData(Data):
    """Port Volume Data."""

    date: dateType = Field(description=DATA_DESCRIPTIONS.get("date", ""))
    port_code: str | None = Field(default=None, description="Port code.")
    port_name: str | None = Field(default=None, description="Port name.")
    country: str | None = Field(
        default=None, description="Country where the port is located."
    )

```

## High-Level Overview

Port Volume Standard Model.

from datetime import date as dateType

from openbb_core.provider.abstract.data import Data
from openbb_core.provider.abstract.query_params import QueryParams
from openbb_core.provider.utils.descriptions import (
DATA_DESCRIPTIONS,
QUERY_DESCRIPTIONS,
)
from pydantic import Field


class PortVolumeQueryParams(QueryParams):
Port Volume Query.
Port Volume Data.

date: dateType = Field(description=DATA_DESCRIPTIONS.get("date", ""))
port_code: str | None = Field(default=None, description="Port code.")
port_name: str | None = Field(default=None, description="Port name.")

## Detailed Structure

### Python File Structure

**Classes** (2):
`PortVolumeQueryParams`, `PortVolumeData`

**Functions** (0):
None

**Imports** (9):
`datetime`, `date`, `openbb_core.provider.abstract.data`, `Data`, `openbb_core.provider.abstract.query_params`, `QueryParams`, `openbb_core.provider.utils.descriptions`, `pydantic`, `Field`


## Key Components

**Class `PortVolumeQueryParams`**: Port Volume Query.

**Class `PortVolumeData`**: Port Volume Data.

## Usage & Examples

See source code for usage details.

## Related Files

- `datetime`
- `openbb_core.provider.abstract.data`
- `openbb_core.provider.abstract.query_params`
- `openbb_core.provider.utils.descriptions`
- `pydantic`

## Notes
- Generated: 2025-11-18T07:54:35.715687
- Generator: World's Best Repo Book Generator v1.0.0

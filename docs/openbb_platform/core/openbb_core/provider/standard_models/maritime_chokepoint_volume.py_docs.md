# Documentation: openbb_platform/core/openbb_core/provider/standard_models/maritime_chokepoint_volume.py

## File Metadata
- **Path**: `openbb_platform/core/openbb_core/provider/standard_models/maritime_chokepoint_volume.py`
- **Size**: 870 characters, 29 lines
- **Words**: 68
- **Extension**: .py
- **Classification**: Text file

## Original Source

```python
"""Maritime chokepoint transit calls and trade volume estimates time series."""

from datetime import date as dateType

from openbb_core.provider.abstract.data import Data
from openbb_core.provider.abstract.query_params import QueryParams
from openbb_core.provider.utils.descriptions import (
    DATA_DESCRIPTIONS,
    QUERY_DESCRIPTIONS,
)
from pydantic import Field


class MaritimeChokePointVolumeQueryParams(QueryParams):
    """MaritimeChokepointVolume Query."""

    start_date: dateType | None = Field(
        default=None, description=QUERY_DESCRIPTIONS.get("start_date", "")
    )
    end_date: dateType | None = Field(
        default=None, description=QUERY_DESCRIPTIONS.get("end_date", "")
    )


class MaritimeChokePointVolumeData(Data):
    """MaritimeChokepointVolume Data."""

    date: dateType = Field(description=DATA_DESCRIPTIONS.get("date", ""))

```

## High-Level Overview

Maritime chokepoint transit calls and trade volume estimates time series.

from datetime import date as dateType

from openbb_core.provider.abstract.data import Data
from openbb_core.provider.abstract.query_params import QueryParams
from openbb_core.provider.utils.descriptions import (
DATA_DESCRIPTIONS,
QUERY_DESCRIPTIONS,
)
from pydantic import Field


class MaritimeChokePointVolumeQueryParams(QueryParams):
MaritimeChokepointVolume Query.
MaritimeChokepointVolume Data.

date: dateType = Field(description=DATA_DESCRIPTIONS.get("date", ""))


## Detailed Structure

### Python File Structure

**Classes** (2):
`MaritimeChokePointVolumeQueryParams`, `MaritimeChokePointVolumeData`

**Functions** (0):
None

**Imports** (9):
`datetime`, `date`, `openbb_core.provider.abstract.data`, `Data`, `openbb_core.provider.abstract.query_params`, `QueryParams`, `openbb_core.provider.utils.descriptions`, `pydantic`, `Field`


## Key Components

**Class `MaritimeChokePointVolumeQueryParams`**: MaritimeChokepointVolume Query.

**Class `MaritimeChokePointVolumeData`**: MaritimeChokepointVolume Data.

## Usage & Examples

See source code for usage details.

## Related Files

- `datetime`
- `openbb_core.provider.abstract.data`
- `openbb_core.provider.abstract.query_params`
- `openbb_core.provider.utils.descriptions`
- `pydantic`

## Notes
- Generated: 2025-11-18T07:54:35.695806
- Generator: World's Best Repo Book Generator v1.0.0

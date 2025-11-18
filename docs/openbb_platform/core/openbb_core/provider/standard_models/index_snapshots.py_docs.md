# Documentation: openbb_platform/core/openbb_core/provider/standard_models/index_snapshots.py

## File Metadata
- **Path**: `openbb_platform/core/openbb_core/provider/standard_models/index_snapshots.py`
- **Size**: 1,748 characters, 49 lines
- **Words**: 173
- **Extension**: .py
- **Classification**: Text file

## Original Source

```python
"""Index Snapshots Standard Model."""

from openbb_core.provider.abstract.data import Data
from openbb_core.provider.abstract.query_params import QueryParams
from openbb_core.provider.utils.descriptions import DATA_DESCRIPTIONS
from pydantic import Field


class IndexSnapshotsQueryParams(QueryParams):
    """Index Snapshots Query."""

    region: str = Field(
        default="us", description="The region of focus for the data - i.e., us, eu."
    )


class IndexSnapshotsData(Data):
    """Index Snapshots Data."""

    symbol: str = Field(description=DATA_DESCRIPTIONS.get("symbol", ""))
    name: str | None = Field(default=None, description="Name of the index.")
    currency: str | None = Field(default=None, description="Currency of the index.")
    price: float | None = Field(default=None, description="Current price of the index.")
    open: float | None = Field(
        default=None, description=DATA_DESCRIPTIONS.get("open", "")
    )
    high: float | None = Field(
        default=None, description=DATA_DESCRIPTIONS.get("high", "")
    )
    low: float | None = Field(
        default=None, description=DATA_DESCRIPTIONS.get("low", "")
    )
    close: float | None = Field(
        default=None, description=DATA_DESCRIPTIONS.get("close", "")
    )
    volume: int | None = Field(
        default=None, description=DATA_DESCRIPTIONS.get("volume", "")
    )
    prev_close: float | None = Field(
        default=None, description=DATA_DESCRIPTIONS.get("prev_close", "")
    )
    change: float | None = Field(
        default=None, description="Change in value of the index."
    )
    change_percent: float | None = Field(
        default=None,
        description="Change, in normalized percentage points, of the index.",
    )

```

## High-Level Overview

Index Snapshots Standard Model.

from openbb_core.provider.abstract.data import Data
from openbb_core.provider.abstract.query_params import QueryParams
from openbb_core.provider.utils.descriptions import DATA_DESCRIPTIONS
from pydantic import Field


class IndexSnapshotsQueryParams(QueryParams):
Index Snapshots Query.
Index Snapshots Data.

symbol: str = Field(description=DATA_DESCRIPTIONS.get("symbol", ""))
name: str | None = Field(default=None, description="Name of the index.")
currency: str | None = Field(default=None, description="Currency of the index.")
price: float | None = Field(default=None, description="Current price of the index.")
open: float | None = Field(
default=None, description=DATA_DESCRIPTIONS.get("open", "")
)
high: float | None = Field(

## Detailed Structure

### Python File Structure

**Classes** (2):
`IndexSnapshotsQueryParams`, `IndexSnapshotsData`

**Functions** (0):
None

**Imports** (8):
`openbb_core.provider.abstract.data`, `Data`, `openbb_core.provider.abstract.query_params`, `QueryParams`, `openbb_core.provider.utils.descriptions`, `DATA_DESCRIPTIONS`, `pydantic`, `Field`


## Key Components

**Class `IndexSnapshotsQueryParams`**: Index Snapshots Query.

**Class `IndexSnapshotsData`**: Index Snapshots Data.

## Usage & Examples

See source code for usage details.

## Related Files

- `openbb_core.provider.abstract.data`
- `openbb_core.provider.abstract.query_params`
- `openbb_core.provider.utils.descriptions`
- `pydantic`

## Notes
- Generated: 2025-11-18T07:54:35.678755
- Generator: World's Best Repo Book Generator v1.0.0

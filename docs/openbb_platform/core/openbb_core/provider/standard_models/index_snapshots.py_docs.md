# File Documentation: index_snapshots.py

## Metadata
- **Path**: `openbb_platform/core/openbb_core/provider/standard_models/index_snapshots.py`
- **Size**: 1,748 bytes
- **Lines**: 49
- **Category**: python
- **Extension**: .py

---

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



---

## High-Level Overview

This is a **python** file named `index_snapshots.py`.

**Python Module**

- **Classes** (2): IndexSnapshotsQueryParams, IndexSnapshotsData
- **Import Statements**: 1


---

## Detailed Analysis

### Python Code Structure

#### Classes

- **`IndexSnapshotsQueryParams`**(QueryParams)
- **`IndexSnapshotsData`**(Data)


---

## Related Files

The following files may be related based on imports and references:

**Imported Modules**:
- `DATA_DESCRIPTIONS`
- `Data`
- `Field`
- `QueryParams`
- `openbb_core.provider.abstract.data`
- `openbb_core.provider.abstract.query_params`
- `openbb_core.provider.utils.descriptions`
- `pydantic`


---

## Performance & Security Notes

No obvious security concerns detected in static analysis.


---

**Generated**: 2025-11-19T02:16:46.506829Z
**Generator**: World's Best Repo Book Generator v1.0

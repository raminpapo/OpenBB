# File Documentation: maritime_chokepoint_volume.py

## Metadata
- **Path**: `openbb_platform/core/openbb_core/provider/standard_models/maritime_chokepoint_volume.py`
- **Size**: 870 bytes
- **Lines**: 29
- **Category**: python
- **Extension**: .py

---

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



---

## High-Level Overview

This is a **python** file named `maritime_chokepoint_volume.py`.

**Python Module**

- **Classes** (2): MaritimeChokePointVolumeQueryParams, MaritimeChokePointVolumeData
- **Import Statements**: 2


---

## Detailed Analysis

### Python Code Structure

#### Classes

- **`MaritimeChokePointVolumeQueryParams`**(QueryParams)
- **`MaritimeChokePointVolumeData`**(Data)


---

## Related Files

The following files may be related based on imports and references:

**Imported Modules**:
- `Data`
- `Field`
- `QueryParams`
- `date`
- `datetime`
- `openbb_core.provider.abstract.data`
- `openbb_core.provider.abstract.query_params`
- `openbb_core.provider.utils.descriptions`
- `pydantic`


---

## Performance & Security Notes

No obvious security concerns detected in static analysis.


---

**Generated**: 2025-11-19T02:16:46.525191Z
**Generator**: World's Best Repo Book Generator v1.0

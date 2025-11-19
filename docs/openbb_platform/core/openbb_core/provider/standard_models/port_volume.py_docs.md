# File Documentation: port_volume.py

## Metadata
- **Path**: `openbb_platform/core/openbb_core/provider/standard_models/port_volume.py`
- **Size**: 1,028 bytes
- **Lines**: 34
- **Category**: python
- **Extension**: .py

---

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



---

## High-Level Overview

This is a **python** file named `port_volume.py`.

**Python Module**

- **Classes** (2): PortVolumeQueryParams, PortVolumeData
- **Import Statements**: 2


---

## Detailed Analysis

### Python Code Structure

#### Classes

- **`PortVolumeQueryParams`**(QueryParams)
- **`PortVolumeData`**(Data)


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

**Generated**: 2025-11-19T02:16:46.547209Z
**Generator**: World's Best Repo Book Generator v1.0

# File Documentation: port_info.py

## Metadata
- **Path**: `openbb_platform/core/openbb_core/provider/standard_models/port_info.py`
- **Size**: 410 bytes
- **Lines**: 16
- **Category**: python
- **Extension**: .py

---

## Original Source

```python
"""Port information and metadata."""

from openbb_core.provider.abstract.data import Data
from openbb_core.provider.abstract.query_params import QueryParams
from pydantic import Field


class PortInfoQueryParams(QueryParams):
    """Port Information Query."""


class PortInfoData(Data):
    """Port Information Data."""

    port_code: str = Field(description="Unique ID assigned to the port by the source.")

```



---

## High-Level Overview

This is a **python** file named `port_info.py`.

**Python Module**

- **Classes** (2): PortInfoQueryParams, PortInfoData
- **Import Statements**: 1


---

## Detailed Analysis

### Python Code Structure

#### Classes

- **`PortInfoQueryParams`**(QueryParams)
- **`PortInfoData`**(Data)


---

## Related Files

The following files may be related based on imports and references:

**Imported Modules**:
- `Data`
- `Field`
- `QueryParams`
- `openbb_core.provider.abstract.data`
- `openbb_core.provider.abstract.query_params`
- `pydantic`


---

## Performance & Security Notes

No obvious security concerns detected in static analysis.


---

**Generated**: 2025-11-19T02:16:46.546056Z
**Generator**: World's Best Repo Book Generator v1.0

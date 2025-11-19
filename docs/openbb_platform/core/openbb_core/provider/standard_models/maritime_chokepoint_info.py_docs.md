# File Documentation: maritime_chokepoint_info.py

## Metadata
- **Path**: `openbb_platform/core/openbb_core/provider/standard_models/maritime_chokepoint_info.py`
- **Size**: 491 bytes
- **Lines**: 18
- **Category**: python
- **Extension**: .py

---

## Original Source

```python
"""Maritime chokepoint information and metadata."""

from openbb_core.provider.abstract.data import Data
from openbb_core.provider.abstract.query_params import QueryParams
from pydantic import Field


class MaritimeChokePointInfoQueryParams(QueryParams):
    """MaritimeChokepointInfo Query."""


class MaritimeChokePointInfoData(Data):
    """MaritimeChokepointInfo Data."""

    chokepoint_code: str = Field(
        description="Unique ID assigned to the chokepoint by the source."
    )

```



---

## High-Level Overview

This is a **python** file named `maritime_chokepoint_info.py`.

**Python Module**

- **Classes** (2): MaritimeChokePointInfoQueryParams, MaritimeChokePointInfoData
- **Import Statements**: 1


---

## Detailed Analysis

### Python Code Structure

#### Classes

- **`MaritimeChokePointInfoQueryParams`**(QueryParams)
- **`MaritimeChokePointInfoData`**(Data)


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

**Generated**: 2025-11-19T02:16:46.523571Z
**Generator**: World's Best Repo Book Generator v1.0

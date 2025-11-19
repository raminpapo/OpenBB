# File Documentation: compare_groups.py

## Metadata
- **Path**: `openbb_platform/core/openbb_core/provider/standard_models/compare_groups.py`
- **Size**: 291 bytes
- **Lines**: 13
- **Category**: python
- **Extension**: .py

---

## Original Source

```python
"""Compare Groups Model."""

from openbb_core.provider.abstract.data import Data
from openbb_core.provider.abstract.query_params import QueryParams


class CompareGroupsQueryParams(QueryParams):
    """Compare Groups Query."""


class CompareGroupsData(Data):
    """Compare Groups Data."""

```



---

## High-Level Overview

This is a **python** file named `compare_groups.py`.

**Python Module**

- **Classes** (2): CompareGroupsQueryParams, CompareGroupsData
- **Import Statements**: 1


---

## Detailed Analysis

### Python Code Structure

#### Classes

- **`CompareGroupsQueryParams`**(QueryParams)
- **`CompareGroupsData`**(Data)


---

## Related Files

The following files may be related based on imports and references:

**Imported Modules**:
- `Data`
- `QueryParams`
- `openbb_core.provider.abstract.data`
- `openbb_core.provider.abstract.query_params`


---

## Performance & Security Notes

No obvious security concerns detected in static analysis.


---

**Generated**: 2025-11-19T02:16:46.385292Z
**Generator**: World's Best Repo Book Generator v1.0

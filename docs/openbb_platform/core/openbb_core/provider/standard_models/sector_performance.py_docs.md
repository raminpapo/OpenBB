# File Documentation: sector_performance.py

## Metadata
- **Path**: `openbb_platform/core/openbb_core/provider/standard_models/sector_performance.py`
- **Size**: 493 bytes
- **Lines**: 17
- **Category**: python
- **Extension**: .py

---

## Original Source

```python
"""Sector Performance Standard Model."""

from openbb_core.provider.abstract.data import Data
from openbb_core.provider.abstract.query_params import QueryParams
from pydantic import Field


class SectorPerformanceQueryParams(QueryParams):
    """Sector Performance Query."""


class SectorPerformanceData(Data):
    """Sector Performance Data."""

    sector: str = Field(description="The name of the sector.")
    change_percent: float = Field(description="The change in percent from open.")

```



---

## High-Level Overview

This is a **python** file named `sector_performance.py`.

**Python Module**

- **Classes** (2): SectorPerformanceQueryParams, SectorPerformanceData
- **Import Statements**: 1


---

## Detailed Analysis

### Python Code Structure

#### Classes

- **`SectorPerformanceQueryParams`**(QueryParams)
- **`SectorPerformanceData`**(Data)


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

**Generated**: 2025-11-19T02:16:46.566317Z
**Generator**: World's Best Repo Book Generator v1.0

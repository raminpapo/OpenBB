# File Documentation: fed_projections.py

## Metadata
- **Path**: `openbb_platform/core/openbb_core/provider/standard_models/fed_projections.py`
- **Size**: 1,184 bytes
- **Lines**: 32
- **Category**: python
- **Extension**: .py

---

## Original Source

```python
"""PROJECTION Standard Model."""

from datetime import date as dateType

from openbb_core.provider.abstract.data import Data
from openbb_core.provider.abstract.query_params import QueryParams
from openbb_core.provider.utils.descriptions import DATA_DESCRIPTIONS
from pydantic import Field


class PROJECTIONQueryParams(QueryParams):
    """PROJECTION Query."""


class PROJECTIONData(Data):
    """PROJECTION Data."""

    date: dateType = Field(description=DATA_DESCRIPTIONS.get("date", ""))
    range_high: float | None = Field(description="High projection of rates.")
    central_tendency_high: float | None = Field(
        description="Central tendency of high projection of rates."
    )
    median: float | None = Field(description="Median projection of rates.")
    range_midpoint: float | None = Field(description="Midpoint projection of rates.")
    central_tendency_midpoint: float | None = Field(
        description="Central tendency of midpoint projection of rates."
    )
    range_low: float | None = Field(description="Low projection of rates.")
    central_tendency_low: float | None = Field(
        description="Central tendency of low projection of rates."
    )

```



---

## High-Level Overview

This is a **python** file named `fed_projections.py`.

**Python Module**

- **Classes** (2): PROJECTIONQueryParams, PROJECTIONData
- **Import Statements**: 1


---

## Detailed Analysis

### Python Code Structure

#### Classes

- **`PROJECTIONQueryParams`**(QueryParams)
- **`PROJECTIONData`**(Data)


---

## Related Files

The following files may be related based on imports and references:

**Imported Modules**:
- `DATA_DESCRIPTIONS`
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

**Generated**: 2025-11-19T02:16:46.456403Z
**Generator**: World's Best Repo Book Generator v1.0

# File Documentation: sector_pe.py

## Metadata
- **Path**: `openbb_platform/core/openbb_core/provider/standard_models/sector_pe.py`
- **Size**: 784 bytes
- **Lines**: 26
- **Category**: python
- **Extension**: .py

---

## Original Source

```python
"""Sector P/E Ratio Standard Model."""

from datetime import date as dateType

from openbb_core.provider.abstract.data import Data
from openbb_core.provider.abstract.query_params import QueryParams
from openbb_core.provider.utils.descriptions import DATA_DESCRIPTIONS
from pydantic import Field


class SectorPEQueryParams(QueryParams):
    """Sector P/E Ratio Query."""


class SectorPEData(Data):
    """Sector P/E Ratio Data."""

    date: dateType | None = Field(
        description=DATA_DESCRIPTIONS.get("date", ""), default=None
    )
    exchange: str | None = Field(
        default=None, description="The exchange where the data is from."
    )
    sector: str = Field(description="The name of the sector.")
    pe: float = Field(description="The P/E ratio of the sector.")

```



---

## High-Level Overview

This is a **python** file named `sector_pe.py`.

**Python Module**

- **Classes** (2): SectorPEQueryParams, SectorPEData
- **Import Statements**: 1


---

## Detailed Analysis

### Python Code Structure

#### Classes

- **`SectorPEQueryParams`**(QueryParams)
- **`SectorPEData`**(Data)


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

**Generated**: 2025-11-19T02:16:46.565114Z
**Generator**: World's Best Repo Book Generator v1.0

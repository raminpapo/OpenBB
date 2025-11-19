# File Documentation: industry_pe.py

## Metadata
- **Path**: `openbb_platform/core/openbb_core/provider/standard_models/industry_pe.py`
- **Size**: 800 bytes
- **Lines**: 26
- **Category**: python
- **Extension**: .py

---

## Original Source

```python
"""Industry P/E Ratio Standard Model."""

from datetime import date as dateType

from openbb_core.provider.abstract.data import Data
from openbb_core.provider.abstract.query_params import QueryParams
from openbb_core.provider.utils.descriptions import DATA_DESCRIPTIONS
from pydantic import Field


class IndustryPEQueryParams(QueryParams):
    """Industry P/E Ratio Query."""


class IndustryPEData(Data):
    """Industry P/E Ratio Data."""

    date: dateType | None = Field(
        description=DATA_DESCRIPTIONS.get("date", ""), default=None
    )
    exchange: str | None = Field(
        default=None, description="The exchange where the data is from."
    )
    industry: str = Field(description="The name of the industry.")
    pe: float = Field(description="The P/E ratio of the industry.")

```



---

## High-Level Overview

This is a **python** file named `industry_pe.py`.

**Python Module**

- **Classes** (2): IndustryPEQueryParams, IndustryPEData
- **Import Statements**: 1


---

## Detailed Analysis

### Python Code Structure

#### Classes

- **`IndustryPEQueryParams`**(QueryParams)
- **`IndustryPEData`**(Data)


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

**Generated**: 2025-11-19T02:16:46.508124Z
**Generator**: World's Best Repo Book Generator v1.0

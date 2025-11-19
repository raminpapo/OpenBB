# File Documentation: equity_search.py

## Metadata
- **Path**: `openbb_platform/core/openbb_core/provider/standard_models/equity_search.py`
- **Size**: 753 bytes
- **Lines**: 25
- **Category**: python
- **Extension**: .py

---

## Original Source

```python
"""Equity Search Standard Model."""

from openbb_core.provider.abstract.data import Data
from openbb_core.provider.abstract.query_params import QueryParams
from openbb_core.provider.utils.descriptions import DATA_DESCRIPTIONS
from pydantic import Field


class EquitySearchQueryParams(QueryParams):
    """Equity Search Query."""

    query: str = Field(description="Search query.", default="")
    is_symbol: bool = Field(
        description="Whether to search by ticker symbol.", default=False
    )


class EquitySearchData(Data):
    """Equity Search Data."""

    symbol: str | None = Field(
        default=None, description=DATA_DESCRIPTIONS.get("symbol", "")
    )
    name: str | None = Field(default=None, description="Name of the company.")

```



---

## High-Level Overview

This is a **python** file named `equity_search.py`.

**Python Module**

- **Classes** (2): EquitySearchQueryParams, EquitySearchData
- **Import Statements**: 1


---

## Detailed Analysis

### Python Code Structure

#### Classes

- **`EquitySearchQueryParams`**(QueryParams)
- **`EquitySearchData`**(Data)


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

**Generated**: 2025-11-19T02:16:46.431920Z
**Generator**: World's Best Repo Book Generator v1.0

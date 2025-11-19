# File Documentation: index_search.py

## Metadata
- **Path**: `openbb_platform/core/openbb_core/provider/standard_models/index_search.py`
- **Size**: 690 bytes
- **Lines**: 23
- **Category**: python
- **Extension**: .py

---

## Original Source

```python
"""Index Search Standard Model."""

from openbb_core.provider.abstract.data import Data
from openbb_core.provider.abstract.query_params import QueryParams
from openbb_core.provider.utils.descriptions import DATA_DESCRIPTIONS
from pydantic import Field


class IndexSearchQueryParams(QueryParams):
    """Index Search Query."""

    query: str = Field(description="Search query.", default="")
    is_symbol: bool = Field(
        description="Whether to search by ticker symbol.", default=False
    )


class IndexSearchData(Data):
    """Index Search Data."""

    symbol: str = Field(description=DATA_DESCRIPTIONS.get("symbol", ""))
    name: str = Field(description="Name of the index.")

```



---

## High-Level Overview

This is a **python** file named `index_search.py`.

**Python Module**

- **Classes** (2): IndexSearchQueryParams, IndexSearchData
- **Import Statements**: 1


---

## Detailed Analysis

### Python Code Structure

#### Classes

- **`IndexSearchQueryParams`**(QueryParams)
- **`IndexSearchData`**(Data)


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

**Generated**: 2025-11-19T02:16:46.504404Z
**Generator**: World's Best Repo Book Generator v1.0

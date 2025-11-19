# File Documentation: bls_search.py

## Metadata
- **Path**: `openbb_platform/core/openbb_core/provider/standard_models/bls_search.py`
- **Size**: 772 bytes
- **Lines**: 24
- **Category**: python
- **Extension**: .py

---

## Original Source

```python
"""BLS Search Model."""

from openbb_core.provider.abstract.data import Data
from openbb_core.provider.abstract.query_params import QueryParams
from openbb_core.provider.utils.descriptions import DATA_DESCRIPTIONS
from pydantic import Field


class SearchQueryParams(QueryParams):
    """BLS Search Query Params."""

    query: str = Field(
        default="",
        description="The search word(s). Use semi-colon to separate multiple queries as an & operator.",
    )


class SearchData(Data):
    """BLS Search Data."""

    symbol: str = Field(description=DATA_DESCRIPTIONS.get("symbol", ""))
    title: str | None = Field(default=None, description="The title of the series.")
    survey_name: str | None = Field(default=None, description="The name of the survey.")

```



---

## High-Level Overview

This is a **python** file named `bls_search.py`.

**Python Module**

- **Classes** (2): SearchQueryParams, SearchData
- **Import Statements**: 1


---

## Detailed Analysis

### Python Code Structure

#### Classes

- **`SearchQueryParams`**(QueryParams)
- **`SearchData`**(Data)


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

**Generated**: 2025-11-19T02:16:46.352907Z
**Generator**: World's Best Repo Book Generator v1.0

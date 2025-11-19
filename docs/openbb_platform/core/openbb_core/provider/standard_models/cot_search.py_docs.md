# File Documentation: cot_search.py

## Metadata
- **Path**: `openbb_platform/core/openbb_core/provider/standard_models/cot_search.py`
- **Size**: 1,087 bytes
- **Lines**: 30
- **Category**: python
- **Extension**: .py

---

## Original Source

```python
"""Commitment of Traders Reports Search Standard Model."""

from openbb_core.provider.abstract.data import Data
from openbb_core.provider.abstract.query_params import QueryParams
from openbb_core.provider.utils.descriptions import DATA_DESCRIPTIONS
from pydantic import Field


class CotSearchQueryParams(QueryParams):
    """Commitment of Traders Reports Search Query."""

    query: str = Field(description="Search query.", default="")


class CotSearchData(Data):
    """Commitment of Traders Reports Search Data."""

    code: str = Field(description="CFTC market contract code of the report.")
    name: str = Field(description="Name of the underlying asset.")
    category: str | None = Field(
        default=None, description="Category of the underlying asset."
    )
    subcategory: str | None = Field(
        default=None, description="Subcategory of the underlying asset."
    )
    units: str | None = Field(default=None, description="The units for one contract.")
    symbol: str | None = Field(
        default=None, description=DATA_DESCRIPTIONS.get("symbol", "")
    )

```



---

## High-Level Overview

This is a **python** file named `cot_search.py`.

**Python Module**

- **Classes** (2): CotSearchQueryParams, CotSearchData
- **Import Statements**: 1


---

## Detailed Analysis

### Python Code Structure

#### Classes

- **`CotSearchQueryParams`**(QueryParams)
- **`CotSearchData`**(Data)


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

**Generated**: 2025-11-19T02:16:46.391411Z
**Generator**: World's Best Repo Book Generator v1.0

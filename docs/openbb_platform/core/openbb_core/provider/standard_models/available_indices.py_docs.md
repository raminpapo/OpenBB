# File Documentation: available_indices.py

## Metadata
- **Path**: `openbb_platform/core/openbb_core/provider/standard_models/available_indices.py`
- **Size**: 891 bytes
- **Lines**: 31
- **Category**: python
- **Extension**: .py

---

## Original Source

```python
"""Available Indices Standard Model."""

from openbb_core.provider.abstract.data import Data
from openbb_core.provider.abstract.query_params import QueryParams
from openbb_core.provider.utils.descriptions import (
    DATA_DESCRIPTIONS,
)
from pydantic import Field


class AvailableIndicesQueryParams(QueryParams):
    """Available Indices Query."""


class AvailableIndicesData(Data):
    """Available Indices Data.

    Returns the list of available indices from a provider.
    """

    symbol: str = Field(description=DATA_DESCRIPTIONS.get("symbol", ""))
    name: str | None = Field(
        default=None, description=DATA_DESCRIPTIONS.get("name", "")
    )
    exchange: str | None = Field(
        default=None, description="Stock exchange where the index is listed."
    )
    currency: str | None = Field(
        default=None, description="Currency the index is traded in."
    )

```



---

## High-Level Overview

This is a **python** file named `available_indices.py`.

**Python Module**

- **Classes** (2): AvailableIndicesQueryParams, AvailableIndicesData
- **Import Statements**: 2


---

## Detailed Analysis

### Python Code Structure

#### Classes

- **`AvailableIndicesQueryParams`**(QueryParams)
- **`AvailableIndicesData`**(Data)


---

## Related Files

The following files may be related based on imports and references:

**Imported Modules**:
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

**Generated**: 2025-11-19T02:16:46.344615Z
**Generator**: World's Best Repo Book Generator v1.0

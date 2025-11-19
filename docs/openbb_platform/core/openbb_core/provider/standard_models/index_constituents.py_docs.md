# File Documentation: index_constituents.py

## Metadata
- **Path**: `openbb_platform/core/openbb_core/provider/standard_models/index_constituents.py`
- **Size**: 882 bytes
- **Lines**: 31
- **Category**: python
- **Extension**: .py

---

## Original Source

```python
"""Index Constituents Standard Model."""

from openbb_core.provider.abstract.data import Data
from openbb_core.provider.abstract.query_params import QueryParams
from openbb_core.provider.utils.descriptions import (
    DATA_DESCRIPTIONS,
    QUERY_DESCRIPTIONS,
)
from pydantic import Field, field_validator


class IndexConstituentsQueryParams(QueryParams):
    """Index Constituents Query."""

    symbol: str = Field(description=QUERY_DESCRIPTIONS.get("symbol", ""))

    @classmethod
    @field_validator("symbol")
    def _to_upper(cls, v):
        """Convert the symbol to uppercase."""
        return v.upper()


class IndexConstituentsData(Data):
    """Index Constituents Data."""

    symbol: str = Field(description=DATA_DESCRIPTIONS.get("symbol", ""))
    name: str | None = Field(
        default=None, description="Name of the constituent company in the index."
    )

```



---

## High-Level Overview

This is a **python** file named `index_constituents.py`.

**Python Module**

- **Classes** (2): IndexConstituentsQueryParams, IndexConstituentsData
- **Functions** (1): _to_upper
- **Import Statements**: 2


---

## Detailed Analysis

### Python Code Structure

#### Classes

- **`IndexConstituentsQueryParams`**(QueryParams)
- **`IndexConstituentsData`**(Data)

#### Functions

- **`_to_upper(cls, v)`**

#### Decorators Used

classmethod, field_validator


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

**Generated**: 2025-11-19T02:16:46.500254Z
**Generator**: World's Best Repo Book Generator v1.0

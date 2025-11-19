# File Documentation: index_info.py

## Metadata
- **Path**: `openbb_platform/core/openbb_core/provider/standard_models/index_info.py`
- **Size**: 1,250 bytes
- **Lines**: 41
- **Category**: python
- **Extension**: .py

---

## Original Source

```python
"""Index Info Standard Model."""

from openbb_core.provider.abstract.data import Data
from openbb_core.provider.abstract.query_params import QueryParams
from openbb_core.provider.utils.descriptions import (
    DATA_DESCRIPTIONS,
    QUERY_DESCRIPTIONS,
)
from pydantic import Field, field_validator


class IndexInfoQueryParams(QueryParams):
    """Index Info Query."""

    symbol: str = Field(description=QUERY_DESCRIPTIONS.get("symbol", ""))

    @field_validator("symbol")
    @classmethod
    def to_upper(cls, v: str) -> str:
        """Convert field to uppercase."""
        return v.upper()


class IndexInfoData(Data):
    """Index Info Data."""

    symbol: str = Field(description=DATA_DESCRIPTIONS.get("symbol", ""))
    name: str = Field(description="The name of the index.")
    description: str | None = Field(
        description="The short description of the index.", default=None
    )
    methodology: str | None = Field(
        description="URL to the methodology document.", default=None
    )
    factsheet: str | None = Field(
        description="URL to the factsheet document.", default=None
    )
    num_constituents: int | None = Field(
        description="The number of constituents in the index.", default=None
    )

```



---

## High-Level Overview

This is a **python** file named `index_info.py`.

**Python Module**

- **Classes** (2): IndexInfoQueryParams, IndexInfoData
- **Functions** (1): to_upper
- **Import Statements**: 2


---

## Detailed Analysis

### Python Code Structure

#### Classes

- **`IndexInfoQueryParams`**(QueryParams)
- **`IndexInfoData`**(Data)

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

**Generated**: 2025-11-19T02:16:46.503065Z
**Generator**: World's Best Repo Book Generator v1.0

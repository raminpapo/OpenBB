# File Documentation: index_sectors.py

## Metadata
- **Path**: `openbb_platform/core/openbb_core/provider/standard_models/index_sectors.py`
- **Size**: 776 bytes
- **Lines**: 26
- **Category**: python
- **Extension**: .py

---

## Original Source

```python
"""Index Sectors Standard Model."""

from openbb_core.provider.abstract.data import Data
from openbb_core.provider.abstract.query_params import QueryParams
from openbb_core.provider.utils.descriptions import QUERY_DESCRIPTIONS
from pydantic import Field, field_validator


class IndexSectorsQueryParams(QueryParams):
    """Index Sectors Query."""

    symbol: str = Field(description=QUERY_DESCRIPTIONS.get("symbol", ""))

    @field_validator("symbol")
    @classmethod
    def to_upper(cls, v: str) -> str:
        """Convert field to uppercase."""
        return v.upper()


class IndexSectorsData(Data):
    """Index Sectors Data."""

    sector: str = Field(description="The sector name.")
    weight: float = Field(description="The weight of the sector in the index.")

```



---

## High-Level Overview

This is a **python** file named `index_sectors.py`.

**Python Module**

- **Classes** (2): IndexSectorsQueryParams, IndexSectorsData
- **Functions** (1): to_upper
- **Import Statements**: 1


---

## Detailed Analysis

### Python Code Structure

#### Classes

- **`IndexSectorsQueryParams`**(QueryParams)
- **`IndexSectorsData`**(Data)

#### Decorators Used

classmethod, field_validator


---

## Related Files

The following files may be related based on imports and references:

**Imported Modules**:
- `Data`
- `Field`
- `QUERY_DESCRIPTIONS`
- `QueryParams`
- `openbb_core.provider.abstract.data`
- `openbb_core.provider.abstract.query_params`
- `openbb_core.provider.utils.descriptions`
- `pydantic`


---

## Performance & Security Notes

No obvious security concerns detected in static analysis.


---

**Generated**: 2025-11-19T02:16:46.505609Z
**Generator**: World's Best Repo Book Generator v1.0

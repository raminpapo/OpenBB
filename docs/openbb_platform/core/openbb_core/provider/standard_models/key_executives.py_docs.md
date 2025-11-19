# File Documentation: key_executives.py

## Metadata
- **Path**: `openbb_platform/core/openbb_core/provider/standard_models/key_executives.py`
- **Size**: 1,185 bytes
- **Lines**: 32
- **Category**: python
- **Extension**: .py

---

## Original Source

```python
"""Key Executives Standard Model."""

from openbb_core.provider.abstract.data import Data
from openbb_core.provider.abstract.query_params import QueryParams
from openbb_core.provider.utils.descriptions import QUERY_DESCRIPTIONS
from pydantic import Field, field_validator


class KeyExecutivesQueryParams(QueryParams):
    """Key Executives Query."""

    symbol: str = Field(description=QUERY_DESCRIPTIONS.get("symbol", ""))

    @field_validator("symbol", mode="before", check_fields=False)
    @classmethod
    def to_upper(cls, v: str) -> str:
        """Convert field to uppercase."""
        return v.upper()


class KeyExecutivesData(Data):
    """Key Executives Data."""

    title: str = Field(description="Designation of the key executive.")
    name: str = Field(description="Name of the key executive.")
    pay: int | None = Field(default=None, description="Pay of the key executive.")
    currency_pay: str | None = Field(default=None, description="Currency of the pay.")
    gender: str | None = Field(default=None, description="Gender of the key executive.")
    year_born: int | None = Field(
        default=None, description="Birth year of the key executive."
    )

```



---

## High-Level Overview

This is a **python** file named `key_executives.py`.

**Python Module**

- **Classes** (2): KeyExecutivesQueryParams, KeyExecutivesData
- **Functions** (1): to_upper
- **Import Statements**: 1


---

## Detailed Analysis

### Python Code Structure

#### Classes

- **`KeyExecutivesQueryParams`**(QueryParams)
- **`KeyExecutivesData`**(Data)

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

**Generated**: 2025-11-19T02:16:46.513872Z
**Generator**: World's Best Repo Book Generator v1.0

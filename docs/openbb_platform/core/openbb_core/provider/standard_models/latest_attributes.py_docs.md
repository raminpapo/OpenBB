# File Documentation: latest_attributes.py

## Metadata
- **Path**: `openbb_platform/core/openbb_core/provider/standard_models/latest_attributes.py`
- **Size**: 1,371 bytes
- **Lines**: 41
- **Category**: python
- **Extension**: .py

---

## Original Source

```python
"""Latest Attributes Standard Model."""

from openbb_core.provider.abstract.data import Data
from openbb_core.provider.abstract.query_params import QueryParams
from openbb_core.provider.utils.descriptions import (
    DATA_DESCRIPTIONS,
    QUERY_DESCRIPTIONS,
)
from pydantic import Field, field_validator


class LatestAttributesQueryParams(QueryParams):
    """Latest Attributes Query."""

    symbol: str = Field(description=QUERY_DESCRIPTIONS.get("symbol"))
    tag: str = Field(description="Intrinio data tag ID or code.")

    @field_validator("tag", mode="before", check_fields=False)
    @classmethod
    def multiple_tags(cls, v: str | list[str] | set[str]):
        """Accept a comma-separated string or list of tags."""
        if isinstance(v, str):
            return v.lower()
        return ",".join([tag.lower() for tag in list(v)])

    @field_validator("symbol", mode="before", check_fields=False)
    @classmethod
    def to_upper(cls, v: str) -> str:
        """Convert field to uppercase."""
        return v.upper()


class LatestAttributesData(Data):
    """Latest Attributes Data."""

    symbol: str = Field(description=DATA_DESCRIPTIONS.get("symbol"))
    tag: str | None = Field(default=None, description="Tag name for the fetched data.")
    value: str | float | None = Field(
        default=None, description="The value of the data."
    )

```



---

## High-Level Overview

This is a **python** file named `latest_attributes.py`.

**Python Module**

- **Classes** (2): LatestAttributesQueryParams, LatestAttributesData
- **Functions** (2): multiple_tags, to_upper
- **Import Statements**: 2


---

## Detailed Analysis

### Python Code Structure

#### Classes

- **`LatestAttributesQueryParams`**(QueryParams)
- **`LatestAttributesData`**(Data)

#### Functions

- **`multiple_tags(cls, v: str | list[str] | set[str])`**

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

**Generated**: 2025-11-19T02:16:46.516443Z
**Generator**: World's Best Repo Book Generator v1.0

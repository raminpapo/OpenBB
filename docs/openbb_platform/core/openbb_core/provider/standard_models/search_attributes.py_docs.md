# File Documentation: search_attributes.py

## Metadata
- **Path**: `openbb_platform/core/openbb_core/provider/standard_models/search_attributes.py`
- **Size**: 1,661 bytes
- **Lines**: 45
- **Category**: python
- **Extension**: .py

---

## Original Source

```python
"""Search Attributes Standard Model."""

from openbb_core.provider.abstract.data import Data
from openbb_core.provider.abstract.query_params import QueryParams
from openbb_core.provider.utils.descriptions import QUERY_DESCRIPTIONS
from pydantic import Field


class SearchAttributesQueryParams(QueryParams):
    """Search Attributes Query."""

    query: str = Field(description="Query to search for.")
    limit: int | None = Field(default=1000, description=QUERY_DESCRIPTIONS.get("limit"))


class SearchAttributesData(Data):
    """Search Attributes Data."""

    id: str = Field(description="ID of the financial attribute.")
    name: str = Field(description="Name of the financial attribute.")
    tag: str = Field(description="Tag of the financial attribute.")
    statement_code: str = Field(description="Code of the financial statement.")
    statement_type: str | None = Field(
        default=None, description="Type of the financial statement."
    )
    parent_name: str | None = Field(
        default=None, description="Parent's name of the financial attribute."
    )
    sequence: int | None = Field(
        default=None, description="Sequence of the financial statement."
    )
    factor: str | None = Field(
        default=None, description="Unit of the financial attribute."
    )
    transaction: str | None = Field(
        default=None,
        description="Transaction type (credit/debit) of the financial attribute.",
    )
    type: str | None = Field(
        default=None, description="Type of the financial attribute."
    )
    unit: str | None = Field(
        default=None, description="Unit of the financial attribute."
    )

```



---

## High-Level Overview

This is a **python** file named `search_attributes.py`.

**Python Module**

- **Classes** (2): SearchAttributesQueryParams, SearchAttributesData
- **Import Statements**: 1


---

## Detailed Analysis

### Python Code Structure

#### Classes

- **`SearchAttributesQueryParams`**(QueryParams)
- **`SearchAttributesData`**(Data)


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

**Generated**: 2025-11-19T02:16:46.562530Z
**Generator**: World's Best Repo Book Generator v1.0

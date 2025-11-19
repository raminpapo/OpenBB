# File Documentation: analyst_search.py

## Metadata
- **Path**: `openbb_platform/core/openbb_core/provider/standard_models/analyst_search.py`
- **Size**: 1,223 bytes
- **Lines**: 49
- **Category**: python
- **Extension**: .py

---

## Original Source

```python
"""Analyst Search Standard Model."""

from datetime import (
    datetime,
)

from openbb_core.provider.abstract.data import Data
from openbb_core.provider.abstract.query_params import QueryParams
from pydantic import Field


class AnalystSearchQueryParams(QueryParams):
    """Analyst Search Query."""

    analyst_name: str | None = Field(
        default=None,
        description="Analyst names to return."
        + " Omitting will return all available analysts.",
    )
    firm_name: str | None = Field(
        default=None,
        description="Firm names to return."
        + " Omitting will return all available firms.",
    )


class AnalystSearchData(Data):
    """Analyst Search data."""

    last_updated: datetime | None = Field(
        default=None,
        description="Date of the last update.",
    )
    firm_name: str | None = Field(
        default=None,
        description="Firm name of the analyst.",
    )
    name_first: str | None = Field(
        default=None,
        description="Analyst first name.",
    )
    name_last: str | None = Field(
        default=None,
        description="Analyst last name.",
    )
    name_full: str = Field(
        description="Analyst full name.",
    )

```



---

## High-Level Overview

This is a **python** file named `analyst_search.py`.

**Python Module**

- **Classes** (2): AnalystSearchQueryParams, AnalystSearchData
- **Import Statements**: 1


---

## Detailed Analysis

### Python Code Structure

#### Classes

- **`AnalystSearchQueryParams`**(QueryParams)
- **`AnalystSearchData`**(Data)


---

## Related Files

The following files may be related based on imports and references:

**Imported Modules**:
- `Data`
- `Field`
- `QueryParams`
- `datetime`
- `openbb_core.provider.abstract.data`
- `openbb_core.provider.abstract.query_params`
- `pydantic`


---

## Performance & Security Notes

No obvious security concerns detected in static analysis.


---

**Generated**: 2025-11-19T02:16:46.342093Z
**Generator**: World's Best Repo Book Generator v1.0

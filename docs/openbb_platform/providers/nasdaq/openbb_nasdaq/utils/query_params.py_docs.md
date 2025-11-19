# File Documentation: query_params.py

## Metadata
- **Path**: `openbb_platform/providers/nasdaq/openbb_nasdaq/utils/query_params.py`
- **Size**: 1,037 bytes
- **Lines**: 31
- **Category**: python
- **Extension**: .py

---

## Original Source

```python
"""Nasdaq Data Link Standard Query Params."""

from datetime import date as dateType
from typing import Literal

from openbb_core.provider.abstract.query_params import QueryParams
from openbb_core.provider.utils.descriptions import QUERY_DESCRIPTIONS
from pydantic import Field


class DataLinkQueryParams(QueryParams):
    """Standard Nasdaq Data Link Query Params"""

    start_date: dateType | None = Field(
        description=QUERY_DESCRIPTIONS.get("start_date", ""), default=None
    )
    end_date: dateType | None = Field(
        description=QUERY_DESCRIPTIONS.get("start_date", ""),
        default=None,
    )
    transform: Literal["diff", "rdiff", "cumul", "normalize", None] = Field(
        description="Transform the data as difference, percent change, cumulative, or normalize.",
        default=None,
    )
    collapse: Literal["daily", "weekly", "monthly", "quarterly", "annual", None] = (
        Field(
            description="Collapse the frequency of the time series.",
            default=None,
        )
    )

```



---

## High-Level Overview

This is a **python** file named `query_params.py`.

**Python Module**

- **Classes** (1): DataLinkQueryParams
- **Import Statements**: 1


---

## Detailed Analysis

### Python Code Structure

#### Classes

- **`DataLinkQueryParams`**(QueryParams)


---

## Related Files

The following files may be related based on imports and references:

**Imported Modules**:
- `Field`
- `Literal`
- `QUERY_DESCRIPTIONS`
- `QueryParams`
- `date`
- `datetime`
- `openbb_core.provider.abstract.query_params`
- `openbb_core.provider.utils.descriptions`
- `pydantic`
- `typing`


---

## Performance & Security Notes

No obvious security concerns detected in static analysis.


---

**Generated**: 2025-11-19T02:16:51.660557Z
**Generator**: World's Best Repo Book Generator v1.0

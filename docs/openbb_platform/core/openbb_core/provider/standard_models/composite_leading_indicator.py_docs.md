# File Documentation: composite_leading_indicator.py

## Metadata
- **Path**: `openbb_platform/core/openbb_core/provider/standard_models/composite_leading_indicator.py`
- **Size**: 1,049 bytes
- **Lines**: 35
- **Category**: python
- **Extension**: .py

---

## Original Source

```python
"""Composite Leading Indicator Standard Model."""

from datetime import date as dateType

from openbb_core.provider.abstract.data import Data
from openbb_core.provider.abstract.query_params import QueryParams
from openbb_core.provider.utils.descriptions import (
    DATA_DESCRIPTIONS,
    QUERY_DESCRIPTIONS,
)
from pydantic import Field


class CompositeLeadingIndicatorQueryParams(QueryParams):
    """Composite Leading Indicator Query."""

    start_date: dateType | None = Field(
        default=None, description=QUERY_DESCRIPTIONS.get("start_date")
    )
    end_date: dateType | None = Field(
        default=None, description=QUERY_DESCRIPTIONS.get("end_date")
    )


class CompositeLeadingIndicatorData(Data):
    """Composite Leading Indicator Data."""

    date: dateType = Field(description=DATA_DESCRIPTIONS.get("date"))
    value: float = Field(
        default=None,
        description="CLI value",
        json_schema_extra={"x-unit_measurement": "index"},
    )
    country: str = Field(description="Country for the CLI value.")

```



---

## High-Level Overview

This is a **python** file named `composite_leading_indicator.py`.

**Python Module**

- **Classes** (2): CompositeLeadingIndicatorQueryParams, CompositeLeadingIndicatorData
- **Import Statements**: 2


---

## Detailed Analysis

### Python Code Structure

#### Classes

- **`CompositeLeadingIndicatorQueryParams`**(QueryParams)
- **`CompositeLeadingIndicatorData`**(Data)


---

## Related Files

The following files may be related based on imports and references:

**Imported Modules**:
- `Data`
- `Field`
- `QueryParams`
- `date`
- `datetime`
- `openbb_core.provider.abstract.data`
- `openbb_core.provider.abstract.query_params`
- `openbb_core.provider.utils.descriptions`
- `pydantic`


---

## Performance & Security Notes

No obvious security concerns detected in static analysis.


---

**Generated**: 2025-11-19T02:16:46.386863Z
**Generator**: World's Best Repo Book Generator v1.0

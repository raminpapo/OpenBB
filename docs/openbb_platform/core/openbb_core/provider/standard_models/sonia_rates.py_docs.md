# File Documentation: sonia_rates.py

## Metadata
- **Path**: `openbb_platform/core/openbb_core/provider/standard_models/sonia_rates.py`
- **Size**: 818 bytes
- **Lines**: 32
- **Category**: python
- **Extension**: .py

---

## Original Source

```python
"""SONIA Standard Model."""

from datetime import date as dateType

from openbb_core.provider.abstract.data import Data
from openbb_core.provider.abstract.query_params import QueryParams
from openbb_core.provider.utils.descriptions import (
    DATA_DESCRIPTIONS,
    QUERY_DESCRIPTIONS,
)
from pydantic import Field


class SONIAQueryParams(QueryParams):
    """SONIA Query."""

    start_date: dateType | None = Field(
        default=None,
        description=QUERY_DESCRIPTIONS.get("start_date", ""),
    )
    end_date: dateType | None = Field(
        default=None,
        description=QUERY_DESCRIPTIONS.get("end_date", ""),
    )


class SONIAData(Data):
    """SONIA Data."""

    date: dateType = Field(description=DATA_DESCRIPTIONS.get("date", ""))
    rate: float | None = Field(description="SONIA rate.")

```



---

## High-Level Overview

This is a **python** file named `sonia_rates.py`.

**Python Module**

- **Classes** (2): SONIAQueryParams, SONIAData
- **Import Statements**: 2


---

## Detailed Analysis

### Python Code Structure

#### Classes

- **`SONIAQueryParams`**(QueryParams)
- **`SONIAData`**(Data)


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

**Generated**: 2025-11-19T02:16:46.575887Z
**Generator**: World's Best Repo Book Generator v1.0

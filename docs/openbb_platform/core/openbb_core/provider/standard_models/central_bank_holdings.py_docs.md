# File Documentation: central_bank_holdings.py

## Metadata
- **Path**: `openbb_platform/core/openbb_core/provider/standard_models/central_bank_holdings.py`
- **Size**: 706 bytes
- **Lines**: 29
- **Category**: python
- **Extension**: .py

---

## Original Source

```python
"""Central Bank Holdings Standard Model."""

from datetime import (
    date as dateType,
)

from openbb_core.provider.abstract.data import Data
from openbb_core.provider.abstract.query_params import QueryParams
from openbb_core.provider.utils.descriptions import (
    DATA_DESCRIPTIONS,
    QUERY_DESCRIPTIONS,
)
from pydantic import Field


class CentralBankHoldingsQueryParams(QueryParams):
    """Central Bank Holdings Query."""

    date: dateType | None = Field(
        default=None,
        description=QUERY_DESCRIPTIONS.get("date", ""),
    )


class CentralBankHoldingsData(Data):
    """Central Bank Holdings Data."""

    date: dateType = Field(description=DATA_DESCRIPTIONS.get("date", ""))

```



---

## High-Level Overview

This is a **python** file named `central_bank_holdings.py`.

**Python Module**

- **Classes** (2): CentralBankHoldingsQueryParams, CentralBankHoldingsData
- **Import Statements**: 2


---

## Detailed Analysis

### Python Code Structure

#### Classes

- **`CentralBankHoldingsQueryParams`**(QueryParams)
- **`CentralBankHoldingsData`**(Data)


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
- `openbb_core.provider.utils.descriptions`
- `pydantic`


---

## Performance & Security Notes

No obvious security concerns detected in static analysis.


---

**Generated**: 2025-11-19T02:16:46.373579Z
**Generator**: World's Best Repo Book Generator v1.0

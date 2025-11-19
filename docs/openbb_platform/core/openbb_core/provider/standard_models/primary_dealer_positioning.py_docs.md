# File Documentation: primary_dealer_positioning.py

## Metadata
- **Path**: `openbb_platform/core/openbb_core/provider/standard_models/primary_dealer_positioning.py`
- **Size**: 925 bytes
- **Lines**: 32
- **Category**: python
- **Extension**: .py

---

## Original Source

```python
"""Primray Dealer Positioning Standard Model."""

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


class PrimaryDealerPositioningQueryParams(QueryParams):
    """Primary Dealer Positioning Query."""

    start_date: dateType | None = Field(
        default=None, description=QUERY_DESCRIPTIONS.get("start_date", "")
    )
    end_date: dateType | None = Field(
        default=None, description=QUERY_DESCRIPTIONS.get("end_date", "")
    )


class PrimaryDealerPositioningData(Data):
    """Primary Dealer Positioning Data."""

    date: dateType = Field(description=DATA_DESCRIPTIONS.get("date", ""))
    symbol: str = Field(description=DATA_DESCRIPTIONS.get("symbol", ""))

```



---

## High-Level Overview

This is a **python** file named `primary_dealer_positioning.py`.

**Python Module**

- **Classes** (2): PrimaryDealerPositioningQueryParams, PrimaryDealerPositioningData
- **Import Statements**: 2


---

## Detailed Analysis

### Python Code Structure

#### Classes

- **`PrimaryDealerPositioningQueryParams`**(QueryParams)
- **`PrimaryDealerPositioningData`**(Data)


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

**Generated**: 2025-11-19T02:16:46.552476Z
**Generator**: World's Best Repo Book Generator v1.0

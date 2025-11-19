# File Documentation: otc_aggregate.py

## Metadata
- **Path**: `openbb_platform/core/openbb_core/provider/standard_models/otc_aggregate.py`
- **Size**: 986 bytes
- **Lines**: 32
- **Category**: python
- **Extension**: .py

---

## Original Source

```python
"""OTC Aggregate Standard Model."""

from datetime import date as dateType

from openbb_core.provider.abstract.data import Data
from openbb_core.provider.abstract.query_params import QueryParams
from openbb_core.provider.utils.descriptions import QUERY_DESCRIPTIONS
from pydantic import Field


class OTCAggregateQueryParams(QueryParams):
    """OTC Aggregate Query."""

    symbol: str | None = Field(
        description=QUERY_DESCRIPTIONS.get("symbol", ""),
        default=None,
    )


class OTCAggregateData(Data):
    """OTC Aggregate Data."""

    update_date: dateType = Field(
        description="Most recent date on which total trades is updated based on data received from each ATS/OTC."
    )
    share_quantity: float = Field(
        description="Aggregate weekly total number of shares reported by each ATS for the Symbol."
    )
    trade_quantity: float = Field(
        description="Aggregate weekly total number of trades reported by each ATS for the Symbol"
    )

```



---

## High-Level Overview

This is a **python** file named `otc_aggregate.py`.

**Python Module**

- **Classes** (2): OTCAggregateQueryParams, OTCAggregateData
- **Import Statements**: 1


---

## Detailed Analysis

### Python Code Structure

#### Classes

- **`OTCAggregateQueryParams`**(QueryParams)
- **`OTCAggregateData`**(Data)


---

## Related Files

The following files may be related based on imports and references:

**Imported Modules**:
- `Data`
- `Field`
- `QUERY_DESCRIPTIONS`
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

**Generated**: 2025-11-19T02:16:46.540904Z
**Generator**: World's Best Repo Book Generator v1.0

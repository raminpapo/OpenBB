# File Documentation: top_retail.py

## Metadata
- **Path**: `openbb_platform/core/openbb_core/provider/standard_models/top_retail.py`
- **Size**: 874 bytes
- **Lines**: 29
- **Category**: python
- **Extension**: .py

---

## Original Source

```python
"""Top Retail Standard Model."""

from datetime import date as DateType

from openbb_core.provider.abstract.data import Data
from openbb_core.provider.abstract.query_params import QueryParams
from openbb_core.provider.utils.descriptions import (
    DATA_DESCRIPTIONS,
    QUERY_DESCRIPTIONS,
)
from pydantic import Field


class TopRetailQueryParams(QueryParams):
    """Top Retail Search Query."""

    limit: int = Field(description=QUERY_DESCRIPTIONS.get("limit", ""), default=5)


class TopRetailData(Data):
    """Top Retail Search Data."""

    date: DateType = Field(description=DATA_DESCRIPTIONS.get("date", ""))
    symbol: str = Field(description=DATA_DESCRIPTIONS.get("symbol", ""))
    activity: float = Field(description="Activity of the symbol.")
    sentiment: float = Field(
        description="Sentiment of the symbol. 1 is bullish, -1 is bearish."
    )

```



---

## High-Level Overview

This is a **python** file named `top_retail.py`.

**Python Module**

- **Classes** (2): TopRetailQueryParams, TopRetailData
- **Import Statements**: 2


---

## Detailed Analysis

### Python Code Structure

#### Classes

- **`TopRetailQueryParams`**(QueryParams)
- **`TopRetailData`**(Data)


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

**Generated**: 2025-11-19T02:16:46.585959Z
**Generator**: World's Best Repo Book Generator v1.0

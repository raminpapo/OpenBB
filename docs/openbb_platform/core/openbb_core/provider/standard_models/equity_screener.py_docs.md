# File Documentation: equity_screener.py

## Metadata
- **Path**: `openbb_platform/core/openbb_core/provider/standard_models/equity_screener.py`
- **Size**: 555 bytes
- **Lines**: 18
- **Category**: python
- **Extension**: .py

---

## Original Source

```python
"""Equity Screener Standard Model."""

from openbb_core.provider.abstract.data import Data
from openbb_core.provider.abstract.query_params import QueryParams
from openbb_core.provider.utils.descriptions import DATA_DESCRIPTIONS
from pydantic import Field


class EquityScreenerQueryParams(QueryParams):
    """Equity Screener Query."""


class EquityScreenerData(Data):
    """Equity Screener Data."""

    symbol: str = Field(description=DATA_DESCRIPTIONS.get("symbol", ""))
    name: str | None = Field(default=None, description="Name of the company.")

```



---

## High-Level Overview

This is a **python** file named `equity_screener.py`.

**Python Module**

- **Classes** (2): EquityScreenerQueryParams, EquityScreenerData
- **Import Statements**: 1


---

## Detailed Analysis

### Python Code Structure

#### Classes

- **`EquityScreenerQueryParams`**(QueryParams)
- **`EquityScreenerData`**(Data)


---

## Related Files

The following files may be related based on imports and references:

**Imported Modules**:
- `DATA_DESCRIPTIONS`
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

**Generated**: 2025-11-19T02:16:46.430658Z
**Generator**: World's Best Repo Book Generator v1.0

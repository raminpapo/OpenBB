# File Documentation: futures_info.py

## Metadata
- **Path**: `openbb_platform/core/openbb_core/provider/standard_models/futures_info.py`
- **Size**: 547 bytes
- **Lines**: 19
- **Category**: python
- **Extension**: .py

---

## Original Source

```python
"""Futures Info Standard Model."""

from openbb_core.provider.abstract.data import Data
from openbb_core.provider.abstract.query_params import QueryParams
from openbb_core.provider.utils.descriptions import DATA_DESCRIPTIONS
from pydantic import Field


class FuturesInfoQueryParams(QueryParams):
    """Futures Info Query."""

    # leaving this empty to let the provider create custom symbol docstrings.


class FuturesInfoData(Data):
    """Futures Instruments Data."""

    symbol: str = Field(description=DATA_DESCRIPTIONS.get("symbol", ""))

```



---

## High-Level Overview

This is a **python** file named `futures_info.py`.

**Python Module**

- **Classes** (2): FuturesInfoQueryParams, FuturesInfoData
- **Import Statements**: 1


---

## Detailed Analysis

### Python Code Structure

#### Classes

- **`FuturesInfoQueryParams`**(QueryParams)
- **`FuturesInfoData`**(Data)


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

**Generated**: 2025-11-19T02:16:46.479623Z
**Generator**: World's Best Repo Book Generator v1.0

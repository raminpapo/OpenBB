# File Documentation: futures_instruments.py

## Metadata
- **Path**: `openbb_platform/core/openbb_core/provider/standard_models/futures_instruments.py`
- **Size**: 325 bytes
- **Lines**: 13
- **Category**: python
- **Extension**: .py

---

## Original Source

```python
"""Futures Instruments Standard Model."""

from openbb_core.provider.abstract.data import Data
from openbb_core.provider.abstract.query_params import QueryParams


class FuturesInstrumentsQueryParams(QueryParams):
    """Futures Instruments Query."""


class FuturesInstrumentsData(Data):
    """Futures Instruments Data."""

```



---

## High-Level Overview

This is a **python** file named `futures_instruments.py`.

**Python Module**

- **Classes** (2): FuturesInstrumentsQueryParams, FuturesInstrumentsData
- **Import Statements**: 1


---

## Detailed Analysis

### Python Code Structure

#### Classes

- **`FuturesInstrumentsQueryParams`**(QueryParams)
- **`FuturesInstrumentsData`**(Data)


---

## Related Files

The following files may be related based on imports and references:

**Imported Modules**:
- `Data`
- `QueryParams`
- `openbb_core.provider.abstract.data`
- `openbb_core.provider.abstract.query_params`


---

## Performance & Security Notes

No obvious security concerns detected in static analysis.


---

**Generated**: 2025-11-19T02:16:46.480812Z
**Generator**: World's Best Repo Book Generator v1.0

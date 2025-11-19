# File Documentation: crypto_search.py

## Metadata
- **Path**: `openbb_platform/core/openbb_core/provider/standard_models/crypto_search.py`
- **Size**: 632 bytes
- **Lines**: 20
- **Category**: python
- **Extension**: .py

---

## Original Source

```python
"""Crypto Search Standard Model."""

from openbb_core.provider.abstract.data import Data
from openbb_core.provider.abstract.query_params import QueryParams
from openbb_core.provider.utils.descriptions import DATA_DESCRIPTIONS
from pydantic import Field


class CryptoSearchQueryParams(QueryParams):
    """Crypto Search Query."""

    query: str | None = Field(description="Search query.", default=None)


class CryptoSearchData(Data):
    """Crypto Search Data."""

    symbol: str = Field(description=DATA_DESCRIPTIONS.get("symbol", "") + " (Crypto)")
    name: str | None = Field(description="Name of the crypto.", default=None)

```



---

## High-Level Overview

This is a **python** file named `crypto_search.py`.

**Python Module**

- **Classes** (2): CryptoSearchQueryParams, CryptoSearchData
- **Import Statements**: 1


---

## Detailed Analysis

### Python Code Structure

#### Classes

- **`CryptoSearchQueryParams`**(QueryParams)
- **`CryptoSearchData`**(Data)


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

**Generated**: 2025-11-19T02:16:46.398251Z
**Generator**: World's Best Repo Book Generator v1.0

# File Documentation: etf_search.py

## Metadata
- **Path**: `openbb_platform/core/openbb_core/provider/standard_models/etf_search.py`
- **Size**: 608 bytes
- **Lines**: 20
- **Category**: python
- **Extension**: .py

---

## Original Source

```python
"""ETF Search Standard Model."""

from openbb_core.provider.abstract.data import Data
from openbb_core.provider.abstract.query_params import QueryParams
from openbb_core.provider.utils.descriptions import DATA_DESCRIPTIONS
from pydantic import Field


class EtfSearchQueryParams(QueryParams):
    """ETF Search Query."""

    query: str | None = Field(description="Search query.", default="")


class EtfSearchData(Data):
    """ETF Search Data."""

    symbol: str = Field(description=DATA_DESCRIPTIONS.get("symbol", "") + "(ETF)")
    name: str | None = Field(description="Name of the ETF.", default=None)

```



---

## High-Level Overview

This is a **python** file named `etf_search.py`.

**Python Module**

- **Classes** (2): EtfSearchQueryParams, EtfSearchData
- **Import Statements**: 1


---

## Detailed Analysis

### Python Code Structure

#### Classes

- **`EtfSearchQueryParams`**(QueryParams)
- **`EtfSearchData`**(Data)


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

**Generated**: 2025-11-19T02:16:46.449091Z
**Generator**: World's Best Repo Book Generator v1.0

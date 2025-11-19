# File Documentation: currency_pairs.py

## Metadata
- **Path**: `openbb_platform/core/openbb_core/provider/standard_models/currency_pairs.py`
- **Size**: 696 bytes
- **Lines**: 22
- **Category**: python
- **Extension**: .py

---

## Original Source

```python
"""Currency Available Pairs Standard Model."""

from openbb_core.provider.abstract.data import Data
from openbb_core.provider.abstract.query_params import QueryParams
from openbb_core.provider.utils.descriptions import DATA_DESCRIPTIONS
from pydantic import Field


class CurrencyPairsQueryParams(QueryParams):
    """Currency Available Pairs Query."""

    query: str | None = Field(
        default=None, description="Query to search for currency pairs."
    )


class CurrencyPairsData(Data):
    """Currency Available Pairs Data."""

    symbol: str = Field(description=DATA_DESCRIPTIONS.get("symbol", ""))
    name: str | None = Field(default=None, description="Name of the currency pair.")

```



---

## High-Level Overview

This is a **python** file named `currency_pairs.py`.

**Python Module**

- **Classes** (2): CurrencyPairsQueryParams, CurrencyPairsData
- **Import Statements**: 1


---

## Detailed Analysis

### Python Code Structure

#### Classes

- **`CurrencyPairsQueryParams`**(QueryParams)
- **`CurrencyPairsData`**(Data)


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

**Generated**: 2025-11-19T02:16:46.401067Z
**Generator**: World's Best Repo Book Generator v1.0

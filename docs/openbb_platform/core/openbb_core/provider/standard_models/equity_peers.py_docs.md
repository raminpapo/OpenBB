# File Documentation: equity_peers.py

## Metadata
- **Path**: `openbb_platform/core/openbb_core/provider/standard_models/equity_peers.py`
- **Size**: 775 bytes
- **Lines**: 28
- **Category**: python
- **Extension**: .py

---

## Original Source

```python
"""Equity Peers Standard Model."""

from openbb_core.provider.abstract.data import Data
from openbb_core.provider.abstract.query_params import QueryParams
from openbb_core.provider.utils.descriptions import (
    DATA_DESCRIPTIONS,
    QUERY_DESCRIPTIONS,
)
from pydantic import Field, field_validator


class EquityPeersQueryParams(QueryParams):
    """Equity Peers Query."""

    symbol: str = Field(description=QUERY_DESCRIPTIONS.get("symbol", ""))

    @field_validator("symbol", mode="before", check_fields=False)
    @classmethod
    def to_upper(cls, v: str) -> str:
        """Convert field to uppercase."""
        return v.upper()


class EquityPeersData(Data):
    """Equity Peers Data."""

    symbol: str = Field(description=DATA_DESCRIPTIONS.get("symbol", ""))

```



---

## High-Level Overview

This is a **python** file named `equity_peers.py`.

**Python Module**

- **Classes** (2): EquityPeersQueryParams, EquityPeersData
- **Functions** (1): to_upper
- **Import Statements**: 2


---

## Detailed Analysis

### Python Code Structure

#### Classes

- **`EquityPeersQueryParams`**(QueryParams)
- **`EquityPeersData`**(Data)

#### Decorators Used

classmethod, field_validator


---

## Related Files

The following files may be related based on imports and references:

**Imported Modules**:
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

**Generated**: 2025-11-19T02:16:46.425592Z
**Generator**: World's Best Repo Book Generator v1.0

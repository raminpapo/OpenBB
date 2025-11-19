# File Documentation: etf_holdings.py

## Metadata
- **Path**: `openbb_platform/core/openbb_core/provider/standard_models/etf_holdings.py`
- **Size**: 886 bytes
- **Lines**: 34
- **Category**: python
- **Extension**: .py

---

## Original Source

```python
"""ETF Holdings Standard Model."""

from openbb_core.provider.abstract.data import Data
from openbb_core.provider.abstract.query_params import QueryParams
from openbb_core.provider.utils.descriptions import (
    DATA_DESCRIPTIONS,
    QUERY_DESCRIPTIONS,
)
from pydantic import Field, field_validator


class EtfHoldingsQueryParams(QueryParams):
    """ETF Holdings Query."""

    symbol: str = Field(description=QUERY_DESCRIPTIONS.get("symbol", "") + " (ETF)")

    @field_validator("symbol")
    @classmethod
    def to_upper(cls, v: str) -> str:
        """Convert field to uppercase."""
        return v.upper()


class EtfHoldingsData(Data):
    """ETF Holdings Data."""

    symbol: str | None = Field(
        default=None, description=DATA_DESCRIPTIONS.get("symbol", "")
    )
    name: str | None = Field(
        default=None,
        description="Name of the asset.",
    )

```



---

## High-Level Overview

This is a **python** file named `etf_holdings.py`.

**Python Module**

- **Classes** (2): EtfHoldingsQueryParams, EtfHoldingsData
- **Functions** (1): to_upper
- **Import Statements**: 2


---

## Detailed Analysis

### Python Code Structure

#### Classes

- **`EtfHoldingsQueryParams`**(QueryParams)
- **`EtfHoldingsData`**(Data)

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

**Generated**: 2025-11-19T02:16:46.444981Z
**Generator**: World's Best Repo Book Generator v1.0

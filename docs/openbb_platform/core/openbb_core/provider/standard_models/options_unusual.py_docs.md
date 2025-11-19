# File Documentation: options_unusual.py

## Metadata
- **Path**: `openbb_platform/core/openbb_core/provider/standard_models/options_unusual.py`
- **Size**: 1,035 bytes
- **Lines**: 35
- **Category**: python
- **Extension**: .py

---

## Original Source

```python
"""Unusual Options Standard Model."""

from openbb_core.provider.abstract.data import Data
from openbb_core.provider.abstract.query_params import QueryParams
from openbb_core.provider.utils.descriptions import (
    DATA_DESCRIPTIONS,
    QUERY_DESCRIPTIONS,
)
from pydantic import Field, field_validator


class OptionsUnusualQueryParams(QueryParams):
    """Unusual Options Query."""

    symbol: str | None = Field(
        default=None,
        description=QUERY_DESCRIPTIONS.get("symbol", "") + " (the underlying symbol)",
    )

    @field_validator("symbol", mode="before", check_fields=False)
    @classmethod
    def to_upper(cls, v: str):
        """Convert field to uppercase."""
        return v.upper() if v else None


class OptionsUnusualData(Data):
    """Unusual Options Data."""

    underlying_symbol: str | None = Field(
        description=DATA_DESCRIPTIONS.get("symbol", "") + " (the underlying symbol)",
        default=None,
    )
    contract_symbol: str = Field(description="Contract symbol for the option.")

```



---

## High-Level Overview

This is a **python** file named `options_unusual.py`.

**Python Module**

- **Classes** (2): OptionsUnusualQueryParams, OptionsUnusualData
- **Functions** (1): to_upper
- **Import Statements**: 2


---

## Detailed Analysis

### Python Code Structure

#### Classes

- **`OptionsUnusualQueryParams`**(QueryParams)
- **`OptionsUnusualData`**(Data)

#### Functions

- **`to_upper(cls, v: str)`**

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

**Generated**: 2025-11-19T02:16:46.539670Z
**Generator**: World's Best Repo Book Generator v1.0

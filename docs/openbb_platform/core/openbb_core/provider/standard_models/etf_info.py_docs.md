# File Documentation: etf_info.py

## Metadata
- **Path**: `openbb_platform/core/openbb_core/provider/standard_models/etf_info.py`
- **Size**: 1,303 bytes
- **Lines**: 40
- **Category**: python
- **Extension**: .py

---

## Original Source

```python
"""ETF Info Standard Model."""

from datetime import date as dateType

from openbb_core.provider.abstract.data import Data
from openbb_core.provider.abstract.query_params import QueryParams
from openbb_core.provider.utils.descriptions import (
    DATA_DESCRIPTIONS,
    QUERY_DESCRIPTIONS,
)
from pydantic import Field, field_validator


class EtfInfoQueryParams(QueryParams):
    """ETF Info Query."""

    symbol: str = Field(description=QUERY_DESCRIPTIONS.get("symbol", "") + " (ETF)")

    @field_validator("symbol")
    @classmethod
    def to_upper(cls, v: str) -> str:
        """Convert field to uppercase."""
        return v.upper()


class EtfInfoData(Data):
    """ETF Info Data."""

    symbol: str = Field(description=DATA_DESCRIPTIONS.get("symbol", "") + " (ETF)")
    name: str | None = Field(description="Name of the ETF.")
    issuer: str | None = Field(default=None, description="Issuer of the ETF.")
    domicile: str | None = Field(default=None, description="Domicile of the ETF.")
    website: str | None = Field(default=None, description="Website of the ETF.")
    description: str | None = Field(
        default=None, description="Description of the fund."
    )
    inception_date: dateType | None = Field(
        default=None, description="Inception date of the ETF."
    )

```



---

## High-Level Overview

This is a **python** file named `etf_info.py`.

**Python Module**

- **Classes** (2): EtfInfoQueryParams, EtfInfoData
- **Functions** (1): to_upper
- **Import Statements**: 2


---

## Detailed Analysis

### Python Code Structure

#### Classes

- **`EtfInfoQueryParams`**(QueryParams)
- **`EtfInfoData`**(Data)

#### Decorators Used

classmethod, field_validator


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

**Generated**: 2025-11-19T02:16:46.446282Z
**Generator**: World's Best Repo Book Generator v1.0

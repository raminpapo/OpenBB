# File Documentation: etf_sectors.py

## Metadata
- **Path**: `openbb_platform/core/openbb_core/provider/standard_models/etf_sectors.py`
- **Size**: 1,043 bytes
- **Lines**: 35
- **Category**: python
- **Extension**: .py

---

## Original Source

```python
"""ETF Sectors Standard Model."""

from openbb_core.provider.abstract.data import Data
from openbb_core.provider.abstract.query_params import QueryParams
from openbb_core.provider.utils.descriptions import (
    DATA_DESCRIPTIONS,
    QUERY_DESCRIPTIONS,
)
from pydantic import Field, field_validator


class EtfSectorsQueryParams(QueryParams):
    """ETF Sectors Query."""

    symbol: str = Field(description=QUERY_DESCRIPTIONS.get("symbol", "") + " (ETF)")

    @field_validator("symbol")
    @classmethod
    def to_upper(cls, v: str) -> str:
        """Convert field to uppercase."""
        return v.upper()


class EtfSectorsData(Data):
    """ETF Sectors Data."""

    symbol: str | None = Field(
        default=None, description=DATA_DESCRIPTIONS.get("symbol", "")
    )
    sector: str = Field(description="Sector of exposure.")
    weight: float = Field(
        description="Sector exposure for the ETF as a percent of total assets.",
        json_schema_extra={"x-unit_measurement": "percent", "x-frontend_multiply": 100},
    )

```



---

## High-Level Overview

This is a **python** file named `etf_sectors.py`.

**Python Module**

- **Classes** (2): EtfSectorsQueryParams, EtfSectorsData
- **Functions** (1): to_upper
- **Import Statements**: 2


---

## Detailed Analysis

### Python Code Structure

#### Classes

- **`EtfSectorsQueryParams`**(QueryParams)
- **`EtfSectorsData`**(Data)

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

**Generated**: 2025-11-19T02:16:46.450386Z
**Generator**: World's Best Repo Book Generator v1.0

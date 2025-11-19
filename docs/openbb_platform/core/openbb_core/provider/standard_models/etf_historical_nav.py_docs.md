# File Documentation: etf_historical_nav.py

## Metadata
- **Path**: `openbb_platform/core/openbb_core/provider/standard_models/etf_historical_nav.py`
- **Size**: 870 bytes
- **Lines**: 31
- **Category**: python
- **Extension**: .py

---

## Original Source

```python
"""ETF Historical NAV model."""

from datetime import date as dateType

from openbb_core.provider.abstract.data import Data
from openbb_core.provider.abstract.query_params import QueryParams
from openbb_core.provider.utils.descriptions import (
    DATA_DESCRIPTIONS,
    QUERY_DESCRIPTIONS,
)
from pydantic import Field, field_validator


class EtfHistoricalNavQueryParams(QueryParams):
    """ETF Historical NAV Query."""

    symbol: str = Field(description=QUERY_DESCRIPTIONS.get("symbol", ""))

    @field_validator("symbol")
    @classmethod
    def to_upper(cls, v: str) -> str:
        """Convert field to uppercase."""
        return v.upper()


class EtfHistoricalNavData(Data):
    """ETF Historical NAV Data."""

    date: dateType = Field(description=DATA_DESCRIPTIONS.get("date", ""))
    nav: float = Field(description="The net asset value on the date.")

```



---

## High-Level Overview

This is a **python** file named `etf_historical_nav.py`.

**Python Module**

- **Classes** (2): EtfHistoricalNavQueryParams, EtfHistoricalNavData
- **Functions** (1): to_upper
- **Import Statements**: 2


---

## Detailed Analysis

### Python Code Structure

#### Classes

- **`EtfHistoricalNavQueryParams`**(QueryParams)
- **`EtfHistoricalNavData`**(Data)

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

**Generated**: 2025-11-19T02:16:46.443706Z
**Generator**: World's Best Repo Book Generator v1.0

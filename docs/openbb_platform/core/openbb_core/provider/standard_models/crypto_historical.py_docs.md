# File Documentation: crypto_historical.py

## Metadata
- **Path**: `openbb_platform/core/openbb_core/provider/standard_models/crypto_historical.py`
- **Size**: 2,083 bytes
- **Lines**: 66
- **Category**: python
- **Extension**: .py

---

## Original Source

```python
"""Crypto Historical Price Standard Model."""

from datetime import (
    date as dateType,
    datetime,
)

from dateutil import parser
from openbb_core.provider.abstract.data import Data
from openbb_core.provider.abstract.query_params import QueryParams
from openbb_core.provider.utils.descriptions import (
    DATA_DESCRIPTIONS,
    QUERY_DESCRIPTIONS,
)
from pydantic import Field, field_validator


class CryptoHistoricalQueryParams(QueryParams):
    """Crypto Historical Price Query."""

    symbol: str = Field(description=QUERY_DESCRIPTIONS.get("symbol", ""))
    start_date: dateType | None = Field(
        default=None,
        description=QUERY_DESCRIPTIONS.get("start_date", ""),
    )
    end_date: dateType | None = Field(
        default=None,
        description=QUERY_DESCRIPTIONS.get("end_date", ""),
    )

    @field_validator("symbol", mode="before", check_fields=False)
    @classmethod
    def _to_upper(cls, v):
        """Convert field to uppercase and remove '-'."""
        return str(v).upper()


class CryptoHistoricalData(Data):
    """Crypto Historical Price Data."""

    date: dateType | datetime = Field(description=DATA_DESCRIPTIONS.get("date", ""))
    open: float | None = Field(
        default=None, description=DATA_DESCRIPTIONS.get("open", "")
    )
    high: float | None = Field(
        default=None, description=DATA_DESCRIPTIONS.get("high", "")
    )
    low: float | None = Field(
        default=None, description=DATA_DESCRIPTIONS.get("low", "")
    )
    close: float = Field(description=DATA_DESCRIPTIONS.get("close", ""))
    volume: float | None = Field(
        default=None, description=DATA_DESCRIPTIONS.get("volume", "")
    )
    vwap: float | None = Field(
        default=None, description=DATA_DESCRIPTIONS.get("vwap", "")
    )

    @field_validator("date", mode="before", check_fields=False)
    @classmethod
    def date_validate(cls, v):  # pylint: disable=E0213
        """Return formatted datetime."""
        if ":" in str(v):
            return parser.isoparse(str(v))
        return parser.parse(str(v)).date()

```



---

## High-Level Overview

This is a **python** file named `crypto_historical.py`.

**Python Module**

- **Classes** (2): CryptoHistoricalQueryParams, CryptoHistoricalData
- **Functions** (2): _to_upper, date_validate
- **Import Statements**: 2


---

## Detailed Analysis

### Python Code Structure

#### Classes

- **`CryptoHistoricalQueryParams`**(QueryParams)
- **`CryptoHistoricalData`**(Data)

#### Functions

- **`_to_upper(cls, v)`**
- **`date_validate(cls, v)`**

#### Decorators Used

classmethod, field_validator


---

## Related Files

The following files may be related based on imports and references:

**Imported Modules**:
- `Data`
- `Field`
- `QueryParams`
- `datetime`
- `dateutil`
- `openbb_core.provider.abstract.data`
- `openbb_core.provider.abstract.query_params`
- `openbb_core.provider.utils.descriptions`
- `parser`
- `pydantic`


---

## Performance & Security Notes

No obvious security concerns detected in static analysis.


---

**Generated**: 2025-11-19T02:16:46.396667Z
**Generator**: World's Best Repo Book Generator v1.0

# File Documentation: futures_curve.py

## Metadata
- **Path**: `openbb_platform/core/openbb_core/provider/standard_models/futures_curve.py`
- **Size**: 1,881 bytes
- **Lines**: 63
- **Category**: python
- **Extension**: .py

---

## Original Source

```python
"""Futures Curve Standard Model."""

from datetime import date as dateType

from openbb_core.provider.abstract.data import Data
from openbb_core.provider.abstract.query_params import QueryParams
from openbb_core.provider.utils.descriptions import (
    DATA_DESCRIPTIONS,
    QUERY_DESCRIPTIONS,
)
from pydantic import Field, field_validator


class FuturesCurveQueryParams(QueryParams):
    """Futures Curve Query."""

    symbol: str = Field(description=QUERY_DESCRIPTIONS.get("symbol", ""))
    date: dateType | str | None = Field(
        default=None,
        description=QUERY_DESCRIPTIONS.get("date", ""),
    )

    @field_validator("symbol", mode="before", check_fields=False)
    @classmethod
    def to_upper(cls, v):
        """Convert field to uppercase."""
        return v.upper()

    @field_validator("date", mode="before", check_fields=False)
    @classmethod
    def _validate_date(cls, v):
        """Validate the date."""
        # pylint: disable=import-outside-toplevel
        from pandas import to_datetime

        if v is None:
            return None
        if isinstance(v, dateType):
            return v.strftime("%Y-%m-%d")
        new_dates: list = []
        if isinstance(v, str):
            dates = v.split(",")
        if isinstance(v, list):
            dates = v
        for date in dates:
            new_dates.append(to_datetime(date).date().strftime("%Y-%m-%d"))

        return ",".join(new_dates) if new_dates else None


class FuturesCurveData(Data):
    """Futures Curve Data."""

    date: dateType | None = Field(
        default=None, description=DATA_DESCRIPTIONS.get("date", "")
    )
    expiration: str = Field(description="Futures expiration month.")
    price: float = Field(
        default=None,
        description="The price of the futures contract.",
        json_schema_extra={"x-unit_measurement": "currency"},
    )

```



---

## High-Level Overview

This is a **python** file named `futures_curve.py`.

**Python Module**

- **Classes** (2): FuturesCurveQueryParams, FuturesCurveData
- **Functions** (2): to_upper, _validate_date
- **Import Statements**: 3


---

## Detailed Analysis

### Python Code Structure

#### Classes

- **`FuturesCurveQueryParams`**(QueryParams)
- **`FuturesCurveData`**(Data)

#### Functions

- **`to_upper(cls, v)`**
- **`_validate_date(cls, v)`**

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
- `pandas`
- `pydantic`
- `to_datetime`


---

## Performance & Security Notes

No obvious security concerns detected in static analysis.


---

**Generated**: 2025-11-19T02:16:46.476683Z
**Generator**: World's Best Repo Book Generator v1.0

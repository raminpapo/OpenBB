# File Documentation: yield_curve.py

## Metadata
- **Path**: `openbb_platform/core/openbb_core/provider/standard_models/yield_curve.py`
- **Size**: 2,128 bytes
- **Lines**: 72
- **Category**: python
- **Extension**: .py

---

## Original Source

```python
"""Yield Curve Standard Model."""

from datetime import date as dateType

from openbb_core.provider.abstract.data import Data
from openbb_core.provider.abstract.query_params import QueryParams
from openbb_core.provider.utils.descriptions import (
    DATA_DESCRIPTIONS,
    QUERY_DESCRIPTIONS,
)
from pydantic import Field, computed_field, field_validator


class YieldCurveQueryParams(QueryParams):
    """Yield Curve Query."""

    date: dateType | str | None = Field(
        default=None,
        description=QUERY_DESCRIPTIONS.get("date", "")
        + " By default is the current data.",
    )

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
        dates: list = []
        if isinstance(v, str):
            dates = v.split(",")
        elif isinstance(v, list):
            dates = v
        for date in dates:
            new_dates.append(to_datetime(date).date().strftime("%Y-%m-%d"))

        return ",".join(new_dates) if new_dates else None


class YieldCurveData(Data):
    """Yield Curve Data."""

    date: dateType | None = Field(
        default=None,
        description=DATA_DESCRIPTIONS.get("date", ""),
    )
    maturity: str = Field(description="Maturity length of the security.")

    @computed_field(  # type: ignore
        description="Maturity length, in years, as a decimal.",
        return_type=float | None,
    )
    @property
    def maturity_years(self) -> float | None:
        """Get the maturity in years as a decimal."""
        if "_" not in self.maturity:  # pylint: disable=E1135
            return None

        parts = self.maturity.split("_")  # pylint: disable=E1101
        months = sum(
            int(parts[i + 1]) * (12 if parts[i] == "year" else 1)
            for i in range(0, len(parts), 2)
        )

        return months / 12

```



---

## High-Level Overview

This is a **python** file named `yield_curve.py`.

**Python Module**

- **Classes** (2): YieldCurveQueryParams, YieldCurveData
- **Functions** (2): _validate_date, maturity_years
- **Import Statements**: 3


---

## Detailed Analysis

### Python Code Structure

#### Classes

- **`YieldCurveQueryParams`**(QueryParams)
- **`YieldCurveData`**(Data)

#### Functions

- **`_validate_date(cls, v)`**

#### Decorators Used

classmethod, computed_field, field_validator, property


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

**Generated**: 2025-11-19T02:16:46.599410Z
**Generator**: World's Best Repo Book Generator v1.0

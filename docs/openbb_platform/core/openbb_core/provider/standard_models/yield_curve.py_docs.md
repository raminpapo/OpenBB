# Documentation: openbb_platform/core/openbb_core/provider/standard_models/yield_curve.py

## File Metadata
- **Path**: `openbb_platform/core/openbb_core/provider/standard_models/yield_curve.py`
- **Size**: 2,128 characters, 72 lines
- **Words**: 209
- **Extension**: .py
- **Classification**: Text file

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

## High-Level Overview

Yield Curve Standard Model.

from datetime import date as dateType

from openbb_core.provider.abstract.data import Data
from openbb_core.provider.abstract.query_params import QueryParams
from openbb_core.provider.utils.descriptions import (
DATA_DESCRIPTIONS,
QUERY_DESCRIPTIONS,
)
from pydantic import Field, computed_field, field_validator


class YieldCurveQueryParams(QueryParams):
Yield Curve Query.
Validate the date.
# pylint: disable=import-outside-toplevel
from pandas import to_datetime

if v is None:

## Detailed Structure

### Python File Structure

**Classes** (2):
`YieldCurveQueryParams`, `YieldCurveData`

**Functions** (2):
`_validate_date`, `maturity_years`

**Imports** (11):
`datetime`, `date`, `openbb_core.provider.abstract.data`, `Data`, `openbb_core.provider.abstract.query_params`, `QueryParams`, `openbb_core.provider.utils.descriptions`, `pydantic`, `Field`, `pandas`, `to_datetime`


## Key Components

**Class `YieldCurveQueryParams`**: Yield Curve Query.

**Class `YieldCurveData`**: Yield Curve Data.

## Usage & Examples

See source code for usage details.

## Related Files

- `datetime`
- `openbb_core.provider.abstract.data`
- `openbb_core.provider.abstract.query_params`
- `openbb_core.provider.utils.descriptions`
- `pydantic`
- `pandas`

## Notes
- Generated: 2025-11-18T07:54:35.763792
- Generator: World's Best Repo Book Generator v1.0.0

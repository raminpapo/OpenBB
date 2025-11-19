# File Documentation: iorb_rates.py

## Metadata
- **Path**: `openbb_platform/providers/fred/openbb_fred/models/iorb_rates.py`
- **Size**: 1,727 bytes
- **Lines**: 63
- **Category**: python
- **Extension**: .py

---

## Original Source

```python
"""FRED IORB Model."""

# pylint: disable=unused-argument

from typing import Any

from openbb_core.provider.abstract.fetcher import Fetcher
from openbb_core.provider.standard_models.iorb_rates import (
    IORBData,
    IORBQueryParams,
)
from pydantic import field_validator


class FREDIORBQueryParams(IORBQueryParams):
    """FRED IORB Query."""


class FREDIORBData(IORBData):
    """FRED IORB Data."""

    __alias_dict__ = {"rate": "value"}

    @field_validator("rate", mode="before", check_fields=False)
    @classmethod
    def value_validate(cls, v):
        """Validate rate."""
        try:
            return float(v)
        except ValueError:
            return None


class FREDIORBFetcher(Fetcher[FREDIORBQueryParams, list[FREDIORBData]]):
    """FRED IORB Fetcher."""

    @staticmethod
    def transform_query(params: dict[str, Any]) -> FREDIORBQueryParams:
        """Transform query."""
        return FREDIORBQueryParams(**params)

    @staticmethod
    def extract_data(
        query: FREDIORBQueryParams, credentials: dict[str, str] | None, **kwargs: Any
    ) -> dict:
        """Extract data."""
        # pylint: disable=import-outside-toplevel
        from openbb_fred.utils.fred_base import Fred

        key = credentials.get("fred_api_key") if credentials else ""
        fred_series = "IORB"
        fred = Fred(key)
        data = fred.get_series(fred_series, query.start_date, query.end_date, **kwargs)
        return data

    @staticmethod
    def transform_data(
        query: FREDIORBQueryParams, data: dict, **kwargs: Any
    ) -> list[FREDIORBData]:
        """Transform data."""
        keys = ["date", "value"]
        return [FREDIORBData(**{k: x[k] for k in keys}) for x in data]

```



---

## High-Level Overview

This is a **python** file named `iorb_rates.py`.

**Python Module**

- **Classes** (3): FREDIORBQueryParams, FREDIORBData, FREDIORBFetcher
- **Functions** (4): value_validate, transform_query, extract_data, transform_data
- **Import Statements**: 3


---

## Detailed Analysis

### Python Code Structure

#### Classes

- **`FREDIORBQueryParams`**(IORBQueryParams)
- **`FREDIORBData`**(IORBData)
- **`FREDIORBFetcher`**(Fetcher[FREDIORBQueryParams, list[FREDIORBData]])

#### Functions

- **`value_validate(cls, v)`**

#### Decorators Used

classmethod, field_validator, staticmethod


---

## Related Files

The following files may be related based on imports and references:

**Imported Modules**:
- `Any`
- `Fetcher`
- `Fred`
- `field_validator`
- `openbb_core.provider.abstract.fetcher`
- `openbb_core.provider.standard_models.iorb_rates`
- `openbb_fred.utils.fred_base`
- `pydantic`
- `typing`


---

## Performance & Security Notes

No obvious security concerns detected in static analysis.


---

**Generated**: 2025-11-19T02:16:50.969669Z
**Generator**: World's Best Repo Book Generator v1.0

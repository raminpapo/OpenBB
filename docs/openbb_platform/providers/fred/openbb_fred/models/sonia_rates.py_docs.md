# File Documentation: sonia_rates.py

## Metadata
- **Path**: `openbb_platform/providers/fred/openbb_fred/models/sonia_rates.py`
- **Size**: 2,323 bytes
- **Lines**: 82
- **Category**: python
- **Extension**: .py

---

## Original Source

```python
"""FRED SONIA Model."""

# pylint: disable=unused-argument

from typing import Any, Literal

from openbb_core.provider.abstract.fetcher import Fetcher
from openbb_core.provider.standard_models.sonia_rates import SONIAData, SONIAQueryParams
from pydantic import Field, field_validator

SONIA_PARAMETER_TO_FRED_ID = {
    "rate": "IUDSOIA",
    "index": "IUDZOS2",
    "10th_percentile": "IUDZLS6",
    "25th_percentile": "IUDZLS7",
    "75th_percentile": "IUDZLS8",
    "90th_percentile": "IUDZLS9",
    "total_nominal_value": "IUDZLT2",
}


class FREDSONIAQueryParams(SONIAQueryParams):
    """FRED SONIA Query."""

    parameter: Literal[
        "rate",
        "index",
        "10th_percentile",
        "25th_percentile",
        "75th_percentile",
        "90th_percentile",
        "total_nominal_value",
    ] = Field(default="rate", description="Period of SONIA rate.")


class FREDSONIAData(SONIAData):
    """FRED SONIA Data."""

    __alias_dict__ = {"rate": "value"}

    @field_validator("rate", mode="before", check_fields=False)
    @classmethod
    def value_validate(cls, v):
        """Validate rate."""
        try:
            return float(v)
        except ValueError:
            return None


class FREDSONIAFetcher(Fetcher[FREDSONIAQueryParams, list[FREDSONIAData]]):
    """FRED SONIA Fetcher."""

    @staticmethod
    def transform_query(params: dict[str, Any]) -> FREDSONIAQueryParams:
        """Transform query."""
        return FREDSONIAQueryParams(**params)

    @staticmethod
    def extract_data(
        query: FREDSONIAQueryParams,
        credentials: dict[str, str] | None,
        **kwargs: Any,
    ) -> dict:
        """Extract data."""
        # pylint: disable=import-outside-toplevel
        from openbb_fred.utils.fred_base import Fred

        key = credentials.get("fred_api_key") if credentials else ""
        fred_series = SONIA_PARAMETER_TO_FRED_ID[query.parameter]
        fred = Fred(key)
        data = fred.get_series(fred_series, query.start_date, query.end_date, **kwargs)
        return data

    @staticmethod
    def transform_data(
        query: FREDSONIAQueryParams, data: dict, **kwargs: Any
    ) -> list[FREDSONIAData]:
        """Transform data."""
        keys = ["date", "value"]
        return [FREDSONIAData(**{k: x[k] for k in keys}) for x in data]

```



---

## High-Level Overview

This is a **python** file named `sonia_rates.py`.

**Python Module**

- **Classes** (3): FREDSONIAQueryParams, FREDSONIAData, FREDSONIAFetcher
- **Functions** (4): value_validate, transform_query, extract_data, transform_data
- **Import Statements**: 2


---

## Detailed Analysis

### Python Code Structure

#### Classes

- **`FREDSONIAQueryParams`**(SONIAQueryParams)
- **`FREDSONIAData`**(SONIAData)
- **`FREDSONIAFetcher`**(Fetcher[FREDSONIAQueryParams, list[FREDSONIAData]])

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
- `Field`
- `Fred`
- `SONIAData`
- `openbb_core.provider.abstract.fetcher`
- `openbb_core.provider.standard_models.sonia_rates`
- `openbb_fred.utils.fred_base`
- `pydantic`
- `typing`


---

## Performance & Security Notes

No obvious security concerns detected in static analysis.


---

**Generated**: 2025-11-19T02:16:51.009237Z
**Generator**: World's Best Repo Book Generator v1.0

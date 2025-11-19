# File Documentation: ecb_interest_rates.py

## Metadata
- **Path**: `openbb_platform/providers/fred/openbb_fred/models/ecb_interest_rates.py`
- **Size**: 2,451 bytes
- **Lines**: 83
- **Category**: python
- **Extension**: .py

---

## Original Source

```python
"""FRED European Central Bank Interest Rates Model."""

# pylint: disable=unused-argument

from typing import Any

from openbb_core.provider.abstract.fetcher import Fetcher
from openbb_core.provider.standard_models.ecb_interest_rates import (
    EuropeanCentralBankInterestRatesData,
    EuropeanCentralBankInterestRatesParams,
)
from pydantic import field_validator

NAME_TO_ID_ECB = {"deposit": "ECBDFR", "lending": "ECBMLFR", "refinancing": "ECBMRRFR"}


class FREDEuropeanCentralBankInterestRatesParams(
    EuropeanCentralBankInterestRatesParams
):
    """FRED European Central Bank Interest Rates Query."""


class FREDEuropeanCentralBankInterestRatesData(EuropeanCentralBankInterestRatesData):
    """FRED European Central Bank Interest Rates Data."""

    __alias_dict__ = {"rate": "value"}

    @field_validator("rate", mode="before", check_fields=False)
    @classmethod
    def value_validate(cls, v):
        """Validate rate."""
        try:
            return float(v)
        except ValueError:
            return None


class FREDEuropeanCentralBankInterestRatesFetcher(
    Fetcher[
        FREDEuropeanCentralBankInterestRatesParams,
        list[FREDEuropeanCentralBankInterestRatesData],
    ]
):
    """FRED ECB Interest Rates Fetcher."""

    @staticmethod
    def transform_query(
        params: dict[str, Any],
    ) -> FREDEuropeanCentralBankInterestRatesParams:
        """Transform query."""
        return FREDEuropeanCentralBankInterestRatesParams(**params)

    @staticmethod
    def extract_data(
        query: FREDEuropeanCentralBankInterestRatesParams,
        credentials: dict[str, str] | None,
        **kwargs: Any
    ) -> list:
        """Extract data."""
        # pylint: disable=import-outside-toplevel
        from openbb_fred.utils.fred_base import Fred

        key = credentials.get("fred_api_key") if credentials else ""
        fred = Fred(key)

        data = fred.get_series(
            series_id=NAME_TO_ID_ECB[query.interest_rate_type],
            start_date=query.start_date,
            end_date=query.end_date,
            **kwargs,
        )

        return data

    @staticmethod
    def transform_data(
        query: FREDEuropeanCentralBankInterestRatesParams, data: list, **kwargs: Any
    ) -> list[FREDEuropeanCentralBankInterestRatesData]:
        """Transform data."""
        return [
            FREDEuropeanCentralBankInterestRatesData.model_validate(d) for d in data
        ]

```



---

## High-Level Overview

This is a **python** file named `ecb_interest_rates.py`.

**Python Module**

- **Classes** (3): FREDEuropeanCentralBankInterestRatesParams, FREDEuropeanCentralBankInterestRatesData, FREDEuropeanCentralBankInterestRatesFetcher
- **Functions** (4): value_validate, transform_query, extract_data, transform_data
- **Import Statements**: 3


---

## Detailed Analysis

### Python Code Structure

#### Classes

- **`FREDEuropeanCentralBankInterestRatesParams`**(
    EuropeanCentralBankInterestRatesParams
)
- **`FREDEuropeanCentralBankInterestRatesData`**(EuropeanCentralBankInterestRatesData)
- **`FREDEuropeanCentralBankInterestRatesFetcher`**(
    Fetcher[
        FREDEuropeanCentralBankInterestRatesParams,
        list[FREDEuropeanCentralBankInterestRatesData],
    ]
)

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
- `openbb_core.provider.standard_models.ecb_interest_rates`
- `openbb_fred.utils.fred_base`
- `pydantic`
- `typing`


---

## Performance & Security Notes

No obvious security concerns detected in static analysis.


---

**Generated**: 2025-11-19T02:16:50.958768Z
**Generator**: World's Best Repo Book Generator v1.0

# Documentation: openbb_platform/providers/fred/openbb_fred/models/ecb_interest_rates.py

## File Metadata
- **Path**: `openbb_platform/providers/fred/openbb_fred/models/ecb_interest_rates.py`
- **Size**: 2,451 characters, 83 lines
- **Words**: 168
- **Extension**: .py
- **Classification**: Text file

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

## High-Level Overview

FRED European Central Bank Interest Rates Model.

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
FRED European Central Bank Interest Rates Query.

## Detailed Structure

### Python File Structure

**Classes** (3):
`FREDEuropeanCentralBankInterestRatesParams`, `FREDEuropeanCentralBankInterestRatesData`, `FREDEuropeanCentralBankInterestRatesFetcher`

**Functions** (4):
`value_validate`, `transform_query`, `extract_data`, `transform_data`

**Imports** (9):
`typing`, `Any`, `openbb_core.provider.abstract.fetcher`, `Fetcher`, `openbb_core.provider.standard_models.ecb_interest_rates`, `pydantic`, `field_validator`, `openbb_fred.utils.fred_base`, `Fred`


## Key Components

**Class `FREDEuropeanCentralBankInterestRatesParams`**: FRED European Central Bank Interest Rates Query.

**Class `FREDEuropeanCentralBankInterestRatesData`**: FRED European Central Bank Interest Rates Data.

**Class `FREDEuropeanCentralBankInterestRatesFetcher`**: FRED ECB Interest Rates Fetcher.

## Usage & Examples

See source code for usage details.

## Related Files

- `typing`
- `openbb_core.provider.abstract.fetcher`
- `openbb_core.provider.standard_models.ecb_interest_rates`
- `pydantic`
- `openbb_fred.utils.fred_base`

## Notes
- Generated: 2025-11-18T07:54:39.669692
- Generator: World's Best Repo Book Generator v1.0.0

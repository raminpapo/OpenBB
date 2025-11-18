# Documentation: openbb_platform/providers/fred/openbb_fred/models/dwpcr_rates.py

## File Metadata
- **Path**: `openbb_platform/providers/fred/openbb_fred/models/dwpcr_rates.py`
- **Size**: 2,712 characters, 89 lines
- **Words**: 190
- **Extension**: .py
- **Classification**: Text file

## Original Source

```python
"""FRED Discount Window Primary Credit Rate Model."""

# pylint: disable=unused-argument

from typing import Any, Literal

from openbb_core.provider.abstract.fetcher import Fetcher
from openbb_core.provider.standard_models.dwpcr_rates import (
    DiscountWindowPrimaryCreditRateData,
    DiscountWindowPrimaryCreditRateParams,
)
from pydantic import Field, field_validator

DWPCR_PARAMETER_TO_FRED_ID = {
    "daily_excl_weekend": "DPCREDIT",
    "monthly": "MPCREDIT",
    "weekly": "WPCREDIT",
    "daily": "RIFSRPF02ND",
    "annual": "RIFSRPF02NA",
}


class FREDDiscountWindowPrimaryCreditRateParams(DiscountWindowPrimaryCreditRateParams):
    """FRED Discount Window Primary Credit Rate Query."""

    parameter: Literal["daily_excl_weekend", "monthly", "weekly", "daily", "annual"] = (
        Field(default="daily_excl_weekend", description="FRED series ID of DWPCR data.")
    )


class FREDDiscountWindowPrimaryCreditRateData(DiscountWindowPrimaryCreditRateData):
    """FRED Discount Window Primary Credit Rate Data."""

    __alias_dict__ = {"rate": "value"}

    @field_validator("rate", mode="before", check_fields=False)
    @classmethod
    def value_validate(cls, v):
        """Validate rate."""
        try:
            return float(v)
        except ValueError:
            return None


class FREDDiscountWindowPrimaryCreditRateFetcher(
    Fetcher[
        FREDDiscountWindowPrimaryCreditRateParams,
        list[FREDDiscountWindowPrimaryCreditRateData],
    ]
):
    """FRED Discount Window Primary Credit Rate Fetcher."""

    @staticmethod
    def transform_query(
        params: dict[str, Any],
    ) -> FREDDiscountWindowPrimaryCreditRateParams:
        """Transform query."""
        return FREDDiscountWindowPrimaryCreditRateParams(**params)

    @staticmethod
    def extract_data(
        query: FREDDiscountWindowPrimaryCreditRateParams,
        credentials: dict[str, str] | None,
        **kwargs: Any
    ) -> list:
        """Extract data."""
        # pylint: disable=import-outside-toplevel
        from openbb_fred.utils.fred_base import Fred

        key = credentials.get("fred_api_key") if credentials else ""
        fred = Fred(key)

        data = fred.get_series(
            series_id=DWPCR_PARAMETER_TO_FRED_ID[query.parameter],
            start_date=query.start_date,
            end_date=query.end_date,
            **kwargs,
        )

        return data

    @staticmethod
    def transform_data(
        query: FREDDiscountWindowPrimaryCreditRateParams, data: list, **kwargs: Any
    ) -> list[FREDDiscountWindowPrimaryCreditRateData]:
        """Transform data."""
        return [FREDDiscountWindowPrimaryCreditRateData.model_validate(d) for d in data]

```

## High-Level Overview

FRED Discount Window Primary Credit Rate Model.

# pylint: disable=unused-argument

from typing import Any, Literal

from openbb_core.provider.abstract.fetcher import Fetcher
from openbb_core.provider.standard_models.dwpcr_rates import (
DiscountWindowPrimaryCreditRateData,
DiscountWindowPrimaryCreditRateParams,
)
from pydantic import Field, field_validator

DWPCR_PARAMETER_TO_FRED_ID = {
"daily_excl_weekend": "DPCREDIT",
"monthly": "MPCREDIT",
"weekly": "WPCREDIT",
"daily": "RIFSRPF02ND",
"annual": "RIFSRPF02NA",
}

## Detailed Structure

### Python File Structure

**Classes** (3):
`FREDDiscountWindowPrimaryCreditRateParams`, `FREDDiscountWindowPrimaryCreditRateData`, `FREDDiscountWindowPrimaryCreditRateFetcher`

**Functions** (4):
`value_validate`, `transform_query`, `extract_data`, `transform_data`

**Imports** (9):
`typing`, `Any`, `openbb_core.provider.abstract.fetcher`, `Fetcher`, `openbb_core.provider.standard_models.dwpcr_rates`, `pydantic`, `Field`, `openbb_fred.utils.fred_base`, `Fred`


## Key Components

**Class `FREDDiscountWindowPrimaryCreditRateParams`**: FRED Discount Window Primary Credit Rate Query.

**Class `FREDDiscountWindowPrimaryCreditRateData`**: FRED Discount Window Primary Credit Rate Data.

**Class `FREDDiscountWindowPrimaryCreditRateFetcher`**: FRED Discount Window Primary Credit Rate Fetcher.

## Usage & Examples

See source code for usage details.

## Related Files

- `typing`
- `openbb_core.provider.abstract.fetcher`
- `openbb_core.provider.standard_models.dwpcr_rates`
- `pydantic`
- `openbb_fred.utils.fred_base`

## Notes
- Generated: 2025-11-18T07:54:39.668030
- Generator: World's Best Repo Book Generator v1.0.0

# File Documentation: etf_equity_exposure.py

## Metadata
- **Path**: `openbb_platform/providers/fmp/openbb_fmp/models/etf_equity_exposure.py`
- **Size**: 3,068 bytes
- **Lines**: 97
- **Category**: python
- **Extension**: .py

---

## Original Source

```python
"""FMP ETF Equity Exposure Model."""

# pylint: disable=unused-argument

from typing import Any

from openbb_core.provider.abstract.fetcher import Fetcher
from openbb_core.provider.standard_models.etf_equity_exposure import (
    EtfEquityExposureData,
    EtfEquityExposureQueryParams,
)
from openbb_core.provider.utils.errors import EmptyDataError
from pydantic import field_validator


class FMPEtfEquityExposureQueryParams(EtfEquityExposureQueryParams):
    """
    FMP ETF Equity Exposure Query Params.

    Source: https://site.financialmodelingprep.com/developer/docs#etf-asset-exposure
    """

    __json_schema_extra__ = {"symbol": {"multiple_items_allowed": True}}


class FMPEtfEquityExposureData(EtfEquityExposureData):
    """FMP ETF Equity Exposure Data."""

    __alias_dict__ = {
        "equity_symbol": "asset",
        "etf_symbol": "symbol",
        "shares": "sharesNumber",
        "weight": "weightPercentage",
        "market_value": "marketValue",
    }

    @field_validator("weight", mode="before", check_fields=False)
    @classmethod
    def normalize_percent(cls, v):
        """Normalize percent values."""
        return float(v) / 100 if v else None


class FMPEtfEquityExposureFetcher(
    Fetcher[FMPEtfEquityExposureQueryParams, list[FMPEtfEquityExposureData]]
):
    """FMP ETF Equity Exposure Fetcher."""

    @staticmethod
    def transform_query(params: dict[str, Any]) -> FMPEtfEquityExposureQueryParams:
        """Transform the query."""
        return FMPEtfEquityExposureQueryParams(**params)

    @staticmethod
    async def aextract_data(
        query: FMPEtfEquityExposureQueryParams,
        credentials: dict[str, str] | None,
        **kwargs: Any,
    ) -> list[dict]:
        """Return the raw data from the FMP endpoint."""
        # pylint: disable=import-outside-toplevel
        import asyncio  # noqa
        import warnings
        from openbb_fmp.utils.helpers import get_data

        api_key = credentials.get("fmp_api_key") if credentials else ""
        symbols = query.symbol.split(",")
        results: list[dict] = []

        async def get_one(symbol):
            """Get one symbol."""
            url = f"https://financialmodelingprep.com/stable/etf/asset-exposure?symbol={symbol}&apikey={api_key}"
            response = await get_data(url, **kwargs)
            if not response:
                warnings.warn(f"No results found for {symbol}.")
            if response:
                results.extend(response)

        await asyncio.gather(*[get_one(symbol) for symbol in symbols])

        if not results:
            raise EmptyDataError("No data was found for the given symbols.")

        return results

    @staticmethod
    def transform_data(
        query: FMPEtfEquityExposureQueryParams,
        data: list[dict],
        **kwargs: Any,
    ) -> list[FMPEtfEquityExposureData]:
        """Return the transformed data."""
        return [
            FMPEtfEquityExposureData.model_validate(d)
            for d in sorted(data, key=lambda x: x["marketValue"], reverse=True)
        ]

```



---

## High-Level Overview

This is a **python** file named `etf_equity_exposure.py`.

**Python Module**

- **Classes** (3): FMPEtfEquityExposureQueryParams, FMPEtfEquityExposureData, FMPEtfEquityExposureFetcher
- **Functions** (5): normalize_percent, transform_query, aextract_data, get_one, transform_data
- **Import Statements**: 4


---

## Detailed Analysis

### Python Code Structure

#### Classes

- **`FMPEtfEquityExposureQueryParams`**(EtfEquityExposureQueryParams)
- **`FMPEtfEquityExposureData`**(EtfEquityExposureData)
- **`FMPEtfEquityExposureFetcher`**(
    Fetcher[FMPEtfEquityExposureQueryParams, list[FMPEtfEquityExposureData]]
)

#### Functions

- **`normalize_percent(cls, v)`**
- **`get_one(symbol)`**

#### Decorators Used

classmethod, field_validator, staticmethod


---

## Related Files

The following files may be related based on imports and references:

**Imported Modules**:
- `Any`
- `EmptyDataError`
- `Fetcher`
- `asyncio`
- `field_validator`
- `get_data`
- `openbb_core.provider.abstract.fetcher`
- `openbb_core.provider.standard_models.etf_equity_exposure`
- `openbb_core.provider.utils.errors`
- `openbb_fmp.utils.helpers`
- `pydantic`
- `typing`
- `warnings`


---

## Performance & Security Notes

No obvious security concerns detected in static analysis.


---

**Generated**: 2025-11-19T02:16:50.630273Z
**Generator**: World's Best Repo Book Generator v1.0

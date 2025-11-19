# File Documentation: historical_eps.py

## Metadata
- **Path**: `openbb_platform/providers/alpha_vantage/openbb_alpha_vantage/models/historical_eps.py`
- **Size**: 5,811 bytes
- **Lines**: 165
- **Category**: python
- **Extension**: .py

---

## Original Source

```python
"""AlphaVantage Historical EPS Model."""

# pylint: disable=unused-argument

from datetime import date as dateType
from typing import Any, Literal
from warnings import warn

from openbb_core.provider.abstract.fetcher import Fetcher
from openbb_core.provider.standard_models.historical_eps import (
    HistoricalEpsData,
    HistoricalEpsQueryParams,
)
from openbb_core.provider.utils.descriptions import QUERY_DESCRIPTIONS
from openbb_core.provider.utils.errors import EmptyDataError
from pydantic import Field, field_validator


class AlphaVantageHistoricalEpsQueryParams(HistoricalEpsQueryParams):
    """
    AlphaVantage Historical EPS Query Params.

    Source: https://www.alphavantage.co/documentation/#earnings
    """

    __json_schema_extra__ = {"symbol": {"multiple_items_allowed": True}}

    period: Literal["annual", "quarter"] = Field(
        default="quarter", description=QUERY_DESCRIPTIONS.get("period", "")
    )
    limit: int | None = Field(
        default=None, description=QUERY_DESCRIPTIONS.get("limit", "")
    )


class AlphaVantageHistoricalEpsData(HistoricalEpsData):
    """AlphaVantage Historical EPS Data."""

    __alias_dict__ = {
        "date": "fiscalDateEnding",
        "eps_actual": "reportedEPS",
        "eps_estimated": "estimatedEPS",
        "surprise_percent": "surprisePercentage",
        "reported_date": "reportedDate",
    }

    surprise: float | None = Field(
        default=None,
        description="Surprise in EPS (Actual - Estimated).",
    )
    surprise_percent: float | str | None = Field(
        default=None,
        description="EPS surprise as a normalized percent.",
        json_schema_extra={"x-unit_measurement": "percent", "x-frontend_multiply": 100},
    )
    reported_date: dateType | None = Field(
        default=None,
        description="Date of the earnings report.",
    )
    report_time: str | None = Field(
        default=None,
        description="Time of day when the earnings report was released, e.g., 'post-market'.",
    )

    @field_validator(
        "eps_estimated",
        "eps_actual",
        "surprise",
        mode="before",
        check_fields=False,
    )
    @classmethod
    def validate_null(cls, v):
        """Clean None returned as a string."""
        return None if str(v).strip() == "None" or str(v) == "0" else v

    @field_validator("surprise_percent", mode="before", check_fields=False)
    @classmethod
    def normalize_percent(cls, v):
        """Normalize percent values."""
        if isinstance(v, str) and v == "None" or str(v) == "0":
            return None
        return float(v) / 100


class AVHistoricalEpsFetcher(
    Fetcher[AlphaVantageHistoricalEpsQueryParams, list[AlphaVantageHistoricalEpsData]]
):
    """AlphaVantage Historical EPS Fetcher."""

    @staticmethod
    def transform_query(params: dict[str, Any]) -> AlphaVantageHistoricalEpsQueryParams:
        """Transform the query params."""
        return AlphaVantageHistoricalEpsQueryParams(**params)

    @staticmethod
    async def aextract_data(
        query: AlphaVantageHistoricalEpsQueryParams,
        credentials: dict[str, str] | None,
        **kwargs: Any,
    ) -> list[dict]:
        """Return the raw data from the AlphaVantage endpoint."""
        # pylint: disable=import-outside-toplevel
        from openbb_core.provider.utils.helpers import (
            ClientResponse,
            ClientSession,
            amake_requests,
        )

        api_key = credentials.get("alpha_vantage_api_key") if credentials else ""
        BASE_URL = "https://www.alphavantage.co/query?function=EARNINGS&"
        # We are allowing multiple symbols to be passed in the query, so we need to handle that.
        symbols = query.symbol.split(",")
        urls = [f"{BASE_URL}symbol={symbol}&apikey={api_key}" for symbol in symbols]
        results: list = []
        messages: list = []

        # We need to make a custom callback function for this async request.
        async def response_callback(response: ClientResponse, _: ClientSession):
            """Response callback function."""
            symbol = response.url.query.get("symbol", None)
            data = await response.json()
            target = (
                "annualEarnings" if query.period == "annual" else "quarterlyEarnings"
            )
            message = data.get("Information", "")  # type: ignore
            if message:
                messages.append(message)
                warn(f"Symbol Error for {symbol}: {message}")
            result: list = []
            # If data is returned, append it to the results list.
            if data:
                result = [
                    {
                        "symbol": symbol,
                        **d,
                    }
                    for d in data.get(target, [])  # type: ignore
                ]
                if query.limit is not None:
                    results.extend(result[: query.limit])
                else:
                    results.extend(result)
            # If no data is returned, raise a warning and move on to the next symbol.
            if not data:
                warn(f"Symbol Error: No data found for {symbol}")

        await amake_requests(urls, response_callback, **kwargs)  # type: ignore

        if not results:
            raise EmptyDataError(f"No data was returned -> \n{messages[-1]}")

        return results

    @staticmethod
    def transform_data(
        query: AlphaVantageHistoricalEpsQueryParams,
        data: list[dict],
        **kwargs: Any,
    ) -> list[AlphaVantageHistoricalEpsData]:
        """Transform the raw data into the standard model."""
        if not data:
            raise EmptyDataError("No data found.")
        return [AlphaVantageHistoricalEpsData.model_validate(d) for d in data]

```



---

## High-Level Overview

This is a **python** file named `historical_eps.py`.

**Python Module**

- **Classes** (3): AlphaVantageHistoricalEpsQueryParams, AlphaVantageHistoricalEpsData, AVHistoricalEpsFetcher
- **Functions** (6): validate_null, normalize_percent, transform_query, aextract_data, response_callback, transform_data
- **Import Statements**: 2


---

## Detailed Analysis

### Python Code Structure

#### Classes

- **`AlphaVantageHistoricalEpsQueryParams`**(HistoricalEpsQueryParams)
- **`AlphaVantageHistoricalEpsData`**(HistoricalEpsData)
- **`AVHistoricalEpsFetcher`**(
    Fetcher[AlphaVantageHistoricalEpsQueryParams, list[AlphaVantageHistoricalEpsData]]
)

#### Functions

- **`validate_null(cls, v)`**
- **`normalize_percent(cls, v)`**
- **`response_callback(response: ClientResponse, _: ClientSession)`**

#### Decorators Used

classmethod, field_validator, staticmethod


---

## Related Files

The following files may be related based on imports and references:

**Imported Modules**:
- `Any`
- `EmptyDataError`
- `Fetcher`
- `Field`
- `QUERY_DESCRIPTIONS`
- `date`
- `datetime`
- `openbb_core.provider.abstract.fetcher`
- `openbb_core.provider.standard_models.historical_eps`
- `openbb_core.provider.utils.descriptions`
- `openbb_core.provider.utils.errors`
- `openbb_core.provider.utils.helpers`
- `pydantic`
- `typing`
- `warn`


---

## Performance & Security Notes

No obvious security concerns detected in static analysis.


---

**Generated**: 2025-11-19T02:16:48.249290Z
**Generator**: World's Best Repo Book Generator v1.0

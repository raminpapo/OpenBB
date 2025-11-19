# File Documentation: price_target_consensus.py

## Metadata
- **Path**: `openbb_platform/providers/yfinance/openbb_yfinance/models/price_target_consensus.py`
- **Size**: 5,169 bytes
- **Lines**: 157
- **Category**: python
- **Extension**: .py

---

## Original Source

```python
"""YFinance Price Target Consensus Model."""

# pylint: disable=unused-argument

from typing import Any

from openbb_core.app.model.abstract.error import OpenBBError
from openbb_core.provider.abstract.fetcher import Fetcher
from openbb_core.provider.standard_models.price_target_consensus import (
    PriceTargetConsensusData,
    PriceTargetConsensusQueryParams,
)
from pydantic import Field, field_validator


class YFinancePriceTargetConsensusQueryParams(PriceTargetConsensusQueryParams):
    """YFinance Price Target Consensus Query."""

    __json_schema_extra__ = {"symbol": {"multiple_items_allowed": True}}

    @field_validator("symbol", mode="before", check_fields=False)
    @classmethod
    def check_symbol(cls, value):
        """Check the symbol."""
        if not value:
            raise OpenBBError("Error: Symbol is a required field for yFinance.")
        return value


class YFinancePriceTargetConsensusData(PriceTargetConsensusData):
    """YFinance Price Target Consensus Data."""

    __alias_dict__ = {
        "target_high": "targetHighPrice",
        "target_low": "targetLowPrice",
        "target_consensus": "targetMeanPrice",
        "target_median": "targetMedianPrice",
        "recommendation": "recommendationKey",
        "recommendation_mean": "recommendationMean",
        "number_of_analysts": "numberOfAnalystOpinions",
        "current_price": "currentPrice",
    }

    recommendation: str | None = Field(
        default=None,
        description="Recommendation - buy, sell, etc.",
    )
    recommendation_mean: float | None = Field(
        default=None,
        description="Mean recommendation score where 1 is strong buy and 5 is strong sell.",
    )
    number_of_analysts: int | None = Field(
        default=None, description="Number of analysts providing opinions."
    )
    current_price: float | None = Field(
        default=None,
        description="Current price of the stock.",
    )
    currency: str | None = Field(
        default=None,
        description="Currency the stock is priced in.",
    )


class YFinancePriceTargetConsensusFetcher(
    Fetcher[
        YFinancePriceTargetConsensusQueryParams, list[YFinancePriceTargetConsensusData]
    ]
):
    """YFinance Price Target Consensus Fetcher."""

    @staticmethod
    def transform_query(
        params: dict[str, Any],
    ) -> YFinancePriceTargetConsensusQueryParams:
        """Transform the query."""
        return YFinancePriceTargetConsensusQueryParams(**params)

    @staticmethod
    async def aextract_data(
        query: YFinancePriceTargetConsensusQueryParams,
        credentials: dict[str, str] | None,
        **kwargs: Any,
    ) -> list[dict]:
        """Extract the raw data from YFinance."""
        # pylint: disable=import-outside-toplevel
        import asyncio  # noqa
        from curl_adapter import CurlCffiAdapter
        from openbb_core.provider.utils.errors import EmptyDataError
        from openbb_core.provider.utils.helpers import get_requests_session
        from warnings import warn
        from yfinance import Ticker

        symbols = query.symbol.split(",")  # type: ignore
        results = []
        fields = [
            "symbol",
            "currentPrice",
            "currency",
            "targetHighPrice",
            "targetLowPrice",
            "targetMeanPrice",
            "targetMedianPrice",
            "recommendationMean",
            "recommendationKey",
            "numberOfAnalystOpinions",
        ]
        session = get_requests_session()
        session.mount("https://", CurlCffiAdapter())
        session.mount("http://", CurlCffiAdapter())
        messages: list = []

        async def get_one(symbol):
            """Get the data for one ticker symbol."""
            result: dict = {}
            ticker: dict = {}
            try:
                ticker = Ticker(
                    symbol,
                    session=session,
                ).get_info()
            except Exception as e:
                messages.append(
                    f"Error getting data for {symbol}: {e.__class__.__name__}: {e}"
                )
            if ticker:
                for field in fields:
                    if field in ticker:
                        result[field] = ticker.get(field, None)
                if result and result.get("numberOfAnalystOpinions") is not None:
                    results.append(result)

        tasks = [get_one(symbol) for symbol in symbols]

        await asyncio.gather(*tasks)

        if not results and not messages:
            raise EmptyDataError("No data was returned for the given symbol(s)")

        if not results and messages:
            raise OpenBBError("\n".join(messages))

        if results and messages:
            for message in messages:
                warn(message)

        return results

    @staticmethod
    def transform_data(
        query: YFinancePriceTargetConsensusQueryParams,
        data: list[dict],
        **kwargs: Any,
    ) -> list[YFinancePriceTargetConsensusData]:
        """Transform the data."""
        return [YFinancePriceTargetConsensusData.model_validate(d) for d in data]

```



---

## High-Level Overview

This is a **python** file named `price_target_consensus.py`.

**Python Module**

- **Classes** (3): YFinancePriceTargetConsensusQueryParams, YFinancePriceTargetConsensusData, YFinancePriceTargetConsensusFetcher
- **Functions** (5): check_symbol, transform_query, aextract_data, get_one, transform_data
- **Import Statements**: 4


---

## Detailed Analysis

### Python Code Structure

#### Classes

- **`YFinancePriceTargetConsensusQueryParams`**(PriceTargetConsensusQueryParams)
- **`YFinancePriceTargetConsensusData`**(PriceTargetConsensusData)
- **`YFinancePriceTargetConsensusFetcher`**(
    Fetcher[
        YFinancePriceTargetConsensusQueryParams, list[YFinancePriceTargetConsensusData]
    ]
)

#### Functions

- **`check_symbol(cls, value)`**
- **`get_one(symbol)`**

#### Decorators Used

classmethod, field_validator, staticmethod


---

## Related Files

The following files may be related based on imports and references:

**Imported Modules**:
- `Any`
- `CurlCffiAdapter`
- `EmptyDataError`
- `Fetcher`
- `Field`
- `OpenBBError`
- `Ticker`
- `asyncio`
- `curl_adapter`
- `get_requests_session`
- `openbb_core.app.model.abstract.error`
- `openbb_core.provider.abstract.fetcher`
- `openbb_core.provider.standard_models.price_target_consensus`
- `openbb_core.provider.utils.errors`
- `openbb_core.provider.utils.helpers`


---

## Performance & Security Notes

No obvious security concerns detected in static analysis.


---

**Generated**: 2025-11-19T02:16:55.198093Z
**Generator**: World's Best Repo Book Generator v1.0

# File Documentation: price_target.py

## Metadata
- **Path**: `openbb_platform/providers/fmp/openbb_fmp/models/price_target.py`
- **Size**: 3,325 bytes
- **Lines**: 108
- **Category**: python
- **Extension**: .py

---

## Original Source

```python
"""FMP Equity Ownership Model."""

# pylint: disable=unused-argument

from typing import Any

from openbb_core.provider.abstract.fetcher import Fetcher
from openbb_core.provider.standard_models.price_target import (
    PriceTargetData,
    PriceTargetQueryParams,
)
from openbb_core.provider.utils.errors import EmptyDataError
from pydantic import ConfigDict, Field


class FMPPriceTargetQueryParams(PriceTargetQueryParams):
    """FMP Price Target Query.

    Source: https://site.financialmodelingprep.com/developer/docs#analyst
    """

    __json_schema_extra__ = {"symbol": {"multiple_items_allowed": True}}


class FMPPriceTargetData(PriceTargetData):
    """FMP Price Target Data."""

    model_config = ConfigDict(extra="ignore")

    __alias_dict__ = {
        "analyst_firm": "analystCompany",
        "rating_current": "newGrade",
        "rating_previous": "previousGrade",
        "news_title": "newsTitle",
        "news_url": "newsURL",
    }

    news_title: str | None = Field(
        default=None, description="News title of the price target."
    )
    news_url: str | None = Field(
        default=None, description="News URL of the price target."
    )


class FMPPriceTargetFetcher(
    Fetcher[
        FMPPriceTargetQueryParams,
        list[FMPPriceTargetData],
    ]
):
    """FMP Price Target Fetcher."""

    @staticmethod
    def transform_query(params: dict[str, Any]) -> FMPPriceTargetQueryParams:
        """Transform the query params."""
        return FMPPriceTargetQueryParams(**params)

    @staticmethod
    async def aextract_data(
        query: FMPPriceTargetQueryParams,
        credentials: dict[str, str] | None,
        **kwargs: Any,
    ) -> list[dict]:
        """Return the raw data from the FMP endpoint."""
        # pylint: disable=import-outside-toplevel
        import asyncio  # noqa
        import math
        from warnings import warn
        from openbb_fmp.utils.helpers import get_data_urls

        api_key = credentials.get("fmp_api_key") if credentials else ""
        base_url = "https://financialmodelingprep.com/stable/price-target-news?"
        symbols = query.symbol.split(",")  # type: ignore
        limit = query.limit if query.limit else 100
        pages = math.ceil(limit / 100)
        results: list[dict] = []

        async def get_one(symbol):
            """Get data for one symbol."""
            urls = [
                f"{base_url}symbol={symbol}&page={page}&limit={limit}&apikey={api_key}"
                for page in range(pages)
            ]
            result = await get_data_urls(urls, **kwargs)

            if not result or len(result) == 0:
                warn(f"Symbol Error: No data found for {symbol}")

            if result:
                results.extend(result)

        await asyncio.gather(*[get_one(symbol) for symbol in symbols])

        if not results:
            raise EmptyDataError("No data returned for the given symbols.")

        return sorted(
            results, key=lambda x: (x["publishedDate"], x["symbol"]), reverse=True
        )

    @staticmethod
    def transform_data(
        query: FMPPriceTargetQueryParams, data: list[dict], **kwargs: Any
    ) -> list[FMPPriceTargetData]:
        """Return the transformed data."""
        return [FMPPriceTargetData.model_validate(item) for item in data]

```



---

## High-Level Overview

This is a **python** file named `price_target.py`.

**Python Module**

- **Classes** (3): FMPPriceTargetQueryParams, FMPPriceTargetData, FMPPriceTargetFetcher
- **Functions** (4): transform_query, aextract_data, get_one, transform_data
- **Import Statements**: 4


---

## Detailed Analysis

### Python Code Structure

#### Classes

- **`FMPPriceTargetQueryParams`**(PriceTargetQueryParams)
- **`FMPPriceTargetData`**(PriceTargetData)
- **`FMPPriceTargetFetcher`**(
    Fetcher[
        FMPPriceTargetQueryParams,
        list[FMPPriceTargetData],
    ]
)

#### Functions

- **`get_one(symbol)`**

#### Decorators Used

staticmethod


---

## Related Files

The following files may be related based on imports and references:

**Imported Modules**:
- `Any`
- `ConfigDict`
- `EmptyDataError`
- `Fetcher`
- `asyncio`
- `get_data_urls`
- `math`
- `openbb_core.provider.abstract.fetcher`
- `openbb_core.provider.standard_models.price_target`
- `openbb_core.provider.utils.errors`
- `openbb_fmp.utils.helpers`
- `pydantic`
- `typing`
- `warn`
- `warnings`


---

## Performance & Security Notes

No obvious security concerns detected in static analysis.


---

**Generated**: 2025-11-19T02:16:50.684367Z
**Generator**: World's Best Repo Book Generator v1.0

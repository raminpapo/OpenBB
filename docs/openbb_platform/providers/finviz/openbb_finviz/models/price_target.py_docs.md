# File Documentation: price_target.py

## Metadata
- **Path**: `openbb_platform/providers/finviz/openbb_finviz/models/price_target.py`
- **Size**: 4,593 bytes
- **Lines**: 135
- **Category**: python
- **Extension**: .py

---

## Original Source

```python
"""Finviz Price Target Model."""

# pylint: disable=unused-argument

from typing import Any

from openbb_core.provider.abstract.fetcher import Fetcher
from openbb_core.provider.standard_models.price_target import (
    PriceTargetData,
    PriceTargetQueryParams,
)
from pydantic import Field


class FinvizPriceTargetQueryParams(PriceTargetQueryParams):
    """Finviz Price Target Query.

    Source: https://finviz.com/quote.ashx?
    """

    __json_schema_extra__ = {"symbol": {"multiple_items_allowed": True}}


class FinvizPriceTargetData(PriceTargetData):
    """Finviz Price Target Data."""

    __alias_dict__ = {
        "published_date": "Date",
        "status": "Status",
        "analyst_company": "Outer",
        "rating_change": "Rating",
    }

    status: str | None = Field(
        default=None,
        description="The action taken by the firm."
        + " This could be 'Upgrade', 'Downgrade', 'Reiterated', etc.",
    )
    rating_change: str | None = Field(
        default=None,
        description="The rating given by the analyst."
        + " This could be 'Buy', 'Sell', 'Underweight', etc."
        + " If the rating is a revision, the change is indicated by '->'",
    )


class FinvizPriceTargetFetcher(
    Fetcher[FinvizPriceTargetQueryParams, list[FinvizPriceTargetData]]
):
    """Finviz Price Target Fetcher."""

    @staticmethod
    def transform_query(params: dict[str, Any]) -> FinvizPriceTargetQueryParams:
        """Transform the query params."""
        return FinvizPriceTargetQueryParams(**params)

    @staticmethod
    def extract_data(
        query: FinvizPriceTargetQueryParams,
        credentials: dict[str, str] | None,
        **kwargs: Any,
    ) -> list[dict]:
        """Return the raw data from the Finviz endpoint."""
        # pylint: disable=import-outside-toplevel
        from finvizfinance import util  # noqa
        from finvizfinance.quote import finvizfinance
        from openbb_core.app.model.abstract.error import OpenBBError
        from openbb_core.provider.utils.errors import EmptyDataError
        from openbb_core.provider.utils.helpers import get_requests_session
        from pandas import DataFrame
        from warnings import warn

        results: list[dict] = []
        util.session = get_requests_session()
        messages: list = []

        def get_one(symbol) -> list[dict]:
            """Get the data for one symbol."""
            price_targets = DataFrame()
            result: list[dict] = []
            try:
                data = finvizfinance(symbol)
                price_targets = data.ticker_outer_ratings()
                if price_targets is None or len(price_targets) == 0:
                    messages.append(f"Failed to get data for {symbol}")
                    return result
                price_targets["symbol"] = symbol
                prices = (
                    price_targets["Price"].astype(str).str.replace("$", "", regex=False)
                )
                price_targets["price_target"] = (
                    prices.str.split("→").str.get(0).str.strip()
                )
                price_targets["adj_price_target"] = (
                    prices.str.split("→").str.get(-1).str.strip()
                )
                price_targets.loc[
                    price_targets["adj_price_target"] == price_targets["price_target"],
                    "price_target",
                ] = None
                price_targets = price_targets.replace("", None).drop(columns="Price")
            except Exception as e:  # pylint: disable=W0718
                messages.append(f"Failed to get data for {symbol} -> {e}")
                return result
            result = price_targets.to_dict(orient="records")
            return result

        symbols = query.symbol.split(",") if query.symbol else []

        for symbol in symbols:
            result = get_one(symbol)
            if result:
                results.extend(result)

        if not results and messages:
            raise OpenBBError("\n".join(messages))

        if not results and not messages:
            raise EmptyDataError("No data was returned for any symbol")

        if results and messages:
            for message in messages:
                warn(message)

        return results

    @staticmethod
    def transform_data(
        query: FinvizPriceTargetQueryParams,
        data: list[dict],
        **kwargs: Any,
    ) -> list[FinvizPriceTargetData]:
        """Transform and validate the raw data."""
        return [FinvizPriceTargetData.model_validate(d) for d in data]

```



---

## High-Level Overview

This is a **python** file named `price_target.py`.

**Python Module**

- **Classes** (3): FinvizPriceTargetQueryParams, FinvizPriceTargetData, FinvizPriceTargetFetcher
- **Functions** (4): transform_query, extract_data, get_one, transform_data
- **Import Statements**: 4


---

## Detailed Analysis

### Python Code Structure

#### Classes

- **`FinvizPriceTargetQueryParams`**(PriceTargetQueryParams)
- **`FinvizPriceTargetData`**(PriceTargetData)
- **`FinvizPriceTargetFetcher`**(
    Fetcher[FinvizPriceTargetQueryParams, list[FinvizPriceTargetData]]
)

#### Decorators Used

staticmethod


---

## Related Files

The following files may be related based on imports and references:

**Imported Modules**:
- `Any`
- `DataFrame`
- `EmptyDataError`
- `Fetcher`
- `Field`
- `OpenBBError`
- `finvizfinance`
- `finvizfinance.quote`
- `get_requests_session`
- `openbb_core.app.model.abstract.error`
- `openbb_core.provider.abstract.fetcher`
- `openbb_core.provider.standard_models.price_target`
- `openbb_core.provider.utils.errors`
- `openbb_core.provider.utils.helpers`
- `pandas`


---

## Performance & Security Notes

No obvious security concerns detected in static analysis.


---

**Generated**: 2025-11-19T02:16:50.412269Z
**Generator**: World's Best Repo Book Generator v1.0

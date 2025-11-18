# Documentation: openbb_platform/providers/finviz/openbb_finviz/models/price_performance.py

## File Metadata
- **Path**: `openbb_platform/providers/finviz/openbb_finviz/models/price_performance.py`
- **Size**: 4,566 characters, 137 lines
- **Words**: 379
- **Extension**: .py
- **Classification**: Text file

## Original Source

```python
"""Finviz Price Performance Model."""

# pylint: disable=unused-argument
from typing import Any
from warnings import warn

from openbb_core.provider.abstract.fetcher import Fetcher
from openbb_core.provider.standard_models.recent_performance import (
    RecentPerformanceData,
    RecentPerformanceQueryParams,
)
from openbb_core.provider.utils.errors import EmptyDataError
from pydantic import Field


class FinvizPricePerformanceQueryParams(RecentPerformanceQueryParams):
    """
    Finviz Price Performance Query.

    Source: https://finviz.com/screener.ashx
    """

    __json_schema_extra__ = {"symbol": {"multiple_items_allowed": True}}


class FinvizPricePerformanceData(RecentPerformanceData):
    """Finviz Price Performance Data."""

    __alias_dict__ = {
        "symbol": "Ticker",
        "one_week": "Perf Week",
        "one_month": "Perf Month",
        "three_month": "Perf Quart",
        "six_month": "Perf Half",
        "one_year": "Perf Year",
        "ytd": "Perf YTD",
        "volatility_week": "Volatility W",
        "volatility_month": "Volatility M",
        "price": "Price",
        "one_day": "Change",
        "volume": "Volume",
        "average_volume": "Avg Volume",
        "relative_volume": "Rel Volume",
        "analyst_score": "Recom",
    }

    volatility_week: float | None = Field(
        default=None,
        description="One-week realized volatility, as a normalized percent.",
        json_schema_extra={"x-unit_measurement": "percent", "x-frontend_multiply": 100},
    )
    volatility_month: float | None = Field(
        default=None,
        description="One-month realized volatility, as a normalized percent.",
        json_schema_extra={"x-unit_measurement": "percent", "x-frontend_multiply": 100},
    )
    price: float | None = Field(
        default=None,
        description="Last Price.",
    )
    volume: float | None = Field(
        default=None,
        description="Current volume.",
    )
    average_volume: float | None = Field(
        default=None,
        description="Average daily volume.",
    )
    relative_volume: float | None = Field(
        default=None,
        description="Relative volume as a ratio of current volume to average volume.",
    )
    analyst_recommendation: float | None = Field(
        default=None,
        description="The analyst consensus, on a scale of 1-5 where 1 is a buy and 5 is a sell.",
    )
    symbol: str | None = Field(
        default=None,
        description="The ticker symbol.",
    )


class FinvizPricePerformanceFetcher(
    Fetcher[FinvizPricePerformanceQueryParams, list[FinvizPricePerformanceData]]
):
    """Finviz Price Performance Fetcher."""

    @staticmethod
    def transform_query(params: dict[str, Any]) -> FinvizPricePerformanceQueryParams:
        """Transform the query params."""
        return FinvizPricePerformanceQueryParams(**params)

    @staticmethod
    def extract_data(
        query: FinvizPricePerformanceQueryParams,
        credentials: dict[str, str] | None,
        **kwargs: Any,
    ) -> list[dict]:
        """Extract the raw data from Finviz."""
        # pylint: disable=import-outside-toplevel
        from finvizfinance import util
        from finvizfinance.screener import performance
        from openbb_core.provider.utils.helpers import get_requests_session

        util.session = get_requests_session()
        screen = performance.Performance()
        screen.set_filter(ticker=query.symbol)
        try:
            screen_df = screen.screener_view(verbose=0)
            if screen_df is None:
                raise EmptyDataError()
            screen_df.columns = screen_df.columns.str.strip()  # type: ignore
            screen_df = screen_df.fillna("N/A").replace("N/A", None)  # type: ignore
        except Exception as e:
            raise e from e

        symbols = query.symbol.split(",")

        # Check for missing symbols and warn of the missing symbols.
        for symbol in symbols:
            if symbol not in screen_df["Ticker"].tolist():
                warn(f"Symbol Error: {symbol} was not found.")

        return sorted(
            screen_df.to_dict(orient="records"),
            key=(lambda item: (symbols.index(item.get("Ticker", len(symbols))))),
        )

    @staticmethod
    def transform_data(
        query: FinvizPricePerformanceQueryParams,
        data: list[dict],
        **kwargs: Any,
    ) -> list[FinvizPricePerformanceData]:
        """Transform the raw data."""
        return [FinvizPricePerformanceData.model_validate(d) for d in data]

```

## High-Level Overview

Finviz Price Performance Model.

# pylint: disable=unused-argument
from typing import Any
from warnings import warn

from openbb_core.provider.abstract.fetcher import Fetcher
from openbb_core.provider.standard_models.recent_performance import (
RecentPerformanceData,
RecentPerformanceQueryParams,
)
from openbb_core.provider.utils.errors import EmptyDataError
from pydantic import Field


class FinvizPricePerformanceQueryParams(RecentPerformanceQueryParams):



__json_schema_extra__ = {"symbol": {"multiple_items_allowed": True}}

## Detailed Structure

### Python File Structure

**Classes** (3):
`FinvizPricePerformanceQueryParams`, `FinvizPricePerformanceData`, `FinvizPricePerformanceFetcher`

**Functions** (3):
`transform_query`, `extract_data`, `transform_data`

**Imports** (19):
`typing`, `Any`, `warnings`, `warn`, `openbb_core.provider.abstract.fetcher`, `Fetcher`, `openbb_core.provider.standard_models.recent_performance`, `openbb_core.provider.utils.errors`, `EmptyDataError`, `pydantic`, `Field`, `Finviz.`, `finvizfinance`, `util`, `finvizfinance.screener`, `performance`, `openbb_core.provider.utils.helpers`, `get_requests_session`, `e`


## Key Components

**Class `FinvizPricePerformanceQueryParams`**: Finviz Price Performance Query.

    Source: https://finviz.com/screener.ashx

**Class `FinvizPricePerformanceData`**: Finviz Price Performance Data.

**Class `FinvizPricePerformanceFetcher`**: Finviz Price Performance Fetcher.

## Usage & Examples

See source code for usage details.

## Related Files

- `typing`
- `warnings`
- `openbb_core.provider.abstract.fetcher`
- `openbb_core.provider.standard_models.recent_performance`
- `openbb_core.provider.utils.errors`
- `pydantic`
- `finvizfinance`
- `finvizfinance.screener`
- `openbb_core.provider.utils.helpers`

## Notes
- Generated: 2025-11-18T07:54:39.170832
- Generator: World's Best Repo Book Generator v1.0.0

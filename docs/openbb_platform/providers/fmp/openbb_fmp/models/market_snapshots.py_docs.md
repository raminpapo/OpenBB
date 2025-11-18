# Documentation: openbb_platform/providers/fmp/openbb_fmp/models/market_snapshots.py

## File Metadata
- **Path**: `openbb_platform/providers/fmp/openbb_fmp/models/market_snapshots.py`
- **Size**: 5,133 characters, 151 lines
- **Words**: 427
- **Extension**: .py
- **Classification**: Text file

## Original Source

```python
"""FMP Market Snapshots Model."""

# pylint: disable=unused-argument

from datetime import (
    date as dateType,
    datetime,
)
from typing import Any

from openbb_core.provider.abstract.fetcher import Fetcher
from openbb_core.provider.standard_models.market_snapshots import (
    MarketSnapshotsData,
    MarketSnapshotsQueryParams,
)
from openbb_fmp.utils.definitions import MARKETS
from pydantic import Field, field_validator


class FMPMarketSnapshotsQueryParams(MarketSnapshotsQueryParams):
    """FMP Market Snapshots Query.

    Source: https://site.financialmodelingprep.com/developer/docs#exchange-prices-quote
    """

    __json_schema_extra__ = {
        "market": {
            "x-widget_config": {
                "options": [{"label": m.upper(), "value": m} for m in MARKETS.__args__]
            }
        }
    }

    market: MARKETS = Field(
        description="The market to fetch data for.", default="nasdaq"
    )


class FMPMarketSnapshotsData(MarketSnapshotsData):
    """FMP Market Snapshots Data."""

    __alias_dict__ = {
        "high": "dayHigh",
        "low": "dayLow",
        "prev_close": "previousClose",
        "change_percent": "changePercentage",
        "close": "price",
        "last_price_timestamp": "timestamp",
        "ma50": "priceAvg50",
        "ma200": "priceAvg200",
        "year_high": "yearHigh",
        "year_low": "yearLow",
        "market_cap": "marketCap",
    }
    ma50: float | None = Field(description="The 50-day moving average.", default=None)
    ma200: float | None = Field(description="The 200-day moving average.", default=None)
    year_high: float | None = Field(description="The 52-week high.", default=None)
    year_low: float | None = Field(description="The 52-week low.", default=None)
    market_cap: int | float | None = Field(
        description="Market cap of the stock.", default=None
    )
    last_price_timestamp: datetime | dateType | None = Field(
        description="The timestamp of the last price.", default=None
    )

    @field_validator("change_percent", mode="before", check_fields=False)
    @classmethod
    def _normalize_percent(cls, v):
        """Normalize the percent."""
        return float(v) / 100 if v else 0

    @field_validator("name", mode="before", check_fields=False)
    @classmethod
    def _empty_strings(cls, v):
        """Clear empty strings."""
        return v if v and v not in (" ", "''") else None


class FMPMarketSnapshotsFetcher(
    Fetcher[
        FMPMarketSnapshotsQueryParams,
        list[FMPMarketSnapshotsData],
    ]
):
    """FMP Market Snapshots Fetcher."""

    @staticmethod
    def transform_query(params: dict[str, Any]) -> FMPMarketSnapshotsQueryParams:
        """Transform the query params."""
        return FMPMarketSnapshotsQueryParams(**params)

    @staticmethod
    async def aextract_data(
        query: FMPMarketSnapshotsQueryParams,
        credentials: dict[str, str] | None,
        **kwargs: Any,
    ) -> list:
        """Return the raw data from the FMP endpoint."""
        # pylint: disable=import-outside-toplevel
        from openbb_fmp.utils.helpers import get_data_many

        api_key = credentials.get("fmp_api_key") if credentials else ""
        base_url = "https://financialmodelingprep.com/stable/batch-"
        market = query.market.upper()

        if market == "ETF":
            url = f"{base_url}etf-quotes?short=false&apikey={api_key}"
        elif market == "MUTUAL_FUND":
            url = f"{base_url}mutualfund-quotes?short=false&apikey={api_key}"
        elif market == "FOREX":
            url = f"{base_url}forex-quotes?short=false&apikey={api_key}"
        elif market == "CRYPTO":
            url = f"{base_url}crypto-quotes?short=false&apikey={api_key}"
        elif market == "INDEX":
            url = f"{base_url}index-quotes?short=false&apikey={api_key}"
        elif market == "COMMODITY":
            url = f"{base_url}commodity-quotes?short=false&apikey={api_key}"
        else:
            url = f"{base_url}exchange-quote?exchange={market}&short=false&apikey={api_key}"

        return await get_data_many(url, **kwargs)

    @staticmethod
    def transform_data(
        query: FMPMarketSnapshotsQueryParams, data: list, **kwargs: Any
    ) -> list[FMPMarketSnapshotsData]:
        """Return the transformed data."""
        # pylint: disable=import-outside-toplevel
        import pandas as pd
        from openbb_core.provider.utils.errors import EmptyDataError

        df = pd.DataFrame(data)

        if df.empty:
            raise EmptyDataError("No data was returned")

        # We need to clean up the response because there is lots of very old data included.
        # Purge to most recent day only
        df.timestamp = pd.to_datetime(df.timestamp, unit="s", utc=True).dt.tz_localize(
            None
        )
        max_date = df.timestamp.max().date()
        df = df[df.timestamp.dt.date == max_date]

        return [
            FMPMarketSnapshotsData.model_validate(d)
            for d in df.sort_values(by="timestamp", ascending=False).to_dict(
                orient="records"
            )
        ]

```

## High-Level Overview

FMP Market Snapshots Model.

# pylint: disable=unused-argument

from datetime import (
date as dateType,
datetime,
)
from typing import Any

from openbb_core.provider.abstract.fetcher import Fetcher
from openbb_core.provider.standard_models.market_snapshots import (
MarketSnapshotsData,
MarketSnapshotsQueryParams,
)
from openbb_fmp.utils.definitions import MARKETS
from pydantic import Field, field_validator


class FMPMarketSnapshotsQueryParams(MarketSnapshotsQueryParams):

## Detailed Structure

### Python File Structure

**Classes** (3):
`FMPMarketSnapshotsQueryParams`, `FMPMarketSnapshotsData`, `FMPMarketSnapshotsFetcher`

**Functions** (5):
`_normalize_percent`, `_empty_strings`, `transform_query`, `aextract_data`, `transform_data`

**Imports** (16):
`datetime`, `typing`, `Any`, `openbb_core.provider.abstract.fetcher`, `Fetcher`, `openbb_core.provider.standard_models.market_snapshots`, `openbb_fmp.utils.definitions`, `MARKETS`, `pydantic`, `Field`, `the`, `openbb_fmp.utils.helpers`, `get_data_many`, `pandas`, `openbb_core.provider.utils.errors`, `EmptyDataError`


## Key Components

**Class `FMPMarketSnapshotsQueryParams`**: FMP Market Snapshots Query.

    Source: https://site.financialmodelingprep.com/developer/docs#exchange-prices-quote

**Class `FMPMarketSnapshotsData`**: FMP Market Snapshots Data.

**Class `FMPMarketSnapshotsFetcher`**: FMP Market Snapshots Fetcher.

## Usage & Examples

See source code for usage details.

## Related Files

- `datetime`
- `typing`
- `openbb_core.provider.abstract.fetcher`
- `openbb_core.provider.standard_models.market_snapshots`
- `openbb_fmp.utils.definitions`
- `pydantic`
- `openbb_fmp.utils.helpers`
- `pandas`
- `openbb_core.provider.utils.errors`

## Notes
- Generated: 2025-11-18T07:54:39.406747
- Generator: World's Best Repo Book Generator v1.0.0

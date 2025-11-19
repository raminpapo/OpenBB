# File Documentation: historical_dividends.py

## Metadata
- **Path**: `openbb_platform/providers/yfinance/openbb_yfinance/models/historical_dividends.py`
- **Size**: 2,897 bytes
- **Lines**: 79
- **Category**: python
- **Extension**: .py

---

## Original Source

```python
"""YFinance Historical Dividends Model."""

# pylint: disable=unused-argument
from typing import Any

from openbb_core.app.model.abstract.error import OpenBBError
from openbb_core.provider.abstract.fetcher import Fetcher
from openbb_core.provider.standard_models.historical_dividends import (
    HistoricalDividendsData,
    HistoricalDividendsQueryParams,
)


class YFinanceHistoricalDividendsQueryParams(HistoricalDividendsQueryParams):
    """YFinance Historical Dividends Query."""


class YFinanceHistoricalDividendsData(HistoricalDividendsData):
    """YFinance Historical Dividends Data. All data is split-adjusted."""


class YFinanceHistoricalDividendsFetcher(
    Fetcher[
        YFinanceHistoricalDividendsQueryParams, list[YFinanceHistoricalDividendsData]
    ]
):
    """YFinance Historical Dividends Fetcher."""

    @staticmethod
    def transform_query(
        params: dict[str, Any],
    ) -> YFinanceHistoricalDividendsQueryParams:
        """Transform the query."""
        return YFinanceHistoricalDividendsQueryParams(**params)

    @staticmethod
    def extract_data(
        query: YFinanceHistoricalDividendsQueryParams,
        credentials: dict[str, str] | None,
        **kwargs: Any,
    ) -> list[dict]:
        """Extract the raw data from YFinance."""
        # pylint: disable=import-outside-toplevel
        from curl_adapter import CurlCffiAdapter
        from openbb_core.provider.utils.helpers import get_requests_session
        from yfinance import Ticker

        session = get_requests_session()
        session.mount("https://", CurlCffiAdapter())
        session.mount("http://", CurlCffiAdapter())

        try:
            ticker = Ticker(
                query.symbol,
                session=session,
            ).get_dividends()
            if isinstance(ticker, list) and not ticker or ticker.empty:  # type: ignore
                raise OpenBBError(f"No dividend data found for {query.symbol}")
        except Exception as e:
            raise OpenBBError(f"Error getting data for {query.symbol}: {e}") from e
        ticker.index.name = "ex_dividend_date"  # type: ignore[union-attr]
        ticker.name = "amount"  # type: ignore
        if query.start_date is not None:
            ticker = ticker[ticker.index.astype(str) >= query.start_date.strftime("%Y-%m-%d")]  # type: ignore
        if query.end_date is not None:
            ticker = ticker[ticker.index.astype(str) <= query.end_date.strftime("%Y-%m-%d")]  # type: ignore
        dividends = ticker.reset_index().to_dict("records")  # type: ignore

        return dividends

    @staticmethod
    def transform_data(
        query: YFinanceHistoricalDividendsQueryParams,
        data: list[dict],
        **kwargs: Any,
    ) -> list[YFinanceHistoricalDividendsData]:
        """Transform the data."""
        return [YFinanceHistoricalDividendsData.model_validate(d) for d in data]

```



---

## High-Level Overview

This is a **python** file named `historical_dividends.py`.

**Python Module**

- **Classes** (3): YFinanceHistoricalDividendsQueryParams, YFinanceHistoricalDividendsData, YFinanceHistoricalDividendsFetcher
- **Functions** (3): transform_query, extract_data, transform_data
- **Import Statements**: 2


---

## Detailed Analysis

### Python Code Structure

#### Classes

- **`YFinanceHistoricalDividendsQueryParams`**(HistoricalDividendsQueryParams)
- **`YFinanceHistoricalDividendsData`**(HistoricalDividendsData)
- **`YFinanceHistoricalDividendsFetcher`**(
    Fetcher[
        YFinanceHistoricalDividendsQueryParams, list[YFinanceHistoricalDividendsData]
    ]
)

#### Decorators Used

staticmethod


---

## Related Files

The following files may be related based on imports and references:

**Imported Modules**:
- `Any`
- `CurlCffiAdapter`
- `Fetcher`
- `OpenBBError`
- `Ticker`
- `curl_adapter`
- `get_requests_session`
- `openbb_core.app.model.abstract.error`
- `openbb_core.provider.abstract.fetcher`
- `openbb_core.provider.standard_models.historical_dividends`
- `openbb_core.provider.utils.helpers`
- `typing`
- `yfinance`


---

## Performance & Security Notes

No obvious security concerns detected in static analysis.


---

**Generated**: 2025-11-19T02:16:55.183862Z
**Generator**: World's Best Repo Book Generator v1.0

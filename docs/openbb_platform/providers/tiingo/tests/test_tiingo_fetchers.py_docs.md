# File Documentation: test_tiingo_fetchers.py

## Metadata
- **Path**: `openbb_platform/providers/tiingo/tests/test_tiingo_fetchers.py`
- **Size**: 3,014 bytes
- **Lines**: 100
- **Category**: python
- **Extension**: .py

---

## Original Source

```python
"""Test Tiingo fetchers."""

from datetime import date

import pytest
from openbb_core.app.service.user_service import UserService
from openbb_tiingo.models.company_news import TiingoCompanyNewsFetcher
from openbb_tiingo.models.crypto_historical import TiingoCryptoHistoricalFetcher
from openbb_tiingo.models.currency_historical import TiingoCurrencyHistoricalFetcher
from openbb_tiingo.models.equity_historical import TiingoEquityHistoricalFetcher
from openbb_tiingo.models.trailing_dividend_yield import TiingoTrailingDivYieldFetcher
from openbb_tiingo.models.world_news import TiingoWorldNewsFetcher

test_credentials = UserService().default_user_settings.credentials.model_dump(
    mode="json"
)


@pytest.fixture(scope="module")
def vcr_config():
    """VCR configuration."""
    return {
        "filter_headers": [("User-Agent", None)],
        "filter_query_parameters": [
            ("token", "MOCK_TOKEN"),
        ],
    }


@pytest.mark.record_http
def test_tiingo_equity_historical_fetcher(credentials=test_credentials):
    """Test Tiingo equity historical fetcher."""
    params = {
        "symbol": "AAPL",
        "start_date": date(2023, 1, 1),
        "end_date": date(2023, 6, 6),
    }

    fetcher = TiingoEquityHistoricalFetcher()
    result = fetcher.test(params, credentials)
    assert result is None


@pytest.mark.record_http
def test_tiingo_company_news_fetcher(credentials=test_credentials):
    """Test Tiingo company news fetcher."""
    params = {"symbol": "AAPL,MSFT", "limit": 2}

    fetcher = TiingoCompanyNewsFetcher()
    result = fetcher.test(params, credentials)
    assert result is None


@pytest.mark.record_http
def test_tiingo_world_news_fetcher(credentials=test_credentials):
    """Test Tiingo world news fetcher."""
    params = {"limit": 20}

    fetcher = TiingoWorldNewsFetcher()
    result = fetcher.test(params, credentials)
    assert result is None


@pytest.mark.record_http
def test_tiingo_crypto_historical_fetcher(credentials=test_credentials):
    """Test Tiingo crypto historical fetcher."""
    params = {
        "symbol": "BTCUSD",
        "start_date": date(2023, 1, 1),
        "end_date": date(2023, 6, 6),
    }

    fetcher = TiingoCryptoHistoricalFetcher()
    result = fetcher.test(params, credentials)
    assert result is None


@pytest.mark.record_http
def test_tiingo_currency_historical_fetcher(credentials=test_credentials):
    """Test Tiingo currency historical fetcher."""
    params = {
        "symbol": "EURUSD",
        "start_date": date(2023, 1, 1),
        "end_date": date(2023, 6, 6),
    }

    fetcher = TiingoCurrencyHistoricalFetcher()
    result = fetcher.test(params, credentials)
    assert result is None


@pytest.mark.record_http
def test_tiingo_trailing_div_yield_fetcher(credentials=test_credentials):
    """Test Tiingo trailing dividend yield fetcher."""
    params = {"symbol": "SCHD"}

    fetcher = TiingoTrailingDivYieldFetcher()
    result = fetcher.test(params, credentials)
    assert result is None

```



---

## High-Level Overview

This is a **python** file named `test_tiingo_fetchers.py`.

**Python Module**

- **Functions** (7): vcr_config, test_tiingo_equity_historical_fetcher, test_tiingo_company_news_fetcher, test_tiingo_world_news_fetcher, test_tiingo_crypto_historical_fetcher, test_tiingo_currency_historical_fetcher, test_tiingo_trailing_div_yield_fetcher
- **Import Statements**: 1


---

## Detailed Analysis

### Python Code Structure


#### Functions

- **`vcr_config()`**
- **`test_tiingo_equity_historical_fetcher(credentials=test_credentials)`**
- **`test_tiingo_company_news_fetcher(credentials=test_credentials)`**
- **`test_tiingo_world_news_fetcher(credentials=test_credentials)`**
- **`test_tiingo_crypto_historical_fetcher(credentials=test_credentials)`**
- **`test_tiingo_currency_historical_fetcher(credentials=test_credentials)`**
- **`test_tiingo_trailing_div_yield_fetcher(credentials=test_credentials)`**

#### Decorators Used

pytest


---

## Related Files

The following files may be related based on imports and references:

**Imported Modules**:
- `TiingoCompanyNewsFetcher`
- `TiingoCryptoHistoricalFetcher`
- `TiingoCurrencyHistoricalFetcher`
- `TiingoEquityHistoricalFetcher`
- `TiingoTrailingDivYieldFetcher`
- `TiingoWorldNewsFetcher`
- `UserService`
- `date`
- `datetime`
- `openbb_core.app.service.user_service`
- `openbb_tiingo.models.company_news`
- `openbb_tiingo.models.crypto_historical`
- `openbb_tiingo.models.currency_historical`
- `openbb_tiingo.models.equity_historical`
- `openbb_tiingo.models.trailing_dividend_yield`


---

## Performance & Security Notes

No obvious security concerns detected in static analysis.


---

**Generated**: 2025-11-19T02:16:53.021876Z
**Generator**: World's Best Repo Book Generator v1.0

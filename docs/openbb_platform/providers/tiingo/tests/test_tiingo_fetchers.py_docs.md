# Documentation: openbb_platform/providers/tiingo/tests/test_tiingo_fetchers.py

## File Metadata
- **Path**: `openbb_platform/providers/tiingo/tests/test_tiingo_fetchers.py`
- **Size**: 3,014 characters, 100 lines
- **Words**: 229
- **Extension**: .py
- **Classification**: Text file

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

## High-Level Overview

Test Tiingo fetchers.

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

## Detailed Structure

### Python File Structure

**Classes** (0):
None

**Functions** (7):
`vcr_config`, `test_tiingo_equity_historical_fetcher`, `test_tiingo_company_news_fetcher`, `test_tiingo_world_news_fetcher`, `test_tiingo_crypto_historical_fetcher`, `test_tiingo_currency_historical_fetcher`, `test_tiingo_trailing_div_yield_fetcher`

**Imports** (17):
`datetime`, `date`, `pytest`, `openbb_core.app.service.user_service`, `UserService`, `openbb_tiingo.models.company_news`, `TiingoCompanyNewsFetcher`, `openbb_tiingo.models.crypto_historical`, `TiingoCryptoHistoricalFetcher`, `openbb_tiingo.models.currency_historical`, `TiingoCurrencyHistoricalFetcher`, `openbb_tiingo.models.equity_historical`, `TiingoEquityHistoricalFetcher`, `openbb_tiingo.models.trailing_dividend_yield`, `TiingoTrailingDivYieldFetcher`, `openbb_tiingo.models.world_news`, `TiingoWorldNewsFetcher`


## Key Components

No major components extracted.

## Usage & Examples

See source code for usage details.

## Related Files

- `datetime`
- `pytest`
- `openbb_core.app.service.user_service`
- `openbb_tiingo.models.company_news`
- `openbb_tiingo.models.crypto_historical`
- `openbb_tiingo.models.currency_historical`
- `openbb_tiingo.models.equity_historical`
- `openbb_tiingo.models.trailing_dividend_yield`
- `openbb_tiingo.models.world_news`

## Notes
- Generated: 2025-11-18T07:54:41.755144
- Generator: World's Best Repo Book Generator v1.0.0

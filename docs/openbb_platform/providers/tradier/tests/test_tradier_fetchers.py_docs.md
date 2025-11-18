# Documentation: openbb_platform/providers/tradier/tests/test_tradier_fetchers.py

## File Metadata
- **Path**: `openbb_platform/providers/tradier/tests/test_tradier_fetchers.py`
- **Size**: 2,231 characters, 76 lines
- **Words**: 164
- **Extension**: .py
- **Classification**: Text file

## Original Source

```python
"""Tradier Fetchers Tests."""

from datetime import datetime

import pytest
from openbb_core.app.service.user_service import UserService
from openbb_tradier.models.equity_historical import TradierEquityHistoricalFetcher
from openbb_tradier.models.equity_quote import TradierEquityQuoteFetcher
from openbb_tradier.models.equity_search import TradierEquitySearchFetcher
from openbb_tradier.models.options_chains import TradierOptionsChainsFetcher

test_credentials = UserService().default_user_settings.credentials.model_dump(
    mode="json"
)


@pytest.fixture(scope="module")
def vcr_config():
    """VCR configuration."""
    return {
        "filter_headers": [
            ("User-Agent", None),
            ("Authorization", "MOCK_API_KEY"),
        ],
        "filter_query_parameters": [],
    }


@pytest.mark.record_http
def test_tradier_equity_historical_fetcher(credentials=test_credentials):
    """Test the Tradier Equity Historical fetcher."""
    params = {
        "start_date": datetime(2024, 2, 1).date(),
        "end_date": datetime(2024, 2, 29).date(),
        "symbol": "AAPL",
        "interval": "1d",
    }

    fetcher = TradierEquityHistoricalFetcher()
    result = fetcher.test(params, credentials)
    assert result is None


@pytest.mark.record_http
def test_tradier_equity_search_fetcher(credentials=test_credentials):
    """Test the Tradier Equity Search fetcher."""
    params = {
        "query": "brookfield",
        "is_symbol": False,
    }

    fetcher = TradierEquitySearchFetcher()
    result = fetcher.test(params, credentials)
    assert result is None


@pytest.mark.record_http
def test_tradier_equity_quote_fetcher(credentials=test_credentials):
    """Test the Tradier Equity Quote fetcher."""
    params = {"symbol": "SPY,SPY251219P00450000"}

    fetcher = TradierEquityQuoteFetcher()
    result = fetcher.test(params, credentials)
    assert result is None


@pytest.mark.record_http
def test_tradier_derivatives_options_chains_fetcher(credentials=test_credentials):
    """Test the Tradier Derivatives Options Chains fetcher."""

    params = {"symbol": "PLTR"}

    fetcher = TradierOptionsChainsFetcher()
    result = fetcher.test(params, credentials)
    assert result is None

```

## High-Level Overview

Tradier Fetchers Tests.

from datetime import datetime

import pytest
from openbb_core.app.service.user_service import UserService
from openbb_tradier.models.equity_historical import TradierEquityHistoricalFetcher
from openbb_tradier.models.equity_quote import TradierEquityQuoteFetcher
from openbb_tradier.models.equity_search import TradierEquitySearchFetcher
from openbb_tradier.models.options_chains import TradierOptionsChainsFetcher

test_credentials = UserService().default_user_settings.credentials.model_dump(
mode="json"
)


@pytest.fixture(scope="module")
def vcr_config():
VCR configuration.
Test the Tradier Equity Historical fetcher.

## Detailed Structure

### Python File Structure

**Classes** (0):
None

**Functions** (5):
`vcr_config`, `test_tradier_equity_historical_fetcher`, `test_tradier_equity_search_fetcher`, `test_tradier_equity_quote_fetcher`, `test_tradier_derivatives_options_chains_fetcher`

**Imports** (13):
`datetime`, `datetime`, `pytest`, `openbb_core.app.service.user_service`, `UserService`, `openbb_tradier.models.equity_historical`, `TradierEquityHistoricalFetcher`, `openbb_tradier.models.equity_quote`, `TradierEquityQuoteFetcher`, `openbb_tradier.models.equity_search`, `TradierEquitySearchFetcher`, `openbb_tradier.models.options_chains`, `TradierOptionsChainsFetcher`


## Key Components

No major components extracted.

## Usage & Examples

See source code for usage details.

## Related Files

- `datetime`
- `pytest`
- `openbb_core.app.service.user_service`
- `openbb_tradier.models.equity_historical`
- `openbb_tradier.models.equity_quote`
- `openbb_tradier.models.equity_search`
- `openbb_tradier.models.options_chains`

## Notes
- Generated: 2025-11-18T07:54:43.473080
- Generator: World's Best Repo Book Generator v1.0.0

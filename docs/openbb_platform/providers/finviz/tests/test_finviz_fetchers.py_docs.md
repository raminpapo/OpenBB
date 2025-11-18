# Documentation: openbb_platform/providers/finviz/tests/test_finviz_fetchers.py

## File Metadata
- **Path**: `openbb_platform/providers/finviz/tests/test_finviz_fetchers.py`
- **Size**: 2,831 characters, 91 lines
- **Words**: 204
- **Extension**: .py
- **Classification**: Text file

## Original Source

```python
"""Finviz Fetcher Tests."""

import pytest
from openbb_core.app.service.user_service import UserService
from openbb_finviz.models.compare_groups import FinvizCompareGroupsFetcher
from openbb_finviz.models.equity_profile import FinvizEquityProfileFetcher
from openbb_finviz.models.equity_screener import FinvizEquityScreenerFetcher
from openbb_finviz.models.key_metrics import FinvizKeyMetricsFetcher
from openbb_finviz.models.price_performance import FinvizPricePerformanceFetcher
from openbb_finviz.models.price_target import FinvizPriceTargetFetcher

test_credentials = UserService().default_user_settings.credentials.model_dump(
    mode="json"
)


@pytest.fixture(scope="module")
def vcr_config():
    """VCR configuration."""
    return {
        "filter_headers": [
            ("User-Agent", None),
            ("Cookie", "MOCK_COOKIE"),
            ("Set-Cookie", "MOCK_COOKIE"),
        ],
        "filter_query_parameters": [
            ("Cookie", "MOCK_COOKIE"),
            ("Set-Cookie", "MOCK_COOKIE"),
        ],
    }


@pytest.mark.record_http
def test_finviz_price_target_fetcher(credentials=test_credentials):
    """Test Finviz Price Target Fetcher."""
    params = {"symbol": "AAPL"}

    fetcher = FinvizPriceTargetFetcher()
    result = fetcher.test(params, credentials)
    assert result is None


@pytest.mark.record_http
def test_finviz_price_performance_fetcher(credentials=test_credentials):
    """Test Finviz Price Performance Fetcher."""
    params = {"symbol": "AAPL"}

    fetcher = FinvizPricePerformanceFetcher()
    result = fetcher.test(params, credentials)
    assert result is None


@pytest.mark.record_http
def test_finviz_key_metrics_fetcher(credentials=test_credentials):
    """Test Finviz Key Metrics Fetcher."""
    params = {"symbol": "AAPL"}

    fetcher = FinvizKeyMetricsFetcher()
    result = fetcher.test(params, credentials)
    assert result is None


@pytest.mark.record_http
def test_finviz_equity_profile_fetcher(credentials=test_credentials):
    """Test Finviz Equity Profile Fetcher."""
    params = {"symbol": "AAPL"}

    fetcher = FinvizEquityProfileFetcher()
    result = fetcher.test(params, credentials)
    assert result is None


@pytest.mark.record_http
def test_finviz_compare_groups_fetcher(credentials=test_credentials):
    """Test Finviz Compare Groups Fetcher."""
    params = {"group": "country", "metric": "performance"}

    fetcher = FinvizCompareGroupsFetcher()
    result = fetcher.test(params, credentials)
    assert result is None


@pytest.mark.record_http
def test_finviz_equity_screener_fetcher(credentials=test_credentials):
    """Test Finviz Equity Screener Fetcher."""
    params = {"signal": "most_active", "limit": 20}

    fetcher = FinvizEquityScreenerFetcher()
    result = fetcher.test(params, credentials)
    assert result is None

```

## High-Level Overview

Finviz Fetcher Tests.

import pytest
from openbb_core.app.service.user_service import UserService
from openbb_finviz.models.compare_groups import FinvizCompareGroupsFetcher
from openbb_finviz.models.equity_profile import FinvizEquityProfileFetcher
from openbb_finviz.models.equity_screener import FinvizEquityScreenerFetcher
from openbb_finviz.models.key_metrics import FinvizKeyMetricsFetcher
from openbb_finviz.models.price_performance import FinvizPricePerformanceFetcher
from openbb_finviz.models.price_target import FinvizPriceTargetFetcher

test_credentials = UserService().default_user_settings.credentials.model_dump(
mode="json"
)


@pytest.fixture(scope="module")
def vcr_config():
VCR configuration.
Test Finviz Price Target Fetcher.

## Detailed Structure

### Python File Structure

**Classes** (0):
None

**Functions** (7):
`vcr_config`, `test_finviz_price_target_fetcher`, `test_finviz_price_performance_fetcher`, `test_finviz_key_metrics_fetcher`, `test_finviz_equity_profile_fetcher`, `test_finviz_compare_groups_fetcher`, `test_finviz_equity_screener_fetcher`

**Imports** (15):
`pytest`, `openbb_core.app.service.user_service`, `UserService`, `openbb_finviz.models.compare_groups`, `FinvizCompareGroupsFetcher`, `openbb_finviz.models.equity_profile`, `FinvizEquityProfileFetcher`, `openbb_finviz.models.equity_screener`, `FinvizEquityScreenerFetcher`, `openbb_finviz.models.key_metrics`, `FinvizKeyMetricsFetcher`, `openbb_finviz.models.price_performance`, `FinvizPricePerformanceFetcher`, `openbb_finviz.models.price_target`, `FinvizPriceTargetFetcher`


## Key Components

No major components extracted.

## Usage & Examples

See source code for usage details.

## Related Files

- `pytest`
- `openbb_core.app.service.user_service`
- `openbb_finviz.models.compare_groups`
- `openbb_finviz.models.equity_profile`
- `openbb_finviz.models.equity_screener`
- `openbb_finviz.models.key_metrics`
- `openbb_finviz.models.price_performance`
- `openbb_finviz.models.price_target`

## Notes
- Generated: 2025-11-18T07:54:39.305846
- Generator: World's Best Repo Book Generator v1.0.0

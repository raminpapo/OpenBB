# File Documentation: test_finviz_fetchers.py

## Metadata
- **Path**: `openbb_platform/providers/finviz/tests/test_finviz_fetchers.py`
- **Size**: 2,831 bytes
- **Lines**: 91
- **Category**: python
- **Extension**: .py

---

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



---

## High-Level Overview

This is a **python** file named `test_finviz_fetchers.py`.

**Python Module**

- **Functions** (7): vcr_config, test_finviz_price_target_fetcher, test_finviz_price_performance_fetcher, test_finviz_key_metrics_fetcher, test_finviz_equity_profile_fetcher, test_finviz_compare_groups_fetcher, test_finviz_equity_screener_fetcher
- **Import Statements**: 1


---

## Detailed Analysis

### Python Code Structure


#### Functions

- **`vcr_config()`**
- **`test_finviz_price_target_fetcher(credentials=test_credentials)`**
- **`test_finviz_price_performance_fetcher(credentials=test_credentials)`**
- **`test_finviz_key_metrics_fetcher(credentials=test_credentials)`**
- **`test_finviz_equity_profile_fetcher(credentials=test_credentials)`**
- **`test_finviz_compare_groups_fetcher(credentials=test_credentials)`**
- **`test_finviz_equity_screener_fetcher(credentials=test_credentials)`**

#### Decorators Used

pytest


---

## Related Files

The following files may be related based on imports and references:

**Imported Modules**:
- `FinvizCompareGroupsFetcher`
- `FinvizEquityProfileFetcher`
- `FinvizEquityScreenerFetcher`
- `FinvizKeyMetricsFetcher`
- `FinvizPricePerformanceFetcher`
- `FinvizPriceTargetFetcher`
- `UserService`
- `openbb_core.app.service.user_service`
- `openbb_finviz.models.compare_groups`
- `openbb_finviz.models.equity_profile`
- `openbb_finviz.models.equity_screener`
- `openbb_finviz.models.key_metrics`
- `openbb_finviz.models.price_performance`
- `openbb_finviz.models.price_target`
- `pytest`


---

## Performance & Security Notes

No obvious security concerns detected in static analysis.


---

**Generated**: 2025-11-19T02:16:50.463501Z
**Generator**: World's Best Repo Book Generator v1.0

# File Documentation: test_alpha_vantage_fetchers.py

## Metadata
- **Path**: `openbb_platform/providers/alpha_vantage/tests/test_alpha_vantage_fetchers.py`
- **Size**: 1,403 bytes
- **Lines**: 49
- **Category**: python
- **Extension**: .py

---

## Original Source

```python
"""Test the Alpha Vantage fetchers."""

from datetime import date

import pytest
from openbb_alpha_vantage.models.equity_historical import AVEquityHistoricalFetcher
from openbb_alpha_vantage.models.historical_eps import AVHistoricalEpsFetcher
from openbb_core.app.service.user_service import UserService

test_credentials = UserService().default_user_settings.credentials.model_dump(
    mode="json"
)


@pytest.fixture(scope="module")
def vcr_config():
    """VCR configuration."""
    return {
        "filter_headers": [("User-Agent", None)],
        "filter_query_parameters": [
            ("apikey", "MOCK_API_KEY"),
        ],
    }


@pytest.mark.record_http
def test_av_equity_historical_fetcher(credentials=test_credentials):
    """Test the Alpha Vantage Equity Historical fetcher."""
    params = {
        "symbol": "AAPL",
        "start_date": date(2023, 1, 1),
        "end_date": date(2023, 1, 10),
        "interval": "15m",
    }

    fetcher = AVEquityHistoricalFetcher()
    result = fetcher.test(params, credentials)
    assert result is None


@pytest.mark.record_http
def test_av_historical_eps_fetcher(credentials=test_credentials):
    """Test the Alpha Vantage Historical Earnings fetcher."""
    params = {"symbol": "AAPL,MSFT", "period": "quarter", "limit": 4}

    fetcher = AVHistoricalEpsFetcher()
    result = fetcher.test(params, credentials)
    assert result is None

```



---

## High-Level Overview

This is a **python** file named `test_alpha_vantage_fetchers.py`.

**Python Module**

- **Functions** (3): vcr_config, test_av_equity_historical_fetcher, test_av_historical_eps_fetcher
- **Import Statements**: 1


---

## Detailed Analysis

### Python Code Structure


#### Functions

- **`vcr_config()`**
- **`test_av_equity_historical_fetcher(credentials=test_credentials)`**
- **`test_av_historical_eps_fetcher(credentials=test_credentials)`**

#### Decorators Used

pytest


---

## Related Files

The following files may be related based on imports and references:

**Imported Modules**:
- `AVEquityHistoricalFetcher`
- `AVHistoricalEpsFetcher`
- `UserService`
- `date`
- `datetime`
- `openbb_alpha_vantage.models.equity_historical`
- `openbb_alpha_vantage.models.historical_eps`
- `openbb_core.app.service.user_service`
- `pytest`


---

## Performance & Security Notes

No obvious security concerns detected in static analysis.


---

**Generated**: 2025-11-19T02:16:48.255372Z
**Generator**: World's Best Repo Book Generator v1.0

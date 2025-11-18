# Documentation: openbb_platform/providers/alpha_vantage/tests/test_alpha_vantage_fetchers.py

## File Metadata
- **Path**: `openbb_platform/providers/alpha_vantage/tests/test_alpha_vantage_fetchers.py`
- **Size**: 1,403 characters, 49 lines
- **Words**: 110
- **Extension**: .py
- **Classification**: Text file

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

## High-Level Overview

Test the Alpha Vantage fetchers.

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
VCR configuration.
Test the Alpha Vantage Equity Historical fetcher.
params = {
"symbol": "AAPL",

## Detailed Structure

### Python File Structure

**Classes** (0):
None

**Functions** (3):
`vcr_config`, `test_av_equity_historical_fetcher`, `test_av_historical_eps_fetcher`

**Imports** (9):
`datetime`, `date`, `pytest`, `openbb_alpha_vantage.models.equity_historical`, `AVEquityHistoricalFetcher`, `openbb_alpha_vantage.models.historical_eps`, `AVHistoricalEpsFetcher`, `openbb_core.app.service.user_service`, `UserService`


## Key Components

No major components extracted.

## Usage & Examples

See source code for usage details.

## Related Files

- `datetime`
- `pytest`
- `openbb_alpha_vantage.models.equity_historical`
- `openbb_alpha_vantage.models.historical_eps`
- `openbb_core.app.service.user_service`

## Notes
- Generated: 2025-11-18T07:54:37.267378
- Generator: World's Best Repo Book Generator v1.0.0

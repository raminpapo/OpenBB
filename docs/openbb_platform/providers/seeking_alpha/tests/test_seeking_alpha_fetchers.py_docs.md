# Documentation: openbb_platform/providers/seeking_alpha/tests/test_seeking_alpha_fetchers.py

## File Metadata
- **Path**: `openbb_platform/providers/seeking_alpha/tests/test_seeking_alpha_fetchers.py`
- **Size**: 1,857 characters, 61 lines
- **Words**: 133
- **Extension**: .py
- **Classification**: Text file

## Original Source

```python
"""Tests for the Seeking Alpha fetchers."""

import pytest
from openbb_core.app.service.user_service import UserService
from openbb_seeking_alpha.models.calendar_earnings import SACalendarEarningsFetcher
from openbb_seeking_alpha.models.forward_eps_estimates import (
    SAForwardEpsEstimatesFetcher,
)
from openbb_seeking_alpha.models.forward_sales_estimates import (
    SAForwardSalesEstimatesFetcher,
)

test_credentials = UserService().default_user_settings.credentials.model_dump(
    mode="json"
)


@pytest.fixture(scope="module")
def vcr_config():
    """VCR configuration."""
    return {
        "filter_headers": [("User-Agent", None)],
        "filter_query_parameters": [
            ("filter[selected_date]", "MOCK_DATE"),
            ("relative_periods", "MOCK_PERIODS"),
            ("estimates_data_items", "MOCK_ITEMS"),
            ("period_type", "MOCK_PERIOD"),
            ("ticker_ids", "MOCK_TICKER_IDS"),
        ],
    }


@pytest.mark.record_http
def test_sa_calendar_earnings_fetcher(credentials=test_credentials):
    """Test the Seeking Alpha Calendar Earnings fetcher."""
    params = {}

    fetcher = SACalendarEarningsFetcher()
    result = fetcher.test(params, credentials)
    assert result is None


@pytest.mark.record_http
def test_sa_forward_eps_estimates(credentials=test_credentials):
    """Test the Seeking Alpha Forward EPS Estimates fetcher."""
    params = {"symbol": "NVDA"}

    fetcher = SAForwardEpsEstimatesFetcher()
    result = fetcher.test(params, credentials)
    assert result is None


@pytest.mark.record_http
def test_sa_forward_sales_estimates(credentials=test_credentials):
    """Test the Seeking Alpha Forward Sales Estimates fetcher."""
    params = {"symbol": "NVDA"}

    fetcher = SAForwardSalesEstimatesFetcher()
    result = fetcher.test(params, credentials)
    assert result is None

```

## High-Level Overview

Tests for the Seeking Alpha fetchers.

import pytest
from openbb_core.app.service.user_service import UserService
from openbb_seeking_alpha.models.calendar_earnings import SACalendarEarningsFetcher
from openbb_seeking_alpha.models.forward_eps_estimates import (
SAForwardEpsEstimatesFetcher,
)
from openbb_seeking_alpha.models.forward_sales_estimates import (
SAForwardSalesEstimatesFetcher,
)

test_credentials = UserService().default_user_settings.credentials.model_dump(
mode="json"
)


@pytest.fixture(scope="module")
def vcr_config():
VCR configuration.

## Detailed Structure

### Python File Structure

**Classes** (0):
None

**Functions** (4):
`vcr_config`, `test_sa_calendar_earnings_fetcher`, `test_sa_forward_eps_estimates`, `test_sa_forward_sales_estimates`

**Imports** (7):
`pytest`, `openbb_core.app.service.user_service`, `UserService`, `openbb_seeking_alpha.models.calendar_earnings`, `SACalendarEarningsFetcher`, `openbb_seeking_alpha.models.forward_eps_estimates`, `openbb_seeking_alpha.models.forward_sales_estimates`


## Key Components

No major components extracted.

## Usage & Examples

See source code for usage details.

## Related Files

- `pytest`
- `openbb_core.app.service.user_service`
- `openbb_seeking_alpha.models.calendar_earnings`
- `openbb_seeking_alpha.models.forward_eps_estimates`
- `openbb_seeking_alpha.models.forward_sales_estimates`

## Notes
- Generated: 2025-11-18T07:54:41.678644
- Generator: World's Best Repo Book Generator v1.0.0

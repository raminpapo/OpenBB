# File Documentation: test_seeking_alpha_fetchers.py

## Metadata
- **Path**: `openbb_platform/providers/seeking_alpha/tests/test_seeking_alpha_fetchers.py`
- **Size**: 1,857 bytes
- **Lines**: 61
- **Category**: python
- **Extension**: .py

---

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



---

## High-Level Overview

This is a **python** file named `test_seeking_alpha_fetchers.py`.

**Python Module**

- **Functions** (4): vcr_config, test_sa_calendar_earnings_fetcher, test_sa_forward_eps_estimates, test_sa_forward_sales_estimates
- **Import Statements**: 1


---

## Detailed Analysis

### Python Code Structure


#### Functions

- **`vcr_config()`**
- **`test_sa_calendar_earnings_fetcher(credentials=test_credentials)`**
- **`test_sa_forward_eps_estimates(credentials=test_credentials)`**
- **`test_sa_forward_sales_estimates(credentials=test_credentials)`**

#### Decorators Used

pytest


---

## Related Files

The following files may be related based on imports and references:

**Imported Modules**:
- `SACalendarEarningsFetcher`
- `UserService`
- `openbb_core.app.service.user_service`
- `openbb_seeking_alpha.models.calendar_earnings`
- `openbb_seeking_alpha.models.forward_eps_estimates`
- `openbb_seeking_alpha.models.forward_sales_estimates`
- `pytest`


---

## Performance & Security Notes

No obvious security concerns detected in static analysis.


---

**Generated**: 2025-11-19T02:16:52.950966Z
**Generator**: World's Best Repo Book Generator v1.0

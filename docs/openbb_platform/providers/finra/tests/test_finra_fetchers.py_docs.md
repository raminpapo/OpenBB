# File Documentation: test_finra_fetchers.py

## Metadata
- **Path**: `openbb_platform/providers/finra/tests/test_finra_fetchers.py`
- **Size**: 1,248 bytes
- **Lines**: 43
- **Category**: python
- **Extension**: .py

---

## Original Source

```python
"""Tests for the Finra fetchers."""

import pytest
from openbb_core.app.service.user_service import UserService
from openbb_finra.models.equity_short_interest import FinraShortInterestFetcher
from openbb_finra.models.otc_aggregate import FinraOTCAggregateFetcher

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
def test_finra_otc_aggregate_fetcher(credentials=test_credentials):
    """Test the Finra OTC Aggregate fetcher."""
    params = {"symbol": "AAPL", "tier": "T1", "is_ats": True}

    fetcher = FinraOTCAggregateFetcher()
    result = fetcher.test(params, credentials)
    assert result is None


@pytest.mark.freeze_time("2021-10-21")
@pytest.mark.record_http
def test_finra_short_interest_fetcher(credentials=test_credentials):
    """Test the Finra Short Interest fetcher."""
    params = {"symbol": "AAPL"}

    fetcher = FinraShortInterestFetcher()
    result = fetcher.test(params, credentials)
    assert result is None

```



---

## High-Level Overview

This is a **python** file named `test_finra_fetchers.py`.

**Python Module**

- **Functions** (3): vcr_config, test_finra_otc_aggregate_fetcher, test_finra_short_interest_fetcher
- **Import Statements**: 1


---

## Detailed Analysis

### Python Code Structure


#### Functions

- **`vcr_config()`**
- **`test_finra_otc_aggregate_fetcher(credentials=test_credentials)`**
- **`test_finra_short_interest_fetcher(credentials=test_credentials)`**

#### Decorators Used

pytest


---

## Related Files

The following files may be related based on imports and references:

**Imported Modules**:
- `FinraOTCAggregateFetcher`
- `FinraShortInterestFetcher`
- `UserService`
- `openbb_core.app.service.user_service`
- `openbb_finra.models.equity_short_interest`
- `openbb_finra.models.otc_aggregate`
- `pytest`


---

## Performance & Security Notes

No obvious security concerns detected in static analysis.


---

**Generated**: 2025-11-19T02:16:49.794666Z
**Generator**: World's Best Repo Book Generator v1.0

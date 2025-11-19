# File Documentation: test_ecb_fetchers.py

## Metadata
- **Path**: `openbb_platform/providers/ecb/tests/test_ecb_fetchers.py`
- **Size**: 1,588 bytes
- **Lines**: 55
- **Category**: python
- **Extension**: .py

---

## Original Source

```python
"""Test ECB Fetchers."""

import datetime

import pytest
from openbb_core.app.service.user_service import UserService
from openbb_ecb.models.balance_of_payments import ECBBalanceOfPaymentsFetcher
from openbb_ecb.models.currency_reference_rates import ECBCurrencyReferenceRatesFetcher
from openbb_ecb.models.yield_curve import ECBYieldCurveFetcher

test_credentials = UserService().default_user_settings.credentials.model_dump(
    mode="json"
)


@pytest.fixture(scope="module")
def vcr_config():
    """VCR config."""
    return {
        "filter_headers": [("User-Agent", None)],
        "filter_query_parameters": [
            ("token", "MOCK_TOKEN"),
        ],
    }


@pytest.mark.record_http
def test_ecb_currency_reference_rates_fetcher(credentials=test_credentials):
    """Test ECB Currency Reference Rates Fecher."""
    params = {}

    fetcher = ECBCurrencyReferenceRatesFetcher()
    result = fetcher.test(params, credentials)
    assert result is None


@pytest.mark.record_http
def test_ecb_balance_of_payments_fetcher(credentials=test_credentials):
    """Test ECB Balance Of Payments Fetcher."""
    params = {"date": datetime.date(2023, 1, 1)}

    fetcher = ECBBalanceOfPaymentsFetcher()
    result = fetcher.test(params, credentials)
    assert result is None


@pytest.mark.record_http
def test_ecb_yield_curve_fetcher(credentials=test_credentials):
    """Test ECBYieldCurveFetcher."""
    params = {"date": "2004-11-19,2023-11-19", "use_cache": False}

    fetcher = ECBYieldCurveFetcher()
    result = fetcher.test(params, credentials)
    assert result is None

```



---

## High-Level Overview

This is a **python** file named `test_ecb_fetchers.py`.

**Python Module**

- **Functions** (4): vcr_config, test_ecb_currency_reference_rates_fetcher, test_ecb_balance_of_payments_fetcher, test_ecb_yield_curve_fetcher
- **Import Statements**: 1


---

## Detailed Analysis

### Python Code Structure


#### Functions

- **`vcr_config()`**
- **`test_ecb_currency_reference_rates_fetcher(credentials=test_credentials)`**
- **`test_ecb_balance_of_payments_fetcher(credentials=test_credentials)`**
- **`test_ecb_yield_curve_fetcher(credentials=test_credentials)`**

#### Decorators Used

pytest


---

## Related Files

The following files may be related based on imports and references:

**Imported Modules**:
- `ECBBalanceOfPaymentsFetcher`
- `ECBCurrencyReferenceRatesFetcher`
- `ECBYieldCurveFetcher`
- `UserService`
- `datetime`
- `openbb_core.app.service.user_service`
- `openbb_ecb.models.balance_of_payments`
- `openbb_ecb.models.currency_reference_rates`
- `openbb_ecb.models.yield_curve`
- `pytest`


---

## Performance & Security Notes

No obvious security concerns detected in static analysis.


---

**Generated**: 2025-11-19T02:16:48.804650Z
**Generator**: World's Best Repo Book Generator v1.0

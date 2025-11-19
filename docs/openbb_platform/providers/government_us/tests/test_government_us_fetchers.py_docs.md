# File Documentation: test_government_us_fetchers.py

## Metadata
- **Path**: `openbb_platform/providers/government_us/tests/test_government_us_fetchers.py`
- **Size**: 1,373 bytes
- **Lines**: 51
- **Category**: python
- **Extension**: .py

---

## Original Source

```python
"""Government US Fetchers tests."""

import datetime

import pytest
from openbb_core.app.service.user_service import UserService
from openbb_government_us.models.treasury_auctions import (
    GovernmentUSTreasuryAuctionsFetcher,
)
from openbb_government_us.models.treasury_prices import (
    GovernmentUSTreasuryPricesFetcher,
)

test_credentials = UserService().default_user_settings.credentials.model_dump(
    mode="json"
)


@pytest.fixture(scope="module")
def vcr_config():
    """VCR config."""
    return {
        "filter_headers": [("User-Agent", None)],
        "filter_query_parameters": [
            None,
        ],
    }


@pytest.mark.record_http
def test_government_us_treasury_auctions_fetcher(credentials=test_credentials):
    """Test GovernmentUSTreasuryAuctionsFetcher."""
    params = {
        "start_date": datetime.date(2023, 9, 1),
        "end_date": datetime.date(2023, 11, 16),
    }

    fetcher = GovernmentUSTreasuryAuctionsFetcher()
    result = fetcher.test(params, credentials)
    assert result is None


@pytest.mark.record_http
def test_government_us_treasury_prices_fetcher(credentials=test_credentials):
    """Test GovernmentUSTreasuryAuctionsFetcher."""
    params = {"date": datetime.date(2024, 6, 25)}

    fetcher = GovernmentUSTreasuryPricesFetcher()
    result = fetcher.test(params, credentials)
    assert result is None

```



---

## High-Level Overview

This is a **python** file named `test_government_us_fetchers.py`.

**Python Module**

- **Functions** (3): vcr_config, test_government_us_treasury_auctions_fetcher, test_government_us_treasury_prices_fetcher
- **Import Statements**: 1


---

## Detailed Analysis

### Python Code Structure


#### Functions

- **`vcr_config()`**
- **`test_government_us_treasury_auctions_fetcher(credentials=test_credentials)`**
- **`test_government_us_treasury_prices_fetcher(credentials=test_credentials)`**

#### Decorators Used

pytest


---

## Related Files

The following files may be related based on imports and references:

**Imported Modules**:
- `UserService`
- `datetime`
- `openbb_core.app.service.user_service`
- `openbb_government_us.models.treasury_auctions`
- `openbb_government_us.models.treasury_prices`
- `pytest`


---

## Performance & Security Notes

No obvious security concerns detected in static analysis.


---

**Generated**: 2025-11-19T02:16:51.216768Z
**Generator**: World's Best Repo Book Generator v1.0

# Documentation: openbb_platform/providers/government_us/tests/test_government_us_fetchers.py

## File Metadata
- **Path**: `openbb_platform/providers/government_us/tests/test_government_us_fetchers.py`
- **Size**: 1,373 characters, 51 lines
- **Words**: 94
- **Extension**: .py
- **Classification**: Text file

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

## High-Level Overview

Government US Fetchers tests.

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

## Detailed Structure

### Python File Structure

**Classes** (0):
None

**Functions** (3):
`vcr_config`, `test_government_us_treasury_auctions_fetcher`, `test_government_us_treasury_prices_fetcher`

**Imports** (6):
`datetime`, `pytest`, `openbb_core.app.service.user_service`, `UserService`, `openbb_government_us.models.treasury_auctions`, `openbb_government_us.models.treasury_prices`


## Key Components

No major components extracted.

## Usage & Examples

See source code for usage details.

## Related Files

- `datetime`
- `pytest`
- `openbb_core.app.service.user_service`
- `openbb_government_us.models.treasury_auctions`
- `openbb_government_us.models.treasury_prices`

## Notes
- Generated: 2025-11-18T07:54:39.937141
- Generator: World's Best Repo Book Generator v1.0.0

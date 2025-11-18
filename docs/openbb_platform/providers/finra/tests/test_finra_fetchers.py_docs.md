# Documentation: openbb_platform/providers/finra/tests/test_finra_fetchers.py

## File Metadata
- **Path**: `openbb_platform/providers/finra/tests/test_finra_fetchers.py`
- **Size**: 1,248 characters, 43 lines
- **Words**: 93
- **Extension**: .py
- **Classification**: Text file

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

## High-Level Overview

Tests for the Finra fetchers.

import pytest
from openbb_core.app.service.user_service import UserService
from openbb_finra.models.equity_short_interest import FinraShortInterestFetcher
from openbb_finra.models.otc_aggregate import FinraOTCAggregateFetcher

test_credentials = UserService().default_user_settings.credentials.model_dump(
mode="json"
)


@pytest.fixture(scope="module")
def vcr_config():
VCR configuration.
Test the Finra OTC Aggregate fetcher.
params = {"symbol": "AAPL", "tier": "T1", "is_ats": True}

fetcher = FinraOTCAggregateFetcher()
result = fetcher.test(params, credentials)

## Detailed Structure

### Python File Structure

**Classes** (0):
None

**Functions** (3):
`vcr_config`, `test_finra_otc_aggregate_fetcher`, `test_finra_short_interest_fetcher`

**Imports** (7):
`pytest`, `openbb_core.app.service.user_service`, `UserService`, `openbb_finra.models.equity_short_interest`, `FinraShortInterestFetcher`, `openbb_finra.models.otc_aggregate`, `FinraOTCAggregateFetcher`


## Key Components

No major components extracted.

## Usage & Examples

See source code for usage details.

## Related Files

- `pytest`
- `openbb_core.app.service.user_service`
- `openbb_finra.models.equity_short_interest`
- `openbb_finra.models.otc_aggregate`

## Notes
- Generated: 2025-11-18T07:54:39.153093
- Generator: World's Best Repo Book Generator v1.0.0

# Documentation: openbb_platform/providers/tradingeconomics/tests/test_tradingeconomics_fetchers.py

## File Metadata
- **Path**: `openbb_platform/providers/tradingeconomics/tests/test_tradingeconomics_fetchers.py`
- **Size**: 953 characters, 36 lines
- **Words**: 73
- **Extension**: .py
- **Classification**: Text file

## Original Source

```python
"""Test the Trading Economics fetchers."""

from datetime import date

import pytest
from openbb_core.app.service.user_service import UserService
from openbb_tradingeconomics.models.economic_calendar import TEEconomicCalendarFetcher

test_credentials = UserService().default_user_settings.credentials.model_dump(
    mode="json"
)


@pytest.fixture(scope="module")
def vcr_config():
    """VCR configuration."""
    return {
        "filter_headers": [("User-Agent", None)],
        "filter_query_parameters": [
            ("c", "mock_api_key"),
        ],
    }


@pytest.mark.record_http
def test_tradingeconomics_economic_calendar_fetcher(credentials=test_credentials):
    """Test the Trading Economics economic calendar fetcher."""
    params = {
        "start_date": date(2023, 1, 1),
        "end_date": date(2023, 6, 6),
    }

    fetcher = TEEconomicCalendarFetcher()
    result = fetcher.test(params, credentials)
    assert result is None

```

## High-Level Overview

Test the Trading Economics fetchers.

from datetime import date

import pytest
from openbb_core.app.service.user_service import UserService
from openbb_tradingeconomics.models.economic_calendar import TEEconomicCalendarFetcher

test_credentials = UserService().default_user_settings.credentials.model_dump(
mode="json"
)


@pytest.fixture(scope="module")
def vcr_config():
VCR configuration.
Test the Trading Economics economic calendar fetcher.
params = {
"start_date": date(2023, 1, 1),
"end_date": date(2023, 6, 6),

## Detailed Structure

### Python File Structure

**Classes** (0):
None

**Functions** (2):
`vcr_config`, `test_tradingeconomics_economic_calendar_fetcher`

**Imports** (7):
`datetime`, `date`, `pytest`, `openbb_core.app.service.user_service`, `UserService`, `openbb_tradingeconomics.models.economic_calendar`, `TEEconomicCalendarFetcher`


## Key Components

No major components extracted.

## Usage & Examples

See source code for usage details.

## Related Files

- `datetime`
- `pytest`
- `openbb_core.app.service.user_service`
- `openbb_tradingeconomics.models.economic_calendar`

## Notes
- Generated: 2025-11-18T07:54:43.516341
- Generator: World's Best Repo Book Generator v1.0.0

# Documentation: openbb_platform/providers/cftc/tests/test_cftc_fetchers.py

## File Metadata
- **Path**: `openbb_platform/providers/cftc/tests/test_cftc_fetchers.py`
- **Size**: 1,804 characters, 66 lines
- **Words**: 143
- **Extension**: .py
- **Classification**: Text file

## Original Source

```python
"""CFTC Fetcher Tests."""

from datetime import date

import pytest
from openbb_cftc.models.cot import CftcCotFetcher
from openbb_cftc.models.cot_search import CftcCotSearchFetcher
from openbb_core.app.service.user_service import UserService

test_credentials = UserService().default_user_settings.credentials.model_dump(
    mode="json"
)


def scrub_string(key):
    """Scrub a string from the response."""

    def before_record_response(response):
        response["headers"][key] = response["headers"].update({key: "MOCK_VALUE"})
        return response

    return before_record_response


@pytest.fixture(scope="module")
def vcr_config():
    """VCR configuration."""
    return {
        "filter_headers": [("User-Agent", None)],
        "filter_query_parameters": [
            ("$$app_token", "MOCK_APP_TOKEN"),
            ("$limit", "MOCK_LIMIT"),
            ("$order", "MOCK_ORDER"),
            ("$where", "MOCK_WHERE"),
        ],
        "before_record_response": [
            scrub_string("Etag"),
            scrub_string("X-Socrata-RequestId"),
            scrub_string("X-Socrata-Region"),
        ],
    }


@pytest.mark.record_http
def test_cftc_cot_fetcher(credentials=test_credentials):
    """Test the CFTC COT fetcher."""
    params = {
        "id": "239747",
        "start_date": date(2024, 8, 19),
        "end_date": date(2024, 8, 21),
    }

    fetcher = CftcCotFetcher()
    result = fetcher.test(params, credentials)
    assert result is None


# The data for this request are local files, so we can't record them.
def test_cftc_cot_sarch_fetcher(credentials=test_credentials):
    """Test the CFTC COT Search fetcher."""
    params = {"query": "S&P 500"}

    fetcher = CftcCotSearchFetcher()
    result = fetcher.test(params, credentials)
    assert result is None

```

## High-Level Overview

CFTC Fetcher Tests.

from datetime import date

import pytest
from openbb_cftc.models.cot import CftcCotFetcher
from openbb_cftc.models.cot_search import CftcCotSearchFetcher
from openbb_core.app.service.user_service import UserService

test_credentials = UserService().default_user_settings.credentials.model_dump(
mode="json"
)


def scrub_string(key):
Scrub a string from the response.
VCR configuration.
return {
"filter_headers": [("User-Agent", None)],
"filter_query_parameters": [

## Detailed Structure

### Python File Structure

**Classes** (0):
None

**Functions** (5):
`scrub_string`, `before_record_response`, `vcr_config`, `test_cftc_cot_fetcher`, `test_cftc_cot_sarch_fetcher`

**Imports** (10):
`datetime`, `date`, `pytest`, `openbb_cftc.models.cot`, `CftcCotFetcher`, `openbb_cftc.models.cot_search`, `CftcCotSearchFetcher`, `openbb_core.app.service.user_service`, `UserService`, `the`


## Key Components

No major components extracted.

## Usage & Examples

See source code for usage details.

## Related Files

- `datetime`
- `pytest`
- `openbb_cftc.models.cot`
- `openbb_cftc.models.cot_search`
- `openbb_core.app.service.user_service`

## Notes
- Generated: 2025-11-18T07:54:37.591547
- Generator: World's Best Repo Book Generator v1.0.0

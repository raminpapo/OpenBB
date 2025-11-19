# File Documentation: test_cftc_fetchers.py

## Metadata
- **Path**: `openbb_platform/providers/cftc/tests/test_cftc_fetchers.py`
- **Size**: 1,804 bytes
- **Lines**: 66
- **Category**: python
- **Extension**: .py

---

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



---

## High-Level Overview

This is a **python** file named `test_cftc_fetchers.py`.

**Python Module**

- **Functions** (5): scrub_string, before_record_response, vcr_config, test_cftc_cot_fetcher, test_cftc_cot_sarch_fetcher
- **Import Statements**: 1


---

## Detailed Analysis

### Python Code Structure


#### Functions

- **`scrub_string(key)`**
- **`before_record_response(response)`**
- **`vcr_config()`**
- **`test_cftc_cot_fetcher(credentials=test_credentials)`**
- **`test_cftc_cot_sarch_fetcher(credentials=test_credentials)`**

#### Decorators Used

pytest


---

## Related Files

The following files may be related based on imports and references:

**Imported Modules**:
- `CftcCotFetcher`
- `CftcCotSearchFetcher`
- `UserService`
- `date`
- `datetime`
- `openbb_cftc.models.cot`
- `openbb_cftc.models.cot_search`
- `openbb_core.app.service.user_service`
- `pytest`


---

## Performance & Security Notes

No obvious security concerns detected in static analysis.


---

**Generated**: 2025-11-19T02:16:48.667797Z
**Generator**: World's Best Repo Book Generator v1.0

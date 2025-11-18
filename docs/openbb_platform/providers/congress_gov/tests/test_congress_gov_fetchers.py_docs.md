# Documentation: openbb_platform/providers/congress_gov/tests/test_congress_gov_fetchers.py

## File Metadata
- **Path**: `openbb_platform/providers/congress_gov/tests/test_congress_gov_fetchers.py`
- **Size**: 2,248 characters, 80 lines
- **Words**: 165
- **Extension**: .py
- **Classification**: Text file

## Original Source

```python
"""Congress.gov Fetchers tests."""

from datetime import datetime

import pytest
from openbb_congress_gov.models.bill_info import CongressBillInfoFetcher
from openbb_congress_gov.models.bill_text import CongressBillTextFetcher
from openbb_congress_gov.models.congress_bills import CongressBillsFetcher
from openbb_congress_gov.utils.helpers import year_to_congress
from openbb_core.app.service.user_service import UserService

test_credentials = UserService().default_user_settings.credentials.model_dump(
    mode="json"
)
test_credentials = (
    test_credentials
    if test_credentials and test_credentials.get("congress_gov_api_key")
    else {"congress_gov_api_key": "MOCK_API_KEY"}
)


@pytest.fixture(scope="module")
def vcr_config():
    """VCR configuration."""
    return {
        "filter_headers": [
            ("User-Agent", None),
            ("api_key", "MOCK_API_KEY"),
        ],
        "filter_query_parameters": [
            ("api_key", "MOCK_API_KEY"),
        ],
    }


def test_year_to_congress():
    """Test year to congress conversion."""
    current_year = datetime.now().year
    assert year_to_congress(current_year) >= 119
    assert year_to_congress(2000) == 106
    assert year_to_congress(1993) == 103
    with pytest.raises(ValueError):
        year_to_congress(1930)


@pytest.mark.record_http
def test_congress_bills_fetcher(credentials=test_credentials):
    """Test Congress Bills fetcher."""
    params = {
        "limit": 1,
    }

    fetcher = CongressBillsFetcher()
    result = fetcher.test(params, credentials)
    assert result is None


@pytest.mark.record_http
def test_congress_bill_info_fetcher(credentials=test_credentials):
    """Test Congress Bill Info fetcher."""
    params = {
        "bill_url": "119/s/1947",
    }

    fetcher = CongressBillInfoFetcher()
    result = fetcher.test(params, credentials)
    assert result is None


@pytest.mark.record_http
def test_congress_bill_text_fetcher(credentials=test_credentials):
    """Test Congress Bill Text fetcher."""
    params = {
        "urls": ["https://www.congress.gov/119/bills/s1947/BILLS-119s1947is.pdf"],
    }

    fetcher = CongressBillTextFetcher()
    result = fetcher.test(params, credentials)
    assert result is None

```

## High-Level Overview

Congress.gov Fetchers tests.

from datetime import datetime

import pytest
from openbb_congress_gov.models.bill_info import CongressBillInfoFetcher
from openbb_congress_gov.models.bill_text import CongressBillTextFetcher
from openbb_congress_gov.models.congress_bills import CongressBillsFetcher
from openbb_congress_gov.utils.helpers import year_to_congress
from openbb_core.app.service.user_service import UserService

test_credentials = UserService().default_user_settings.credentials.model_dump(
mode="json"
)
test_credentials = (
test_credentials
if test_credentials and test_credentials.get("congress_gov_api_key")
else {"congress_gov_api_key": "MOCK_API_KEY"}
)


## Detailed Structure

### Python File Structure

**Classes** (0):
None

**Functions** (5):
`vcr_config`, `test_year_to_congress`, `test_congress_bills_fetcher`, `test_congress_bill_info_fetcher`, `test_congress_bill_text_fetcher`

**Imports** (13):
`datetime`, `datetime`, `pytest`, `openbb_congress_gov.models.bill_info`, `CongressBillInfoFetcher`, `openbb_congress_gov.models.bill_text`, `CongressBillTextFetcher`, `openbb_congress_gov.models.congress_bills`, `CongressBillsFetcher`, `openbb_congress_gov.utils.helpers`, `year_to_congress`, `openbb_core.app.service.user_service`, `UserService`


## Key Components

No major components extracted.

## Usage & Examples

See source code for usage details.

## Related Files

- `datetime`
- `pytest`
- `openbb_congress_gov.models.bill_info`
- `openbb_congress_gov.models.bill_text`
- `openbb_congress_gov.models.congress_bills`
- `openbb_congress_gov.utils.helpers`
- `openbb_core.app.service.user_service`

## Notes
- Generated: 2025-11-18T07:54:37.638326
- Generator: World's Best Repo Book Generator v1.0.0

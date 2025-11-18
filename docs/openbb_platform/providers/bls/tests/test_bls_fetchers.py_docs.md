# Documentation: openbb_platform/providers/bls/tests/test_bls_fetchers.py

## File Metadata
- **Path**: `openbb_platform/providers/bls/tests/test_bls_fetchers.py`
- **Size**: 1,372 characters, 49 lines
- **Words**: 118
- **Extension**: .py
- **Classification**: Text file

## Original Source

```python
"""Test the BLS fetchers."""

from datetime import date

import pytest
from openbb_bls.models.search import BlsSearchFetcher
from openbb_bls.models.series import BlsSeriesFetcher
from openbb_core.app.service.user_service import UserService

test_credentials = UserService().default_user_settings.credentials.model_dump(
    mode="json"
)


@pytest.fixture(scope="module")
def vcr_config():
    """VCR configuration."""
    return {
        "filter_headers": [("User-Agent", None)],
        "filter_post_data_parameters": [("registrationkey", "MOCK_API_KEY")],
        "filter_query_parameters": [
            ("registrationkey", "MOCK_API_KEY"),
        ],
    }


@pytest.mark.record_http
def test_bls_series_fetcher(credentials=test_credentials):
    """Test the BLS Series fetcher."""
    params = {
        "symbol": "APU0000701111",
        "start_date": date(2022, 1, 1),
        "end_date": date(2022, 12, 1),
    }

    fetcher = BlsSeriesFetcher()
    result = fetcher.test(params, credentials)
    assert result is None


# The data for this request are local files, so we can't record them.
def test_bls_search_fetcher(credentials=test_credentials):
    """Test the BLS Search fetcher."""
    params = {"category": "cpi", "query": "average price;flour"}

    fetcher = BlsSearchFetcher()
    result = fetcher.test(params, credentials)
    assert result is None

```

## High-Level Overview

Test the BLS fetchers.

from datetime import date

import pytest
from openbb_bls.models.search import BlsSearchFetcher
from openbb_bls.models.series import BlsSeriesFetcher
from openbb_core.app.service.user_service import UserService

test_credentials = UserService().default_user_settings.credentials.model_dump(
mode="json"
)


@pytest.fixture(scope="module")
def vcr_config():
VCR configuration.
Test the BLS Series fetcher.
params = {
"symbol": "APU0000701111",

## Detailed Structure

### Python File Structure

**Classes** (0):
None

**Functions** (3):
`vcr_config`, `test_bls_series_fetcher`, `test_bls_search_fetcher`

**Imports** (9):
`datetime`, `date`, `pytest`, `openbb_bls.models.search`, `BlsSearchFetcher`, `openbb_bls.models.series`, `BlsSeriesFetcher`, `openbb_core.app.service.user_service`, `UserService`


## Key Components

No major components extracted.

## Usage & Examples

See source code for usage details.

## Related Files

- `datetime`
- `pytest`
- `openbb_bls.models.search`
- `openbb_bls.models.series`
- `openbb_core.app.service.user_service`

## Notes
- Generated: 2025-11-18T07:54:37.448349
- Generator: World's Best Repo Book Generator v1.0.0

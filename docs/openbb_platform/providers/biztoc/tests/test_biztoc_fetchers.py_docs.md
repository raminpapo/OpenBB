# Documentation: openbb_platform/providers/biztoc/tests/test_biztoc_fetchers.py

## File Metadata
- **Path**: `openbb_platform/providers/biztoc/tests/test_biztoc_fetchers.py`
- **Size**: 876 characters, 34 lines
- **Words**: 64
- **Extension**: .py
- **Classification**: Text file

## Original Source

```python
"""Tests for the Biztoc fetchers."""

import pytest
from openbb_biztoc.models.world_news import BiztocWorldNewsFetcher
from openbb_core.app.service.user_service import UserService

test_credentials = UserService().default_user_settings.credentials.model_dump(
    mode="json"
)


@pytest.fixture(scope="module")
def vcr_config():
    """VCR configuration."""
    return {
        "filter_headers": [
            ("X-RapidAPI-Key", "MOCK_API_KEY"),
            ("User-Agent", None),
        ],
        "filter_query_parameters": [
            ("apikey", "MOCK_API_KEY"),
        ],
    }


@pytest.mark.record_http
def test_biztoc_world_news_fetcher(credentials=test_credentials):
    """Test the Biztoc World News fetcher."""
    params = {"source": "bloomberg"}

    fetcher = BiztocWorldNewsFetcher()
    result = fetcher.test(params, credentials)
    assert result is None

```

## High-Level Overview

Tests for the Biztoc fetchers.

import pytest
from openbb_biztoc.models.world_news import BiztocWorldNewsFetcher
from openbb_core.app.service.user_service import UserService

test_credentials = UserService().default_user_settings.credentials.model_dump(
mode="json"
)


@pytest.fixture(scope="module")
def vcr_config():
VCR configuration.
Test the Biztoc World News fetcher.
params = {"source": "bloomberg"}

fetcher = BiztocWorldNewsFetcher()
result = fetcher.test(params, credentials)
assert result is None

## Detailed Structure

### Python File Structure

**Classes** (0):
None

**Functions** (2):
`vcr_config`, `test_biztoc_world_news_fetcher`

**Imports** (5):
`pytest`, `openbb_biztoc.models.world_news`, `BiztocWorldNewsFetcher`, `openbb_core.app.service.user_service`, `UserService`


## Key Components

No major components extracted.

## Usage & Examples

See source code for usage details.

## Related Files

- `pytest`
- `openbb_biztoc.models.world_news`
- `openbb_core.app.service.user_service`

## Notes
- Generated: 2025-11-18T07:54:37.334185
- Generator: World's Best Repo Book Generator v1.0.0

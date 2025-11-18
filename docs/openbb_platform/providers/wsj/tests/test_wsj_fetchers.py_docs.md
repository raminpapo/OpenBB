# Documentation: openbb_platform/providers/wsj/tests/test_wsj_fetchers.py

## File Metadata
- **Path**: `openbb_platform/providers/wsj/tests/test_wsj_fetchers.py`
- **Size**: 1,354 characters, 53 lines
- **Words**: 110
- **Extension**: .py
- **Classification**: Text file

## Original Source

```python
"""Tests for the WSJ fetchers."""

import pytest
from openbb_core.app.service.user_service import UserService
from openbb_wsj.models.active import WSJActiveFetcher
from openbb_wsj.models.gainers import WSJGainersFetcher
from openbb_wsj.models.losers import WSJLosersFetcher

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
def test_wsj_gainers_fetcher(credentials=test_credentials):
    """Test the WSJ Gainers fetcher."""
    params = {}

    fetcher = WSJGainersFetcher()
    result = fetcher.test(params, credentials)
    assert result is None


@pytest.mark.record_http
def test_wsj_losers_fetcher(credentials=test_credentials):
    """Test the WSJ Losers fetcher."""
    params = {}

    fetcher = WSJLosersFetcher()
    result = fetcher.test(params, credentials)
    assert result is None


@pytest.mark.record_http
def test_wsj_active_fetcher(credentials=test_credentials):
    """Test the WSJ Active fetcher."""
    params = {}

    fetcher = WSJActiveFetcher()
    result = fetcher.test(params, credentials)
    assert result is None

```

## High-Level Overview

Tests for the WSJ fetchers.

import pytest
from openbb_core.app.service.user_service import UserService
from openbb_wsj.models.active import WSJActiveFetcher
from openbb_wsj.models.gainers import WSJGainersFetcher
from openbb_wsj.models.losers import WSJLosersFetcher

test_credentials = UserService().default_user_settings.credentials.model_dump(
mode="json"
)


@pytest.fixture(scope="module")
def vcr_config():
VCR configuration.
Test the WSJ Gainers fetcher.
params = {}

fetcher = WSJGainersFetcher()

## Detailed Structure

### Python File Structure

**Classes** (0):
None

**Functions** (4):
`vcr_config`, `test_wsj_gainers_fetcher`, `test_wsj_losers_fetcher`, `test_wsj_active_fetcher`

**Imports** (9):
`pytest`, `openbb_core.app.service.user_service`, `UserService`, `openbb_wsj.models.active`, `WSJActiveFetcher`, `openbb_wsj.models.gainers`, `WSJGainersFetcher`, `openbb_wsj.models.losers`, `WSJLosersFetcher`


## Key Components

No major components extracted.

## Usage & Examples

See source code for usage details.

## Related Files

- `pytest`
- `openbb_core.app.service.user_service`
- `openbb_wsj.models.active`
- `openbb_wsj.models.gainers`
- `openbb_wsj.models.losers`

## Notes
- Generated: 2025-11-18T07:54:43.545716
- Generator: World's Best Repo Book Generator v1.0.0

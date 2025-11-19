# File Documentation: test_wsj_fetchers.py

## Metadata
- **Path**: `openbb_platform/providers/wsj/tests/test_wsj_fetchers.py`
- **Size**: 1,354 bytes
- **Lines**: 53
- **Category**: python
- **Extension**: .py

---

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



---

## High-Level Overview

This is a **python** file named `test_wsj_fetchers.py`.

**Python Module**

- **Functions** (4): vcr_config, test_wsj_gainers_fetcher, test_wsj_losers_fetcher, test_wsj_active_fetcher
- **Import Statements**: 1


---

## Detailed Analysis

### Python Code Structure


#### Functions

- **`vcr_config()`**
- **`test_wsj_gainers_fetcher(credentials=test_credentials)`**
- **`test_wsj_losers_fetcher(credentials=test_credentials)`**
- **`test_wsj_active_fetcher(credentials=test_credentials)`**

#### Decorators Used

pytest


---

## Related Files

The following files may be related based on imports and references:

**Imported Modules**:
- `UserService`
- `WSJActiveFetcher`
- `WSJGainersFetcher`
- `WSJLosersFetcher`
- `openbb_core.app.service.user_service`
- `openbb_wsj.models.active`
- `openbb_wsj.models.gainers`
- `openbb_wsj.models.losers`
- `pytest`


---

## Performance & Security Notes

No obvious security concerns detected in static analysis.


---

**Generated**: 2025-11-19T02:16:55.117757Z
**Generator**: World's Best Repo Book Generator v1.0

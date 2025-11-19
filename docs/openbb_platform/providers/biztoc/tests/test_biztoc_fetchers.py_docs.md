# File Documentation: test_biztoc_fetchers.py

## Metadata
- **Path**: `openbb_platform/providers/biztoc/tests/test_biztoc_fetchers.py`
- **Size**: 876 bytes
- **Lines**: 34
- **Category**: python
- **Extension**: .py

---

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



---

## High-Level Overview

This is a **python** file named `test_biztoc_fetchers.py`.

**Python Module**

- **Functions** (2): vcr_config, test_biztoc_world_news_fetcher
- **Import Statements**: 1


---

## Detailed Analysis

### Python Code Structure


#### Functions

- **`vcr_config()`**
- **`test_biztoc_world_news_fetcher(credentials=test_credentials)`**

#### Decorators Used

pytest


---

## Related Files

The following files may be related based on imports and references:

**Imported Modules**:
- `BiztocWorldNewsFetcher`
- `UserService`
- `openbb_biztoc.models.world_news`
- `openbb_core.app.service.user_service`
- `pytest`


---

## Performance & Security Notes

No obvious security concerns detected in static analysis.


---

**Generated**: 2025-11-19T02:16:48.333857Z
**Generator**: World's Best Repo Book Generator v1.0

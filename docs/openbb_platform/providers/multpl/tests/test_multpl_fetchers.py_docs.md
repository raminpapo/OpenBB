# File Documentation: test_multpl_fetchers.py

## Metadata
- **Path**: `openbb_platform/providers/multpl/tests/test_multpl_fetchers.py`
- **Size**: 696 bytes
- **Lines**: 28
- **Category**: python
- **Extension**: .py

---

## Original Source

```python
"""Multpl Fetcher Tests."""

import pytest
from openbb_core.app.service.user_service import UserService
from openbb_multpl.models.sp500_multiples import MultplSP500MultiplesFetcher

test_credentials = UserService().default_user_settings.credentials.model_dump(
    mode="json"
)


@pytest.fixture(scope="module")
def vcr_config():
    """VCR configuration."""
    return {
        "filter_headers": [("User-Agent", None)],
    }


@pytest.mark.record_http
def test_multpl_sp500_multiples_fetcher(credentials=None):
    """Test multpl sp500 multiples fetcher."""
    params = {}

    fetcher = MultplSP500MultiplesFetcher()
    result = fetcher.test(params, credentials)
    assert result is None

```



---

## High-Level Overview

This is a **python** file named `test_multpl_fetchers.py`.

**Python Module**

- **Functions** (2): vcr_config, test_multpl_sp500_multiples_fetcher
- **Import Statements**: 1


---

## Detailed Analysis

### Python Code Structure


#### Functions

- **`vcr_config()`**
- **`test_multpl_sp500_multiples_fetcher(credentials=None)`**

#### Decorators Used

pytest


---

## Related Files

The following files may be related based on imports and references:

**Imported Modules**:
- `MultplSP500MultiplesFetcher`
- `UserService`
- `openbb_core.app.service.user_service`
- `openbb_multpl.models.sp500_multiples`
- `pytest`


---

## Performance & Security Notes

No obvious security concerns detected in static analysis.


---

**Generated**: 2025-11-19T02:16:51.610466Z
**Generator**: World's Best Repo Book Generator v1.0

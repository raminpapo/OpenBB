# Documentation: openbb_platform/providers/multpl/tests/test_multpl_fetchers.py

## File Metadata
- **Path**: `openbb_platform/providers/multpl/tests/test_multpl_fetchers.py`
- **Size**: 696 characters, 28 lines
- **Words**: 51
- **Extension**: .py
- **Classification**: Text file

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

## High-Level Overview

Multpl Fetcher Tests.

import pytest
from openbb_core.app.service.user_service import UserService
from openbb_multpl.models.sp500_multiples import MultplSP500MultiplesFetcher

test_credentials = UserService().default_user_settings.credentials.model_dump(
mode="json"
)


@pytest.fixture(scope="module")
def vcr_config():
VCR configuration.
Test multpl sp500 multiples fetcher.
params = {}

fetcher = MultplSP500MultiplesFetcher()
result = fetcher.test(params, credentials)
assert result is None

## Detailed Structure

### Python File Structure

**Classes** (0):
None

**Functions** (2):
`vcr_config`, `test_multpl_sp500_multiples_fetcher`

**Imports** (5):
`pytest`, `openbb_core.app.service.user_service`, `UserService`, `openbb_multpl.models.sp500_multiples`, `MultplSP500MultiplesFetcher`


## Key Components

No major components extracted.

## Usage & Examples

See source code for usage details.

## Related Files

- `pytest`
- `openbb_core.app.service.user_service`
- `openbb_multpl.models.sp500_multiples`

## Notes
- Generated: 2025-11-18T07:54:40.305460
- Generator: World's Best Repo Book Generator v1.0.0

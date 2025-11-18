# Documentation: openbb_platform/providers/stockgrid/tests/test_stockgrid_fetchers.py

## File Metadata
- **Path**: `openbb_platform/providers/stockgrid/tests/test_stockgrid_fetchers.py`
- **Size**: 802 characters, 31 lines
- **Words**: 56
- **Extension**: .py
- **Classification**: Text file

## Original Source

```python
"""Test stockgrid fetchers."""

import pytest
from openbb_core.app.service.user_service import UserService
from openbb_stockgrid.models.short_volume import StockgridShortVolumeFetcher

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
def test_stockgrid_short_volume_fetcher(credentials=test_credentials):
    """Test short volume fetcher."""
    params = {"symbol": "AAPL"}

    fetcher = StockgridShortVolumeFetcher()
    result = fetcher.test(params, credentials)
    assert result is None

```

## High-Level Overview

Test stockgrid fetchers.

import pytest
from openbb_core.app.service.user_service import UserService
from openbb_stockgrid.models.short_volume import StockgridShortVolumeFetcher

test_credentials = UserService().default_user_settings.credentials.model_dump(
mode="json"
)


@pytest.fixture(scope="module")
def vcr_config():
VCR configuration.
Test short volume fetcher.
params = {"symbol": "AAPL"}

fetcher = StockgridShortVolumeFetcher()
result = fetcher.test(params, credentials)
assert result is None

## Detailed Structure

### Python File Structure

**Classes** (0):
None

**Functions** (2):
`vcr_config`, `test_stockgrid_short_volume_fetcher`

**Imports** (5):
`pytest`, `openbb_core.app.service.user_service`, `UserService`, `openbb_stockgrid.models.short_volume`, `StockgridShortVolumeFetcher`


## Key Components

No major components extracted.

## Usage & Examples

See source code for usage details.

## Related Files

- `pytest`
- `openbb_core.app.service.user_service`
- `openbb_stockgrid.models.short_volume`

## Notes
- Generated: 2025-11-18T07:54:41.697035
- Generator: World's Best Repo Book Generator v1.0.0

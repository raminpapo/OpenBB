# File Documentation: test_stockgrid_fetchers.py

## Metadata
- **Path**: `openbb_platform/providers/stockgrid/tests/test_stockgrid_fetchers.py`
- **Size**: 802 bytes
- **Lines**: 31
- **Category**: python
- **Extension**: .py

---

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



---

## High-Level Overview

This is a **python** file named `test_stockgrid_fetchers.py`.

**Python Module**

- **Functions** (2): vcr_config, test_stockgrid_short_volume_fetcher
- **Import Statements**: 1


---

## Detailed Analysis

### Python Code Structure


#### Functions

- **`vcr_config()`**
- **`test_stockgrid_short_volume_fetcher(credentials=test_credentials)`**

#### Decorators Used

pytest


---

## Related Files

The following files may be related based on imports and references:

**Imported Modules**:
- `StockgridShortVolumeFetcher`
- `UserService`
- `openbb_core.app.service.user_service`
- `openbb_stockgrid.models.short_volume`
- `pytest`


---

## Performance & Security Notes

No obvious security concerns detected in static analysis.


---

**Generated**: 2025-11-19T02:16:52.974145Z
**Generator**: World's Best Repo Book Generator v1.0

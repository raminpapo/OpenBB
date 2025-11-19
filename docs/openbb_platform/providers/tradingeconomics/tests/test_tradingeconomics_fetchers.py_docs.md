# File Documentation: test_tradingeconomics_fetchers.py

## Metadata
- **Path**: `openbb_platform/providers/tradingeconomics/tests/test_tradingeconomics_fetchers.py`
- **Size**: 953 bytes
- **Lines**: 36
- **Category**: python
- **Extension**: .py

---

## Original Source

```python
"""Test the Trading Economics fetchers."""

from datetime import date

import pytest
from openbb_core.app.service.user_service import UserService
from openbb_tradingeconomics.models.economic_calendar import TEEconomicCalendarFetcher

test_credentials = UserService().default_user_settings.credentials.model_dump(
    mode="json"
)


@pytest.fixture(scope="module")
def vcr_config():
    """VCR configuration."""
    return {
        "filter_headers": [("User-Agent", None)],
        "filter_query_parameters": [
            ("c", "mock_api_key"),
        ],
    }


@pytest.mark.record_http
def test_tradingeconomics_economic_calendar_fetcher(credentials=test_credentials):
    """Test the Trading Economics economic calendar fetcher."""
    params = {
        "start_date": date(2023, 1, 1),
        "end_date": date(2023, 6, 6),
    }

    fetcher = TEEconomicCalendarFetcher()
    result = fetcher.test(params, credentials)
    assert result is None

```



---

## High-Level Overview

This is a **python** file named `test_tradingeconomics_fetchers.py`.

**Python Module**

- **Functions** (2): vcr_config, test_tradingeconomics_economic_calendar_fetcher
- **Import Statements**: 1


---

## Detailed Analysis

### Python Code Structure


#### Functions

- **`vcr_config()`**
- **`test_tradingeconomics_economic_calendar_fetcher(credentials=test_credentials)`**

#### Decorators Used

pytest


---

## Related Files

The following files may be related based on imports and references:

**Imported Modules**:
- `TEEconomicCalendarFetcher`
- `UserService`
- `date`
- `datetime`
- `openbb_core.app.service.user_service`
- `openbb_tradingeconomics.models.economic_calendar`
- `pytest`


---

## Performance & Security Notes

No obvious security concerns detected in static analysis.


---

**Generated**: 2025-11-19T02:16:55.070305Z
**Generator**: World's Best Repo Book Generator v1.0

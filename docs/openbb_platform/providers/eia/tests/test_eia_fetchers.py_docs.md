# File Documentation: test_eia_fetchers.py

## Metadata
- **Path**: `openbb_platform/providers/eia/tests/test_eia_fetchers.py`
- **Size**: 2,023 bytes
- **Lines**: 70
- **Category**: python
- **Extension**: .py

---

## Original Source

```python
"""EIA Fetcher Tests."""

import datetime

import pytest
from openbb_core.app.service.user_service import UserService
from openbb_us_eia.models.petroleum_status_report import EiaPetroleumStatusReportFetcher
from openbb_us_eia.models.short_term_energy_outlook import (
    EiaShortTermEnergyOutlookFetcher,
)

test_credentials = UserService().default_user_settings.credentials.model_dump(
    mode="json"
)


def scrub_string(key):
    """Scrub a string from the response."""

    def before_record_response(response):
        response["headers"][key] = response["headers"].update({key: "MOCK_VALUE"})
        return response

    return before_record_response


@pytest.fixture(scope="module")
def vcr_config():
    """VCR configuration."""
    return {
        "filter_headers": [("User-Agent", None)],
        "filter_query_parameters": [
            ("api_key", "MOCK_API_KEY"),
        ],
        "before_record_response": [
            scrub_string("X-Amz-Cf-Id"),
            scrub_string("Etag"),
            scrub_string("Via"),
            scrub_string("X-Amz-Cf-Pop"),
            scrub_string("X-Cache"),
            scrub_string("X-Api-Umbrella-Request-Id"),
            scrub_string("X-Vcap-Request-Id"),
        ],
    }


@pytest.mark.record_http
def test_eia_petroleum_status_report_fetcher(credentials=None):
    """Test EIA petroleum status report fetcher."""
    params = {"category": "crude_petroleum_stocks", "table": "all"}

    fetcher = EiaPetroleumStatusReportFetcher()
    result = fetcher.test(params, credentials)
    assert result is None


@pytest.mark.record_http
def test_eia_short_term_energy_outlook_fetcher(credentials=test_credentials):
    """Test EIA short term energy outlook fetcher."""
    params = {
        "table": "10b",
        "start_date": datetime.date(2024, 1, 1),
        "end_date": datetime.date(2024, 4, 1),
        "frequency": "quarter",
    }

    fetcher = EiaShortTermEnergyOutlookFetcher()
    result = fetcher.test(params, credentials)
    assert result is None

```



---

## High-Level Overview

This is a **python** file named `test_eia_fetchers.py`.

**Python Module**

- **Functions** (5): scrub_string, before_record_response, vcr_config, test_eia_petroleum_status_report_fetcher, test_eia_short_term_energy_outlook_fetcher
- **Import Statements**: 1


---

## Detailed Analysis

### Python Code Structure


#### Functions

- **`scrub_string(key)`**
- **`before_record_response(response)`**
- **`vcr_config()`**
- **`test_eia_petroleum_status_report_fetcher(credentials=None)`**
- **`test_eia_short_term_energy_outlook_fetcher(credentials=test_credentials)`**

#### Decorators Used

pytest


---

## Related Files

The following files may be related based on imports and references:

**Imported Modules**:
- `EiaPetroleumStatusReportFetcher`
- `UserService`
- `datetime`
- `openbb_core.app.service.user_service`
- `openbb_us_eia.models.petroleum_status_report`
- `openbb_us_eia.models.short_term_energy_outlook`
- `pytest`


---

## Performance & Security Notes

No obvious security concerns detected in static analysis.


---

**Generated**: 2025-11-19T02:16:49.401543Z
**Generator**: World's Best Repo Book Generator v1.0

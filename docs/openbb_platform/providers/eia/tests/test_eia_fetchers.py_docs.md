# Documentation: openbb_platform/providers/eia/tests/test_eia_fetchers.py

## File Metadata
- **Path**: `openbb_platform/providers/eia/tests/test_eia_fetchers.py`
- **Size**: 2,023 characters, 70 lines
- **Words**: 133
- **Extension**: .py
- **Classification**: Text file

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

## High-Level Overview

EIA Fetcher Tests.

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
Scrub a string from the response.
VCR configuration.
return {

## Detailed Structure

### Python File Structure

**Classes** (0):
None

**Functions** (5):
`scrub_string`, `before_record_response`, `vcr_config`, `test_eia_petroleum_status_report_fetcher`, `test_eia_short_term_energy_outlook_fetcher`

**Imports** (8):
`datetime`, `pytest`, `openbb_core.app.service.user_service`, `UserService`, `openbb_us_eia.models.petroleum_status_report`, `EiaPetroleumStatusReportFetcher`, `openbb_us_eia.models.short_term_energy_outlook`, `the`


## Key Components

No major components extracted.

## Usage & Examples

See source code for usage details.

## Related Files

- `datetime`
- `pytest`
- `openbb_core.app.service.user_service`
- `openbb_us_eia.models.petroleum_status_report`
- `openbb_us_eia.models.short_term_energy_outlook`

## Notes
- Generated: 2025-11-18T07:54:38.310572
- Generator: World's Best Repo Book Generator v1.0.0

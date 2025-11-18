# Documentation: openbb_platform/providers/imf/tests/test_imf_fetchers.py

## File Metadata
- **Path**: `openbb_platform/providers/imf/tests/test_imf_fetchers.py`
- **Size**: 3,986 characters, 132 lines
- **Words**: 301
- **Extension**: .py
- **Classification**: Text file

## Original Source

```python
"""IMF Fetcher Tests."""

from datetime import date

import pytest
from openbb_core.app.service.user_service import UserService
from openbb_imf.models.available_indicators import ImfAvailableIndicatorsFetcher
from openbb_imf.models.direction_of_trade import ImfDirectionOfTradeFetcher
from openbb_imf.models.economic_indicators import ImfEconomicIndicatorsFetcher
from openbb_imf.models.maritime_chokepoint_info import ImfMaritimeChokePointInfoFetcher
from openbb_imf.models.maritime_chokepoint_volume import (
    ImfMaritimeChokePointVolumeFetcher,
)
from openbb_imf.models.port_info import ImfPortInfoFetcher
from openbb_imf.models.port_volume import ImfPortVolumeFetcher

test_credentials = UserService().default_user_settings.credentials.model_dump(
    mode="json"
)


def scrub_string(key):
    """Scrub a string from the response."""

    def before_record_response(response):
        response["headers"][key] = response["headers"].update({key: None})
        return response

    return before_record_response


@pytest.fixture(scope="module")
def vcr_config():
    """VCR configuration."""
    return {
        "filter_headers": [("User-Agent", None)],
        "before_record_response": [
            scrub_string("Set-Cookie"),
        ],
    }


@pytest.mark.record_http
def test_imf_economic_indicators_fetcher(credentials=test_credentials):
    """Test the IMF EconomicIndicators fetcher."""
    params = {
        "country": "JP",
        "frequency": "month",
        "symbol": "RAMFDA_USD",
        "start_date": date(2023, 1, 1),
        "end_date": date(2023, 12, 31),
    }

    fetcher = ImfEconomicIndicatorsFetcher()
    result = fetcher.test(params, credentials)
    assert result is None


# The data for this request are local files, so we can't record them.
def test_imf_available_indicators_fetcher(credentials=test_credentials):
    """Test the IMF Available Indicators fetcher."""
    params = {}

    fetcher = ImfAvailableIndicatorsFetcher()
    result = fetcher.test(params, credentials)
    assert result is None


@pytest.mark.record_http
def test_imf_direction_of_trade_fetcher(credentials=test_credentials):
    """Test the ImfDirectionOfTrade fetcher."""
    params = {
        "country": "us",
        "counterpart": "world,eu",
        "frequency": "annual",
        "direction": "exports",
        "start_date": date(2020, 1, 1),
        "end_date": date(2023, 1, 1),
    }

    fetcher = ImfDirectionOfTradeFetcher()
    result = fetcher.test(params, credentials)
    assert result is None


@pytest.mark.record_http
def test_imf_port_info_fetcher(credentials=test_credentials):
    """Test the ImfPortInfo fetcher."""
    params = {"continent": "asia_pacific", "limit": 10}

    fetcher = ImfPortInfoFetcher()
    result = fetcher.test(params, credentials)
    assert result is None


@pytest.mark.record_http
def test_imf_port_volume_fetcher(credentials=test_credentials):
    """Test the ImfPortVolume fetcher."""
    params = {
        "port_code": "port1201",
        "start_date": date(year=2023, month=1, day=1),
        "end_date": date(year=2023, month=1, day=31),
    }

    fetcher = ImfPortVolumeFetcher()
    result = fetcher.test(params, credentials)
    assert result is None


@pytest.mark.record_http
def test_imf_maritime_chokepoint_info_fetcher(credentials=test_credentials):
    """Test the ImfMaritimeChokePointInfo fetcher."""
    params = {}

    fetcher = ImfMaritimeChokePointInfoFetcher()
    result = fetcher.test(params, credentials)
    assert result is None


@pytest.mark.record_http
def test_imf_maritime_chokepoint_volume_fetcher(credentials=test_credentials):
    """Test the ImfMaritimeChokePointVolume fetcher."""
    params = {
        "chokepoint": "taiwan_strait",
        "start_date": date(year=2023, month=1, day=1),
        "end_date": date(year=2023, month=1, day=31),
    }

    fetcher = ImfMaritimeChokePointVolumeFetcher()
    result = fetcher.test(params, credentials)
    assert result is None

```

## High-Level Overview

IMF Fetcher Tests.

from datetime import date

import pytest
from openbb_core.app.service.user_service import UserService
from openbb_imf.models.available_indicators import ImfAvailableIndicatorsFetcher
from openbb_imf.models.direction_of_trade import ImfDirectionOfTradeFetcher
from openbb_imf.models.economic_indicators import ImfEconomicIndicatorsFetcher
from openbb_imf.models.maritime_chokepoint_info import ImfMaritimeChokePointInfoFetcher
from openbb_imf.models.maritime_chokepoint_volume import (
ImfMaritimeChokePointVolumeFetcher,
)
from openbb_imf.models.port_info import ImfPortInfoFetcher
from openbb_imf.models.port_volume import ImfPortVolumeFetcher

test_credentials = UserService().default_user_settings.credentials.model_dump(
mode="json"
)


## Detailed Structure

### Python File Structure

**Classes** (0):
None

**Functions** (10):
`scrub_string`, `before_record_response`, `vcr_config`, `test_imf_economic_indicators_fetcher`, `test_imf_available_indicators_fetcher`, `test_imf_direction_of_trade_fetcher`, `test_imf_port_info_fetcher`, `test_imf_port_volume_fetcher`, `test_imf_maritime_chokepoint_info_fetcher`, `test_imf_maritime_chokepoint_volume_fetcher`

**Imports** (19):
`datetime`, `date`, `pytest`, `openbb_core.app.service.user_service`, `UserService`, `openbb_imf.models.available_indicators`, `ImfAvailableIndicatorsFetcher`, `openbb_imf.models.direction_of_trade`, `ImfDirectionOfTradeFetcher`, `openbb_imf.models.economic_indicators`, `ImfEconomicIndicatorsFetcher`, `openbb_imf.models.maritime_chokepoint_info`, `ImfMaritimeChokePointInfoFetcher`, `openbb_imf.models.maritime_chokepoint_volume`, `openbb_imf.models.port_info`, `ImfPortInfoFetcher`, `openbb_imf.models.port_volume`, `ImfPortVolumeFetcher`, `the`


## Key Components

No major components extracted.

## Usage & Examples

See source code for usage details.

## Related Files

- `datetime`
- `pytest`
- `openbb_core.app.service.user_service`
- `openbb_imf.models.available_indicators`
- `openbb_imf.models.direction_of_trade`
- `openbb_imf.models.economic_indicators`
- `openbb_imf.models.maritime_chokepoint_info`
- `openbb_imf.models.maritime_chokepoint_volume`
- `openbb_imf.models.port_info`
- `openbb_imf.models.port_volume`

## Notes
- Generated: 2025-11-18T07:54:40.067213
- Generator: World's Best Repo Book Generator v1.0.0

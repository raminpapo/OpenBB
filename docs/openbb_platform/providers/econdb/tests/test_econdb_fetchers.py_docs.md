# Documentation: openbb_platform/providers/econdb/tests/test_econdb_fetchers.py

## File Metadata
- **Path**: `openbb_platform/providers/econdb/tests/test_econdb_fetchers.py`
- **Size**: 4,315 characters, 146 lines
- **Words**: 324
- **Extension**: .py
- **Classification**: Text file

## Original Source

```python
"""Test EconDB Fetchers."""

import datetime

import pytest
from openbb_core.app.service.user_service import UserService
from openbb_econdb.models.available_indicators import EconDbAvailableIndicatorsFetcher
from openbb_econdb.models.country_profile import EconDbCountryProfileFetcher
from openbb_econdb.models.economic_indicators import EconDbEconomicIndicatorsFetcher
from openbb_econdb.models.export_destinations import EconDbExportDestinationsFetcher
from openbb_econdb.models.gdp_nominal import EconDbGdpNominalFetcher
from openbb_econdb.models.gdp_real import EconDbGdpRealFetcher
from openbb_econdb.models.port_volume import EconDbPortVolumeFetcher
from openbb_econdb.models.yield_curve import EconDbYieldCurveFetcher

test_credentials = UserService().default_user_settings.credentials.model_dump(
    mode="json"
)


@pytest.fixture(scope="module")
def vcr_config():
    """VCR config."""
    return {
        "filter_headers": [("User-Agent", None)],
        "filter_query_parameters": [
            ("token", "MOCK_TOKEN"),
        ],
    }


@pytest.mark.record_http
def test_econdb_yield_curve_fetcher(credentials=test_credentials):
    """Test EconDB Yield Curve Fetcher."""
    params = {
        "country": "united_kingdom",
        "date": "2024-05-10,2020-05-10",
        "use_cache": False,
    }

    fetcher = EconDbYieldCurveFetcher()
    result = fetcher.test(params, credentials)
    assert result is None


@pytest.mark.record_http
def test_econdb_available_indicators_fetcher(credentials=test_credentials):
    """Test EconDB Available Indicators Fetcher."""
    params = {"use_cache": False}

    fetcher = EconDbAvailableIndicatorsFetcher()
    result = fetcher.test(params, credentials)
    assert result is None


@pytest.mark.record_http
def test_econdb_country_profile_fetcher(credentials=test_credentials):
    """Test EconDB Country Profile Fetcher."""
    params = {"country": "us", "latest": True, "use_cache": False}

    fetcher = EconDbCountryProfileFetcher()
    result = fetcher.test(params, credentials)
    assert result is None


@pytest.mark.record_http
def test_econdb_economic_indicators_fetcher(credentials=test_credentials):
    """Test EconDB Economic Indicators Fetcher."""
    params = {
        "country": "us",
        "symbol": "GDP",
        "start_date": datetime.date(2020, 1, 1),
        "end_date": datetime.date(2024, 1, 1),
        "use_cache": False,
    }

    fetcher = EconDbEconomicIndicatorsFetcher()
    result = fetcher.test(params, credentials)
    assert result is None


@pytest.mark.record_http
def test_econdb_economic_indicators_main_fetcher(credentials=test_credentials):
    """Test EconDB Economic Indicators Fetcher with main."""
    params = {
        "symbol": "main",
        "country": "jp",
        "start_date": datetime.date(2022, 1, 1),
        "end_date": datetime.date(2024, 4, 1),
        "transform": None,
        "frequency": "quarter",
        "use_cache": False,
    }

    fetcher = EconDbEconomicIndicatorsFetcher()
    result = fetcher.test(params, credentials)
    assert result is None


@pytest.mark.record_http
def test_econdb_gdp_nominal_fetcher(credentials=test_credentials):
    """Test EconDB GDP Nominal Fetcher."""
    params = {
        "country": "IN",
        "use_cache": False,
    }

    fetcher = EconDbGdpNominalFetcher()
    result = fetcher.test(params, credentials)
    assert result is None


@pytest.mark.record_http
def test_econdb_gdp_real_fetcher(credentials=test_credentials):
    """Test EconDB GDP Real Fetcher."""
    params = {
        "country": "IN",
        "use_cache": False,
    }

    fetcher = EconDbGdpRealFetcher()
    result = fetcher.test(params, credentials)
    assert result is None


@pytest.mark.record_http
def test_econdb_export_destinations_fetcher(credentials=test_credentials):
    """Test EconDB Export Destinations Fetcher."""
    params = {
        "country": "US",
    }

    fetcher = EconDbExportDestinationsFetcher()
    result = fetcher.test(params, credentials)
    assert result is None


@pytest.mark.record_http
def test_econdb_port_volume_fetcher(credentials=test_credentials):
    """Test EconDB Port Volume Fetcher."""
    params = {}

    fetcher = EconDbPortVolumeFetcher()
    result = fetcher.test(params, credentials)
    assert result is None

```

## High-Level Overview

Test EconDB Fetchers.

import datetime

import pytest
from openbb_core.app.service.user_service import UserService
from openbb_econdb.models.available_indicators import EconDbAvailableIndicatorsFetcher
from openbb_econdb.models.country_profile import EconDbCountryProfileFetcher
from openbb_econdb.models.economic_indicators import EconDbEconomicIndicatorsFetcher
from openbb_econdb.models.export_destinations import EconDbExportDestinationsFetcher
from openbb_econdb.models.gdp_nominal import EconDbGdpNominalFetcher
from openbb_econdb.models.gdp_real import EconDbGdpRealFetcher
from openbb_econdb.models.port_volume import EconDbPortVolumeFetcher
from openbb_econdb.models.yield_curve import EconDbYieldCurveFetcher

test_credentials = UserService().default_user_settings.credentials.model_dump(
mode="json"
)



## Detailed Structure

### Python File Structure

**Classes** (0):
None

**Functions** (10):
`vcr_config`, `test_econdb_yield_curve_fetcher`, `test_econdb_available_indicators_fetcher`, `test_econdb_country_profile_fetcher`, `test_econdb_economic_indicators_fetcher`, `test_econdb_economic_indicators_main_fetcher`, `test_econdb_gdp_nominal_fetcher`, `test_econdb_gdp_real_fetcher`, `test_econdb_export_destinations_fetcher`, `test_econdb_port_volume_fetcher`

**Imports** (20):
`datetime`, `pytest`, `openbb_core.app.service.user_service`, `UserService`, `openbb_econdb.models.available_indicators`, `EconDbAvailableIndicatorsFetcher`, `openbb_econdb.models.country_profile`, `EconDbCountryProfileFetcher`, `openbb_econdb.models.economic_indicators`, `EconDbEconomicIndicatorsFetcher`, `openbb_econdb.models.export_destinations`, `EconDbExportDestinationsFetcher`, `openbb_econdb.models.gdp_nominal`, `EconDbGdpNominalFetcher`, `openbb_econdb.models.gdp_real`, `EconDbGdpRealFetcher`, `openbb_econdb.models.port_volume`, `EconDbPortVolumeFetcher`, `openbb_econdb.models.yield_curve`, `EconDbYieldCurveFetcher`


## Key Components

No major components extracted.

## Usage & Examples

See source code for usage details.

## Related Files

- `datetime`
- `pytest`
- `openbb_core.app.service.user_service`
- `openbb_econdb.models.available_indicators`
- `openbb_econdb.models.country_profile`
- `openbb_econdb.models.economic_indicators`
- `openbb_econdb.models.export_destinations`
- `openbb_econdb.models.gdp_nominal`
- `openbb_econdb.models.gdp_real`
- `openbb_econdb.models.port_volume`

## Notes
- Generated: 2025-11-18T07:54:38.260169
- Generator: World's Best Repo Book Generator v1.0.0

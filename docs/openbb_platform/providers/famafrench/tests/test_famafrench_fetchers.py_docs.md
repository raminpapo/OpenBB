# Documentation: openbb_platform/providers/famafrench/tests/test_famafrench_fetchers.py

## File Metadata
- **Path**: `openbb_platform/providers/famafrench/tests/test_famafrench_fetchers.py`
- **Size**: 3,012 characters, 106 lines
- **Words**: 215
- **Extension**: .py
- **Classification**: Text file

## Original Source

```python
"""Fama-French fetchers tests."""

import pytest
from openbb_core.app.service.user_service import UserService
from openbb_famafrench.models.breakpoints import FamaFrenchBreakpointFetcher
from openbb_famafrench.models.country_portfolio_returns import (
    FamaFrenchCountryPortfolioReturnsFetcher,
)
from openbb_famafrench.models.factors import FamaFrenchFactorsFetcher
from openbb_famafrench.models.international_index_returns import (
    FamaFrenchInternationalIndexReturnsFetcher,
)
from openbb_famafrench.models.regional_portfolio_returns import (
    FamaFrenchRegionalPortfolioReturnsFetcher,
)
from openbb_famafrench.models.us_portfolio_returns import (
    FamaFrenchUSPortfolioReturnsFetcher,
)

test_credentials = UserService().default_user_settings.credentials.model_dump(
    mode="json"
)


@pytest.fixture(scope="module")
def vcr_config():
    """VCR configuration."""
    return {
        "filter_headers": [
            ("User-Agent", None),
        ],
    }


@pytest.mark.record_http
def test_famafrench_factors(credentials=test_credentials):
    """Test Fama-French factors fetcher."""
    params = {"region": "america", "factor": "3_factors", "interval": "annual"}

    fetcher = FamaFrenchFactorsFetcher()
    result = fetcher.test(params, credentials)
    assert result is None


@pytest.mark.record_http
def test_us_portfolio_returns(credentials=test_credentials):
    """Test US portfolio returns fetcher."""
    params = {
        "portfolio": "5_industry_portfolios",
        "measure": "value",
        "frequency": "monthly",
    }

    fetcher = FamaFrenchUSPortfolioReturnsFetcher()
    result = fetcher.test(params, credentials)
    assert result is None


@pytest.mark.record_http
def test_regional_portfolio_returns(credentials=test_credentials):
    """Test regional portfolio returns fetcher."""
    params = {
        "region": "europe",
    }

    fetcher = FamaFrenchRegionalPortfolioReturnsFetcher()
    result = fetcher.test(params, credentials)
    assert result is None


@pytest.mark.record_http
def test_country_portfolio_returns(credentials=test_credentials):
    """Test country portfolio returns fetcher."""
    params = {
        "country": "japan",
    }

    fetcher = FamaFrenchCountryPortfolioReturnsFetcher()
    result = fetcher.test(params, credentials)
    assert result is None


@pytest.mark.record_http
def test_international_index_returns(credentials=test_credentials):
    """Test international index returns fetcher."""
    params = {
        "index": "europe_ex_uk",
        "frequency": "annual",
    }

    fetcher = FamaFrenchInternationalIndexReturnsFetcher()
    result = fetcher.test(params, credentials)
    assert result is None


@pytest.mark.record_http
def test_fama_french_breakpoints(credentials=test_credentials):
    """Test Fama-French breakpoints fetcher."""
    params = {
        "breakpoint_type": "op",
    }

    fetcher = FamaFrenchBreakpointFetcher()
    result = fetcher.test(params, credentials)
    assert result is None

```

## High-Level Overview

Fama-French fetchers tests.

import pytest
from openbb_core.app.service.user_service import UserService
from openbb_famafrench.models.breakpoints import FamaFrenchBreakpointFetcher
from openbb_famafrench.models.country_portfolio_returns import (
FamaFrenchCountryPortfolioReturnsFetcher,
)
from openbb_famafrench.models.factors import FamaFrenchFactorsFetcher
from openbb_famafrench.models.international_index_returns import (
FamaFrenchInternationalIndexReturnsFetcher,
)
from openbb_famafrench.models.regional_portfolio_returns import (
FamaFrenchRegionalPortfolioReturnsFetcher,
)
from openbb_famafrench.models.us_portfolio_returns import (
FamaFrenchUSPortfolioReturnsFetcher,
)

test_credentials = UserService().default_user_settings.credentials.model_dump(

## Detailed Structure

### Python File Structure

**Classes** (0):
None

**Functions** (7):
`vcr_config`, `test_famafrench_factors`, `test_us_portfolio_returns`, `test_regional_portfolio_returns`, `test_country_portfolio_returns`, `test_international_index_returns`, `test_fama_french_breakpoints`

**Imports** (11):
`pytest`, `openbb_core.app.service.user_service`, `UserService`, `openbb_famafrench.models.breakpoints`, `FamaFrenchBreakpointFetcher`, `openbb_famafrench.models.country_portfolio_returns`, `openbb_famafrench.models.factors`, `FamaFrenchFactorsFetcher`, `openbb_famafrench.models.international_index_returns`, `openbb_famafrench.models.regional_portfolio_returns`, `openbb_famafrench.models.us_portfolio_returns`


## Key Components

No major components extracted.

## Usage & Examples

See source code for usage details.

## Related Files

- `pytest`
- `openbb_core.app.service.user_service`
- `openbb_famafrench.models.breakpoints`
- `openbb_famafrench.models.country_portfolio_returns`
- `openbb_famafrench.models.factors`
- `openbb_famafrench.models.international_index_returns`
- `openbb_famafrench.models.regional_portfolio_returns`
- `openbb_famafrench.models.us_portfolio_returns`

## Notes
- Generated: 2025-11-18T07:54:38.450244
- Generator: World's Best Repo Book Generator v1.0.0

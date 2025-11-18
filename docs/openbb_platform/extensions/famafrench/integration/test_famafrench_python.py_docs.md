# Documentation: openbb_platform/extensions/famafrench/integration/test_famafrench_python.py

## File Metadata
- **Path**: `openbb_platform/extensions/famafrench/integration/test_famafrench_python.py`
- **Size**: 5,697 characters, 228 lines
- **Words**: 446
- **Extension**: .py
- **Classification**: Text file

## Original Source

```python
"""Test Fama-French Python Interface."""

import pytest
from openbb_core.app.model.obbject import OBBject

# pylint: disable=redefined-outer-name


@pytest.fixture(scope="session")
def obb(pytestconfig):  # pylint: disable=inconsistent-return-statements
    """Fixture to setup obb."""
    if pytestconfig.getoption("markexpr") != "not integration":
        import openbb  # pylint: disable=import-outside-toplevel

        return openbb.obb


@pytest.mark.parametrize(
    "params",
    [
        (
            {
                "provider": "famafrench",
            }
        ),
        (
            {
                "provider": "famafrench",
                "region": "america",
                "factor": "momentum",
                "frequency": "monthly",
                "start_date": None,
                "end_date": None,
            }
        ),
    ],
)
@pytest.mark.integration
def test_famafrench_factors(params, obb):
    """Test the Fama-French factors endpoint."""
    params = {p: v for p, v in params.items() if v}

    result = obb.famafrench.factors(**params)
    assert result
    assert isinstance(result, OBBject)
    assert len(result.results) > 0


@pytest.mark.parametrize(
    "params",
    [
        (
            {
                "provider": "famafrench",
            }
        ),
        (
            {
                "provider": "famafrench",
                "portfolio": "5_industry_portfolios",
                "measure": "equal",
                "frequency": "annual",
                "start_date": None,
                "end_date": None,
            }
        ),
    ],
)
@pytest.mark.integration
def test_famafrench_us_portfolio_returns(params, obb):
    """Test the US portfolio returns endpoint."""
    params = {p: v for p, v in params.items() if v}

    result = obb.famafrench.us_portfolio_returns(**params)
    assert result
    assert isinstance(result, OBBject)
    assert len(result.results) > 0


@pytest.mark.parametrize(
    "params",
    [
        (
            {
                "provider": "famafrench",
            }
        ),
        (
            {
                "provider": "famafrench",
                "portfolio": "developed_ex_us_6_portfolios_me_op",
                "measure": "equal",
                "frequency": None,
                "start_date": None,
                "end_date": None,
            }
        ),
    ],
)
@pytest.mark.integration
def test_famafrench_regional_portfolio_returns(params, obb):
    """Test the regional portfolio returns endpoint."""
    params = {p: v for p, v in params.items() if v}

    result = obb.famafrench.regional_portfolio_returns(**params)
    assert result
    assert isinstance(result, OBBject)
    assert len(result.results) > 0


@pytest.mark.parametrize(
    "params",
    [
        (
            {
                "provider": "famafrench",
            }
        ),
        (
            {
                "provider": "famafrench",
                "country": "japan",
                "measure": "ratios",
                "frequency": None,
                "start_date": None,
                "end_date": None,
                "dividends": True,
                "all_data_items_required": True,
            }
        ),
    ],
)
@pytest.mark.integration
def test_famafrench_country_portfolio_returns(params, obb):
    """Test the country portfolio returns endpoint."""
    params = {p: v for p, v in params.items() if v}

    result = obb.famafrench.country_portfolio_returns(**params)
    assert result
    assert isinstance(result, OBBject)
    assert len(result.results) > 0


@pytest.mark.parametrize(
    "params",
    [
        (
            {
                "provider": "famafrench",
            }
        ),
        (
            {
                "provider": "famafrench",
                "index": "asia_pacific",
                "measure": "local",
                "frequency": "annual",
                "start_date": None,
                "end_date": None,
                "dividends": True,
                "all_data_items_required": True,
            }
        ),
    ],
)
@pytest.mark.integration
def test_famafrench_international_index_returns(params, obb):
    """Test the international index returns endpoint."""
    params = {p: v for p, v in params.items() if v}

    result = obb.famafrench.international_index_returns(**params)
    assert result
    assert isinstance(result, OBBject)
    assert len(result.results) > 0


@pytest.mark.parametrize(
    "params",
    [
        (
            {
                "provider": "famafrench",
            }
        ),
        (
            {
                "provider": "famafrench",
                "breakpoint_type": "op",
                "start_date": None,
                "end_date": None,
            }
        ),
    ],
)
@pytest.mark.integration
def test_famafrench_breakpoints(params, obb):
    """Test the Fama-French breakpoints endpoint."""
    params = {p: v for p, v in params.items() if v}

    result = obb.famafrench.breakpoints(**params)
    assert result
    assert isinstance(result, OBBject)
    assert len(result.results) > 0


@pytest.mark.parametrize(
    "params",
    [
        (
            {
                "region": "america",
                "factor": "Momentum",
                "is_portfolio": None,
                "portfolio": None,
            }
        ),
    ],
)
@pytest.mark.integration
def test_famafrench_factor_choices(params, obb):
    """Test Fama-French available factors endpoint."""
    params = {p: v for p, v in params.items() if v}

    result = obb.famafrench.factor_choices(**params)
    assert result
    assert isinstance(result, list)
    assert len(result) > 0

```

## High-Level Overview

Test Fama-French Python Interface.

import pytest
from openbb_core.app.model.obbject import OBBject

# pylint: disable=redefined-outer-name


@pytest.fixture(scope="session")
def obb(pytestconfig):  # pylint: disable=inconsistent-return-statements
Fixture to setup obb.
Test the Fama-French factors endpoint.
params = {p: v for p, v in params.items() if v}

result = obb.famafrench.factors(**params)
assert result
assert isinstance(result, OBBject)
assert len(result.results) > 0



## Detailed Structure

### Python File Structure

**Classes** (0):
None

**Functions** (8):
`obb`, `test_famafrench_factors`, `test_famafrench_us_portfolio_returns`, `test_famafrench_regional_portfolio_returns`, `test_famafrench_country_portfolio_returns`, `test_famafrench_international_index_returns`, `test_famafrench_breakpoints`, `test_famafrench_factor_choices`

**Imports** (4):
`pytest`, `openbb_core.app.model.obbject`, `OBBject`, `openbb`


## Key Components

No major components extracted.

## Usage & Examples

See source code for usage details.

## Related Files

- `pytest`
- `openbb_core.app.model.obbject`
- `openbb`

## Notes
- Generated: 2025-11-18T07:54:36.126583
- Generator: World's Best Repo Book Generator v1.0.0

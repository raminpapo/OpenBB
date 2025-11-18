# Documentation: openbb_platform/extensions/derivatives/integration/test_derivatives_python.py

## File Metadata
- **Path**: `openbb_platform/extensions/derivatives/integration/test_derivatives_python.py`
- **Size**: 6,984 characters, 229 lines
- **Words**: 537
- **Extension**: .py
- **Classification**: Text file

## Original Source

```python
"""Python interface integration tests for the derivatives extension."""

import pytest
from openbb_core.app.model.obbject import OBBject

# pylint: disable=too-many-lines,redefined-outer-name
# pylint: disable=import-outside-toplevel,inconsistent-return-statements


@pytest.fixture(scope="session")
def obb(pytestconfig):
    """Fixture to setup obb."""
    if pytestconfig.getoption("markexpr") != "not integration":
        import openbb

        return openbb.obb


@pytest.mark.parametrize(
    "params",
    [
        (
            {
                "provider": "intrinio",
                "symbol": "AAPL",
                "date": "2023-01-25",
                "option_type": None,
                "moneyness": "all",
                "strike_gt": None,
                "strike_lt": None,
                "volume_gt": None,
                "volume_lt": None,
                "oi_gt": None,
                "oi_lt": None,
                "model": "black_scholes",
                "show_extended_price": False,
                "include_related_symbols": False,
                "delay": "delayed",
            }
        ),
        ({"provider": "cboe", "symbol": "AAPL", "use_cache": False}),
        ({"provider": "tradier", "symbol": "AAPL"}),
        ({"provider": "yfinance", "symbol": "AAPL"}),
        ({"provider": "deribit", "symbol": "BTC"}),
        (
            {
                "provider": "tmx",
                "symbol": "SHOP",
                "date": "2022-12-28",
                "use_cache": False,
            }
        ),
    ],
)
@pytest.mark.integration
def test_derivatives_options_chains(params, obb):
    """Test the options chains endpoint."""
    result = obb.derivatives.options.chains(**params)
    assert result
    assert isinstance(result, OBBject)
    result = result.results  # type: ignore
    list_msg = "Unexpected data format, expected List"
    oi_msg = "Unexpected keys in total_oi property, expected ['total', 'expiration', 'strike']"
    assert isinstance(result.expirations, list), list_msg  # type: ignore
    assert isinstance(result.strikes, list), list_msg  # type: ignore
    assert isinstance(result.contract_symbol, list), list_msg  # type: ignore
    assert hasattr(result, "total_oi"), "Missing total_oi property"  # type: ignore
    assert isinstance(result.total_oi, dict), "Unexpected property format, expected dictionary."  # type: ignore
    assert list(result.total_oi) == ["total", "expiration", "strike"], oi_msg  # type: ignore
    assert hasattr(result, "dataframe"), "Missing dataframe attribute"  # type: ignore
    assert result.has_iv, "Expected implied volatility data"  # type: ignore
    assert len(getattr(result, "dataframe", [])) == len(result.contract_symbol)  # type: ignore


@pytest.mark.parametrize(
    "params",
    [
        {
            "symbol": "AAPL",
            "provider": "intrinio",
            "start_date": "2023-11-20",
            "end_date": None,
            "min_value": None,
            "max_value": None,
            "trade_type": None,
            "sentiment": "neutral",
            "limit": 1000,
            "source": "delayed",
        }
    ],
)
@pytest.mark.integration
def test_derivatives_options_unusual(params, obb):
    """Test the unusual options endpoint."""
    result = obb.derivatives.options.unusual(**params)
    assert result
    assert isinstance(result, OBBject)
    assert len(result.results) > 0


@pytest.mark.parametrize(
    "params",
    [
        (
            {
                "provider": "yfinance",
                "interval": "1d",
                "symbol": "CL,BZ",
                "start_date": "2023-01-01",
                "end_date": "2023-06-06",
                "expiration": "2025-12",
            }
        ),
        (
            {
                "provider": "deribit",
                "interval": "1d",
                "symbol": "BTC,ETH",
                "start_date": "2023-01-01",
                "end_date": "2023-06-06",
            }
        ),
    ],
)
@pytest.mark.integration
def test_derivatives_futures_historical(params, obb):
    """Test the futures historical endpoint."""
    result = obb.derivatives.futures.historical(**params)
    assert result
    assert isinstance(result, OBBject)
    assert len(result.results) > 0


@pytest.mark.parametrize(
    "params",
    [
        ({"provider": "yfinance", "symbol": "ES", "date": None}),
        ({"provider": "cboe", "symbol": "VX", "date": "2024-06-25"}),
        ({"provider": "deribit", "date": None, "symbol": "BTC", "hours_ago": 12}),
    ],
)
@pytest.mark.integration
def test_derivatives_futures_curve(params, obb):
    """Test the futures curve endpoint."""
    result = obb.derivatives.futures.curve(**params)
    assert result
    assert isinstance(result, OBBject)
    assert len(result.results) > 0


@pytest.mark.parametrize(
    "params",
    [
        ({"provider": "intrinio", "date": None, "only_traded": True}),
    ],
)
@pytest.mark.skip(
    reason="This test is skipped because the download is excessively large."
)
def test_derivatives_options_snapshots(params, obb):
    """Test the options snapshots endpoint."""
    result = obb.derivatives.options.snapshots(**params)
    assert result
    assert isinstance(result, OBBject)
    assert len(result.results) > 0


@pytest.mark.parametrize(
    "params",
    [
        ({"provider": "deribit"}),
    ],
)
@pytest.mark.integration
def test_derivatives_futures_instruments(params, obb):
    """Test the futures instruments endpoint."""
    result = obb.derivatives.futures.instruments(**params)
    assert result
    assert isinstance(result, OBBject)
    assert len(result.results) > 0


@pytest.mark.parametrize(
    "params",
    [
        ({"provider": "deribit", "symbol": "ETH-PERPETUAL"}),
    ],
)
@pytest.mark.integration
def test_derivatives_futures_info(params, obb):
    """Test the futures info endpoint."""
    result = obb.derivatives.futures.info(**params)
    assert result
    assert isinstance(result, OBBject)
    assert len(result.results) > 0


@pytest.mark.parametrize(
    "params",
    [
        (
            {
                "data": "",
                "target": "implied_volatility",
                "underlying_price": None,
                "option_type": "otm",
                "dte_min": None,
                "dte_max": None,
                "moneyness": None,
                "strike_min": None,
                "strike_max": None,
                "oi": False,
                "volume": False,
                "theme": "dark",
                "chart_params": None,
            }
        ),
    ],
)
@pytest.mark.integration
def test_derivatives_options_surface(params, obb):
    """Test equity price historical."""
    data = obb.derivatives.options.chains("AAPL", provider="cboe")
    params["data"] = data.results
    result = obb.derivatives.options.surface(**params)
    assert result
    assert isinstance(result, OBBject)
    assert len(result.results) > 0

```

## High-Level Overview

Python interface integration tests for the derivatives extension.

import pytest
from openbb_core.app.model.obbject import OBBject

# pylint: disable=too-many-lines,redefined-outer-name
# pylint: disable=import-outside-toplevel,inconsistent-return-statements


@pytest.fixture(scope="session")
def obb(pytestconfig):
Fixture to setup obb.

## Detailed Structure

### Python File Structure

**Classes** (0):
None

**Functions** (9):
`obb`, `test_derivatives_options_chains`, `test_derivatives_options_unusual`, `test_derivatives_futures_historical`, `test_derivatives_futures_curve`, `test_derivatives_options_snapshots`, `test_derivatives_futures_instruments`, `test_derivatives_futures_info`, `test_derivatives_options_surface`

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
- Generated: 2025-11-18T07:54:35.954962
- Generator: World's Best Repo Book Generator v1.0.0

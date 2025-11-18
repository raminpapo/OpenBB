# Documentation: openbb_platform/extensions/crypto/integration/test_crypto_python.py

## File Metadata
- **Path**: `openbb_platform/extensions/crypto/integration/test_crypto_python.py`
- **Size**: 3,069 characters, 117 lines
- **Words**: 213
- **Extension**: .py
- **Classification**: Text file

## Original Source

```python
"""Test crypto extension."""

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
        ({"query": "asd"}),
        ({"query": "btc", "provider": "fmp"}),
    ],
)
@pytest.mark.integration
def test_crypto_search(params, obb):
    """Test the crypto search endpoint."""
    params = {p: v for p, v in params.items() if v}

    result = obb.crypto.search(**params)
    assert result
    assert isinstance(result, OBBject)
    assert len(result.results) > 0


@pytest.mark.parametrize(
    "params",
    [
        (
            {
                "interval": "1d",
                "provider": "fmp",
                "symbol": "BTCUSD",
                "start_date": "2023-01-01",
                "end_date": "2023-01-02",
            }
        ),
        (
            {
                "interval": "1h",
                "provider": "fmp",
                "symbol": "BTCUSD,ETHUSD",
                "start_date": None,
                "end_date": None,
            }
        ),
        (
            {
                "interval": "1m",
                "sort": "desc",
                "limit": 49999,
                "provider": "polygon",
                "symbol": "BTCUSD",
                "start_date": "2023-01-01",
                "end_date": "2023-01-02",
            }
        ),
        (
            {
                "interval": "1d",
                "sort": "desc",
                "limit": 49999,
                "provider": "polygon",
                "symbol": "BTCUSD",
                "start_date": "2023-01-01",
                "end_date": "2023-06-06",
            }
        ),
        (
            {
                "interval": "1d",
                "provider": "yfinance",
                "symbol": "BTCUSD",
                "start_date": "2023-01-01",
                "end_date": "2023-01-04",
            }
        ),
        (
            {
                "provider": "tiingo",
                "interval": "1d",
                "exchanges": None,
                "symbol": "BTCUSD",
                "start_date": "2023-01-01",
                "end_date": "2023-06-06",
            }
        ),
        (
            {
                "provider": "tiingo",
                "interval": "1h",
                "exchanges": ["POLONIEX", "GDAX"],
                "symbol": "BTCUSD",
                "start_date": "2023-01-01",
                "end_date": "2023-01-02",
            }
        ),
    ],
)
@pytest.mark.integration
def test_crypto_price_historical(params, obb):
    """Test crypto price historical."""
    result = obb.crypto.price.historical(**params)
    assert result
    assert isinstance(result, OBBject)
    assert len(result.results) > 0

```

## High-Level Overview

Test crypto extension.

import pytest
from openbb_core.app.model.obbject import OBBject

# pylint: disable=redefined-outer-name


@pytest.fixture(scope="session")
def obb(pytestconfig):  # pylint: disable=inconsistent-return-statements
Fixture to setup obb.
Test the crypto search endpoint.
params = {p: v for p, v in params.items() if v}

result = obb.crypto.search(**params)
assert result
assert isinstance(result, OBBject)
assert len(result.results) > 0



## Detailed Structure

### Python File Structure

**Classes** (0):
None

**Functions** (3):
`obb`, `test_crypto_search`, `test_crypto_price_historical`

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
- Generated: 2025-11-18T07:54:35.914016
- Generator: World's Best Repo Book Generator v1.0.0

# File Documentation: test_commodity_python.py

## Metadata
- **Path**: `openbb_platform/extensions/commodity/integration/test_commodity_python.py`
- **Size**: 2,654 bytes
- **Lines**: 101
- **Category**: python
- **Extension**: .py

---

## Original Source

```python
"""Test Commodity extension."""

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
                "commodity": "all",
                "start_date": None,
                "end_date": None,
                "frequency": None,
                "transform": None,
                "aggregation_method": None,
                "provider": "fred",
            }
        ),
    ],
)
@pytest.mark.integration
def test_commodity_price_spot(params, obb):
    """Test the commodity spot prices endpoint."""
    params = {p: v for p, v in params.items() if v}

    result = obb.commodity.price.spot(**params)
    assert result
    assert isinstance(result, OBBject)
    assert len(result.results) > 0


@pytest.mark.parametrize(
    "params",
    [
        (
            {
                "category": "balance_sheet",
                "table": "stocks",
                "start_date": None,
                "end_date": None,
                "provider": "eia",
                "use_cache": True,
            }
        ),
        (
            {
                "category": "weekly_estimates",
                "table": "crude_production",
                "start_date": "2020-01-01",
                "end_date": "2023-12-31",
                "provider": "eia",
                "use_cache": True,
            }
        ),
    ],
)
@pytest.mark.integration
def test_commodity_petroleum_status_report(params, obb):
    """Test Commodity Petroleum Status Report endpoint."""
    result = obb.commodity.petroleum_status_report(**params)
    assert result
    assert isinstance(result, OBBject)
    assert len(result.results) > 0


@pytest.mark.parametrize(
    "params",
    [
        (
            {
                "table": "01",
                "symbol": None,
                "start_date": "2024-09-01",
                "end_date": "2024-10-01",
                "provider": "eia",
                "frequency": "month",
            }
        ),
    ],
)
@pytest.mark.integration
def test_commodity_short_term_energy_outlook(params, obb):
    """Test Commodity Short Term Energy Outlook endpoint."""
    result = obb.commodity.short_term_energy_outlook(**params)
    assert result
    assert isinstance(result, OBBject)
    assert len(result.results) > 0

```



---

## High-Level Overview

This is a **python** file named `test_commodity_python.py`.

**Python Module**

- **Functions** (4): obb, test_commodity_price_spot, test_commodity_petroleum_status_report, test_commodity_short_term_energy_outlook
- **Import Statements**: 2


---

## Detailed Analysis

### Python Code Structure


#### Functions

- **`obb(pytestconfig)`**
- **`test_commodity_price_spot(params, obb)`**
- **`test_commodity_petroleum_status_report(params, obb)`**
- **`test_commodity_short_term_energy_outlook(params, obb)`**

#### Decorators Used

pytest


---

## Related Files

The following files may be related based on imports and references:

**Imported Modules**:
- `OBBject`
- `openbb`
- `openbb_core.app.model.obbject`
- `pytest`


---

## Performance & Security Notes

No obvious security concerns detected in static analysis.


---

**Generated**: 2025-11-19T02:16:46.738538Z
**Generator**: World's Best Repo Book Generator v1.0

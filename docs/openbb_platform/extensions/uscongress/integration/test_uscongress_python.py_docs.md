# Documentation: openbb_platform/extensions/uscongress/integration/test_uscongress_python.py

## File Metadata
- **Path**: `openbb_platform/extensions/uscongress/integration/test_uscongress_python.py`
- **Size**: 3,166 characters, 125 lines
- **Words**: 252
- **Extension**: .py
- **Classification**: Text file

## Original Source

```python
"""Test Government extension."""

import pytest
from openbb_congress_gov.models.bill_info import CongressBillInfoData
from openbb_congress_gov.models.bill_text import CongressBillTextData
from openbb_core.app.model.obbject import OBBject


@pytest.fixture(scope="session")
def obb(pytestconfig):  # pylint: disable=inconsistent-return-statements
    """Fixture to setup obb."""

    if pytestconfig.getoption("markexpr") != "not integration":
        import openbb  # pylint: disable=import-outside-toplevel

        return openbb.obb


# pylint: disable=redefined-outer-name


@pytest.mark.parametrize(
    "params",
    [
        (
            {
                "provider": "congress_gov",
            }
        ),
        (
            {
                "provider": "congress_gov",
                "limit": 5,
                "offset": 0,
                "sort_by": "desc",
                "congress": None,
                "bill_type": None,
                "start_date": None,
                "end_date": None,
            }
        ),
    ],
)
@pytest.mark.integration
def test_uscongress_bills(params, obb):
    """Test US Congress bills."""
    params = {p: v for p, v in params.items() if v}

    result = obb.uscongress.bills(**params)
    assert result
    assert isinstance(result, OBBject)
    assert len(result.results) > 0


@pytest.mark.parametrize(
    "params",
    [
        (
            {
                "provider": "congress_gov",
                "bill_url": "119/hr/1",
            }
        ),
    ],
)
@pytest.mark.integration
def test_uscongress_bill_info(params, obb):
    """Test US Congress bill info."""
    params = {p: v for p, v in params.items() if v}

    result = obb.uscongress.bill_info(**params)
    assert result
    assert isinstance(result, OBBject)
    assert isinstance(result.results, CongressBillInfoData)
    assert isinstance(result.results.markdown_content, str)
    assert isinstance(result.results.raw_data, dict)


@pytest.mark.parametrize(
    "params",
    [
        (
            {
                "provider": "congress_gov",
                "bill_url": "https://api.congress.gov/v3/bill/119/s/1947?format=json",
                "is_workspace": False,
            }
        ),
    ],
)
@pytest.mark.integration
def test_uscongress_bill_text_urls(params, obb):
    """Test US Congress bill text URLs."""
    params = {p: v for p, v in params.items() if v}

    result = obb.uscongress.bill_text_urls(**params)
    assert result
    assert isinstance(result, list)
    assert len(result) > 0


@pytest.mark.parametrize(
    "params",
    [
        (
            {
                "provider": "congress_gov",
                "urls": [
                    "https://www.congress.gov/119/bills/hr1/BILLS-119hr1eh.pdf",
                ],
            }
        ),
    ],
)
@pytest.mark.integration
def test_uscongress_bill_text(params, obb):
    """Test US Congress bill text."""
    params = {p: v for p, v in params.items() if v}

    result = obb.uscongress.bill_text(**params)
    assert result
    assert isinstance(result, list)
    assert len(result) > 0
    assert isinstance(result[0], CongressBillTextData)

```

## High-Level Overview

Test Government extension.

import pytest
from openbb_congress_gov.models.bill_info import CongressBillInfoData
from openbb_congress_gov.models.bill_text import CongressBillTextData
from openbb_core.app.model.obbject import OBBject


@pytest.fixture(scope="session")
def obb(pytestconfig):  # pylint: disable=inconsistent-return-statements
Fixture to setup obb.
pylint: disable=redefined-outer-name
Test US Congress bills.
params = {p: v for p, v in params.items() if v}

result = obb.uscongress.bills(**params)
assert result

## Detailed Structure

### Python File Structure

**Classes** (0):
None

**Functions** (5):
`obb`, `test_uscongress_bills`, `test_uscongress_bill_info`, `test_uscongress_bill_text_urls`, `test_uscongress_bill_text`

**Imports** (8):
`pytest`, `openbb_congress_gov.models.bill_info`, `CongressBillInfoData`, `openbb_congress_gov.models.bill_text`, `CongressBillTextData`, `openbb_core.app.model.obbject`, `OBBject`, `openbb`


## Key Components

No major components extracted.

## Usage & Examples

See source code for usage details.

## Related Files

- `pytest`
- `openbb_congress_gov.models.bill_info`
- `openbb_congress_gov.models.bill_text`
- `openbb_core.app.model.obbject`
- `openbb`

## Notes
- Generated: 2025-11-18T07:54:36.410729
- Generator: World's Best Repo Book Generator v1.0.0

# Documentation: openbb_platform/providers/yfinance/tests/test_yfinance_helpers.py

## File Metadata
- **Path**: `openbb_platform/providers/yfinance/tests/test_yfinance_helpers.py`
- **Size**: 1,074 characters, 36 lines
- **Words**: 94
- **Extension**: .py
- **Classification**: Text file

## Original Source

```python
"""Test yfinance helpers."""

import pandas as pd
import pytest
from openbb_yfinance.utils.helpers import (
    df_transform_numbers,
    get_futures_data,
)

# pylint: disable=redefined-outer-name, unused-argument

MOCK_FUTURES_DATA = pd.DataFrame({"Ticker": ["ES", "NQ"], "Exchange": ["CME", "CME"]})


@pytest.fixture
def mock_futures_csv(monkeypatch):
    """Mock pd.read_csv to return predefined futures data."""
    monkeypatch.setattr(pd, "read_csv", lambda *args, **kwargs: MOCK_FUTURES_DATA)


def test_get_futures_data(mock_futures_csv):
    """Test get_futures_data."""
    df = get_futures_data()
    assert not df.empty
    assert df.equals(MOCK_FUTURES_DATA)


def test_df_transform_numbers():
    """Test df_transform_numbers."""
    data = pd.DataFrame(
        {"Value": ["1M", "2.5B", "3T"], "% Change": ["1%", "-2%", "3.5%"]}
    )
    transformed = df_transform_numbers(data, ["Value", "% Change"])
    assert transformed["Value"].equals(pd.Series([1e6, 2.5e9, 3e12]))
    assert transformed["% Change"].equals(pd.Series([1 / 100, -2 / 100, 3.5 / 100]))

```

## High-Level Overview

Test yfinance helpers.

import pandas as pd
import pytest
from openbb_yfinance.utils.helpers import (
df_transform_numbers,
get_futures_data,
)

# pylint: disable=redefined-outer-name, unused-argument

MOCK_FUTURES_DATA = pd.DataFrame({"Ticker": ["ES", "NQ"], "Exchange": ["CME", "CME"]})


@pytest.fixture
def mock_futures_csv(monkeypatch):
Mock pd.read_csv to return predefined futures data.
Test get_futures_data.
df = get_futures_data()
assert not df.empty

## Detailed Structure

### Python File Structure

**Classes** (0):
None

**Functions** (3):
`mock_futures_csv`, `test_get_futures_data`, `test_df_transform_numbers`

**Imports** (3):
`pandas`, `pytest`, `openbb_yfinance.utils.helpers`


## Key Components

No major components extracted.

## Usage & Examples

See source code for usage details.

## Related Files

- `pandas`
- `pytest`
- `openbb_yfinance.utils.helpers`

## Notes
- Generated: 2025-11-18T07:54:43.855484
- Generator: World's Best Repo Book Generator v1.0.0

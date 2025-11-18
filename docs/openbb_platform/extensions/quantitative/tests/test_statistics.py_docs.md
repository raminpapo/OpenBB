# Documentation: openbb_platform/extensions/quantitative/tests/test_statistics.py

## File Metadata
- **Path**: `openbb_platform/extensions/quantitative/tests/test_statistics.py`
- **Size**: 822 characters, 33 lines
- **Words**: 87
- **Extension**: .py
- **Classification**: Text file

## Original Source

```python
"""Tests for the statistics module."""

import pandas as pd
import pytest
from openbb_quantitative.statistics import kurtosis_, mean_, skew_, std_dev_, var_

test_data = pd.Series([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])


def test_kurtosis():
    """Test the kurtosis function."""
    assert kurtosis_(test_data) == pytest.approx(-1.224, abs=1e-3)


def test_skew():
    """Test the skewness function."""
    assert skew_(test_data) == pytest.approx(0.0, abs=1e-3)


def test_std_dev():
    """Test the standard deviation function."""
    assert std_dev_(test_data) == pytest.approx(2.872, abs=1e-3)


def test_mean():
    """Test the mean function."""
    assert mean_(test_data) == pytest.approx(5.5, abs=1e-3)


def test_var():
    """Test the variance function."""
    assert var_(test_data) == pytest.approx(8.25, abs=1e-3)

```

## High-Level Overview

Tests for the statistics module.

import pandas as pd
import pytest
from openbb_quantitative.statistics import kurtosis_, mean_, skew_, std_dev_, var_

test_data = pd.Series([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])


def test_kurtosis():
Test the kurtosis function.
Test the skewness function.
assert skew_(test_data) == pytest.approx(0.0, abs=1e-3)


def test_std_dev():
Test the standard deviation function.
Test the mean function.
assert mean_(test_data) == pytest.approx(5.5, abs=1e-3)


## Detailed Structure

### Python File Structure

**Classes** (0):
None

**Functions** (5):
`test_kurtosis`, `test_skew`, `test_std_dev`, `test_mean`, `test_var`

**Imports** (4):
`pandas`, `pytest`, `openbb_quantitative.statistics`, `kurtosis_`


## Key Components

No major components extracted.

## Usage & Examples

See source code for usage details.

## Related Files

- `pandas`
- `pytest`
- `openbb_quantitative.statistics`

## Notes
- Generated: 2025-11-18T07:54:36.335692
- Generator: World's Best Repo Book Generator v1.0.0

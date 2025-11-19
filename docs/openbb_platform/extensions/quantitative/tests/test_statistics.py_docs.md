# File Documentation: test_statistics.py

## Metadata
- **Path**: `openbb_platform/extensions/quantitative/tests/test_statistics.py`
- **Size**: 822 bytes
- **Lines**: 33
- **Category**: python
- **Extension**: .py

---

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



---

## High-Level Overview

This is a **python** file named `test_statistics.py`.

**Python Module**

- **Functions** (5): test_kurtosis, test_skew, test_std_dev, test_mean, test_var
- **Import Statements**: 1


---

## Detailed Analysis

### Python Code Structure


#### Functions

- **`test_kurtosis()`**
- **`test_skew()`**
- **`test_std_dev()`**
- **`test_mean()`**
- **`test_var()`**


---

## Related Files

The following files may be related based on imports and references:

**Imported Modules**:
- `kurtosis_`
- `openbb_quantitative.statistics`
- `pandas`
- `pytest`


---

## Performance & Security Notes

No obvious security concerns detected in static analysis.


---

**Generated**: 2025-11-19T02:16:47.271782Z
**Generator**: World's Best Repo Book Generator v1.0

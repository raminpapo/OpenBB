# File Documentation: test_econometrics_utils.py

## Metadata
- **Path**: `openbb_platform/extensions/econometrics/tests/test_econometrics_utils.py`
- **Size**: 710 bytes
- **Lines**: 26
- **Category**: python
- **Extension**: .py

---

## Original Source

```python
"""Test the econometrics utils module."""

import numpy as np
import pandas as pd
from openbb_econometrics.utils import (
    get_engle_granger_two_step_cointegration_test,
    mock_multi_index_data,
)


def test_get_engle_granger_two_step_cointegration_test():
    """Test the get_engle_granger_two_step_cointegration_test function."""
    x = pd.Series(np.random.randn(100))
    y = pd.Series(np.random.randn(100))

    result = get_engle_granger_two_step_cointegration_test(x, y)

    assert result


def test_mock_multi_index_data():
    """Test the mock_multi_index_data function."""
    mi_data = mock_multi_index_data()
    assert isinstance(mi_data, pd.DataFrame)
    assert mi_data.index.nlevels == 2

```



---

## High-Level Overview

This is a **python** file named `test_econometrics_utils.py`.

**Python Module**

- **Functions** (2): test_get_engle_granger_two_step_cointegration_test, test_mock_multi_index_data
- **Import Statements**: 1


---

## Detailed Analysis

### Python Code Structure


#### Functions

- **`test_get_engle_granger_two_step_cointegration_test()`**
- **`test_mock_multi_index_data()`**


---

## Related Files

The following files may be related based on imports and references:

**Imported Modules**:
- `numpy`
- `openbb_econometrics.utils`
- `pandas`


---

## Performance & Security Notes

No obvious security concerns detected in static analysis.


---

**Generated**: 2025-11-19T02:16:46.880234Z
**Generator**: World's Best Repo Book Generator v1.0

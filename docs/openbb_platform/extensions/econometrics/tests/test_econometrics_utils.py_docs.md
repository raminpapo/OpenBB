# Documentation: openbb_platform/extensions/econometrics/tests/test_econometrics_utils.py

## File Metadata
- **Path**: `openbb_platform/extensions/econometrics/tests/test_econometrics_utils.py`
- **Size**: 710 characters, 26 lines
- **Words**: 54
- **Extension**: .py
- **Classification**: Text file

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

## High-Level Overview

Test the econometrics utils module.

import numpy as np
import pandas as pd
from openbb_econometrics.utils import (
get_engle_granger_two_step_cointegration_test,
mock_multi_index_data,
)


def test_get_engle_granger_two_step_cointegration_test():
Test the get_engle_granger_two_step_cointegration_test function.
Test the mock_multi_index_data function.
mi_data = mock_multi_index_data()
assert isinstance(mi_data, pd.DataFrame)
assert mi_data.index.nlevels == 2


## Detailed Structure

### Python File Structure

**Classes** (0):
None

**Functions** (2):
`test_get_engle_granger_two_step_cointegration_test`, `test_mock_multi_index_data`

**Imports** (3):
`numpy`, `pandas`, `openbb_econometrics.utils`


## Key Components

No major components extracted.

## Usage & Examples

See source code for usage details.

## Related Files

- `numpy`
- `pandas`
- `openbb_econometrics.utils`

## Notes
- Generated: 2025-11-18T07:54:36.023441
- Generator: World's Best Repo Book Generator v1.0.0

# File Documentation: test_charting_core_ta_helpers.py

## Metadata
- **Path**: `openbb_platform/obbject_extensions/charting/tests/test_charting_core_ta_helpers.py`
- **Size**: 754 bytes
- **Lines**: 35
- **Category**: python
- **Extension**: .py

---

## Original Source

```python
"""Test the charting core ta helpers."""

import pandas as pd
import pytest
from openbb_charting.core.plotly_ta.ta_helpers import (
    check_columns,
)


def test_check_columns():
    """Test check_columns."""
    data = pd.DataFrame(
        {
            "open": [1, 2, 3, 4, 5],
            "high": [1, 2, 3, 4, 5],
            "low": [1, 2, 3, 4, 5],
            "close": [1, 2, 3, 4, 5],
            "volume": [1, 2, 3, 4, 5],
        }
    )
    result = check_columns(data)
    assert result


def test_check_columns_fail():
    """Test check_columns."""
    data = pd.DataFrame(
        {
            "open": [1, 2, 3, 4, 5],
            "volume": [1, 2, 3, 4, 5],
        }
    )
    with pytest.raises(IndexError):
        check_columns(data)

```



---

## High-Level Overview

This is a **python** file named `test_charting_core_ta_helpers.py`.

**Python Module**

- **Functions** (2): test_check_columns, test_check_columns_fail
- **Import Statements**: 1


---

## Detailed Analysis

### Python Code Structure


#### Functions

- **`test_check_columns()`**
- **`test_check_columns_fail()`**


---

## Related Files

The following files may be related based on imports and references:

**Imported Modules**:
- `openbb_charting.core.plotly_ta.ta_helpers`
- `pandas`
- `pytest`


---

## Performance & Security Notes

No obvious security concerns detected in static analysis.


---

**Generated**: 2025-11-19T02:16:48.227914Z
**Generator**: World's Best Repo Book Generator v1.0

# File Documentation: test_errors.py

## Metadata
- **Path**: `openbb_platform/core/tests/provider/utils/test_errors.py`
- **Size**: 1,266 bytes
- **Lines**: 40
- **Category**: python
- **Extension**: .py

---

## Original Source

```python
"""Test custom errors."""

import pytest
from openbb_core.app.model.abstract.error import OpenBBError
from openbb_core.provider.utils.errors import EmptyDataError


def function_that_raises_provider_error():
    """Raise a OpenBBError."""
    raise OpenBBError("An error occurred in the provider.")


def function_that_raises_empty_data_error():
    """Raise an EmptyDataError."""
    raise EmptyDataError()


def test_provider_error_is_raised():
    """Test if the OpenBBError is raised."""
    with pytest.raises(OpenBBError) as exc_info:
        function_that_raises_provider_error()
    assert str(exc_info.value) == "An error occurred in the provider."


def test_empty_data_error_is_raised():
    """Test if the EmptyDataError is raised."""
    with pytest.raises(EmptyDataError) as exc_info:
        function_that_raises_empty_data_error()
    assert (
        str(exc_info.value) == "No results found. Try adjusting the query parameters."
    )


def test_empty_data_error_custom_message():
    """Test if the EmptyDataError is raised with a custom message."""
    custom_message = "Custom message for no data."
    with pytest.raises(EmptyDataError) as exc_info:
        raise EmptyDataError(custom_message)
    assert str(exc_info.value) == custom_message

```



---

## High-Level Overview

This is a **python** file named `test_errors.py`.

**Python Module**

- **Functions** (5): function_that_raises_provider_error, function_that_raises_empty_data_error, test_provider_error_is_raised, test_empty_data_error_is_raised, test_empty_data_error_custom_message
- **Import Statements**: 1


---

## Detailed Analysis

### Python Code Structure


#### Functions

- **`function_that_raises_provider_error()`**
- **`function_that_raises_empty_data_error()`**
- **`test_provider_error_is_raised()`**
- **`test_empty_data_error_is_raised()`**
- **`test_empty_data_error_custom_message()`**


---

## Related Files

The following files may be related based on imports and references:

**Imported Modules**:
- `EmptyDataError`
- `OpenBBError`
- `openbb_core.app.model.abstract.error`
- `openbb_core.provider.utils.errors`
- `pytest`


---

## Performance & Security Notes

No obvious security concerns detected in static analysis.


---

**Generated**: 2025-11-19T02:16:46.721226Z
**Generator**: World's Best Repo Book Generator v1.0

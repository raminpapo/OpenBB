# File Documentation: test_data.py

## Metadata
- **Path**: `openbb_platform/core/tests/provider/abstract/test_data.py`
- **Size**: 1,313 bytes
- **Lines**: 44
- **Category**: python
- **Extension**: .py

---

## Original Source

```python
"""Test the Data."""

# pylint: disable=C2801

import pytest
from openbb_core.provider.abstract.data import Data, check_int


def test_check_int_valid():
    """Test if the check_int function returns the value when it is an int."""
    assert check_int(10) == 10


def test_check_int_invalid():
    """Test if the check_int function raises an error when the value is not an int."""
    with pytest.raises(TypeError):
        check_int("not_an_integer")  # type: ignore[arg-type]


def test_data_model():
    """Test the Data model."""
    some_data = Data(test="test")  # type: ignore[call-arg]

    assert some_data.test == "test"  # type: ignore[attr-defined]
    assert not some_data.__alias_dict__
    assert some_data.__repr__() == "Data(test=test)"
    assert some_data.model_dump() == {"test": "test"}


def test_data_model_alias():
    """Test the Data model with an alias."""

    class SomeData(Data):
        """Some data."""

        __alias_dict__ = {"test_alias": "test"}

    some_data = SomeData(test="Hello")  # type: ignore[call-arg]

    assert some_data.__alias_dict__ == {"test_alias": "test"}
    assert some_data.__repr__() == "SomeData(test_alias=Hello)"
    assert some_data.model_dump() == {"test_alias": "Hello"}
    assert some_data.test_alias == "Hello"  # type: ignore[attr-defined]

```



---

## High-Level Overview

This is a **python** file named `test_data.py`.

**Python Module**

- **Classes** (1): SomeData
- **Functions** (4): test_check_int_valid, test_check_int_invalid, test_data_model, test_data_model_alias
- **Import Statements**: 1


---

## Detailed Analysis

### Python Code Structure

#### Classes

- **`SomeData`**(Data)

#### Functions

- **`test_check_int_valid()`**
- **`test_check_int_invalid()`**
- **`test_data_model()`**
- **`test_data_model_alias()`**


---

## Related Files

The following files may be related based on imports and references:

**Imported Modules**:
- `Data`
- `openbb_core.provider.abstract.data`
- `pytest`


---

## Performance & Security Notes

No obvious security concerns detected in static analysis.


---

**Generated**: 2025-11-19T02:16:46.711507Z
**Generator**: World's Best Repo Book Generator v1.0

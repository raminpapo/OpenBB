# Documentation: openbb_platform/core/tests/provider/abstract/test_data.py

## File Metadata
- **Path**: `openbb_platform/core/tests/provider/abstract/test_data.py`
- **Size**: 1,313 characters, 44 lines
- **Words**: 130
- **Extension**: .py
- **Classification**: Text file

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

## High-Level Overview

Test the Data.

# pylint: disable=C2801

import pytest
from openbb_core.provider.abstract.data import Data, check_int


def test_check_int_valid():
Test if the check_int function returns the value when it is an int.
Test if the check_int function raises an error when the value is not an int.
with pytest.raises(TypeError):
check_int("not_an_integer")  # type: ignore[arg-type]


def test_data_model():
Test the Data model.
Test the Data model with an alias.

class SomeData(Data):

## Detailed Structure

### Python File Structure

**Classes** (1):
`SomeData`

**Functions** (4):
`test_check_int_valid`, `test_check_int_invalid`, `test_data_model`, `test_data_model_alias`

**Imports** (3):
`pytest`, `openbb_core.provider.abstract.data`, `Data`


## Key Components

**Class `SomeData`**: Some data.

## Usage & Examples

See source code for usage details.

## Related Files

- `pytest`
- `openbb_core.provider.abstract.data`

## Notes
- Generated: 2025-11-18T07:54:35.875681
- Generator: World's Best Repo Book Generator v1.0.0

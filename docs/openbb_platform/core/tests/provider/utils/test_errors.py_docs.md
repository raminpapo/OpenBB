# Documentation: openbb_platform/core/tests/provider/utils/test_errors.py

## File Metadata
- **Path**: `openbb_platform/core/tests/provider/utils/test_errors.py`
- **Size**: 1,266 characters, 40 lines
- **Words**: 109
- **Extension**: .py
- **Classification**: Text file

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

## High-Level Overview

Test custom errors.

import pytest
from openbb_core.app.model.abstract.error import OpenBBError
from openbb_core.provider.utils.errors import EmptyDataError


def function_that_raises_provider_error():
Raise a OpenBBError.
Raise an EmptyDataError.
raise EmptyDataError()


def test_provider_error_is_raised():
Test if the OpenBBError is raised.
Test if the EmptyDataError is raised.
with pytest.raises(EmptyDataError) as exc_info:
function_that_raises_empty_data_error()
assert (
str(exc_info.value) == "No results found. Try adjusting the query parameters."

## Detailed Structure

### Python File Structure

**Classes** (0):
None

**Functions** (5):
`function_that_raises_provider_error`, `function_that_raises_empty_data_error`, `test_provider_error_is_raised`, `test_empty_data_error_is_raised`, `test_empty_data_error_custom_message`

**Imports** (5):
`pytest`, `openbb_core.app.model.abstract.error`, `OpenBBError`, `openbb_core.provider.utils.errors`, `EmptyDataError`


## Key Components

No major components extracted.

## Usage & Examples

See source code for usage details.

## Related Files

- `pytest`
- `openbb_core.app.model.abstract.error`
- `openbb_core.provider.utils.errors`

## Notes
- Generated: 2025-11-18T07:54:35.888603
- Generator: World's Best Repo Book Generator v1.0.0

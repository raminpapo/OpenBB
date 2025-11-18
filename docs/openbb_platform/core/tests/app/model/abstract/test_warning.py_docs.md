# Documentation: openbb_platform/core/tests/app/model/abstract/test_warning.py

## File Metadata
- **Path**: `openbb_platform/core/tests/app/model/abstract/test_warning.py`
- **Size**: 995 characters, 42 lines
- **Words**: 90
- **Extension**: .py
- **Classification**: Text file

## Original Source

```python
"""Test the Warnings model."""

from unittest.mock import Mock

import pytest
from openbb_core.app.model.abstract.warning import Warning_, cast_warning


@pytest.mark.parametrize(
    "category, message",
    [
        ("test", "test"),
        ("test2", "test2"),
    ],
)
def test_warn_model(category, message):
    """Test the Warning_ model."""
    war = Warning_(category=category, message=message)

    assert war.category == category
    assert war.message == message


def test_fields():
    """Test the Warning_ fields."""
    fields = Warning_.model_fields
    fields_keys = fields.keys()

    assert "category" in fields_keys
    assert "message" in fields_keys


def test_cast_warning():
    """Test the cast_warning function."""
    mock_warning_message = Mock()
    mock_warning_message.category.__name__ = "test"
    mock_warning_message.message = "test"
    warning = cast_warning(mock_warning_message)

    assert warning.category == "test"
    assert warning.message == "test"

```

## High-Level Overview

Test the Warnings model.

from unittest.mock import Mock

import pytest
from openbb_core.app.model.abstract.warning import Warning_, cast_warning


@pytest.mark.parametrize(
"category, message",
[
("test", "test"),
("test2", "test2"),
],
)
def test_warn_model(category, message):
Test the Warning_ model.
Test the Warning_ fields.
fields = Warning_.model_fields
fields_keys = fields.keys()

## Detailed Structure

### Python File Structure

**Classes** (0):
None

**Functions** (3):
`test_warn_model`, `test_fields`, `test_cast_warning`

**Imports** (5):
`unittest.mock`, `Mock`, `pytest`, `openbb_core.app.model.abstract.warning`, `Warning_`


## Key Components

No major components extracted.

## Usage & Examples

See source code for usage details.

## Related Files

- `unittest.mock`
- `pytest`
- `openbb_core.app.model.abstract.warning`

## Notes
- Generated: 2025-11-18T07:54:35.828326
- Generator: World's Best Repo Book Generator v1.0.0

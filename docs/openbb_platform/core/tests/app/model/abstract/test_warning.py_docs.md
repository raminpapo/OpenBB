# File Documentation: test_warning.py

## Metadata
- **Path**: `openbb_platform/core/tests/app/model/abstract/test_warning.py`
- **Size**: 995 bytes
- **Lines**: 42
- **Category**: python
- **Extension**: .py

---

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



---

## High-Level Overview

This is a **python** file named `test_warning.py`.

**Python Module**

- **Functions** (3): test_warn_model, test_fields, test_cast_warning
- **Import Statements**: 1


---

## Detailed Analysis

### Python Code Structure


#### Functions

- **`test_warn_model(category, message)`**
- **`test_fields()`**
- **`test_cast_warning()`**

#### Decorators Used

pytest


---

## Related Files

The following files may be related based on imports and references:

**Imported Modules**:
- `Mock`
- `Warning_`
- `openbb_core.app.model.abstract.warning`
- `pytest`
- `unittest.mock`


---

## Performance & Security Notes

No obvious security concerns detected in static analysis.


---

**Generated**: 2025-11-19T02:16:46.683922Z
**Generator**: World's Best Repo Book Generator v1.0

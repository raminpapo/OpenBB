# File Documentation: test_command_context.py

## Metadata
- **Path**: `openbb_platform/core/tests/app/model/test_command_context.py`
- **Size**: 624 bytes
- **Lines**: 25
- **Category**: python
- **Extension**: .py

---

## Original Source

```python
"""Test the CommandContext model."""

from openbb_core.app.model.command_context import (
    CommandContext,
    SystemSettings,
    UserSettings,
)


def test_command_context():
    """Test the CommandContext model."""
    cc = CommandContext()
    assert isinstance(cc, CommandContext)
    assert isinstance(cc.user_settings, UserSettings)
    assert isinstance(cc.system_settings, SystemSettings)


def test_fields():
    """Test the CommandContext fields."""
    fields = CommandContext.model_fields
    fields_keys = fields.keys()

    assert "user_settings" in fields_keys
    assert "system_settings" in fields_keys

```



---

## High-Level Overview

This is a **python** file named `test_command_context.py`.

**Python Module**

- **Functions** (2): test_command_context, test_fields


---

## Detailed Analysis

### Python Code Structure


#### Functions

- **`test_command_context()`**
- **`test_fields()`**


---

## Related Files

The following files may be related based on imports and references:

**Imported Modules**:
- `openbb_core.app.model.command_context`


---

## Performance & Security Notes

No obvious security concerns detected in static analysis.


---

**Generated**: 2025-11-19T02:16:46.664656Z
**Generator**: World's Best Repo Book Generator v1.0

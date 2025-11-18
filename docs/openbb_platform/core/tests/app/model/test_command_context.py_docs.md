# Documentation: openbb_platform/core/tests/app/model/test_command_context.py

## File Metadata
- **Path**: `openbb_platform/core/tests/app/model/test_command_context.py`
- **Size**: 624 characters, 25 lines
- **Words**: 50
- **Extension**: .py
- **Classification**: Text file

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

## High-Level Overview

Test the CommandContext model.

from openbb_core.app.model.command_context import (
CommandContext,
SystemSettings,
UserSettings,
)


def test_command_context():
Test the CommandContext model.
Test the CommandContext fields.
fields = CommandContext.model_fields
fields_keys = fields.keys()

assert "user_settings" in fields_keys
assert "system_settings" in fields_keys


## Detailed Structure

### Python File Structure

**Classes** (0):
None

**Functions** (2):
`test_command_context`, `test_fields`

**Imports** (1):
`openbb_core.app.model.command_context`


## Key Components

No major components extracted.

## Usage & Examples

See source code for usage details.

## Related Files

- `openbb_core.app.model.command_context`

## Notes
- Generated: 2025-11-18T07:54:35.831843
- Generator: World's Best Repo Book Generator v1.0.0

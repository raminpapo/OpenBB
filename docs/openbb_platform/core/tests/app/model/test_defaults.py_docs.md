# Documentation: openbb_platform/core/tests/app/model/test_defaults.py

## File Metadata
- **Path**: `openbb_platform/core/tests/app/model/test_defaults.py`
- **Size**: 417 characters, 16 lines
- **Words**: 38
- **Extension**: .py
- **Classification**: Text file

## Original Source

```python
"""Test the Defaults class."""

from openbb_core.app.model.defaults import Defaults


def test_defaults():
    """Test the Defaults class."""
    cc = Defaults(commands={"/equity/price": {"provider": "test"}})
    assert isinstance(cc, Defaults)
    assert cc.commands == {"equity.price": {"provider": ["test"]}}


def test_fields():
    """Test the Defaults fields."""
    assert "commands" in Defaults.model_fields

```

## High-Level Overview

Test the Defaults class.

from openbb_core.app.model.defaults import Defaults


def test_defaults():
Test the Defaults class.
Test the Defaults fields.
assert "commands" in Defaults.model_fields


## Detailed Structure

### Python File Structure

**Classes** (0):
None

**Functions** (2):
`test_defaults`, `test_fields`

**Imports** (2):
`openbb_core.app.model.defaults`, `Defaults`


## Key Components

No major components extracted.

## Usage & Examples

See source code for usage details.

## Related Files

- `openbb_core.app.model.defaults`

## Notes
- Generated: 2025-11-18T07:54:35.834632
- Generator: World's Best Repo Book Generator v1.0.0

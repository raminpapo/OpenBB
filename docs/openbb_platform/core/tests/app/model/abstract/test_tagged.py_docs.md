# Documentation: openbb_platform/core/tests/app/model/abstract/test_tagged.py

## File Metadata
- **Path**: `openbb_platform/core/tests/app/model/abstract/test_tagged.py`
- **Size**: 355 characters, 19 lines
- **Words**: 36
- **Extension**: .py
- **Classification**: Text file

## Original Source

```python
"""Test the Tagged model."""

from openbb_core.app.model.abstract.tagged import Tagged


def test_tagged_model():
    """Test the Tagged model."""
    tagged = Tagged()

    assert hasattr(tagged, "id")


def test_fields():
    """Test the Tagged fields."""
    fields = Tagged.model_fields
    fields_keys = fields.keys()

    assert "id" in fields_keys

```

## High-Level Overview

Test the Tagged model.

from openbb_core.app.model.abstract.tagged import Tagged


def test_tagged_model():
Test the Tagged model.
Test the Tagged fields.
fields = Tagged.model_fields
fields_keys = fields.keys()

assert "id" in fields_keys


## Detailed Structure

### Python File Structure

**Classes** (0):
None

**Functions** (2):
`test_tagged_model`, `test_fields`

**Imports** (2):
`openbb_core.app.model.abstract.tagged`, `Tagged`


## Key Components

No major components extracted.

## Usage & Examples

See source code for usage details.

## Related Files

- `openbb_core.app.model.abstract.tagged`

## Notes
- Generated: 2025-11-18T07:54:35.826819
- Generator: World's Best Repo Book Generator v1.0.0

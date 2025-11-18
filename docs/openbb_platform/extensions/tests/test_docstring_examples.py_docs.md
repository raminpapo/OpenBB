# Documentation: openbb_platform/extensions/tests/test_docstring_examples.py

## File Metadata
- **Path**: `openbb_platform/extensions/tests/test_docstring_examples.py`
- **Size**: 292 characters, 13 lines
- **Words**: 26
- **Extension**: .py
- **Classification**: Text file

## Original Source

```python
"""Test utils."""

import pytest

from .utils.helpers import check_docstring_examples


@pytest.mark.integration
def test_docstring_examples():
    """Test that the docstring examples execute without errors."""
    errors = check_docstring_examples()
    assert not errors, "\n".join(errors)

```

## High-Level Overview

Test utils.

import pytest

from .utils.helpers import check_docstring_examples


@pytest.mark.integration
def test_docstring_examples():
Test that the docstring examples execute without errors.

## Detailed Structure

### Python File Structure

**Classes** (0):
None

**Functions** (1):
`test_docstring_examples`

**Imports** (3):
`pytest`, `.utils.helpers`, `check_docstring_examples`


## Key Components

No major components extracted.

## Usage & Examples

See source code for usage details.

## Related Files

- `pytest`
- `.utils.helpers`

## Notes
- Generated: 2025-11-18T07:54:36.391949
- Generator: World's Best Repo Book Generator v1.0.0

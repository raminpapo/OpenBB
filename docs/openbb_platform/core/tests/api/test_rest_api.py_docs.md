# Documentation: openbb_platform/core/tests/api/test_rest_api.py

## File Metadata
- **Path**: `openbb_platform/core/tests/api/test_rest_api.py`
- **Size**: 155 characters, 9 lines
- **Words**: 14
- **Extension**: .py
- **Classification**: Text file

## Original Source

```python
"""Test rest_api.py."""

from openbb_core.api.rest_api import app


def test_openapi():
    """Test openapi schema generation."""
    assert app.openapi()

```

## High-Level Overview

Test rest_api.py.

from openbb_core.api.rest_api import app


def test_openapi():
Test openapi schema generation.

## Detailed Structure

### Python File Structure

**Classes** (0):
None

**Functions** (1):
`test_openapi`

**Imports** (2):
`openbb_core.api.rest_api`, `app`


## Key Components

No major components extracted.

## Usage & Examples

See source code for usage details.

## Related Files

- `openbb_core.api.rest_api`

## Notes
- Generated: 2025-11-18T07:54:35.794981
- Generator: World's Best Repo Book Generator v1.0.0

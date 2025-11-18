# Documentation: openbb_platform/core/tests/provider/utils/test_descriptions.py

## File Metadata
- **Path**: `openbb_platform/core/tests/provider/utils/test_descriptions.py`
- **Size**: 343 characters, 17 lines
- **Words**: 27
- **Extension**: .py
- **Classification**: Text file

## Original Source

```python
"""Test the provider descriptions."""

from openbb_core.provider.utils.descriptions import (
    DATA_DESCRIPTIONS,
    QUERY_DESCRIPTIONS,
)


def test_query_descriptions():
    """Test the query descriptions."""
    assert QUERY_DESCRIPTIONS


def test_data_descriptions():
    """Test the data descriptions."""
    assert DATA_DESCRIPTIONS

```

## High-Level Overview

Test the provider descriptions.

from openbb_core.provider.utils.descriptions import (
DATA_DESCRIPTIONS,
QUERY_DESCRIPTIONS,
)


def test_query_descriptions():
Test the query descriptions.
Test the data descriptions.
assert DATA_DESCRIPTIONS


## Detailed Structure

### Python File Structure

**Classes** (0):
None

**Functions** (2):
`test_query_descriptions`, `test_data_descriptions`

**Imports** (1):
`openbb_core.provider.utils.descriptions`


## Key Components

No major components extracted.

## Usage & Examples

See source code for usage details.

## Related Files

- `openbb_core.provider.utils.descriptions`

## Notes
- Generated: 2025-11-18T07:54:35.887199
- Generator: World's Best Repo Book Generator v1.0.0

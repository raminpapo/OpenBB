# Documentation: openbb_platform/extensions/quantitative/tests/test_quantitative_helpers.py

## File Metadata
- **Path**: `openbb_platform/extensions/quantitative/tests/test_quantitative_helpers.py`
- **Size**: 341 characters, 16 lines
- **Words**: 28
- **Extension**: .py
- **Classification**: Text file

## Original Source

```python
"""Test the quantitative helpers."""

import pandas as pd
from extensions.quantitative.openbb_quantitative.helpers import (
    validate_window,
)


def test_validate_window():
    """Test the validate_window function."""
    input_data = pd.Series(range(1, 100))
    validate_window(
        input_data=input_data,
        window=20,
    )

```

## High-Level Overview

Test the quantitative helpers.

import pandas as pd
from extensions.quantitative.openbb_quantitative.helpers import (
validate_window,
)


def test_validate_window():
Test the validate_window function.

## Detailed Structure

### Python File Structure

**Classes** (0):
None

**Functions** (1):
`test_validate_window`

**Imports** (2):
`pandas`, `extensions.quantitative.openbb_quantitative.helpers`


## Key Components

No major components extracted.

## Usage & Examples

See source code for usage details.

## Related Files

- `pandas`
- `extensions.quantitative.openbb_quantitative.helpers`

## Notes
- Generated: 2025-11-18T07:54:36.334604
- Generator: World's Best Repo Book Generator v1.0.0

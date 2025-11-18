# Documentation: openbb_platform/core/tests/app/model/abstract/test_results.py

## File Metadata
- **Path**: `openbb_platform/core/tests/app/model/abstract/test_results.py`
- **Size**: 311 characters, 16 lines
- **Words**: 30
- **Extension**: .py
- **Classification**: Text file

## Original Source

```python
"""Tests for the Results model."""

from openbb_core.app.model.abstract.results import Results
from pydantic import BaseModel


class MockResults(Results):
    """Mock Results class."""


def test_results_model():
    """Test the Results model."""
    res = MockResults()

    assert isinstance(res, BaseModel)

```

## High-Level Overview

Tests for the Results model.

from openbb_core.app.model.abstract.results import Results
from pydantic import BaseModel


class MockResults(Results):
Mock Results class.
Test the Results model.
res = MockResults()

assert isinstance(res, BaseModel)


## Detailed Structure

### Python File Structure

**Classes** (1):
`MockResults`

**Functions** (1):
`test_results_model`

**Imports** (4):
`openbb_core.app.model.abstract.results`, `Results`, `pydantic`, `BaseModel`


## Key Components

**Class `MockResults`**: Mock Results class.

## Usage & Examples

See source code for usage details.

## Related Files

- `openbb_core.app.model.abstract.results`
- `pydantic`

## Notes
- Generated: 2025-11-18T07:54:35.823678
- Generator: World's Best Repo Book Generator v1.0.0

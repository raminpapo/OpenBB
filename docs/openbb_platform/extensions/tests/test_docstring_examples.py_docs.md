# File Documentation: test_docstring_examples.py

## Metadata
- **Path**: `openbb_platform/extensions/tests/test_docstring_examples.py`
- **Size**: 292 bytes
- **Lines**: 13
- **Category**: python
- **Extension**: .py

---

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



---

## High-Level Overview

This is a **python** file named `test_docstring_examples.py`.

**Python Module**

- **Functions** (1): test_docstring_examples
- **Import Statements**: 1


---

## Detailed Analysis

### Python Code Structure


#### Functions

- **`test_docstring_examples()`**

#### Decorators Used

pytest


---

## Related Files

The following files may be related based on imports and references:

**Imported Modules**:
- `.utils.helpers`
- `check_docstring_examples`
- `pytest`


---

## Performance & Security Notes

No obvious security concerns detected in static analysis.


---

**Generated**: 2025-11-19T02:16:47.346217Z
**Generator**: World's Best Repo Book Generator v1.0

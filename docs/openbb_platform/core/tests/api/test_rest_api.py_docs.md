# File Documentation: test_rest_api.py

## Metadata
- **Path**: `openbb_platform/core/tests/api/test_rest_api.py`
- **Size**: 155 bytes
- **Lines**: 9
- **Category**: python
- **Extension**: .py

---

## Original Source

```python
"""Test rest_api.py."""

from openbb_core.api.rest_api import app


def test_openapi():
    """Test openapi schema generation."""
    assert app.openapi()

```



---

## High-Level Overview

This is a **python** file named `test_rest_api.py`.

**Python Module**

- **Functions** (1): test_openapi
- **Import Statements**: 1


---

## Detailed Analysis

### Python Code Structure


#### Functions

- **`test_openapi()`**


---

## Related Files

The following files may be related based on imports and references:

**Imported Modules**:
- `app`
- `openbb_core.api.rest_api`


---

## Performance & Security Notes

No obvious security concerns detected in static analysis.


---

**Generated**: 2025-11-19T02:16:46.621045Z
**Generator**: World's Best Repo Book Generator v1.0

# File Documentation: test_router_system.py

## Metadata
- **Path**: `openbb_platform/core/tests/api/test_router/test_router_system.py`
- **Size**: 484 bytes
- **Lines**: 17
- **Category**: python
- **Extension**: .py

---

## Original Source

```python
"""Test the router system module."""

from unittest.mock import patch

from openbb_core.api.router.system import get_system_model
from openbb_core.app.model.system_settings import SystemSettings


@patch("openbb_core.api.router.system.get_system_settings")
def test_get_system_model(mock_get_system_settings):
    """Test get system model."""
    mock_get_system_settings.return_value = SystemSettings()

    response = get_system_model(mock_get_system_settings)

    assert response

```



---

## High-Level Overview

This is a **python** file named `test_router_system.py`.

**Python Module**

- **Functions** (1): test_get_system_model
- **Import Statements**: 1


---

## Detailed Analysis

### Python Code Structure


#### Functions

- **`test_get_system_model(mock_get_system_settings)`**

#### Decorators Used

patch


---

## Related Files

The following files may be related based on imports and references:

**Imported Modules**:
- `SystemSettings`
- `get_system_model`
- `openbb_core.api.router.system`
- `openbb_core.app.model.system_settings`
- `patch`
- `unittest.mock`


---

## Performance & Security Notes

No obvious security concerns detected in static analysis.


---

**Generated**: 2025-11-19T02:16:46.629296Z
**Generator**: World's Best Repo Book Generator v1.0

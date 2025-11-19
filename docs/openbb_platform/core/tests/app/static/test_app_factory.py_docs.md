# File Documentation: test_app_factory.py

## Metadata
- **Path**: `openbb_platform/core/tests/app/static/test_app_factory.py`
- **Size**: 1,254 bytes
- **Lines**: 49
- **Category**: python
- **Extension**: .py

---

## Original Source

```python
"""Test static app factory."""

# pylint: disable=redefined-outer-name

import pytest
from openbb_core.app.model.system_settings import SystemSettings
from openbb_core.app.model.user_settings import UserSettings
from openbb_core.app.static.app_factory import create_app
from openbb_core.app.static.coverage import Coverage


@pytest.fixture(scope="module")
def app_factory():
    """Return app factory."""
    return create_app()


def test_app_factory_init(app_factory):
    """Test app factory init."""
    assert app_factory


def test_app_system_settings(app_factory):
    """Test app system settings."""
    system_settings = app_factory.system
    assert system_settings
    assert isinstance(system_settings, SystemSettings)


def test_app_user_settings(app_factory):
    """Test app user settings."""
    user_settings = app_factory.user
    assert user_settings
    assert isinstance(user_settings, UserSettings)


def test_app_coverage(app_factory):
    """Test app coverage."""
    coverage = app_factory.coverage
    assert coverage
    assert isinstance(coverage, Coverage)


def test_app_reference(app_factory):
    """Test app reference."""
    reference = app_factory.reference
    assert reference
    assert isinstance(reference, dict)

```



---

## High-Level Overview

This is a **python** file named `test_app_factory.py`.

**Python Module**

- **Functions** (6): app_factory, test_app_factory_init, test_app_system_settings, test_app_user_settings, test_app_coverage, test_app_reference
- **Import Statements**: 1


---

## Detailed Analysis

### Python Code Structure


#### Functions

- **`app_factory()`**
- **`test_app_factory_init(app_factory)`**
- **`test_app_system_settings(app_factory)`**
- **`test_app_user_settings(app_factory)`**
- **`test_app_coverage(app_factory)`**
- **`test_app_reference(app_factory)`**

#### Decorators Used

pytest


---

## Related Files

The following files may be related based on imports and references:

**Imported Modules**:
- `Coverage`
- `SystemSettings`
- `UserSettings`
- `create_app`
- `openbb_core.app.model.system_settings`
- `openbb_core.app.model.user_settings`
- `openbb_core.app.static.app_factory`
- `openbb_core.app.static.coverage`
- `pytest`


---

## Performance & Security Notes

No obvious security concerns detected in static analysis.


---

**Generated**: 2025-11-19T02:16:46.694880Z
**Generator**: World's Best Repo Book Generator v1.0

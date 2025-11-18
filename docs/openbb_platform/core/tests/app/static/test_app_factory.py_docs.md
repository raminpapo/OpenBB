# Documentation: openbb_platform/core/tests/app/static/test_app_factory.py

## File Metadata
- **Path**: `openbb_platform/core/tests/app/static/test_app_factory.py`
- **Size**: 1,254 characters, 49 lines
- **Words**: 95
- **Extension**: .py
- **Classification**: Text file

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

## High-Level Overview

Test static app factory.

# pylint: disable=redefined-outer-name

import pytest
from openbb_core.app.model.system_settings import SystemSettings
from openbb_core.app.model.user_settings import UserSettings
from openbb_core.app.static.app_factory import create_app
from openbb_core.app.static.coverage import Coverage


@pytest.fixture(scope="module")
def app_factory():
Return app factory.
Test app factory init.
assert app_factory


def test_app_system_settings(app_factory):
Test app system settings.

## Detailed Structure

### Python File Structure

**Classes** (0):
None

**Functions** (6):
`app_factory`, `test_app_factory_init`, `test_app_system_settings`, `test_app_user_settings`, `test_app_coverage`, `test_app_reference`

**Imports** (9):
`pytest`, `openbb_core.app.model.system_settings`, `SystemSettings`, `openbb_core.app.model.user_settings`, `UserSettings`, `openbb_core.app.static.app_factory`, `create_app`, `openbb_core.app.static.coverage`, `Coverage`


## Key Components

No major components extracted.

## Usage & Examples

See source code for usage details.

## Related Files

- `pytest`
- `openbb_core.app.model.system_settings`
- `openbb_core.app.model.user_settings`
- `openbb_core.app.static.app_factory`
- `openbb_core.app.static.coverage`

## Notes
- Generated: 2025-11-18T07:54:35.853477
- Generator: World's Best Repo Book Generator v1.0.0

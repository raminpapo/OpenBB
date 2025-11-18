# Documentation: openbb_platform/core/tests/api/test_router/test_router_system.py

## File Metadata
- **Path**: `openbb_platform/core/tests/api/test_router/test_router_system.py`
- **Size**: 484 characters, 17 lines
- **Words**: 32
- **Extension**: .py
- **Classification**: Text file

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

## High-Level Overview

Test the router system module.

from unittest.mock import patch

from openbb_core.api.router.system import get_system_model
from openbb_core.app.model.system_settings import SystemSettings


@patch("openbb_core.api.router.system.get_system_settings")
def test_get_system_model(mock_get_system_settings):
Test get system model.

## Detailed Structure

### Python File Structure

**Classes** (0):
None

**Functions** (1):
`test_get_system_model`

**Imports** (6):
`unittest.mock`, `patch`, `openbb_core.api.router.system`, `get_system_model`, `openbb_core.app.model.system_settings`, `SystemSettings`


## Key Components

No major components extracted.

## Usage & Examples

See source code for usage details.

## Related Files

- `unittest.mock`
- `openbb_core.api.router.system`
- `openbb_core.app.model.system_settings`

## Notes
- Generated: 2025-11-18T07:54:35.798632
- Generator: World's Best Repo Book Generator v1.0.0

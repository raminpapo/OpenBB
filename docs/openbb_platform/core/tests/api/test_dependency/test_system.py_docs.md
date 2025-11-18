# Documentation: openbb_platform/core/tests/api/test_dependency/test_system.py

## File Metadata
- **Path**: `openbb_platform/core/tests/api/test_dependency/test_system.py`
- **Size**: 534 characters, 20 lines
- **Words**: 35
- **Extension**: .py
- **Classification**: Text file

## Original Source

```python
"""Test the system module."""

import asyncio
from unittest.mock import MagicMock, patch

from openbb_core.api.dependency.system import (
    SystemSettings,
    get_system_settings,
)


@patch("openbb_core.api.dependency.system.SystemService")
def test_get_system_settings(mock_system_service):
    """Test get_system_settings."""
    mock_system_service.return_value.system_settings = SystemSettings()

    response = asyncio.run(get_system_settings(MagicMock(), mock_system_service))  # type: ignore[arg-type]

    assert response

```

## High-Level Overview

Test the system module.

import asyncio
from unittest.mock import MagicMock, patch

from openbb_core.api.dependency.system import (
SystemSettings,
get_system_settings,
)


@patch("openbb_core.api.dependency.system.SystemService")
def test_get_system_settings(mock_system_service):
Test get_system_settings.

## Detailed Structure

### Python File Structure

**Classes** (0):
None

**Functions** (1):
`test_get_system_settings`

**Imports** (4):
`asyncio`, `unittest.mock`, `MagicMock`, `openbb_core.api.dependency.system`


## Key Components

No major components extracted.

## Usage & Examples

See source code for usage details.

## Related Files

- `asyncio`
- `unittest.mock`
- `openbb_core.api.dependency.system`

## Notes
- Generated: 2025-11-18T07:54:35.793794
- Generator: World's Best Repo Book Generator v1.0.0

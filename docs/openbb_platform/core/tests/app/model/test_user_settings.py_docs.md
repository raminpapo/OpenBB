# Documentation: openbb_platform/core/tests/app/model/test_user_settings.py

## File Metadata
- **Path**: `openbb_platform/core/tests/app/model/test_user_settings.py`
- **Size**: 512 characters, 17 lines
- **Words**: 36
- **Extension**: .py
- **Classification**: Text file

## Original Source

```python
"""Test the UserSettings model."""

from openbb_core.app.model.credentials import Credentials
from openbb_core.app.model.defaults import Defaults
from openbb_core.app.model.preferences import Preferences
from openbb_core.app.model.user_settings import UserSettings


def test_user_settings():
    """Test the UserSettings model."""
    settings = UserSettings(
        credentials=Credentials(),
        preferences=Preferences(),
        defaults=Defaults(),
    )
    assert isinstance(settings, UserSettings)

```

## High-Level Overview

Test the UserSettings model.

from openbb_core.app.model.credentials import Credentials
from openbb_core.app.model.defaults import Defaults
from openbb_core.app.model.preferences import Preferences
from openbb_core.app.model.user_settings import UserSettings


def test_user_settings():
Test the UserSettings model.

## Detailed Structure

### Python File Structure

**Classes** (0):
None

**Functions** (1):
`test_user_settings`

**Imports** (8):
`openbb_core.app.model.credentials`, `Credentials`, `openbb_core.app.model.defaults`, `Defaults`, `openbb_core.app.model.preferences`, `Preferences`, `openbb_core.app.model.user_settings`, `UserSettings`


## Key Components

No major components extracted.

## Usage & Examples

See source code for usage details.

## Related Files

- `openbb_core.app.model.credentials`
- `openbb_core.app.model.defaults`
- `openbb_core.app.model.preferences`
- `openbb_core.app.model.user_settings`

## Notes
- Generated: 2025-11-18T07:54:35.843695
- Generator: World's Best Repo Book Generator v1.0.0

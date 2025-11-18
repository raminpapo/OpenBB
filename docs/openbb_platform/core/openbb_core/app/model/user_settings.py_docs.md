# Documentation: openbb_platform/core/openbb_core/app/model/user_settings.py

## File Metadata
- **Path**: `openbb_platform/core/openbb_core/app/model/user_settings.py`
- **Size**: 1,781 characters, 48 lines
- **Words**: 157
- **Extension**: .py
- **Classification**: Text file

## Original Source

```python
"""User settings model."""

import json
import os
import warnings

from openbb_core.app.constants import USER_SETTINGS_PATH
from openbb_core.app.model.abstract.tagged import Tagged
from openbb_core.app.model.credentials import Credentials
from openbb_core.app.model.defaults import Defaults
from openbb_core.app.model.preferences import Preferences
from pydantic import Field


class UserSettings(Tagged):
    """User settings."""

    credentials: Credentials = Field(default_factory=Credentials)
    preferences: Preferences = Field(default_factory=Preferences)
    defaults: Defaults = Field(default_factory=Defaults)

    def __init__(self, **kwargs):
        """Initialize user settings by loading directly from file if it exists."""
        # Check if user settings file exists and load from it
        if os.path.exists(USER_SETTINGS_PATH):
            try:
                with open(USER_SETTINGS_PATH) as f:
                    file_settings = json.load(f)
                # Initialize with settings from file
                super().__init__(**{k: v for k, v in file_settings.items() if v})
            except (json.JSONDecodeError, OSError) as e:
                warnings.warn(
                    f"Error loading user settings from file: {e}",
                    stacklevel=2,
                    category=UserWarning,
                )
                # Fall back to defaults if file can't be read
                super().__init__(**kwargs)
        else:
            # Use defaults if file doesn't exist
            super().__init__(**kwargs)

    def __repr__(self) -> str:
        """Human readable representation of the object."""
        return f"{self.__class__.__name__}\n\n" + "\n".join(
            f"{k}: {v}" for k, v in self.model_dump().items()
        )

```

## High-Level Overview

User settings model.

import json
import os
import warnings

from openbb_core.app.constants import USER_SETTINGS_PATH
from openbb_core.app.model.abstract.tagged import Tagged
from openbb_core.app.model.credentials import Credentials
from openbb_core.app.model.defaults import Defaults
from openbb_core.app.model.preferences import Preferences
from pydantic import Field


class UserSettings(Tagged):
User settings.
Initialize user settings by loading directly from file if it exists.
# Check if user settings file exists and load from it
if os.path.exists(USER_SETTINGS_PATH):
try:

## Detailed Structure

### Python File Structure

**Classes** (1):
`UserSettings`

**Functions** (2):
`__init__`, `__repr__`

**Imports** (19):
`json`, `os`, `warnings`, `openbb_core.app.constants`, `USER_SETTINGS_PATH`, `openbb_core.app.model.abstract.tagged`, `Tagged`, `openbb_core.app.model.credentials`, `Credentials`, `openbb_core.app.model.defaults`, `Defaults`, `openbb_core.app.model.preferences`, `Preferences`, `pydantic`, `Field`, `file`, `it`, `file`, `file`


## Key Components

**Class `UserSettings`**: User settings.

## Usage & Examples

See source code for usage details.

## Related Files

- `json`
- `os`
- `warnings`
- `openbb_core.app.constants`
- `openbb_core.app.model.abstract.tagged`
- `openbb_core.app.model.credentials`
- `openbb_core.app.model.defaults`
- `openbb_core.app.model.preferences`
- `pydantic`

## Notes
- Generated: 2025-11-18T07:54:35.464734
- Generator: World's Best Repo Book Generator v1.0.0

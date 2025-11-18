# Documentation: openbb_platform/core/openbb_core/app/model/command_context.py

## File Metadata
- **Path**: `openbb_platform/core/openbb_core/app/model/command_context.py`
- **Size**: 397 characters, 13 lines
- **Words**: 27
- **Extension**: .py
- **Classification**: Text file

## Original Source

```python
"""Command Context."""

from openbb_core.app.model.system_settings import SystemSettings
from openbb_core.app.model.user_settings import UserSettings
from pydantic import BaseModel, Field


class CommandContext(BaseModel):
    """Command Context."""

    user_settings: UserSettings = Field(default_factory=UserSettings)
    system_settings: SystemSettings = Field(default_factory=SystemSettings)

```

## High-Level Overview

Command Context.

from openbb_core.app.model.system_settings import SystemSettings
from openbb_core.app.model.user_settings import UserSettings
from pydantic import BaseModel, Field


class CommandContext(BaseModel):
Command Context.

## Detailed Structure

### Python File Structure

**Classes** (1):
`CommandContext`

**Functions** (0):
None

**Imports** (6):
`openbb_core.app.model.system_settings`, `SystemSettings`, `openbb_core.app.model.user_settings`, `UserSettings`, `pydantic`, `BaseModel`


## Key Components

**Class `CommandContext`**: Command Context.

## Usage & Examples

See source code for usage details.

## Related Files

- `openbb_core.app.model.system_settings`
- `openbb_core.app.model.user_settings`
- `pydantic`

## Notes
- Generated: 2025-11-18T07:54:35.442841
- Generator: World's Best Repo Book Generator v1.0.0

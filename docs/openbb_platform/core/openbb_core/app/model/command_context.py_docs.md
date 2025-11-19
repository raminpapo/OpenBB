# File Documentation: command_context.py

## Metadata
- **Path**: `openbb_platform/core/openbb_core/app/model/command_context.py`
- **Size**: 397 bytes
- **Lines**: 13
- **Category**: python
- **Extension**: .py

---

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



---

## High-Level Overview

This is a **python** file named `command_context.py`.

**Python Module**

- **Classes** (1): CommandContext
- **Import Statements**: 1


---

## Detailed Analysis

### Python Code Structure

#### Classes

- **`CommandContext`**(BaseModel)


---

## Related Files

The following files may be related based on imports and references:

**Imported Modules**:
- `BaseModel`
- `SystemSettings`
- `UserSettings`
- `openbb_core.app.model.system_settings`
- `openbb_core.app.model.user_settings`
- `pydantic`


---

## Performance & Security Notes

No obvious security concerns detected in static analysis.


---

**Generated**: 2025-11-19T02:16:46.247114Z
**Generator**: World's Best Repo Book Generator v1.0

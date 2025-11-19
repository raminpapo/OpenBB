# File Documentation: utils.py

## Metadata
- **Path**: `cli/openbb_cli/utils/utils.py`
- **Size**: 1,047 bytes
- **Lines**: 35
- **Category**: python
- **Extension**: .py

---

## Original Source

```python
"""OpenBB Platform CLI utilities."""

import json
from pathlib import Path

HOME_DIRECTORY = Path.home()
OPENBB_PLATFORM_DIRECTORY = Path(HOME_DIRECTORY, ".openbb_platform")
SYSTEM_SETTINGS_PATH = Path(OPENBB_PLATFORM_DIRECTORY, "system_settings.json")


def change_logging_sub_app() -> str:
    """Build OpenBB Platform setting files."""
    with open(SYSTEM_SETTINGS_PATH) as file:
        system_settings = json.load(file)

    initial_logging_sub_app = system_settings.get("logging_sub_app", "")

    system_settings["logging_sub_app"] = "cli"

    with open(SYSTEM_SETTINGS_PATH, "w") as file:
        json.dump(system_settings, file, indent=4)

    return initial_logging_sub_app


def reset_logging_sub_app(initial_logging_sub_app: str):
    """Reset OpenBB Platform setting files."""
    with open(SYSTEM_SETTINGS_PATH) as file:
        system_settings = json.load(file)

    system_settings["logging_sub_app"] = initial_logging_sub_app

    with open(SYSTEM_SETTINGS_PATH, "w") as file:
        json.dump(system_settings, file, indent=4)

```



---

## High-Level Overview

This is a **python** file named `utils.py`.

**Python Module**

- **Functions** (2): change_logging_sub_app, reset_logging_sub_app
- **Import Statements**: 1


---

## Detailed Analysis

### Python Code Structure


#### Functions

- **`reset_logging_sub_app(initial_logging_sub_app: str)`**


---

## Related Files

The following files may be related based on imports and references:

**Imported Modules**:
- `Path`
- `json`
- `pathlib`


---

## Performance & Security Notes

No obvious security concerns detected in static analysis.


---

**Generated**: 2025-11-19T02:16:44.907673Z
**Generator**: World's Best Repo Book Generator v1.0

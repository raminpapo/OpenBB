# File Documentation: constants.py

## Metadata
- **Path**: `openbb_platform/core/openbb_core/app/constants.py`
- **Size**: 293 bytes
- **Lines**: 9
- **Category**: python
- **Extension**: .py

---

## Original Source

```python
"""Constants for the OpenBB Platform."""

from pathlib import Path

HOME_DIRECTORY = Path.home()
OPENBB_DIRECTORY = Path(HOME_DIRECTORY, ".openbb_platform")
USER_SETTINGS_PATH = Path(OPENBB_DIRECTORY, "user_settings.json")
SYSTEM_SETTINGS_PATH = Path(OPENBB_DIRECTORY, "system_settings.json")

```



---

## High-Level Overview

This is a **python** file named `constants.py`.

**Python Module**

- **Import Statements**: 1


---

## Detailed Analysis

### Python Code Structure



---

## Related Files

The following files may be related based on imports and references:

**Imported Modules**:
- `Path`
- `pathlib`


---

## Performance & Security Notes

No obvious security concerns detected in static analysis.


---

**Generated**: 2025-11-19T02:16:46.213402Z
**Generator**: World's Best Repo Book Generator v1.0

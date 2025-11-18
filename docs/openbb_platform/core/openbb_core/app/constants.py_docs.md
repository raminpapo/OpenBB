# Documentation: openbb_platform/core/openbb_core/app/constants.py

## File Metadata
- **Path**: `openbb_platform/core/openbb_core/app/constants.py`
- **Size**: 293 characters, 9 lines
- **Words**: 24
- **Extension**: .py
- **Classification**: Text file

## Original Source

```python
"""Constants for the OpenBB Platform."""

from pathlib import Path

HOME_DIRECTORY = Path.home()
OPENBB_DIRECTORY = Path(HOME_DIRECTORY, ".openbb_platform")
USER_SETTINGS_PATH = Path(OPENBB_DIRECTORY, "user_settings.json")
SYSTEM_SETTINGS_PATH = Path(OPENBB_DIRECTORY, "system_settings.json")

```

## High-Level Overview

Constants for the OpenBB Platform.

from pathlib import Path

HOME_DIRECTORY = Path.home()
OPENBB_DIRECTORY = Path(HOME_DIRECTORY, ".openbb_platform")
USER_SETTINGS_PATH = Path(OPENBB_DIRECTORY, "user_settings.json")
SYSTEM_SETTINGS_PATH = Path(OPENBB_DIRECTORY, "system_settings.json")


## Detailed Structure

### Python File Structure

**Classes** (0):
None

**Functions** (0):
None

**Imports** (2):
`pathlib`, `Path`


## Key Components

No major components extracted.

## Usage & Examples

See source code for usage details.

## Related Files

- `pathlib`

## Notes
- Generated: 2025-11-18T07:54:35.414626
- Generator: World's Best Repo Book Generator v1.0.0

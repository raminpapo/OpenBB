# Documentation: openbb_platform/core/openbb_core/app/logs/utils/expired_files.py

## File Metadata
- **Path**: `openbb_platform/core/openbb_core/app/logs/utils/expired_files.py`
- **Size**: 942 characters, 30 lines
- **Words**: 94
- **Extension**: .py
- **Classification**: Text file

## Original Source

```python
"""Expired files management utilities."""

import contextlib
from datetime import datetime
from pathlib import Path


def get_timestamp_from_x_days(x: int) -> float:
    """Get the timestamp from x days ago."""
    timestamp_from_x_days = datetime.now().timestamp() - x * 86400
    return timestamp_from_x_days


def get_expired_file_list(directory: Path, before_timestamp: float) -> list[Path]:
    """Get the list of expired files from a directory."""
    expired_files = []
    if directory.is_dir():  # Check if the directory exists and is a directory
        for file in directory.iterdir():
            if file.is_file() and file.lstat().st_mtime < before_timestamp:
                expired_files.append(file)

    return expired_files


def remove_file_list(file_list: list[Path]):
    """Remove a list of files."""
    for file in file_list:
        with contextlib.suppress(PermissionError):
            file.unlink(missing_ok=True)

```

## High-Level Overview

Expired files management utilities.

import contextlib
from datetime import datetime
from pathlib import Path


def get_timestamp_from_x_days(x: int) -> float:
Get the timestamp from x days ago.
Get the list of expired files from a directory.
expired_files = []
if directory.is_dir():  # Check if the directory exists and is a directory
for file in directory.iterdir():
if file.is_file() and file.lstat().st_mtime < before_timestamp:
expired_files.append(file)

return expired_files


def remove_file_list(file_list: list[Path]):

## Detailed Structure

### Python File Structure

**Classes** (0):
None

**Functions** (3):
`get_timestamp_from_x_days`, `get_expired_file_list`, `remove_file_list`

**Imports** (7):
`contextlib`, `datetime`, `datetime`, `pathlib`, `Path`, `x`, `a`


## Key Components

No major components extracted.

## Usage & Examples

See source code for usage details.

## Related Files

- `contextlib`
- `datetime`
- `pathlib`

## Notes
- Generated: 2025-11-18T07:54:35.426315
- Generator: World's Best Repo Book Generator v1.0.0

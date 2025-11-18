# Documentation: openbb_platform/core/openbb_core/app/logs/utils/utils.py

## File Metadata
- **Path**: `openbb_platform/core/openbb_core/app/logs/utils/utils.py`
- **Size**: 2,247 characters, 75 lines
- **Words**: 199
- **Extension**: .py
- **Classification**: Text file

## Original Source

```python
"""Utility functions for logging."""

import time
import uuid
import warnings
from pathlib import Path, PosixPath


def get_session_id() -> str:
    """UUID of the current session."""
    session_id = str(uuid.uuid4()) + "-" + str(int(time.time()))
    return session_id


def get_app_id(contextual_user_data_directory: str) -> str:
    """Get UUID of the current installation."""
    try:
        app_id = get_log_dir(contextual_user_data_directory).stem
    except OSError as e:
        if e.errno == 30:
            warnings.warn("Please move the application into a writable location.")
            warnings.warn(
                "Note for macOS users: copy `OpenBB Terminal` folder outside the DMG."
            )
        raise e
    except Exception as e:
        raise e

    return app_id


def get_log_dir(contextual_user_data_directory: str) -> PosixPath:
    """Retrieve application's log directory."""
    log_dir = create_log_dir_if_not_exists(contextual_user_data_directory)
    logging_uuid = create_log_uuid_if_not_exists(log_dir)
    uuid_log_dir = create_uuid_dir_if_not_exists(log_dir, logging_uuid)

    return uuid_log_dir


def create_log_dir_if_not_exists(contextual_user_data_directory: str) -> Path:
    """Create a log directory for the current installation."""
    log_dir = Path(contextual_user_data_directory).joinpath("logs").absolute()
    if not log_dir.is_dir():
        log_dir.mkdir(parents=True, exist_ok=True)

    return log_dir


def create_log_uuid_if_not_exists(log_dir: Path) -> str:
    """Create a log id file for the current logging session."""
    log_id = get_log_id(log_dir)
    if not log_id.is_file():
        logging_id = f"{uuid.uuid4()}"
        log_id.write_text(logging_id, encoding="utf-8")
    else:
        logging_id = log_id.read_text(encoding="utf-8").rstrip()

    return logging_id


def get_log_id(log_dir):
    """Get the log id file."""
    return (log_dir / ".logid").absolute()


def create_uuid_dir_if_not_exists(log_dir, logging_id) -> PosixPath:
    """Create a directory for the current logging session."""
    uuid_log_dir = (log_dir / logging_id).absolute()

    if not uuid_log_dir.is_dir():
        uuid_log_dir.mkdir(parents=True, exist_ok=True)

    return uuid_log_dir

```

## High-Level Overview

Utility functions for logging.

import time
import uuid
import warnings
from pathlib import Path, PosixPath


def get_session_id() -> str:
UUID of the current session.
Get UUID of the current installation.
try:
app_id = get_log_dir(contextual_user_data_directory).stem
except OSError as e:
if e.errno == 30:
warnings.warn("Please move the application into a writable location.")
warnings.warn(
"Note for macOS users: copy `OpenBB Terminal` folder outside the DMG."
)
raise e

## Detailed Structure

### Python File Structure

**Classes** (0):
None

**Functions** (7):
`get_session_id`, `get_app_id`, `get_log_dir`, `create_log_dir_if_not_exists`, `create_log_uuid_if_not_exists`, `get_log_id`, `create_uuid_dir_if_not_exists`

**Imports** (5):
`time`, `uuid`, `warnings`, `pathlib`, `Path`


## Key Components

No major components extracted.

## Usage & Examples

See source code for usage details.

## Related Files

- `time`
- `uuid`
- `warnings`
- `pathlib`

## Notes
- Generated: 2025-11-18T07:54:35.427618
- Generator: World's Best Repo Book Generator v1.0.0

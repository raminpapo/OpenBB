# File Documentation: handlers_manager.py

## Metadata
- **Path**: `openbb_platform/core/openbb_core/app/logs/handlers_manager.py`
- **Size**: 2,868 bytes
- **Lines**: 80
- **Category**: python
- **Extension**: .py

---

## Original Source

```python
"""Handlers Manager."""

import logging
import sys

from openbb_core.app.logs.formatters.formatter_with_exceptions import (
    FormatterWithExceptions,
)
from openbb_core.app.logs.handlers.path_tracking_file_handler import (
    PathTrackingFileHandler,
)
from openbb_core.app.logs.models.logging_settings import LoggingSettings


class HandlersManager:
    """Handlers Manager."""

    def __init__(self, logger: logging.Logger, settings: LoggingSettings):
        """Initialize the HandlersManager."""
        self._logger = logger
        self._handlers = settings.handler_list
        self._settings = settings

    def setup(self):
        """Set the logger handlers and settings."""
        # Disable propagation to root logger to avoid duplicate logs
        self._logger.propagate = False
        self._logger.setLevel(self._settings.verbosity)

        for handler_type in self._handlers:
            if handler_type == "stdout":
                self._add_stdout_handler()
            elif handler_type == "stderr":
                self._add_stderr_handler()
            elif handler_type == "noop":
                self._add_noop_handler()
            elif handler_type == "file" and not self._settings.logging_suppress:
                self._add_file_handler()
            else:
                self._logger.debug("Unknown log handler.")

    def _add_stdout_handler(self):
        """Add a stdout handler."""
        handler = logging.StreamHandler(sys.stdout)
        formatter = FormatterWithExceptions(settings=self._settings)
        handler.setFormatter(formatter)
        self._logger.addHandler(handler)

    def _add_stderr_handler(self):
        """Add a stderr handler."""
        handler = logging.StreamHandler(sys.stderr)
        formatter = FormatterWithExceptions(settings=self._settings)
        handler.setFormatter(formatter)
        self._logger.addHandler(handler)

    def _add_noop_handler(self):
        """Add a null handler."""
        handler = logging.NullHandler()
        formatter = FormatterWithExceptions(settings=self._settings)
        handler.setFormatter(formatter)
        self._logger.addHandler(handler)

    def _add_file_handler(self):
        """Add a file handler."""
        handler = PathTrackingFileHandler(settings=self._settings)
        formatter = FormatterWithExceptions(settings=self._settings)
        handler.setFormatter(formatter)
        self._logger.addHandler(handler)

    def update_handlers(self, settings: LoggingSettings):
        """Update the handlers with new settings."""
        logger = self._logger
        for hdlr in logger.handlers:
            if (
                isinstance(hdlr, PathTrackingFileHandler)
                and not settings.logging_suppress
            ):
                hdlr.settings = settings
                hdlr.formatter.settings = settings  # type: ignore

```



---

## High-Level Overview

This is a **python** file named `handlers_manager.py`.

**Python Module**

- **Classes** (1): HandlersManager
- **Functions** (7): __init__, setup, _add_stdout_handler, _add_stderr_handler, _add_noop_handler, _add_file_handler, update_handlers
- **Import Statements**: 2


---

## Detailed Analysis

### Python Code Structure

#### Classes

- **`HandlersManager`**

#### Functions

- **`__init__(self, logger: logging.Logger, settings: LoggingSettings)`**
- **`setup(self)`**
- **`_add_stdout_handler(self)`**
- **`_add_stderr_handler(self)`**
- **`_add_noop_handler(self)`**
- **`_add_file_handler(self)`**
- **`update_handlers(self, settings: LoggingSettings)`**


---

## Related Files

The following files may be related based on imports and references:

**Imported Modules**:
- `LoggingSettings`
- `logging`
- `openbb_core.app.logs.formatters.formatter_with_exceptions`
- `openbb_core.app.logs.handlers.path_tracking_file_handler`
- `openbb_core.app.logs.models.logging_settings`
- `sys`


---

## Performance & Security Notes

No obvious security concerns detected in static analysis.


---

**Generated**: 2025-11-19T02:16:46.231042Z
**Generator**: World's Best Repo Book Generator v1.0

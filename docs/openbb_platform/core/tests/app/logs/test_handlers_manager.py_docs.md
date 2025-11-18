# Documentation: openbb_platform/core/tests/app/logs/test_handlers_manager.py

## File Metadata
- **Path**: `openbb_platform/core/tests/app/logs/test_handlers_manager.py`
- **Size**: 3,010 characters, 97 lines
- **Words**: 198
- **Extension**: .py
- **Classification**: Text file

## Original Source

```python
"""Tests for the handlers manager."""

import logging
from unittest.mock import Mock, patch

from openbb_core.app.logs.handlers_manager import (
    HandlersManager,
    PathTrackingFileHandler,
)

# pylint: disable=W0231


class MockPathTrackingFileHandler(logging.NullHandler):
    """Mock path tracking file handler."""

    def __init__(self, settings):
        """Initialize the handler."""
        self.settings = settings
        self.level = logging.DEBUG


class MockFormatterWithExceptions(logging.Formatter):
    """Mock formatter with exceptions."""

    def __init__(self, settings):
        """Initialize the formatter."""
        self.settings = settings


def test_handlers_added_correctly():
    """Test if the handlers are added correctly."""
    with (
        patch(
            "openbb_core.app.logs.handlers_manager.PathTrackingFileHandler",
            MockPathTrackingFileHandler,
        ),
        patch(
            "openbb_core.app.logs.handlers_manager.FormatterWithExceptions",
            MockFormatterWithExceptions,
        ),
    ):
        settings = Mock()
        settings.verbosity = 20
        settings.handler_list = ["stdout", "stderr", "noop", "file"]
        settings.logging_suppress = False
        logger = logging.getLogger("test_handlers_added_correctly")
        handlers_manager = HandlersManager(logger=logger, settings=settings)
        handlers_manager.setup()
        handlers = logger.handlers

        assert not logger.propagate
        assert logger.level == 20
        assert len(handlers) >= 4

        for handler in handlers:
            assert isinstance(
                handler,
                (
                    logging.NullHandler,
                    logging.StreamHandler,
                    PathTrackingFileHandler,
                ),
            )

        for mock in [MockPathTrackingFileHandler]:
            assert any(isinstance(handler, mock) for handler in handlers)


def test_update_handlers():
    """Test if the handlers are updated correctly."""
    with (
        patch(
            "openbb_core.app.logs.handlers_manager.PathTrackingFileHandler",
            MockPathTrackingFileHandler,
        ),
        patch(
            "openbb_core.app.logs.handlers_manager.FormatterWithExceptions",
            MockFormatterWithExceptions,
        ),
    ):
        settings = Mock()
        settings.handler_list = ["file"]
        settings.any_other_attr = "mock_settings"
        logger = logging.getLogger("test_update_handlers")
        handlers_manager = HandlersManager(logger=logger, settings=settings)

        changed_settings = Mock()
        changed_settings.any_other_attr = "changed_settings"

        handlers_manager.update_handlers(settings=changed_settings)

        for hdlr in logger.handlers:
            if isinstance(hdlr, MockPathTrackingFileHandler):
                assert hdlr.settings == changed_settings
                assert hdlr.formatter.settings == changed_settings  # type: ignore[union-attr]

```

## High-Level Overview

Tests for the handlers manager.

import logging
from unittest.mock import Mock, patch

from openbb_core.app.logs.handlers_manager import (
HandlersManager,
PathTrackingFileHandler,
)

# pylint: disable=W0231


class MockPathTrackingFileHandler(logging.NullHandler):
Mock path tracking file handler.
Initialize the handler.
self.settings = settings
self.level = logging.DEBUG



## Detailed Structure

### Python File Structure

**Classes** (2):
`MockPathTrackingFileHandler`, `MockFormatterWithExceptions`

**Functions** (4):
`__init__`, `__init__`, `test_handlers_added_correctly`, `test_update_handlers`

**Imports** (4):
`logging`, `unittest.mock`, `Mock`, `openbb_core.app.logs.handlers_manager`


## Key Components

**Class `MockPathTrackingFileHandler`**: Mock path tracking file handler.

**Class `MockFormatterWithExceptions`**: Mock formatter with exceptions.

## Usage & Examples

See source code for usage details.

## Related Files

- `logging`
- `unittest.mock`
- `openbb_core.app.logs.handlers_manager`

## Notes
- Generated: 2025-11-18T07:54:35.813341
- Generator: World's Best Repo Book Generator v1.0.0

# Documentation: cli/tests/test_controllers_base_controller.py

## File Metadata
- **Path**: `cli/tests/test_controllers_base_controller.py`
- **Size**: 2,278 characters, 80 lines
- **Words**: 172
- **Extension**: .py
- **Classification**: Text file

## Original Source

```python
"""Test the base controller."""

from unittest.mock import MagicMock, patch

import pytest
from openbb_cli.controllers.base_controller import BaseController

# pylint: disable=unused-argument, unused-variable


class DummyBaseController(BaseController):
    """Testable Base Controller."""

    def __init__(self, queue=None):
        """Initialize the TestableBaseController."""
        self.PATH = "/valid/path/"
        super().__init__(queue=queue)

    def print_help(self):
        """Print help."""


def test_base_controller_initialization():
    """Test the initialization of the base controller."""
    with patch.object(DummyBaseController, "check_path", return_value=None):
        controller = DummyBaseController()
        assert controller.path == ["valid", "path"]  # Checking for correct path split


def test_path_validation():
    """Test the path validation method."""
    controller = DummyBaseController()

    with pytest.raises(ValueError):
        controller.PATH = "invalid/path"
        controller.check_path()

    with pytest.raises(ValueError):
        controller.PATH = "/invalid/path"
        controller.check_path()

    with pytest.raises(ValueError):
        controller.PATH = "/Invalid/Path/"
        controller.check_path()

    controller.PATH = "/valid/path/"


def test_parse_input():
    """Test the parse input method."""
    controller = DummyBaseController()
    input_str = "cmd1/cmd2/cmd3"
    expected = ["cmd1", "cmd2", "cmd3"]
    result = controller.parse_input(input_str)
    assert result == expected


def test_switch():
    """Test the switch method."""
    controller = DummyBaseController()
    with patch.object(controller, "call_exit", MagicMock()) as mock_exit:
        controller.queue = ["exit"]
        controller.switch("exit")
        mock_exit.assert_called_once()


def test_call_help():
    """Test the call help method."""
    controller = DummyBaseController()
    with patch("openbb_cli.controllers.base_controller.session.console.print"):
        controller.call_help(None)


def test_call_exit():
    """Test the call exit method."""
    controller = DummyBaseController()
    with patch.object(controller, "save_class", MagicMock()):
        controller.queue = ["quit"]
        controller.call_exit(None)

```

## High-Level Overview

Test the base controller.

from unittest.mock import MagicMock, patch

import pytest
from openbb_cli.controllers.base_controller import BaseController

# pylint: disable=unused-argument, unused-variable


class DummyBaseController(BaseController):
Testable Base Controller.
Initialize the TestableBaseController.
self.PATH = "/valid/path/"
super().__init__(queue=queue)

def print_help(self):
Print help.
Test the initialization of the base controller.
with patch.object(DummyBaseController, "check_path", return_value=None):

## Detailed Structure

### Python File Structure

**Classes** (1):
`DummyBaseController`

**Functions** (8):
`__init__`, `print_help`, `test_base_controller_initialization`, `test_path_validation`, `test_parse_input`, `test_switch`, `test_call_help`, `test_call_exit`

**Imports** (5):
`unittest.mock`, `MagicMock`, `pytest`, `openbb_cli.controllers.base_controller`, `BaseController`


## Key Components

**Class `DummyBaseController`**: Testable Base Controller.

## Usage & Examples

See source code for usage details.

## Related Files

- `unittest.mock`
- `pytest`
- `openbb_cli.controllers.base_controller`

## Notes
- Generated: 2025-11-18T07:54:34.715674
- Generator: World's Best Repo Book Generator v1.0.0

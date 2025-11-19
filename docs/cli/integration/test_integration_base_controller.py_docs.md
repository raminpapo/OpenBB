# File Documentation: test_integration_base_controller.py

## Metadata
- **Path**: `cli/integration/test_integration_base_controller.py`
- **Size**: 2,699 bytes
- **Lines**: 90
- **Category**: python
- **Extension**: .py

---

## Original Source

```python
"""Integration tests for the base_controller module."""

from unittest.mock import Mock, patch

import pytest
from openbb_cli.controllers.base_controller import BaseController
from openbb_cli.session import Session

# pylint: disable=unused-variable, redefined-outer-name


class DummyController(BaseController):
    """Test controller for the BaseController."""

    PATH = "/test/"

    def print_help(self):
        """Print help message."""


@pytest.fixture
def base_controller():
    """Set up the environment for each test function."""
    session = Session()  # noqa: F841
    controller = DummyController()
    return controller


@pytest.mark.integration
def test_check_path_valid(base_controller):
    """Test that check_path does not raise an error for a valid path."""
    base_controller.PATH = "/equity/"
    try:
        base_controller.check_path()
    except ValueError:
        pytest.fail("check_path raised ValueError unexpectedly!")


@pytest.mark.integration
def test_check_path_invalid(base_controller):
    """Test that check_path raises an error for an invalid path."""
    with pytest.raises(ValueError):
        base_controller.PATH = "invalid_path"  # Missing leading '/'
        base_controller.check_path()

    with pytest.raises(ValueError):
        base_controller.PATH = "/invalid_path"  # Missing trailing '/'
        base_controller.check_path()


@pytest.mark.integration
def test_parse_input(base_controller):
    """Test the parse_input method."""
    input_str = "/equity/price/help"
    expected_output = ["equity", "price", "help"]
    assert (
        base_controller.parse_input(input_str) == expected_output
    ), "Input parsing failed"


@pytest.mark.integration
def test_switch_command_execution(base_controller):
    """Test the switch method."""
    base_controller.queue = []
    base_controller.switch("/home/../reset/")
    assert base_controller.queue == [
        "home",
        "..",
        "reset",
    ], "Switch did not update the queue correctly"


@patch("openbb_cli.controllers.base_controller.BaseController.call_help")
@pytest.mark.integration
def test_command_routing(mock_call_help, base_controller):
    """Test the command routing."""
    base_controller.switch("help")
    mock_call_help.assert_called_once()


@pytest.mark.integration
def test_custom_reset(base_controller):
    """Test the custom reset method."""
    base_controller.custom_reset = Mock(return_value=["custom", "reset"])
    base_controller.call_reset(None)
    expected_queue = ["quit", "reset", "custom", "reset"]
    assert (
        base_controller.queue == expected_queue
    ), f"Expected queue to be {expected_queue}, but was {base_controller.queue}"

```



---

## High-Level Overview

This is a **python** file named `test_integration_base_controller.py`.

**Python Module**

- **Classes** (1): DummyController
- **Functions** (8): print_help, base_controller, test_check_path_valid, test_check_path_invalid, test_parse_input, test_switch_command_execution, test_command_routing, test_custom_reset
- **Import Statements**: 1


---

## Detailed Analysis

### Python Code Structure

#### Classes

- **`DummyController`**(BaseController)

#### Functions

- **`print_help(self)`**
- **`base_controller()`**
- **`test_check_path_valid(base_controller)`**
- **`test_check_path_invalid(base_controller)`**
- **`test_parse_input(base_controller)`**
- **`test_switch_command_execution(base_controller)`**
- **`test_command_routing(mock_call_help, base_controller)`**
- **`test_custom_reset(base_controller)`**

#### Decorators Used

patch, pytest


---

## Related Files

The following files may be related based on imports and references:

**Imported Modules**:
- `BaseController`
- `Mock`
- `Session`
- `openbb_cli.controllers.base_controller`
- `openbb_cli.session`
- `pytest`
- `unittest.mock`


---

## Performance & Security Notes

### Security Considerations

- ⚠️ Uses `input()` - validate user input


---

**Generated**: 2025-11-19T02:15:18.807989Z
**Generator**: World's Best Repo Book Generator v1.0

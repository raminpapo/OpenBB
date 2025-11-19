# File Documentation: test_controllers_base_platform_controller.py

## Metadata
- **Path**: `cli/tests/test_controllers_base_platform_controller.py`
- **Size**: 2,261 bytes
- **Lines**: 71
- **Category**: python
- **Extension**: .py

---

## Original Source

```python
"""Test the BasePlatformController."""

from unittest.mock import MagicMock, patch

import pytest
from openbb_cli.controllers.base_platform_controller import PlatformController, Session

# pylint: disable=redefined-outer-name, protected-access, unused-argument, unused-variable


@pytest.fixture
def mock_session():
    """Mock session fixture."""
    with patch(
        "openbb_cli.controllers.base_platform_controller.session",
        MagicMock(spec=Session),
    ) as mock:
        yield mock


def test_initialization_with_valid_params(mock_session):
    """Test the initialization of the BasePlatformController."""
    translators = {"dummy_translator": MagicMock()}
    controller = PlatformController(
        name="test", parent_path=["parent"], translators=translators
    )
    assert controller._name == "test"
    assert controller.translators == translators


def test_initialization_without_required_params():
    """Test the initialization of the BasePlatformController without required params."""
    with pytest.raises(ValueError):
        PlatformController(name="test", parent_path=["parent"])


def test_command_generation(mock_session):
    """Test the command generation method."""
    translator = MagicMock()
    translators = {"test_command": translator}
    controller = PlatformController(
        name="test", parent_path=["parent"], translators=translators
    )

    # Check if command function is correctly linked
    assert "test_command" in controller.translators


def test_print_help(mock_session):
    """Test the print help method."""
    translators = {"test_command": MagicMock()}
    controller = PlatformController(
        name="test", parent_path=["parent"], translators=translators
    )

    with patch(
        "openbb_cli.controllers.base_platform_controller.MenuText"
    ) as mock_menu_text:
        controller.print_help()
        mock_menu_text.assert_called_once_with("/parent/test/")


def test_sub_controller_generation(mock_session):
    """Test the sub controller generation method."""
    translators = {"test_menu_item": MagicMock()}
    controller = PlatformController(
        name="test", parent_path=["parent"], translators=translators
    )

    assert "test_menu_item" in controller.translators

```



---

## High-Level Overview

This is a **python** file named `test_controllers_base_platform_controller.py`.

**Python Module**

- **Functions** (6): mock_session, test_initialization_with_valid_params, test_initialization_without_required_params, test_command_generation, test_print_help, test_sub_controller_generation
- **Import Statements**: 1


---

## Detailed Analysis

### Python Code Structure


#### Functions

- **`mock_session()`**
- **`test_initialization_with_valid_params(mock_session)`**
- **`test_initialization_without_required_params()`**
- **`test_command_generation(mock_session)`**
- **`test_print_help(mock_session)`**
- **`test_sub_controller_generation(mock_session)`**

#### Decorators Used

pytest


---

## Related Files

The following files may be related based on imports and references:

**Imported Modules**:
- `MagicMock`
- `PlatformController`
- `openbb_cli.controllers.base_platform_controller`
- `pytest`
- `unittest.mock`


---

## Performance & Security Notes

No obvious security concerns detected in static analysis.


---

**Generated**: 2025-11-19T02:16:44.923236Z
**Generator**: World's Best Repo Book Generator v1.0

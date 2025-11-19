# File Documentation: test_controllers_choices.py

## Metadata
- **Path**: `cli/tests/test_controllers_choices.py`
- **Size**: 1,546 bytes
- **Lines**: 52
- **Category**: python
- **Extension**: .py

---

## Original Source

```python
"""Test the choices controller."""

from argparse import ArgumentParser
from unittest.mock import patch

import pytest
from openbb_cli.controllers.choices import (
    build_controller_choice_map,
)

# pylint: disable=redefined-outer-name, protected-access, unused-argument, unused-variable


class MockController:
    """Mock controller class for testing."""

    CHOICES_COMMANDS = ["test_command"]
    controller_choices = ["test_command", "help"]

    def call_test_command(self, args):
        """Mock function for test_command."""
        parser = ArgumentParser()
        parser.add_argument(
            "--example", choices=["option1", "option2"], help="Example argument."
        )
        return parser.parse_args(args)


@pytest.fixture
def mock_controller():
    """Mock controller fixture."""
    return MockController()


def test_build_command_choice_map(mock_controller):
    """Test the building of a command choice map."""
    with patch(
        "openbb_cli.controllers.choices._get_argument_parser"
    ) as mock_get_parser:
        parser = ArgumentParser()
        parser.add_argument(
            "--option", choices=["opt1", "opt2"], help="A choice option."
        )
        mock_get_parser.return_value = parser

        choice_map = build_controller_choice_map(controller=mock_controller)

        assert "test_command" in choice_map
        assert "--option" in choice_map["test_command"]
        assert "opt1" in choice_map["test_command"]["--option"]
        assert "opt2" in choice_map["test_command"]["--option"]

```



---

## High-Level Overview

This is a **python** file named `test_controllers_choices.py`.

**Python Module**

- **Classes** (2): MockController, for
- **Functions** (3): call_test_command, mock_controller, test_build_command_choice_map
- **Import Statements**: 1


---

## Detailed Analysis

### Python Code Structure

#### Classes

- **`MockController`**

#### Functions

- **`call_test_command(self, args)`**
- **`mock_controller()`**
- **`test_build_command_choice_map(mock_controller)`**

#### Decorators Used

pytest


---

## Related Files

The following files may be related based on imports and references:

**Imported Modules**:
- `ArgumentParser`
- `argparse`
- `openbb_cli.controllers.choices`
- `patch`
- `pytest`
- `unittest.mock`


---

## Performance & Security Notes

No obvious security concerns detected in static analysis.


---

**Generated**: 2025-11-19T02:16:44.924383Z
**Generator**: World's Best Repo Book Generator v1.0

# Documentation: cli/tests/test_controllers_choices.py

## File Metadata
- **Path**: `cli/tests/test_controllers_choices.py`
- **Size**: 1,546 characters, 52 lines
- **Words**: 116
- **Extension**: .py
- **Classification**: Text file

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

## High-Level Overview

Test the choices controller.

from argparse import ArgumentParser
from unittest.mock import patch

import pytest
from openbb_cli.controllers.choices import (
build_controller_choice_map,
)

# pylint: disable=redefined-outer-name, protected-access, unused-argument, unused-variable


class MockController:
Mock controller class for testing.
Mock function for test_command.
parser = ArgumentParser()
parser.add_argument(
"--example", choices=["option1", "option2"], help="Example argument."
)

## Detailed Structure

### Python File Structure

**Classes** (2):
`MockController`, `for`

**Functions** (3):
`call_test_command`, `mock_controller`, `test_build_command_choice_map`

**Imports** (6):
`argparse`, `ArgumentParser`, `unittest.mock`, `patch`, `pytest`, `openbb_cli.controllers.choices`


## Key Components

**Class `MockController`**: Mock controller class for testing.

## Usage & Examples

See source code for usage details.

## Related Files

- `argparse`
- `unittest.mock`
- `pytest`
- `openbb_cli.controllers.choices`

## Notes
- Generated: 2025-11-18T07:54:34.718607
- Generator: World's Best Repo Book Generator v1.0.0

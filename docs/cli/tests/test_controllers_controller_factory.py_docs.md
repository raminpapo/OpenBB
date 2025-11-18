# Documentation: cli/tests/test_controllers_controller_factory.py

## File Metadata
- **Path**: `cli/tests/test_controllers_controller_factory.py`
- **Size**: 1,823 characters, 62 lines
- **Words**: 141
- **Extension**: .py
- **Classification**: Text file

## Original Source

```python
"""Test the Controller Factory."""

from unittest.mock import MagicMock, patch

import pytest
from openbb_cli.controllers.platform_controller_factory import (
    PlatformControllerFactory,
)

# pylint: disable=redefined-outer-name, unused-argument


@pytest.fixture
def mock_processor():
    """Fixture to mock ArgparseClassProcessor."""
    with patch(
        "openbb_cli.controllers.platform_controller_factory.ArgparseClassProcessor"
    ) as mock:
        instance = mock.return_value
        instance.paths = {"settings": "menu"}
        instance.translators = {"test_router_settings": MagicMock()}
        yield instance


@pytest.fixture
def platform_router():
    """Fixture to provide a mock platform_router class."""

    class MockRouter:
        pass

    return MockRouter


@pytest.fixture
def factory(platform_router, mock_processor):
    """Fixture to create a PlatformControllerFactory with mocked dependencies."""
    return PlatformControllerFactory(
        platform_router=platform_router, reference={"test": "ref"}
    )


def test_init(mock_processor):
    """Test the initialization of the PlatformControllerFactory."""
    factory = PlatformControllerFactory(
        platform_router=MagicMock(), reference={"test": "ref"}
    )
    assert factory.router_name.lower() == "magicmock"
    assert factory.controller_name == "MagicmockController"


def test_create_controller(factory):
    """Test the creation of a controller class."""
    ControllerClass = factory.create()

    assert "PlatformController" in [base.__name__ for base in ControllerClass.__bases__]
    assert ControllerClass.CHOICES_GENERATION
    assert "settings" in ControllerClass.CHOICES_MENUS
    assert "test_router_settings" not in [
        cmd.replace("test_router_", "") for cmd in ControllerClass.CHOICES_COMMANDS
    ]

```

## High-Level Overview

Test the Controller Factory.

from unittest.mock import MagicMock, patch

import pytest
from openbb_cli.controllers.platform_controller_factory import (
PlatformControllerFactory,
)

# pylint: disable=redefined-outer-name, unused-argument


@pytest.fixture
def mock_processor():
Fixture to mock ArgparseClassProcessor.
Fixture to provide a mock platform_router class.

class MockRouter:
pass


## Detailed Structure

### Python File Structure

**Classes** (1):
`MockRouter`

**Functions** (5):
`mock_processor`, `platform_router`, `factory`, `test_init`, `test_create_controller`

**Imports** (4):
`unittest.mock`, `MagicMock`, `pytest`, `openbb_cli.controllers.platform_controller_factory`


## Key Components

**Class `MockRouter`**: No documentation

## Usage & Examples

See source code for usage details.

## Related Files

- `unittest.mock`
- `pytest`
- `openbb_cli.controllers.platform_controller_factory`

## Notes
- Generated: 2025-11-18T07:54:34.721806
- Generator: World's Best Repo Book Generator v1.0.0

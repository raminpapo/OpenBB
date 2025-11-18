# Documentation: cli/tests/test_argparse_translator_obbject_registry.py

## File Metadata
- **Path**: `cli/tests/test_argparse_translator_obbject_registry.py`
- **Size**: 2,537 characters, 90 lines
- **Words**: 208
- **Extension**: .py
- **Classification**: Text file

## Original Source

```python
"""Test OBBject Registry."""

from unittest.mock import Mock

import pytest
from openbb_cli.argparse_translator.obbject_registry import Registry
from openbb_core.app.model.obbject import OBBject

# pylint: disable=redefined-outer-name, protected-access


@pytest.fixture
def registry():
    """Fixture to create a Registry instance for testing."""
    return Registry()


@pytest.fixture
def mock_obbject():
    """Fixture to create a mock OBBject for testing."""

    class MockModel:
        """Mock model for testing."""

        def __init__(self, value):
            self.mock_value = value
            self._model_json_schema = "mock_json_schema"

        def model_json_schema(self):
            return self._model_json_schema

    obb = Mock(spec=OBBject)
    obb.id = "123"
    obb.provider = "test_provider"
    obb.extra = {"command": "test_command"}
    obb._route = "/test/route"
    obb._standard_params = Mock()
    obb._standard_params = {}
    obb.results = [MockModel(1), MockModel(2)]
    return obb


def test_listing_all_obbjects(registry, mock_obbject):
    """Test listing all obbjects with additional properties."""
    registry.register(mock_obbject)

    all_obbjects = registry.all
    assert len(all_obbjects) == 1
    assert all_obbjects[0]["command"] == "test_command"
    assert all_obbjects[0]["provider"] == "test_provider"


def test_registry_initialization(registry):
    """Test the Registry is initialized correctly."""
    assert registry.obbjects == []


def test_register_new_obbject(registry, mock_obbject):
    """Test registering a new OBBject."""
    registry.register(mock_obbject)
    assert mock_obbject in registry.obbjects


def test_register_duplicate_obbject(registry, mock_obbject):
    """Test that duplicate OBBjects are not added."""
    registry.register(mock_obbject)
    registry.register(mock_obbject)
    assert len(registry.obbjects) == 1


def test_get_obbject_by_index(registry, mock_obbject):
    """Test retrieving an obbject by its index."""
    registry.register(mock_obbject)
    retrieved = registry.get(0)
    assert retrieved == mock_obbject


def test_remove_obbject_by_index(registry, mock_obbject):
    """Test removing an obbject by index."""
    registry.register(mock_obbject)
    registry.remove(0)
    assert mock_obbject not in registry.obbjects


def test_remove_last_obbject_by_default(registry, mock_obbject):
    """Test removing the last obbject by default."""
    registry.register(mock_obbject)
    registry.remove()
    assert not registry.obbjects

```

## High-Level Overview

Test OBBject Registry.

from unittest.mock import Mock

import pytest
from openbb_cli.argparse_translator.obbject_registry import Registry
from openbb_core.app.model.obbject import OBBject

# pylint: disable=redefined-outer-name, protected-access


@pytest.fixture
def registry():
Fixture to create a Registry instance for testing.
Fixture to create a mock OBBject for testing.

class MockModel:
Mock model for testing.
Test listing all obbjects with additional properties.
registry.register(mock_obbject)

## Detailed Structure

### Python File Structure

**Classes** (1):
`MockModel`

**Functions** (11):
`registry`, `mock_obbject`, `__init__`, `model_json_schema`, `test_listing_all_obbjects`, `test_registry_initialization`, `test_register_new_obbject`, `test_register_duplicate_obbject`, `test_get_obbject_by_index`, `test_remove_obbject_by_index`, `test_remove_last_obbject_by_default`

**Imports** (7):
`unittest.mock`, `Mock`, `pytest`, `openbb_cli.argparse_translator.obbject_registry`, `Registry`, `openbb_core.app.model.obbject`, `OBBject`


## Key Components

**Class `MockModel`**: Mock model for testing.

## Usage & Examples

See source code for usage details.

## Related Files

- `unittest.mock`
- `pytest`
- `openbb_cli.argparse_translator.obbject_registry`
- `openbb_core.app.model.obbject`

## Notes
- Generated: 2025-11-18T07:54:34.707530
- Generator: World's Best Repo Book Generator v1.0.0

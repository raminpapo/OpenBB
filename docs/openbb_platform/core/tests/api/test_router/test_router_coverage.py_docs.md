# Documentation: openbb_platform/core/tests/api/test_router/test_router_coverage.py

## File Metadata
- **Path**: `openbb_platform/core/tests/api/test_router/test_router_coverage.py`
- **Size**: 1,259 characters, 40 lines
- **Words**: 75
- **Extension**: .py
- **Classification**: Text file

## Original Source

```python
"""Test coverage for the router module."""

from unittest.mock import patch

from openbb_core.api.router.coverage import get_command_coverage, get_provider_coverage


@patch("openbb_core.api.router.coverage.CommandMap")
def test_get_provider_coverage(mock_command_map):
    """Test get provider coverage."""
    mock_command_map.return_value.provider_coverage = {
        "provider1": ["coverage1", "coverage2"]
    }

    response = get_provider_coverage(mock_command_map)

    assert response


@patch("openbb_core.api.router.coverage.CommandMap")
def test_get_command_coverage(mock_command_map):
    """Test get command coverage."""
    mock_command_map.return_value.command_coverage = {
        "command1": ["coverage1", "coverage2"]
    }

    response = get_command_coverage(mock_command_map)
    assert response


@patch("openbb_core.api.router.coverage.CommandMap")
@patch("openbb_core.api.router.coverage.ProviderInterface")
def test_get_command_model(mock_provider_interface, mock_command_map):
    """Test get command model."""
    mock_command_map.return_value.commands_model = {"command1": "model1"}
    mock_provider_interface.return_value.map = {"model1": "provider1"}

    response = get_command_coverage(mock_command_map)
    assert response

```

## High-Level Overview

Test coverage for the router module.

from unittest.mock import patch

from openbb_core.api.router.coverage import get_command_coverage, get_provider_coverage


@patch("openbb_core.api.router.coverage.CommandMap")
def test_get_provider_coverage(mock_command_map):
Test get provider coverage.
Test get command coverage.
mock_command_map.return_value.command_coverage = {
"command1": ["coverage1", "coverage2"]
}

response = get_command_coverage(mock_command_map)
assert response


@patch("openbb_core.api.router.coverage.CommandMap")

## Detailed Structure

### Python File Structure

**Classes** (0):
None

**Functions** (3):
`test_get_provider_coverage`, `test_get_command_coverage`, `test_get_command_model`

**Imports** (4):
`unittest.mock`, `patch`, `openbb_core.api.router.coverage`, `get_command_coverage`


## Key Components

No major components extracted.

## Usage & Examples

See source code for usage details.

## Related Files

- `unittest.mock`
- `openbb_core.api.router.coverage`

## Notes
- Generated: 2025-11-18T07:54:35.797435
- Generator: World's Best Repo Book Generator v1.0.0

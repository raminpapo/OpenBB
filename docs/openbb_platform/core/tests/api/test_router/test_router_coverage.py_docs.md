# File Documentation: test_router_coverage.py

## Metadata
- **Path**: `openbb_platform/core/tests/api/test_router/test_router_coverage.py`
- **Size**: 1,259 bytes
- **Lines**: 40
- **Category**: python
- **Extension**: .py

---

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



---

## High-Level Overview

This is a **python** file named `test_router_coverage.py`.

**Python Module**

- **Functions** (3): test_get_provider_coverage, test_get_command_coverage, test_get_command_model
- **Import Statements**: 1


---

## Detailed Analysis

### Python Code Structure


#### Functions

- **`test_get_provider_coverage(mock_command_map)`**
- **`test_get_command_coverage(mock_command_map)`**
- **`test_get_command_model(mock_provider_interface, mock_command_map)`**

#### Decorators Used

patch


---

## Related Files

The following files may be related based on imports and references:

**Imported Modules**:
- `get_command_coverage`
- `openbb_core.api.router.coverage`
- `patch`
- `unittest.mock`


---

## Performance & Security Notes

No obvious security concerns detected in static analysis.


---

**Generated**: 2025-11-19T02:16:46.627978Z
**Generator**: World's Best Repo Book Generator v1.0

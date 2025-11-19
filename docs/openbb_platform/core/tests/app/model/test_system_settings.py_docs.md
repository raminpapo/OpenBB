# File Documentation: test_system_settings.py

## Metadata
- **Path**: `openbb_platform/core/tests/app/model/test_system_settings.py`
- **Size**: 4,035 bytes
- **Lines**: 114
- **Category**: python
- **Extension**: .py

---

## Original Source

```python
"""Tests for the SystemSettings class."""

import os
from pathlib import Path

import pytest
from openbb_core.app.model.system_settings import SystemSettings
from pydantic import BaseModel, ConfigDict


class MockSystemSettings(BaseModel):
    """Mock SystemSettings."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)


def test_system_settings():
    """Test the SystemSettings class."""
    sys = SystemSettings()
    assert isinstance(sys, SystemSettings)


def test_create_openbb_directory_directory_and_files_not_exist(tmpdir):
    """Test the create_openbb_directory method."""
    # Arrange
    values = MockSystemSettings(
        **{
            "openbb_directory": str(tmpdir.join("openbb")),
            "user_settings_path": str(tmpdir.join("user_settings.json")),
            "system_settings_path": str(tmpdir.join("system_settings.json")),
        }
    )

    # Act
    SystemSettings.create_openbb_directory(values)  # type: ignore[operator]

    # Assert
    assert os.path.exists(values.openbb_directory)  # type: ignore[attr-defined]
    assert os.path.exists(values.user_settings_path)  # type: ignore[attr-defined]
    assert os.path.exists(values.system_settings_path)  # type: ignore[attr-defined]


def test_create_openbb_directory_directory_exists_user_settings_missing(tmpdir):
    """Test the create_openbb_directory method."""
    # Arrange
    values = MockSystemSettings(
        **{
            "openbb_directory": str(tmpdir.join("openbb")),
            "user_settings_path": str(tmpdir.join("user_settings.json")),
            "system_settings_path": str(tmpdir.join("system_settings.json")),
        }
    )

    # Create the openbb directory
    Path(values.openbb_directory).mkdir(parents=True, exist_ok=True)  # type: ignore[attr-defined]

    # Act
    SystemSettings.create_openbb_directory(values)  # type: ignore[operator]

    # Assert
    assert os.path.exists(values.openbb_directory)  # type: ignore[attr-defined]
    assert os.path.exists(values.user_settings_path)  # type: ignore[attr-defined]
    assert os.path.exists(values.system_settings_path)  # type: ignore[attr-defined]


def test_create_openbb_directory_directory_exists_system_settings_missing(tmpdir):
    """Test the create_openbb_directory method."""
    # Arrange
    values = MockSystemSettings(
        **{
            "openbb_directory": str(tmpdir.join("openbb")),
            "user_settings_path": str(tmpdir.join("user_settings.json")),
            "system_settings_path": str(tmpdir.join("system_settings.json")),
        }
    )

    # Create the openbb directory
    Path(values.openbb_directory).mkdir(parents=True, exist_ok=True)  # type: ignore[attr-defined]

    # Create the user_settings.json file
    with open(values.user_settings_path, "w") as f:  # type: ignore[attr-defined]
        f.write("{}")

    # Act
    SystemSettings.create_openbb_directory(values)  # type: ignore[operator]

    # Assert
    assert os.path.exists(values.openbb_directory)  # type: ignore[attr-defined]
    assert os.path.exists(values.user_settings_path)  # type: ignore[attr-defined]
    assert os.path.exists(values.system_settings_path)  # type: ignore[attr-defined]


@pytest.mark.parametrize(
    "handlers, valid",
    [
        # Test case: Valid handlers
        (["stdout", "file", "noop"], True),
        # Test case: Invalid handler
        (["stdout", "invalid_handler", "file"], False),
        # Test case: Empty list of handlers
        ([], True),
        # Test case: Repeated valid handlers
        (["stdout", "stderr", "stdout", "noop", "stderr"], True),
    ],
)
def test_validate_logging_handlers(handlers, valid):
    """Test the validate_logging_handlers method."""
    # Act and Assert
    if valid:
        assert SystemSettings.validate_logging_handlers(handlers) == handlers  # type: ignore[call-arg]
    else:
        with pytest.raises(ValueError, match="Invalid logging handler"):
            SystemSettings.validate_logging_handlers(handlers)  # type: ignore[call-arg]

```



---

## High-Level Overview

This is a **python** file named `test_system_settings.py`.

**Python Module**

- **Classes** (1): MockSystemSettings
- **Functions** (5): test_system_settings, test_create_openbb_directory_directory_and_files_not_exist, test_create_openbb_directory_directory_exists_user_settings_missing, test_create_openbb_directory_directory_exists_system_settings_missing, test_validate_logging_handlers
- **Import Statements**: 1


---

## Detailed Analysis

### Python Code Structure

#### Classes

- **`MockSystemSettings`**(BaseModel)

#### Functions

- **`test_system_settings()`**
- **`test_create_openbb_directory_directory_and_files_not_exist(tmpdir)`**
- **`test_create_openbb_directory_directory_exists_user_settings_missing(tmpdir)`**
- **`test_create_openbb_directory_directory_exists_system_settings_missing(tmpdir)`**
- **`test_validate_logging_handlers(handlers, valid)`**

#### Decorators Used

pytest


---

## Related Files

The following files may be related based on imports and references:

**Imported Modules**:
- `BaseModel`
- `Path`
- `SystemSettings`
- `openbb_core.app.model.system_settings`
- `os`
- `pathlib`
- `pydantic`
- `pytest`


---

## Performance & Security Notes

No obvious security concerns detected in static analysis.


---

**Generated**: 2025-11-19T02:16:46.676283Z
**Generator**: World's Best Repo Book Generator v1.0

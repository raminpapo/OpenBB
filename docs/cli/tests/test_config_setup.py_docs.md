# File Documentation: test_config_setup.py

## Metadata
- **Path**: `cli/tests/test_config_setup.py`
- **Size**: 1,733 bytes
- **Lines**: 53
- **Category**: python
- **Extension**: .py

---

## Original Source

```python
"""Test the Config Setup."""

from unittest.mock import patch

import pytest
from openbb_cli.config.setup import bootstrap

# pylint: disable=unused-variable


def test_bootstrap_creates_directory_and_file():
    """Test that bootstrap creates the settings directory and environment file."""
    with (
        patch("pathlib.Path.mkdir") as mock_mkdir,
        patch("pathlib.Path.touch") as mock_touch,
    ):
        bootstrap()
        mock_mkdir.assert_called_once_with(parents=True, exist_ok=True)
        mock_touch.assert_called_once_with(exist_ok=True)


def test_bootstrap_directory_exists():
    """Test bootstrap when the directory already exists."""
    with (
        patch("pathlib.Path.mkdir") as mock_mkdir,
        patch("pathlib.Path.touch") as mock_touch,
    ):
        bootstrap()
        mock_mkdir.assert_called_once_with(parents=True, exist_ok=True)
        mock_touch.assert_called_once_with(exist_ok=True)


def test_bootstrap_file_exists():
    """Test bootstrap when the environment file already exists."""
    with (
        patch("pathlib.Path.mkdir") as mock_mkdir,
        patch("pathlib.Path.touch") as mock_touch,
    ):
        bootstrap()
        mock_mkdir.assert_called_once_with(parents=True, exist_ok=True)
        mock_touch.assert_called_once_with(exist_ok=True)


def test_bootstrap_permission_error():
    """Test bootstrap handles permission errors gracefully."""
    with (
        patch("pathlib.Path.mkdir") as mock_mkdir,
        patch("pathlib.Path.touch"),
        pytest.raises(PermissionError),
    ):
        mock_mkdir.side_effect = PermissionError("No permission to create directory")
        bootstrap()  # Expecting to raise a PermissionError and be caught by pytest.raises

```



---

## High-Level Overview

This is a **python** file named `test_config_setup.py`.

**Python Module**

- **Functions** (4): test_bootstrap_creates_directory_and_file, test_bootstrap_directory_exists, test_bootstrap_file_exists, test_bootstrap_permission_error
- **Import Statements**: 1


---

## Detailed Analysis

### Python Code Structure


#### Functions

- **`test_bootstrap_creates_directory_and_file()`**
- **`test_bootstrap_directory_exists()`**
- **`test_bootstrap_file_exists()`**
- **`test_bootstrap_permission_error()`**


---

## Related Files

The following files may be related based on imports and references:

**Imported Modules**:
- `bootstrap`
- `openbb_cli.config.setup`
- `patch`
- `pytest`
- `unittest.mock`


---

## Performance & Security Notes

No obvious security concerns detected in static analysis.


---

**Generated**: 2025-11-19T02:16:44.919409Z
**Generator**: World's Best Repo Book Generator v1.0

# Documentation: cli/tests/test_config_setup.py

## File Metadata
- **Path**: `cli/tests/test_config_setup.py`
- **Size**: 1,733 characters, 53 lines
- **Words**: 122
- **Extension**: .py
- **Classification**: Text file

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

## High-Level Overview

Test the Config Setup.

from unittest.mock import patch

import pytest
from openbb_cli.config.setup import bootstrap

# pylint: disable=unused-variable


def test_bootstrap_creates_directory_and_file():
Test that bootstrap creates the settings directory and environment file.
Test bootstrap when the directory already exists.
with (
patch("pathlib.Path.mkdir") as mock_mkdir,
patch("pathlib.Path.touch") as mock_touch,
):
bootstrap()
mock_mkdir.assert_called_once_with(parents=True, exist_ok=True)
mock_touch.assert_called_once_with(exist_ok=True)

## Detailed Structure

### Python File Structure

**Classes** (0):
None

**Functions** (4):
`test_bootstrap_creates_directory_and_file`, `test_bootstrap_directory_exists`, `test_bootstrap_file_exists`, `test_bootstrap_permission_error`

**Imports** (5):
`unittest.mock`, `patch`, `pytest`, `openbb_cli.config.setup`, `bootstrap`


## Key Components

No major components extracted.

## Usage & Examples

See source code for usage details.

## Related Files

- `unittest.mock`
- `pytest`
- `openbb_cli.config.setup`

## Notes
- Generated: 2025-11-18T07:54:34.713578
- Generator: World's Best Repo Book Generator v1.0.0

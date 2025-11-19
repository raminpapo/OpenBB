# File Documentation: test_expired_files.py

## Metadata
- **Path**: `openbb_platform/core/tests/app/logs/utils/test_expired_files.py`
- **Size**: 5,260 bytes
- **Lines**: 166
- **Category**: python
- **Extension**: .py

---

## Original Source

```python
"""Tests for the expired_files module."""

import os
import tempfile
from pathlib import Path
from time import time
from unittest.mock import MagicMock, patch

import pytest
from openbb_core.app.logs.utils.expired_files import (
    get_expired_file_list,
    get_timestamp_from_x_days,
    remove_file_list,
)

# pylint: disable=W0621


@pytest.fixture
def temp_test_files():
    """Create temporary files for testing."""
    with tempfile.TemporaryDirectory() as temp_dir:
        temp_files = [
            Path(temp_dir) / "file1.txt",
            Path(temp_dir) / "file2.txt",
            Path(temp_dir) / "file3.txt",
        ]

        # Create some test files
        for file_path in temp_files:
            file_path.touch()

        yield temp_dir, temp_files


def test_get_timestamp_from_x_days():
    """Test get_timestamp_from_x_days."""
    result = get_timestamp_from_x_days(0)
    assert isinstance(result, float)


# Test case when all files are expired
def test_all_files_expired(temp_test_files):
    """Test get_expired_file_list when all files are expired."""
    temp_dir, temp_files = temp_test_files
    before_timestamp = time() + 3 * 86400  # timestamp 3 days from now
    expired_files = get_expired_file_list(Path(temp_dir), before_timestamp)
    assert set(expired_files) == set(temp_files)


# Test case when no files are expired
def test_no_files_expired(temp_test_files):
    """Test get_expired_file_list when no files are expired."""
    temp_dir, _ = temp_test_files
    before_timestamp = 0
    expired_files = get_expired_file_list(Path(temp_dir), before_timestamp)
    assert not expired_files


# Test case when some files are expired and some are not
def test_some_files_expired(temp_test_files):
    """Test get_expired_file_list when some files are expired and some are not."""
    temp_dir, _ = temp_test_files

    # add temp file to temp_dir with timestamp in the future
    temp_file = Path(temp_dir) / "file4.txt"
    temp_file.touch()
    time_in_future = time() + 4 * 86400  # timestamp 4 days from now
    os.utime(temp_file, times=(time_in_future, time_in_future))

    before_timestamp = time() + 3 * 86400  # timestamp 3 days from now
    expired_files = get_expired_file_list(Path(temp_dir), before_timestamp)
    assert len(expired_files) == 3

    # assert number of files in temp_dir is 4
    assert len(list(Path(temp_dir).iterdir())) == 4


# Test case when the directory does not exist
def test_directory_not_exists():
    """Test get_expired_file_list when the directory does not exist."""
    directory = Path("/path/that/does/not/exist")
    before_timestamp = time()
    expired_files = get_expired_file_list(directory, before_timestamp)
    assert not expired_files


# Test case when the directory is not a directory
def test_directory_not_dir(temp_test_files):
    """Test get_expired_file_list when the directory is not a directory."""
    _, temp_files = temp_test_files
    before_timestamp = time()
    expired_files = get_expired_file_list(temp_files[0], before_timestamp)
    assert not expired_files


@pytest.fixture
def mock_path():
    """Return a MagicMock for the Path class."""
    # Create a MagicMock for the Path class to represent a file path
    return MagicMock()


def test_remove_file_list_no_files(mock_path):
    """Test remove_file_list when there are no files to remove."""
    # Arrange
    # Let's assume the file list is empty, meaning there are no files to remove
    file_list: list[Path] = []

    # Act
    remove_file_list(file_list)

    # Assert
    # No interaction with the filesystem should occur
    assert not mock_path.unlink.called


def test_remove_file_list_remove_files_successfully(mock_path):
    """Test remove_file_list when unlink is successful."""
    # Arrange
    # Let's assume we have three files in the file list
    file_list = [mock_path, mock_path, mock_path]

    # Mock the unlink method to avoid actual filesystem interaction
    patch.object(mock_path, "unlink")

    # Act
    remove_file_list(file_list)

    # Assert
    # unlink should have been called three times since there are three files in the list
    assert mock_path.unlink.call_count == 3


def test_remove_file_list_ignore_permission_error(mock_path):
    """Test remove_file_list when unlink raises a PermissionError."""
    # Arrange
    # Let's assume we have three files in the file list
    file_list = [mock_path, mock_path, mock_path]

    # Mock the unlink method to raise a PermissionError
    patch.object(mock_path, "unlink", side_effect=PermissionError)

    # Act
    remove_file_list(file_list)

    # Assert
    # unlink should have been called three times since there are three files in the list
    assert mock_path.unlink.call_count == 3


def test_remove_file_list_other_exception(mock_path):
    """Test remove_file_list when unlink raises an exception other than PermissionError."""
    # Arrange
    # Let's assume we have three files in the file list
    file_list = [mock_path, mock_path, mock_path]

    # Mock the unlink method to raise an exception other than PermissionError
    patch.object(mock_path, "unlink", side_effect=OSError)

    # Act
    remove_file_list(file_list)

    # Assert
    assert mock_path.unlink.call_count == 3

```



---

## High-Level Overview

This is a **python** file named `test_expired_files.py`.

**Python Module**

- **Classes** (1): to
- **Functions** (12): temp_test_files, test_get_timestamp_from_x_days, test_all_files_expired, test_no_files_expired, test_some_files_expired, test_directory_not_exists, test_directory_not_dir, mock_path, test_remove_file_list_no_files, test_remove_file_list_remove_files_successfully ... and 2 more
- **Import Statements**: 1


---

## Detailed Analysis

### Python Code Structure


#### Functions

- **`temp_test_files()`**
- **`test_get_timestamp_from_x_days()`**
- **`test_all_files_expired(temp_test_files)`**
- **`test_no_files_expired(temp_test_files)`**
- **`test_some_files_expired(temp_test_files)`**
- **`test_directory_not_exists()`**
- **`test_directory_not_dir(temp_test_files)`**
- **`mock_path()`**
- **`test_remove_file_list_no_files(mock_path)`**
- **`test_remove_file_list_remove_files_successfully(mock_path)`**
- **`test_remove_file_list_ignore_permission_error(mock_path)`**
- **`test_remove_file_list_other_exception(mock_path)`**

#### Decorators Used

pytest


---

## Related Files

The following files may be related based on imports and references:

**Imported Modules**:
- `MagicMock`
- `Path`
- `openbb_core.app.logs.utils.expired_files`
- `os`
- `pathlib`
- `pytest`
- `tempfile`
- `time`
- `unittest.mock`


---

## Performance & Security Notes

No obvious security concerns detected in static analysis.


---

**Generated**: 2025-11-19T02:16:46.660180Z
**Generator**: World's Best Repo Book Generator v1.0

# Documentation: cli/tests/test_controllers_utils.py

## File Metadata
- **Path**: `cli/tests/test_controllers_utils.py`
- **Size**: 3,989 characters, 141 lines
- **Words**: 299
- **Extension**: .py
- **Classification**: Text file

## Original Source

```python
"""Test the Controller utils."""

import argparse
from pathlib import Path
from unittest.mock import MagicMock, patch

import pytest
from openbb_cli.controllers.utils import (
    check_non_negative,
    check_positive,
    get_flair_and_username,
    get_user_agent,
    parse_and_split_input,
    print_goodbye,
    remove_file,
    welcome_message,
)

# pylint: disable=redefined-outer-name, unused-argument


@pytest.fixture
def mock_session():
    """Mock the session and its dependencies."""
    with patch("openbb_cli.controllers.utils.session") as mock_session:
        mock_session.console.print = MagicMock()
        mock_session.settings.VERSION = "1.0"
        mock_session.settings.FLAIR = "rocket"
        yield mock_session


def test_remove_file_existing_file():
    """Test removing an existing file."""
    with patch("os.path.isfile", return_value=True), patch("os.remove") as mock_remove:
        assert remove_file(Path("/path/to/file"))
        mock_remove.assert_called_once()


def test_remove_file_directory():
    """Test removing a directory."""
    with (
        patch("os.path.isfile", return_value=False),
        patch("os.path.isdir", return_value=True),
        patch("shutil.rmtree") as mock_rmtree,
    ):
        assert remove_file(Path("/path/to/directory"))
        mock_rmtree.assert_called_once()


def test_remove_file_failure(mock_session):
    """Test removing a file that fails."""
    with (
        patch("os.path.isfile", return_value=True),
        patch("os.remove", side_effect=Exception("Error")),
    ):
        assert not remove_file(Path("/path/to/file"))
        mock_session.console.print.assert_called()


def test_print_goodbye(mock_session):
    """Test printing the goodbye message."""
    print_goodbye()
    mock_session.console.print.assert_called()


def test_parse_and_split_input():
    """Test parsing and splitting user input."""
    user_input = "ls -f /home/user/docs/document.xlsx"
    result = parse_and_split_input(user_input, [])
    assert "ls" in result[0]


@pytest.mark.parametrize(
    "input_command, expected_output",
    [
        ("/", ["home"]),
        ("ls -f /path/to/file.txt", ["ls -f ", "path", "to", "file.txt"]),
        ("rm -f /home/user/docs", ["rm -f ", "home", "user", "docs"]),
    ],
)
def test_parse_and_split_input_special_cases(input_command, expected_output):
    """Test parsing and splitting user input with special cases."""
    result = parse_and_split_input(input_command, [])
    assert result == expected_output


def test_welcome_message(mock_session):
    """Test printing the welcome message."""
    welcome_message()
    mock_session.console.print.assert_called_with(
        "\nWelcome to OpenBB Platform CLI v1.0"
    )


def test_get_flair_and_username(mock_session):
    """Test getting the flair and username."""
    result = get_flair_and_username()
    assert "rocket" in result


@pytest.mark.parametrize(
    "value, expected",
    [
        ("10", 10),
        ("0", 0),
        ("-1", pytest.raises(argparse.ArgumentTypeError)),
        ("text", pytest.raises(ValueError)),
    ],
)
def test_check_non_negative(value, expected):
    """Test checking for a non-negative value."""
    if isinstance(expected, int):
        assert check_non_negative(value) == expected
    else:
        with expected:
            check_non_negative(value)


@pytest.mark.parametrize(
    "value, expected",
    [
        ("1", 1),
        ("0", pytest.raises(argparse.ArgumentTypeError)),
        ("-1", pytest.raises(argparse.ArgumentTypeError)),
        ("text", pytest.raises(ValueError)),
    ],
)
def test_check_positive(value, expected):
    """Test checking for a positive value."""
    if isinstance(expected, int):
        assert check_positive(value) == expected
    else:
        with expected:
            check_positive(value)


def test_get_user_agent():
    """Test getting the user agent."""
    result = get_user_agent()
    assert result.startswith("Mozilla/5.0")

```

## High-Level Overview

Test the Controller utils.

import argparse
from pathlib import Path
from unittest.mock import MagicMock, patch

import pytest
from openbb_cli.controllers.utils import (
check_non_negative,
check_positive,
get_flair_and_username,
get_user_agent,
parse_and_split_input,
print_goodbye,
remove_file,
welcome_message,
)

# pylint: disable=redefined-outer-name, unused-argument


## Detailed Structure

### Python File Structure

**Classes** (0):
None

**Functions** (12):
`mock_session`, `test_remove_file_existing_file`, `test_remove_file_directory`, `test_remove_file_failure`, `test_print_goodbye`, `test_parse_and_split_input`, `test_parse_and_split_input_special_cases`, `test_welcome_message`, `test_get_flair_and_username`, `test_check_non_negative`, `test_check_positive`, `test_get_user_agent`

**Imports** (7):
`argparse`, `pathlib`, `Path`, `unittest.mock`, `MagicMock`, `pytest`, `openbb_cli.controllers.utils`


## Key Components

No major components extracted.

## Usage & Examples

See source code for usage details.

## Related Files

- `argparse`
- `pathlib`
- `unittest.mock`
- `pytest`
- `openbb_cli.controllers.utils`

## Notes
- Generated: 2025-11-18T07:54:34.728035
- Generator: World's Best Repo Book Generator v1.0.0

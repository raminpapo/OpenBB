# Documentation: cli/tests/test_cli.py

## File Metadata
- **Path**: `cli/tests/test_cli.py`
- **Size**: 1,539 characters, 46 lines
- **Words**: 91
- **Extension**: .py
- **Classification**: Text file

## Original Source

```python
"""Test the CLI module."""

from unittest.mock import patch

from openbb_cli.cli import main


@patch("openbb_cli.config.setup.bootstrap")
@patch("openbb_cli.controllers.cli_controller.launch")
@patch("sys.argv", ["openbb", "--dev", "--debug"])
def test_main_with_dev_and_debug(mock_launch, mock_bootstrap):
    """Test the main function with dev and debug flags."""
    main()
    mock_bootstrap.assert_called_once()
    mock_launch.assert_called_once_with(True, True)


@patch("openbb_cli.config.setup.bootstrap")
@patch("openbb_cli.controllers.cli_controller.launch")
@patch("sys.argv", ["openbb"])
def test_main_without_arguments(mock_launch, mock_bootstrap):
    """Test the main function without arguments."""
    main()
    mock_bootstrap.assert_called_once()
    mock_launch.assert_called_once_with(False, False)


@patch("openbb_cli.config.setup.bootstrap")
@patch("openbb_cli.controllers.cli_controller.launch")
@patch("sys.argv", ["openbb", "--dev"])
def test_main_with_dev_only(mock_launch, mock_bootstrap):
    """Test the main function with dev flag only."""
    main()
    mock_bootstrap.assert_called_once()
    mock_launch.assert_called_once_with(True, False)


@patch("openbb_cli.config.setup.bootstrap")
@patch("openbb_cli.controllers.cli_controller.launch")
@patch("sys.argv", ["openbb", "--debug"])
def test_main_with_debug_only(mock_launch, mock_bootstrap):
    """Test the main function with debug flag only."""
    main()
    mock_bootstrap.assert_called_once()
    mock_launch.assert_called_once_with(False, True)

```

## High-Level Overview

Test the CLI module.

from unittest.mock import patch

from openbb_cli.cli import main


@patch("openbb_cli.config.setup.bootstrap")
@patch("openbb_cli.controllers.cli_controller.launch")
@patch("sys.argv", ["openbb", "--dev", "--debug"])
def test_main_with_dev_and_debug(mock_launch, mock_bootstrap):
Test the main function with dev and debug flags.
Test the main function without arguments.
main()
mock_bootstrap.assert_called_once()
mock_launch.assert_called_once_with(False, False)


@patch("openbb_cli.config.setup.bootstrap")
@patch("openbb_cli.controllers.cli_controller.launch")

## Detailed Structure

### Python File Structure

**Classes** (0):
None

**Functions** (4):
`test_main_with_dev_and_debug`, `test_main_without_arguments`, `test_main_with_dev_only`, `test_main_with_debug_only`

**Imports** (4):
`unittest.mock`, `patch`, `openbb_cli.cli`, `main`


## Key Components

No major components extracted.

## Usage & Examples

See source code for usage details.

## Related Files

- `unittest.mock`
- `openbb_cli.cli`

## Notes
- Generated: 2025-11-18T07:54:34.708668
- Generator: World's Best Repo Book Generator v1.0.0

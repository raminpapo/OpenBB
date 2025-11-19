# File Documentation: test_cli.py

## Metadata
- **Path**: `cli/tests/test_cli.py`
- **Size**: 1,539 bytes
- **Lines**: 46
- **Category**: python
- **Extension**: .py

---

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



---

## High-Level Overview

This is a **python** file named `test_cli.py`.

**Python Module**

- **Functions** (4): test_main_with_dev_and_debug, test_main_without_arguments, test_main_with_dev_only, test_main_with_debug_only
- **Import Statements**: 1


---

## Detailed Analysis

### Python Code Structure


#### Functions

- **`test_main_with_dev_and_debug(mock_launch, mock_bootstrap)`**
- **`test_main_without_arguments(mock_launch, mock_bootstrap)`**
- **`test_main_with_dev_only(mock_launch, mock_bootstrap)`**
- **`test_main_with_debug_only(mock_launch, mock_bootstrap)`**

#### Decorators Used

patch


---

## Related Files

The following files may be related based on imports and references:

**Imported Modules**:
- `main`
- `openbb_cli.cli`
- `patch`
- `unittest.mock`


---

## Performance & Security Notes

No obvious security concerns detected in static analysis.


---

**Generated**: 2025-11-19T02:16:44.914460Z
**Generator**: World's Best Repo Book Generator v1.0

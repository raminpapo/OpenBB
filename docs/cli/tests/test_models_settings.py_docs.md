# File Documentation: test_models_settings.py

## Metadata
- **Path**: `cli/tests/test_models_settings.py`
- **Size**: 2,617 bytes
- **Lines**: 70
- **Category**: python
- **Extension**: .py

---

## Original Source

```python
"""Test the Models Settings module."""

from unittest.mock import mock_open, patch

from openbb_cli.models.settings import Settings

# pylint: disable=unused-argument


def test_default_values():
    """Test the default values of the settings model."""
    fields = Settings.model_fields
    assert fields["TEST_MODE"].default is False
    assert fields["DEBUG_MODE"].default is False
    assert fields["DEV_BACKEND"].default is False
    assert fields["FILE_OVERWRITE"].default is False
    assert fields["SHOW_VERSION"].default is True
    assert fields["USE_INTERACTIVE_DF"].default is True
    assert fields["USE_CLEAR_AFTER_CMD"].default is False
    assert fields["USE_DATETIME"].default is True
    assert fields["USE_PROMPT_TOOLKIT"].default is True
    assert fields["ENABLE_EXIT_AUTO_HELP"].default is True
    assert fields["ENABLE_RICH_PANEL"].default is True
    assert fields["TOOLBAR_HINT"].default is True
    assert fields["SHOW_MSG_OBBJECT_REGISTRY"].default is False
    assert fields["TIMEZONE"].default == "America/New_York"
    assert fields["FLAIR"].default == ":openbb"
    assert fields["PREVIOUS_USE"].default is False
    assert fields["N_TO_KEEP_OBBJECT_REGISTRY"].default == 10
    assert fields["N_TO_DISPLAY_OBBJECT_REGISTRY"].default == 5
    assert fields["RICH_STYLE"].default == "dark"
    assert fields["ALLOWED_NUMBER_OF_ROWS"].default == 20
    assert fields["ALLOWED_NUMBER_OF_COLUMNS"].default == 5
    assert fields["HUB_URL"].default == "https://my.openbb.co"
    assert fields["BASE_URL"].default == "https://payments.openbb.co"


# Test __repr__ output
def test_repr():
    """Test the __repr__ method of the settings model."""
    settings = Settings()
    repr_str = settings.__repr__()  # pylint: disable=C2801
    assert "Settings\n\n" in repr_str


# Test loading from environment variables
@patch(
    "openbb_cli.models.settings.dotenv_values",
    return_value={"OPENBB_TEST_MODE": "True", "OPENBB_VERSION": "2.0.0"},
)
def test_from_env(mock_dotenv_values):
    """Test loading settings from environment variables."""
    settings = Settings.from_env({})  # type: ignore
    assert settings["TEST_MODE"] == "True"
    assert settings["VERSION"] == "2.0.0"


# Test setting an item and updating .env
@patch("openbb_cli.models.settings.set_key")
@patch(
    "openbb_cli.models.settings.open",
    new_callable=mock_open,
    read_data="TEST_MODE=False\n",
)
def test_set_item(mock_file, mock_set_key):
    """Test setting an item and updating the .env file."""
    settings = Settings()
    settings.set_item("TEST_MODE", True)
    assert settings.TEST_MODE is True

```



---

## High-Level Overview

This is a **python** file named `test_models_settings.py`.

**Python Module**

- **Functions** (4): test_default_values, test_repr, test_from_env, test_set_item
- **Import Statements**: 1


---

## Detailed Analysis

### Python Code Structure


#### Functions

- **`test_default_values()`**
- **`test_repr()`**
- **`test_from_env(mock_dotenv_values)`**
- **`test_set_item(mock_file, mock_set_key)`**

#### Decorators Used

patch


---

## Related Files

The following files may be related based on imports and references:

**Imported Modules**:
- `Settings`
- `mock_open`
- `openbb_cli.models.settings`
- `unittest.mock`


---

## Performance & Security Notes

No obvious security concerns detected in static analysis.


---

**Generated**: 2025-11-19T02:16:44.932820Z
**Generator**: World's Best Repo Book Generator v1.0

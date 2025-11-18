# Documentation: openbb_platform/core/tests/app/model/test_credentials.py

## File Metadata
- **Path**: `openbb_platform/core/tests/app/model/test_credentials.py`
- **Size**: 2,363 characters, 64 lines
- **Words**: 136
- **Extension**: .py
- **Classification**: Text file

## Original Source

```python
"""Test the Credentials model."""

import importlib
import json
from unittest.mock import mock_open, patch


# pylint: disable=import-outside-toplevel
def test_credentials():
    """Test the Credentials model."""
    with (
        patch(
            "openbb_core.app.model.credentials.ProviderInterface"
        ) as mock_provider_interface,
        patch.dict("os.environ", {"MOCK_ENV_API_KEY": "mock_env_key_value"}),
    ):
        mock_provider_interface.return_value.credentials = {
            "benzinga": ["benzinga_api_key"],
            "polygon": ["polygon_api_key"],
        }

        # Reload the module so CredentialsLoader picks up the patched environment
        import openbb_core.app.model.credentials as credentials_module

        importlib.reload(credentials_module)
        Credentials = credentials_module.Credentials

        creds = Credentials(
            benzinga_api_key="mock_benzinga_api_key",
            polygon_api_key="mock_polygon_api_key",
        )

        assert isinstance(creds, Credentials)
        assert creds.benzinga_api_key.get_secret_value() == "mock_benzinga_api_key"
        assert creds.polygon_api_key.get_secret_value() == "mock_polygon_api_key"
        assert creds.mock_env_api_key.get_secret_value() == "mock_env_key_value"


def test_credentials_env_overrides_null():
    """Environment variables replace stored null credentials."""
    fake_user_settings = json.dumps({"credentials": {"econdb_api_key": None}})
    with (
        patch(
            "openbb_core.app.model.credentials.ProviderInterface"
        ) as mock_provider_interface,
        patch("openbb_core.app.model.credentials.ExtensionLoader") as mock_loader,
        patch("openbb_core.app.model.credentials.Path.exists", return_value=True),
        patch("builtins.open", mock_open(read_data=fake_user_settings)),
        patch.dict("os.environ", {"ECONDB_API_KEY": "env_econdb_key"}),
    ):
        mock_provider_interface.return_value.credentials = {
            "econdb": ["econdb_api_key"]
        }
        mock_loader.return_value.obbject_objects = {}

        import openbb_core.app.model.credentials as credentials_module

        importlib.reload(credentials_module)
        Credentials = credentials_module.Credentials

        creds = Credentials()

        assert creds.econdb_api_key.get_secret_value() == "env_econdb_key"

```

## High-Level Overview

Test the Credentials model.

import importlib
import json
from unittest.mock import mock_open, patch


# pylint: disable=import-outside-toplevel
def test_credentials():
Test the Credentials model.
Reload the module so CredentialsLoader picks up the patched environment
Environment variables replace stored null credentials.
fake_user_settings = json.dumps({"credentials": {"econdb_api_key": None}})
with (
patch(
"openbb_core.app.model.credentials.ProviderInterface"
) as mock_provider_interface,
patch("openbb_core.app.model.credentials.ExtensionLoader") as mock_loader,
patch("openbb_core.app.model.credentials.Path.exists", return_value=True),
patch("builtins.open", mock_open(read_data=fake_user_settings)),

## Detailed Structure

### Python File Structure

**Classes** (0):
None

**Functions** (2):
`test_credentials`, `test_credentials_env_overrides_null`

**Imports** (6):
`importlib`, `json`, `unittest.mock`, `mock_open`, `openbb_core.app.model.credentials`, `openbb_core.app.model.credentials`


## Key Components

No major components extracted.

## Usage & Examples

See source code for usage details.

## Related Files

- `importlib`
- `json`
- `unittest.mock`
- `openbb_core.app.model.credentials`
- `openbb_core.app.model.credentials`

## Notes
- Generated: 2025-11-18T07:54:35.833019
- Generator: World's Best Repo Book Generator v1.0.0

# File Documentation: test_credentials.py

## Metadata
- **Path**: `openbb_platform/core/tests/app/model/test_credentials.py`
- **Size**: 2,363 bytes
- **Lines**: 64
- **Category**: python
- **Extension**: .py

---

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



---

## High-Level Overview

This is a **python** file named `test_credentials.py`.

**Python Module**

- **Functions** (2): test_credentials, test_credentials_env_overrides_null
- **Import Statements**: 3


---

## Detailed Analysis

### Python Code Structure


#### Functions

- **`test_credentials()`**
- **`test_credentials_env_overrides_null()`**


---

## Related Files

The following files may be related based on imports and references:

**Imported Modules**:
- `importlib`
- `json`
- `mock_open`
- `openbb_core.app.model.credentials`
- `unittest.mock`


---

## Performance & Security Notes

No obvious security concerns detected in static analysis.


---

**Generated**: 2025-11-19T02:16:46.665833Z
**Generator**: World's Best Repo Book Generator v1.0

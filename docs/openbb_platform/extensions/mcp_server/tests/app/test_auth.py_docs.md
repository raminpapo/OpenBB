# Documentation: openbb_platform/extensions/mcp_server/tests/app/test_auth.py

## File Metadata
- **Path**: `openbb_platform/extensions/mcp_server/tests/app/test_auth.py`
- **Size**: 4,946 characters, 142 lines
- **Words**: 348
- **Extension**: .py
- **Classification**: Text file

## Original Source

```python
"""Test the auth module."""

from unittest.mock import patch

import pytest
from fastapi import HTTPException
from openbb_mcp_server.app.auth import TokenAuthProvider, get_auth_provider
from openbb_mcp_server.models.settings import MCPSettings
from starlette.datastructures import Headers
from starlette.requests import Request

# pylint: disable=W0621


@pytest.fixture
def mock_settings():
    """Fixture for mock MCPSettings."""
    settings = MCPSettings()
    settings.server_auth = ("testuser", "testpass")
    return settings


@pytest.fixture
def mock_settings_no_auth():
    """Fixture for mock MCPSettings without server_auth."""
    return MCPSettings()


@pytest.fixture
def mock_request_with_auth(token="valid_token"):  # noqa: S107
    """Fixture for a mock request with an Authorization header."""
    request = Request(
        scope={
            "type": "http",
            "headers": Headers({"authorization": f"Bearer {token}"}).raw,
        }
    )
    return request


@pytest.fixture
def mock_request_without_auth():
    """Fixture for a mock request without an Authorization header."""
    request = Request(scope={"type": "http", "headers": []})
    return request


@pytest.mark.asyncio
@patch("openbb_mcp_server.app.auth.base64")
@patch("openbb_mcp_server.app.auth.secrets")
async def test_authorize_success(
    mock_secrets, mock_base64, mock_settings, mock_request_with_auth
):
    """Test successful authorization."""
    mock_base64.b64decode.return_value.decode.return_value = "testuser:testpass"
    mock_secrets.compare_digest.return_value = True
    auth_provider = TokenAuthProvider(mock_settings)
    result = await auth_provider.authorize(mock_request_with_auth)
    assert result is True
    assert hasattr(mock_request_with_auth.state, "user")


@pytest.mark.asyncio
async def test_authorize_no_auth_configured(
    mock_settings_no_auth, mock_request_with_auth
):
    """Test authorization when no auth is configured."""
    auth_provider = TokenAuthProvider(mock_settings_no_auth)
    result = await auth_provider.authorize(mock_request_with_auth)
    assert result is True


@pytest.mark.asyncio
async def test_authorize_no_header(mock_settings, mock_request_without_auth):
    """Test authorization failure when no header is present."""
    auth_provider = TokenAuthProvider(mock_settings)
    with pytest.raises(HTTPException) as excinfo:
        await auth_provider.authorize(mock_request_without_auth)
    assert excinfo.value.status_code == 401


@pytest.mark.asyncio
async def test_authorize_wrong_scheme(mock_settings):
    """Test authorization failure with the wrong scheme."""
    request = Request(
        scope={
            "type": "http",
            "headers": Headers({"authorization": "Basic some_token"}).raw,
        }
    )
    auth_provider = TokenAuthProvider(mock_settings)
    with pytest.raises(HTTPException) as excinfo:
        await auth_provider.authorize(request)
    assert excinfo.value.status_code == 401


@pytest.mark.asyncio
@patch("openbb_mcp_server.app.auth.base64")
@patch("openbb_mcp_server.app.auth.secrets")
async def test_authorize_invalid_token(
    mock_secrets, mock_base64, mock_settings, mock_request_with_auth
):
    """Test authorization failure with an invalid token."""
    mock_base64.b64decode.return_value.decode.return_value = "wronguser:wrongpass"
    mock_secrets.compare_digest.return_value = False
    auth_provider = TokenAuthProvider(mock_settings)
    with pytest.raises(HTTPException) as excinfo:
        await auth_provider.authorize(mock_request_with_auth)
    assert excinfo.value.status_code == 401


@pytest.mark.asyncio
@patch("openbb_mcp_server.app.auth.base64")
@patch("openbb_mcp_server.app.auth.secrets")
async def test_verify_token_success(mock_secrets, mock_base64, mock_settings):
    """Test successful token verification."""
    mock_base64.b64decode.return_value.decode.return_value = "testuser:testpass"
    mock_secrets.compare_digest.return_value = True
    auth_provider = TokenAuthProvider(mock_settings)
    auth_info = await auth_provider.verify_token("valid_token")
    assert auth_info is not None
    assert auth_info.client_id == "testuser"


@pytest.mark.asyncio
@patch("openbb_mcp_server.app.auth.base64")
@patch("openbb_mcp_server.app.auth.secrets")
async def test_verify_token_invalid(mock_secrets, mock_base64, mock_settings):
    """Test token verification failure."""
    mock_base64.b64decode.return_value.decode.return_value = "wronguser:wrongpass"
    mock_secrets.compare_digest.return_value = False
    auth_provider = TokenAuthProvider(mock_settings)
    auth_info = await auth_provider.verify_token("invalid_token")
    assert auth_info is None


def test_get_auth_provider(mock_settings):
    """Test the get_auth_provider function."""
    provider = get_auth_provider(mock_settings)
    assert isinstance(provider, TokenAuthProvider)
    assert provider.server_auth == ("testuser", "testpass")

```

## High-Level Overview

Test the auth module.

from unittest.mock import patch

import pytest
from fastapi import HTTPException
from openbb_mcp_server.app.auth import TokenAuthProvider, get_auth_provider
from openbb_mcp_server.models.settings import MCPSettings
from starlette.datastructures import Headers
from starlette.requests import Request

# pylint: disable=W0621


@pytest.fixture
def mock_settings():
Fixture for mock MCPSettings.
Fixture for mock MCPSettings without server_auth.
return MCPSettings()


## Detailed Structure

### Python File Structure

**Classes** (0):
None

**Functions** (12):
`mock_settings`, `mock_settings_no_auth`, `mock_request_with_auth`, `mock_request_without_auth`, `test_authorize_success`, `test_authorize_no_auth_configured`, `test_authorize_no_header`, `test_authorize_wrong_scheme`, `test_authorize_invalid_token`, `test_verify_token_success`, `test_verify_token_invalid`, `test_get_auth_provider`

**Imports** (13):
`unittest.mock`, `patch`, `pytest`, `fastapi`, `HTTPException`, `openbb_mcp_server.app.auth`, `TokenAuthProvider`, `openbb_mcp_server.models.settings`, `MCPSettings`, `starlette.datastructures`, `Headers`, `starlette.requests`, `Request`


## Key Components

No major components extracted.

## Usage & Examples

See source code for usage details.

## Related Files

- `unittest.mock`
- `pytest`
- `fastapi`
- `openbb_mcp_server.app.auth`
- `openbb_mcp_server.models.settings`
- `starlette.datastructures`
- `starlette.requests`

## Notes
- Generated: 2025-11-18T07:54:36.219237
- Generator: World's Best Repo Book Generator v1.0.0

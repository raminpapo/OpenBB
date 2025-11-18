# Documentation: openbb_platform/extensions/mcp_server/openbb_mcp_server/app/auth.py

## File Metadata
- **Path**: `openbb_platform/extensions/mcp_server/openbb_mcp_server/app/auth.py`
- **Size**: 3,814 characters, 111 lines
- **Words**: 278
- **Extension**: .py
- **Classification**: Text file

## Original Source

```python
"""Custom authentication for the MCP server."""

import base64
import binascii
import secrets

from fastapi import HTTPException
from fastmcp.server.auth.auth import AuthProvider
from mcp.server.auth.provider import AccessToken
from starlette.requests import Request

from openbb_mcp_server.models.settings import MCPSettings


class TokenAuthProvider(AuthProvider):
    """Token authentication provider for basic authentication via Bearer tokens."""

    def __init__(self, settings: MCPSettings):
        """Initialize the token auth provider."""
        super().__init__()
        self.server_auth = settings.server_auth
        uvicorn_config = settings.uvicorn_config or {}
        host = uvicorn_config.get("host", "127.0.0.1")
        port = uvicorn_config.get("port", "8001")
        use_https = uvicorn_config.get("ssl_keyfile") and uvicorn_config.get(
            "ssl_certfile"
        )
        scheme = "https" if use_https else "http"
        base_url = f"{scheme}://{host}:{port}"

        self.resource_server_url = f"{base_url}/mcp"
        self.authorization_url = f"{base_url}/mcp/auth"
        self.token_url = f"{base_url}/mcp/token"

    async def authorize(self, request: Request) -> bool:
        """Authorize the request."""
        if not self.server_auth:
            return True

        auth_header = request.headers.get("Authorization")
        if not auth_header:
            raise HTTPException(
                status_code=401,
                detail="Not authenticated",
                headers={"WWW-Authenticate": "Bearer"},
            )

        try:
            scheme, token = auth_header.split()
            if scheme.lower() != "bearer":
                raise ValueError("Invalid authentication scheme.")

            try:
                decoded = base64.b64decode(token).decode("utf-8")
                username, password = decoded.split(":", 1)
            except (binascii.Error, ValueError) as e:
                raise ValueError("Invalid base64-encoded token.") from e

            expected_username, expected_password = self.server_auth

            is_user_valid = secrets.compare_digest(username, expected_username)
            is_pass_valid = secrets.compare_digest(password, expected_password)

            if not (is_user_valid and is_pass_valid):
                raise ValueError("Invalid username or password.")

            request.state.user = {"username": username}
        except (ValueError, HTTPException) as e:
            detail = getattr(e, "detail", str(e))
            raise HTTPException(
                status_code=401,
                detail=detail,
                headers={"WWW-Authenticate": "Bearer"},
            ) from e

        return True

    async def verify_token(self, token: str) -> AccessToken | None:
        """Verify the token."""
        if not self.server_auth:
            return None

        try:
            try:
                decoded = base64.b64decode(token).decode("utf-8")
                username, password = decoded.split(":", 1)
            except (binascii.Error, ValueError):
                return None

            expected_username, expected_password = self.server_auth

            is_user_valid = secrets.compare_digest(username, expected_username)
            is_pass_valid = secrets.compare_digest(password, expected_password)

            if not (is_user_valid and is_pass_valid):
                return None

            return AccessToken(
                token=token,
                client_id=username,
                scopes=[],
                expires_at=None,
            )
        except (ValueError, HTTPException):
            return None


def get_auth_provider(settings: MCPSettings) -> TokenAuthProvider:
    """Get the authentication provider."""
    return TokenAuthProvider(settings)

```

## High-Level Overview

Custom authentication for the MCP server.

import base64
import binascii
import secrets

from fastapi import HTTPException
from fastmcp.server.auth.auth import AuthProvider
from mcp.server.auth.provider import AccessToken
from starlette.requests import Request

from openbb_mcp_server.models.settings import MCPSettings


class TokenAuthProvider(AuthProvider):
Token authentication provider for basic authentication via Bearer tokens.
Initialize the token auth provider.
super().__init__()
self.server_auth = settings.server_auth
uvicorn_config = settings.uvicorn_config or {}

## Detailed Structure

### Python File Structure

**Classes** (1):
`TokenAuthProvider`

**Functions** (4):
`__init__`, `authorize`, `verify_token`, `get_auth_provider`

**Imports** (15):
`base64`, `binascii`, `secrets`, `fastapi`, `HTTPException`, `fastmcp.server.auth.auth`, `AuthProvider`, `mcp.server.auth.provider`, `AccessToken`, `starlette.requests`, `Request`, `openbb_mcp_server.models.settings`, `MCPSettings`, `e`, `e`


## Key Components

**Class `TokenAuthProvider`**: Token authentication provider for basic authentication via Bearer tokens.

## Usage & Examples

See source code for usage details.

## Related Files

- `base64`
- `binascii`
- `secrets`
- `fastapi`
- `fastmcp.server.auth.auth`
- `mcp.server.auth.provider`
- `starlette.requests`
- `openbb_mcp_server.models.settings`

## Notes
- Generated: 2025-11-18T07:54:36.185972
- Generator: World's Best Repo Book Generator v1.0.0

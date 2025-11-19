# File Documentation: test_mcp_settings.py

## Metadata
- **Path**: `openbb_platform/extensions/mcp_server/tests/models/test_mcp_settings.py`
- **Size**: 2,393 bytes
- **Lines**: 66
- **Category**: python
- **Extension**: .py

---

## Original Source

```python
"""Unit tests for MCPSettings model."""

from openbb_mcp_server.models.settings import MCPSettings


def test_mcp_settings_defaults():
    """Test the default values of MCPSettings."""
    settings = MCPSettings()
    assert settings.name == "OpenBB MCP"
    assert settings.default_tool_categories == ["all"]
    assert settings.allowed_tool_categories is None
    assert settings.enable_tool_discovery is True
    assert settings.describe_responses is False


def test_mcp_settings_validation():
    """Test the validation of MCPSettings."""
    settings = MCPSettings(
        default_tool_categories="cat1,cat2",
        allowed_tool_categories="cat3",  # type: ignore
    )
    assert settings.default_tool_categories == ["cat1", "cat2"]
    assert settings.allowed_tool_categories == ["cat3"]


def test_mcp_settings_repr():
    """Test the string representation of MCPSettings."""
    settings = MCPSettings(name="Test")  # type: ignore
    repr_str = repr(settings)
    assert "MCPSettings" in repr_str
    assert "name: Test" in repr_str


def test_get_fastmcp_kwargs():
    """Test the get_fastmcp_kwargs method."""
    settings = MCPSettings(name="TestMCP", version="1.0", cache_expiration_seconds=3600)  # type: ignore
    kwargs = settings.get_fastmcp_kwargs()
    assert kwargs["name"] == "TestMCP"
    assert kwargs["version"] == "1.0"
    assert kwargs["cache_expiration_seconds"] == 3600
    assert "api_prefix" not in kwargs


def test_get_http_run_kwargs():
    """Test the get_http_run_kwargs method."""
    settings = MCPSettings(uvicorn_config={"host": "0.0.0.0", "port": 9000})  # type: ignore  # noqa: S104
    kwargs = settings.get_http_run_kwargs()
    assert kwargs["uvicorn_config"]["host"] == "0.0.0.0"  # noqa: S104
    assert kwargs["uvicorn_config"]["port"] == 9000


def test_get_httpx_kwargs():
    """Test the get_httpx_kwargs method."""
    settings = MCPSettings(httpx_client_kwargs={"timeout": 120})  # type: ignore
    kwargs = settings.get_httpx_kwargs()
    assert kwargs["timeout"] == 120


def test_update_settings():
    """Test updating settings from another MCPSettings instance."""
    settings1 = MCPSettings(name="Initial")  # type: ignore
    settings2 = MCPSettings(name="Updated", describe_responses=True)  # type: ignore
    settings1.update(settings2)
    assert settings1.name == "Updated"
    assert settings1.describe_responses is True

```



---

## High-Level Overview

This is a **python** file named `test_mcp_settings.py`.

**Python Module**

- **Functions** (7): test_mcp_settings_defaults, test_mcp_settings_validation, test_mcp_settings_repr, test_get_fastmcp_kwargs, test_get_http_run_kwargs, test_get_httpx_kwargs, test_update_settings
- **Import Statements**: 1


---

## Detailed Analysis

### Python Code Structure


#### Functions

- **`test_mcp_settings_defaults()`**
- **`test_mcp_settings_validation()`**
- **`test_mcp_settings_repr()`**
- **`test_get_fastmcp_kwargs()`**
- **`test_get_http_run_kwargs()`**
- **`test_get_httpx_kwargs()`**
- **`test_update_settings()`**


---

## Related Files

The following files may be related based on imports and references:

**Imported Modules**:
- `MCPSettings`
- `openbb_mcp_server.models.settings`


---

## Performance & Security Notes

No obvious security concerns detected in static analysis.


---

**Generated**: 2025-11-19T02:16:47.139403Z
**Generator**: World's Best Repo Book Generator v1.0

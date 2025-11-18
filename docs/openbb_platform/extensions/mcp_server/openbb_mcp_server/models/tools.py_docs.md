# Documentation: openbb_platform/extensions/mcp_server/openbb_mcp_server/models/tools.py

## File Metadata
- **Path**: `openbb_platform/extensions/mcp_server/openbb_mcp_server/models/tools.py`
- **Size**: 709 characters, 38 lines
- **Words**: 74
- **Extension**: .py
- **Classification**: Text file

## Original Source

```python
"""Tool models for MCP server."""

from typing import Literal

from pydantic import BaseModel


class ToolInfo(BaseModel):
    """Information about a single tool."""

    name: str
    active: bool
    description: str


class SubcategoryInfo(BaseModel):
    """Metadata for a tool subcategory."""

    name: str
    tool_count: int


class CategoryInfo(BaseModel):
    """Metadata for a category of tools."""

    name: str
    subcategories: list[SubcategoryInfo]
    total_tools: int


class ToggleResult(BaseModel):
    """Result of a request to activate or deactivate one or more tools."""

    action: Literal["activated", "deactivated"]
    successful: list[str]
    failed: list[str]
    message: str

```

## High-Level Overview

Tool models for MCP server.

from typing import Literal

from pydantic import BaseModel


class ToolInfo(BaseModel):
Information about a single tool.
Metadata for a tool subcategory.

name: str
tool_count: int


class CategoryInfo(BaseModel):
Metadata for a category of tools.
Result of a request to activate or deactivate one or more tools.

action: Literal["activated", "deactivated"]

## Detailed Structure

### Python File Structure

**Classes** (4):
`ToolInfo`, `SubcategoryInfo`, `CategoryInfo`, `ToggleResult`

**Functions** (0):
None

**Imports** (4):
`typing`, `Literal`, `pydantic`, `BaseModel`


## Key Components

**Class `ToolInfo`**: Information about a single tool.

**Class `SubcategoryInfo`**: Metadata for a tool subcategory.

**Class `CategoryInfo`**: Metadata for a category of tools.

**Class `ToggleResult`**: Result of a request to activate or deactivate one or more tools.

## Usage & Examples

See source code for usage details.

## Related Files

- `typing`
- `pydantic`

## Notes
- Generated: 2025-11-18T07:54:36.194716
- Generator: World's Best Repo Book Generator v1.0.0

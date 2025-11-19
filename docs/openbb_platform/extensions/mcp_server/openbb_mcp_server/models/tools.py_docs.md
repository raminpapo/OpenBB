# File Documentation: tools.py

## Metadata
- **Path**: `openbb_platform/extensions/mcp_server/openbb_mcp_server/models/tools.py`
- **Size**: 709 bytes
- **Lines**: 38
- **Category**: python
- **Extension**: .py

---

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



---

## High-Level Overview

This is a **python** file named `tools.py`.

**Python Module**

- **Classes** (4): ToolInfo, SubcategoryInfo, CategoryInfo, ToggleResult
- **Import Statements**: 1


---

## Detailed Analysis

### Python Code Structure

#### Classes

- **`ToolInfo`**(BaseModel)
- **`SubcategoryInfo`**(BaseModel)
- **`CategoryInfo`**(BaseModel)
- **`ToggleResult`**(BaseModel)


---

## Related Files

The following files may be related based on imports and references:

**Imported Modules**:
- `BaseModel`
- `Literal`
- `pydantic`
- `typing`


---

## Performance & Security Notes

No obvious security concerns detected in static analysis.


---

**Generated**: 2025-11-19T02:16:47.114272Z
**Generator**: World's Best Repo Book Generator v1.0

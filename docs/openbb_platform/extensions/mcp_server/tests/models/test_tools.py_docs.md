# File Documentation: test_tools.py

## Metadata
- **Path**: `openbb_platform/extensions/mcp_server/tests/models/test_tools.py`
- **Size**: 1,495 bytes
- **Lines**: 49
- **Category**: python
- **Extension**: .py

---

## Original Source

```python
"""Unit tests for tools module."""

from openbb_mcp_server.models.tools import (
    CategoryInfo,
    SubcategoryInfo,
    ToggleResult,
    ToolInfo,
)


def test_tool_info():
    """Test the ToolInfo model."""
    tool_info = ToolInfo(name="test_tool", active=True, description="A test tool.")
    assert tool_info.name == "test_tool"
    assert tool_info.active is True
    assert tool_info.description == "A test tool."


def test_subcategory_info():
    """Test the SubcategoryInfo model."""
    subcategory_info = SubcategoryInfo(name="test_sub", tool_count=5)
    assert subcategory_info.name == "test_sub"
    assert subcategory_info.tool_count == 5


def test_category_info():
    """Test the CategoryInfo model."""
    subcategories = [SubcategoryInfo(name="sub1", tool_count=2)]
    category_info = CategoryInfo(
        name="test_cat", subcategories=subcategories, total_tools=2
    )
    assert category_info.name == "test_cat"
    assert len(category_info.subcategories) == 1
    assert category_info.total_tools == 2


def test_toggle_result():
    """Test the ToggleResult model."""
    toggle_result = ToggleResult(
        action="activated",
        successful=["tool1"],
        failed=["tool2"],
        message="Activated: tool1. Not found: tool2.",
    )
    assert toggle_result.action == "activated"
    assert toggle_result.successful == ["tool1"]
    assert toggle_result.failed == ["tool2"]
    assert toggle_result.message == "Activated: tool1. Not found: tool2."

```



---

## High-Level Overview

This is a **python** file named `test_tools.py`.

**Python Module**

- **Functions** (4): test_tool_info, test_subcategory_info, test_category_info, test_toggle_result


---

## Detailed Analysis

### Python Code Structure


#### Functions

- **`test_tool_info()`**
- **`test_subcategory_info()`**
- **`test_category_info()`**
- **`test_toggle_result()`**


---

## Related Files

The following files may be related based on imports and references:

**Imported Modules**:
- `openbb_mcp_server.models.tools`


---

## Performance & Security Notes

No obvious security concerns detected in static analysis.


---

**Generated**: 2025-11-19T02:16:47.142450Z
**Generator**: World's Best Repo Book Generator v1.0

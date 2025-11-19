# File Documentation: test_prompts.py

## Metadata
- **Path**: `openbb_platform/extensions/mcp_server/tests/models/test_prompts.py`
- **Size**: 3,555 bytes
- **Lines**: 104
- **Category**: python
- **Extension**: .py

---

## Original Source

```python
"""Unit tests for prompts module."""

import pytest
from fastmcp.exceptions import PromptError
from fastmcp.prompts.prompt import PromptArgument
from mcp.types import PromptMessage, TextContent
from openbb_mcp_server.models.prompts import StaticPrompt


@pytest.mark.asyncio
async def test_static_prompt_render_success():
    """Test successful rendering of StaticPrompt."""
    prompt = StaticPrompt(
        name="test_prompt",
        content="Hello, {name}!",
        arguments=[PromptArgument(name="name", required=True)],
    )
    rendered = await prompt.render(arguments={"name": "World"})
    assert rendered == [
        PromptMessage(
            role="user", content=TextContent(type="text", text="Hello, World!")
        )
    ]


@pytest.mark.asyncio
async def test_static_prompt_render_missing_required_argument():
    """Test rendering StaticPrompt with a missing required argument."""
    prompt = StaticPrompt(
        name="test_prompt",
        content="Hello, {name}!",
        arguments=[PromptArgument(name="name", required=True)],
    )
    with pytest.raises(PromptError, match="Missing required arguments: {'name'}"):
        await prompt.render(arguments={})


@pytest.mark.asyncio
async def test_static_prompt_render_missing_formatting_key():
    """Test rendering StaticPrompt with a missing formatting key."""
    prompt = StaticPrompt(name="test_prompt", content="Hello, {name}!")
    with pytest.raises(PromptError, match="Missing argument for formatting: 'name'"):
        await prompt.render(arguments={"wrong_key": "World"})


@pytest.mark.asyncio
async def test_static_prompt_render_no_arguments():
    """Test rendering StaticPrompt with no arguments."""
    prompt = StaticPrompt(name="test_prompt", content="Hello, World!")
    rendered = await prompt.render()
    assert rendered == [
        PromptMessage(
            role="user", content=TextContent(type="text", text="Hello, World!")
        )
    ]


@pytest.mark.asyncio
async def test_static_prompt_render_optional_argument():
    """Test rendering StaticPrompt with an optional argument."""
    prompt = StaticPrompt(
        name="test_prompt",
        content="Hello, {name}!",
        arguments=[PromptArgument(name="name", required=False)],
    )
    rendered = await prompt.render(arguments={"name": "Optional"})
    assert rendered == [
        PromptMessage(
            role="user", content=TextContent(type="text", text="Hello, Optional!")
        )
    ]


@pytest.mark.asyncio
async def test_static_prompt_render_multiple_arguments():
    """Test rendering StaticPrompt with multiple arguments."""
    prompt = StaticPrompt(
        name="test_prompt",
        content="Hello, {name}! Welcome to {place}.",
        arguments=[
            PromptArgument(name="name", required=True),
            PromptArgument(name="place", required=True),
        ],
    )
    rendered = await prompt.render(arguments={"name": "User", "place": "OpenBB"})
    assert rendered == [
        PromptMessage(
            role="user",
            content=TextContent(type="text", text="Hello, User! Welcome to OpenBB."),
        )
    ]


@pytest.mark.asyncio
async def test_static_prompt_render_with_none_arguments_in_prompt():
    """Test rendering StaticPrompt when arguments attribute is None."""
    prompt = StaticPrompt(name="test_prompt", content="Hello, World!", arguments=None)
    rendered = await prompt.render()
    assert rendered == [
        PromptMessage(
            role="user", content=TextContent(type="text", text="Hello, World!")
        )
    ]

```



---

## High-Level Overview

This is a **python** file named `test_prompts.py`.

**Python Module**

- **Functions** (7): test_static_prompt_render_success, test_static_prompt_render_missing_required_argument, test_static_prompt_render_missing_formatting_key, test_static_prompt_render_no_arguments, test_static_prompt_render_optional_argument, test_static_prompt_render_multiple_arguments, test_static_prompt_render_with_none_arguments_in_prompt
- **Import Statements**: 1


---

## Detailed Analysis

### Python Code Structure


#### Functions

- **`test_static_prompt_render_success()`**
- **`test_static_prompt_render_missing_required_argument()`**
- **`test_static_prompt_render_missing_formatting_key()`**
- **`test_static_prompt_render_no_arguments()`**
- **`test_static_prompt_render_optional_argument()`**
- **`test_static_prompt_render_multiple_arguments()`**
- **`test_static_prompt_render_with_none_arguments_in_prompt()`**

#### Decorators Used

pytest


---

## Related Files

The following files may be related based on imports and references:

**Imported Modules**:
- `PromptArgument`
- `PromptError`
- `PromptMessage`
- `StaticPrompt`
- `fastmcp.exceptions`
- `fastmcp.prompts.prompt`
- `mcp.types`
- `openbb_mcp_server.models.prompts`
- `pytest`


---

## Performance & Security Notes

No obvious security concerns detected in static analysis.


---

**Generated**: 2025-11-19T02:16:47.140975Z
**Generator**: World's Best Repo Book Generator v1.0

# Documentation: openbb_platform/extensions/mcp_server/tests/models/test_prompts.py

## File Metadata
- **Path**: `openbb_platform/extensions/mcp_server/tests/models/test_prompts.py`
- **Size**: 3,555 characters, 104 lines
- **Words**: 260
- **Extension**: .py
- **Classification**: Text file

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

## High-Level Overview

Unit tests for prompts module.

import pytest
from fastmcp.exceptions import PromptError
from fastmcp.prompts.prompt import PromptArgument
from mcp.types import PromptMessage, TextContent
from openbb_mcp_server.models.prompts import StaticPrompt


@pytest.mark.asyncio
async def test_static_prompt_render_success():
Test successful rendering of StaticPrompt.
Test rendering StaticPrompt with a missing required argument.
prompt = StaticPrompt(
name="test_prompt",
content="Hello, {name}!",
arguments=[PromptArgument(name="name", required=True)],
)
with pytest.raises(PromptError, match="Missing required arguments: {'name'}"):
await prompt.render(arguments={})

## Detailed Structure

### Python File Structure

**Classes** (0):
None

**Functions** (7):
`test_static_prompt_render_success`, `test_static_prompt_render_missing_required_argument`, `test_static_prompt_render_missing_formatting_key`, `test_static_prompt_render_no_arguments`, `test_static_prompt_render_optional_argument`, `test_static_prompt_render_multiple_arguments`, `test_static_prompt_render_with_none_arguments_in_prompt`

**Imports** (9):
`pytest`, `fastmcp.exceptions`, `PromptError`, `fastmcp.prompts.prompt`, `PromptArgument`, `mcp.types`, `PromptMessage`, `openbb_mcp_server.models.prompts`, `StaticPrompt`


## Key Components

No major components extracted.

## Usage & Examples

See source code for usage details.

## Related Files

- `pytest`
- `fastmcp.exceptions`
- `fastmcp.prompts.prompt`
- `mcp.types`
- `openbb_mcp_server.models.prompts`

## Notes
- Generated: 2025-11-18T07:54:36.228142
- Generator: World's Best Repo Book Generator v1.0.0

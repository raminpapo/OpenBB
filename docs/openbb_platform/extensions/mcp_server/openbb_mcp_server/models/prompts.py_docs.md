# Documentation: openbb_platform/extensions/mcp_server/openbb_mcp_server/models/prompts.py

## File Metadata
- **Path**: `openbb_platform/extensions/mcp_server/openbb_mcp_server/models/prompts.py`
- **Size**: 1,167 characters, 39 lines
- **Words**: 112
- **Extension**: .py
- **Classification**: Text file

## Original Source

```python
"""Custom Prompt classes for FastMCP."""

from typing import Any

from fastmcp.exceptions import PromptError
from fastmcp.prompts.prompt import Prompt
from mcp.types import PromptMessage, TextContent


class StaticPrompt(Prompt):
    """A prompt that is a static string template."""

    content: str

    async def render(
        self,
        arguments: dict[str, Any] | None = None,
    ) -> list[PromptMessage]:
        """Render the prompt with arguments."""
        args = arguments or {}

        # Validate required arguments
        if self.arguments:
            required = {arg.name for arg in self.arguments if arg.required}
            provided = set(args)
            missing = required - provided
            if missing:
                raise PromptError(f"Missing required arguments: {missing}")

        try:
            rendered_content = self.content.format(**args)
            return [
                PromptMessage(
                    role="user", content=TextContent(type="text", text=rendered_content)
                )
            ]
        except KeyError as e:
            raise PromptError(f"Missing argument for formatting: {e}") from e

```

## High-Level Overview

Custom Prompt classes for FastMCP.

from typing import Any

from fastmcp.exceptions import PromptError
from fastmcp.prompts.prompt import Prompt
from mcp.types import PromptMessage, TextContent


class StaticPrompt(Prompt):
A prompt that is a static string template.
Render the prompt with arguments.
args = arguments or {}

# Validate required arguments
if self.arguments:
required = {arg.name for arg in self.arguments if arg.required}
provided = set(args)
missing = required - provided
if missing:

## Detailed Structure

### Python File Structure

**Classes** (1):
`StaticPrompt`

**Functions** (1):
`render`

**Imports** (9):
`typing`, `Any`, `fastmcp.exceptions`, `PromptError`, `fastmcp.prompts.prompt`, `Prompt`, `mcp.types`, `PromptMessage`, `e`


## Key Components

**Class `StaticPrompt`**: A prompt that is a static string template.

## Usage & Examples

See source code for usage details.

## Related Files

- `typing`
- `fastmcp.exceptions`
- `fastmcp.prompts.prompt`
- `mcp.types`

## Notes
- Generated: 2025-11-18T07:54:36.190112
- Generator: World's Best Repo Book Generator v1.0.0

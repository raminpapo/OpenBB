# File Documentation: prompts.py

## Metadata
- **Path**: `openbb_platform/extensions/mcp_server/openbb_mcp_server/models/prompts.py`
- **Size**: 1,167 bytes
- **Lines**: 39
- **Category**: python
- **Extension**: .py

---

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



---

## High-Level Overview

This is a **python** file named `prompts.py`.

**Python Module**

- **Classes** (1): StaticPrompt
- **Functions** (1): render
- **Import Statements**: 1


---

## Detailed Analysis

### Python Code Structure

#### Classes

- **`StaticPrompt`**(Prompt)


---

## Related Files

The following files may be related based on imports and references:

**Imported Modules**:
- `Any`
- `Prompt`
- `PromptError`
- `PromptMessage`
- `fastmcp.exceptions`
- `fastmcp.prompts.prompt`
- `mcp.types`
- `typing`


---

## Performance & Security Notes

No obvious security concerns detected in static analysis.


---

**Generated**: 2025-11-19T02:16:47.107118Z
**Generator**: World's Best Repo Book Generator v1.0

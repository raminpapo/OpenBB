# File Documentation: console.py

## Metadata
- **Path**: `cli/openbb_cli/config/console.py`
- **Size**: 3,037 bytes
- **Lines**: 94
- **Category**: python
- **Extension**: .py

---

## Original Source

```python
"""OpenBB CLI Console Module."""

from typing import TYPE_CHECKING, Any

from rich import panel
from rich.console import Console as RichConsole
from rich.text import Text
from rich.theme import Theme

from openbb_cli.config.menu_text import RICH_TAGS

if TYPE_CHECKING:
    from openbb_cli.models.settings import Settings


class Console:
    """Create a rich console to wrap the console print with a Panel."""

    def __init__(
        self,
        settings: "Settings",
        style: dict[str, Any] | None = None,
    ):
        """Initialize the ConsoleAndPanel class."""
        self._console = RichConsole(
            theme=Theme(style),
            highlight=False,
            soft_wrap=True,
        )
        self._settings = settings
        self.menu_text = ""
        self.menu_path = ""

    @staticmethod
    def _filter_rich_tags(text):
        """Filter out rich tags from text."""
        for val in RICH_TAGS:
            text = text.replace(val, "")

        return text

    @staticmethod
    def _blend_text(
        message: str, color1: tuple[int, int, int], color2: tuple[int, int, int]
    ) -> Text:
        """Blend text from one color to another."""
        text = Text(message)
        r1, g1, b1 = color1
        r2, g2, b2 = color2
        dr = r2 - r1
        dg = g2 - g1
        db = b2 - b1
        size = len(text) + 5
        for index in range(size):
            blend = index / size
            color = f"#{int(r1 + dr * blend):02X}{int(g1 + dg * blend):02X}{int(b1 + db * blend):02X}"
            text.stylize(color, index, index + 1)
        return text

    def print(self, *args, **kwargs):
        """Print the text to the console."""
        if kwargs and "text" in list(kwargs) and "menu" in list(kwargs):
            if not self._settings.TEST_MODE:
                if self._settings.ENABLE_RICH_PANEL:
                    if self._settings.SHOW_VERSION:
                        version = self._settings.VERSION
                        version = f"[param]OpenBB Platform CLI v{version}[/param] (https://openbb.co)"
                    else:
                        version = (
                            "[param]OpenBB Platform CLI[/param] (https://openbb.co)"
                        )
                    self._console.print(
                        panel.Panel(
                            "\n" + kwargs["text"],
                            title=kwargs["menu"],
                            subtitle_align="right",
                            subtitle=version,
                        )
                    )

                else:
                    self._console.print(kwargs["text"])
            else:
                print(self._filter_rich_tags(kwargs["text"]))  # noqa: T201
        elif not self._settings.TEST_MODE:
            self._console.print(*args, **kwargs)
        else:
            print(*args, **kwargs)  # noqa: T201

    def input(self, *args, **kwargs):
        """Get input from the user."""
        self.print(*args, **kwargs, end="")
        return input()

```



---

## High-Level Overview

This is a **python** file named `console.py`.

**Python Module**

- **Classes** (1): Console
- **Functions** (5): __init__, _filter_rich_tags, _blend_text, print, input
- **Import Statements**: 2


---

## Detailed Analysis

### Python Code Structure

#### Classes

- **`Console`**

#### Functions

- **`__init__(
        self,
        settings: "Settings",
        style: dict[str, Any] | None = None,
    )`**
- **`_filter_rich_tags(text)`**
- **`print(self, *args, **kwargs)`**
- **`input(self, *args, **kwargs)`**

#### Decorators Used

staticmethod


---

## Related Files

The following files may be related based on imports and references:

**Imported Modules**:
- `Console`
- `RICH_TAGS`
- `Settings`
- `TYPE_CHECKING`
- `Text`
- `Theme`
- `openbb_cli.config.menu_text`
- `openbb_cli.models.settings`
- `panel`
- `rich`
- `rich.console`
- `rich.text`
- `rich.theme`
- `typing`


---

## Performance & Security Notes

### Security Considerations

- ⚠️ Uses `input()` - validate user input


---

**Generated**: 2025-11-19T02:15:18.847970Z
**Generator**: World's Best Repo Book Generator v1.0

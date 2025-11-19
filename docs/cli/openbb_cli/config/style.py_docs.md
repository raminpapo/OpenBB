# File Documentation: style.py

## Metadata
- **Path**: `cli/openbb_cli/config/style.py`
- **Size**: 3,480 bytes
- **Lines**: 107
- **Category**: python
- **Extension**: .py

---

## Original Source

```python
"""Chart and style helpers for Plotly."""

# pylint: disable=C0302,R0902,W3301
import json
from pathlib import Path
from typing import Any

from rich.console import Console

from openbb_cli.config.constants import STYLES_DIRECTORY

console = Console()


class Style:
    """The class that helps with handling of style configurations.

    It serves styles for 2 libraries. For `Plotly` this class serves absolute paths
    to the .pltstyle files. For `Plotly` and `Rich` this class serves custom
    styles as python dictionaries.
    """

    STYLES_REPO = STYLES_DIRECTORY

    console_styles_available: dict[str, Path] = {}
    console_style: dict[str, Any] = {}

    line_color: str = ""
    up_color: str = ""
    down_color: str = ""
    up_colorway: list[str] = []
    down_colorway: list[str] = []
    up_color_transparent: str = ""
    down_color_transparent: str = ""

    line_width: float = 1.5

    def __init__(
        self,
        style: str | None = "",
        directory: Path | None = None,
    ):
        """Initialize the class."""
        self._load(directory)
        self.apply(style, directory)

    def apply(self, style: str | None = None, directory: Path | None = None) -> None:
        """Apply the style to the console."""
        if style:
            if style in self.console_styles_available:
                json_path: Path | None = self.console_styles_available[style]
            else:
                self._load(directory)
                if style in self.console_styles_available:
                    json_path = self.console_styles_available[style]
                else:
                    console.print(f"\nInvalid console style '{style}', using default.")
                    json_path = self.console_styles_available.get("dark", None)

            if json_path:
                self.console_style = self._from_json(json_path)
            else:
                console.print("Error loading default.")

    def _from_directory(self, folder: Path | None) -> None:
        """Load custom styles from folder.

        Parses the styles/default and styles/user folders and loads style files.
        To be recognized files need to follow a naming convention:
        *.pltstyle        - plotly stylesheets
        *.richstyle.json  - rich stylesheets

        Parameters
        ----------
        folder : str
            Path to the folder containing the stylesheets
        """
        if not folder or not folder.exists():
            return

        for attr, ext in zip(
            ["console_styles_available"],
            [".richstyle.json"],
        ):
            for file in folder.rglob(f"*{ext}"):
                getattr(self, attr)[file.name.replace(ext, "")] = file

    def _load(self, directory: Path | None = None) -> None:
        """Load custom styles from default and user folders."""
        self._from_directory(self.STYLES_REPO)
        self._from_directory(directory)

    def _from_json(self, file: Path) -> dict[str, Any]:
        """Load style from json file."""
        with open(file) as f:
            json_style: dict = json.load(f)
            for key, value in json_style.items():
                json_style[key] = value.replace(
                    " ", ""
                )  # remove whitespaces so Rich can parse it
            return json_style

    @property
    def available_styles(self) -> list[str]:
        """Return available styles."""
        return list(self.console_styles_available.keys())

```



---

## High-Level Overview

This is a **python** file named `style.py`.

**Python Module**

- **Classes** (4): Style, that, serves, serves
- **Functions** (6): __init__, apply, _from_directory, _load, _from_json, available_styles
- **Import Statements**: 1


---

## Detailed Analysis

### Python Code Structure

#### Classes

- **`Style`**

#### Functions

- **`__init__(
        self,
        style: str | None = "",
        directory: Path | None = None,
    )`**

#### Decorators Used

property


---

## Related Files

The following files may be related based on imports and references:

**Imported Modules**:
- `Any`
- `Console`
- `Path`
- `STYLES_DIRECTORY`
- `json`
- `openbb_cli.config.constants`
- `pathlib`
- `rich.console`
- `typing`


---

## Performance & Security Notes

No obvious security concerns detected in static analysis.


---

**Generated**: 2025-11-19T02:15:18.853717Z
**Generator**: World's Best Repo Book Generator v1.0

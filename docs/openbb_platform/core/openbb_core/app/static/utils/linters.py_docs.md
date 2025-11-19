# File Documentation: linters.py

## Metadata
- **Path**: `openbb_platform/core/openbb_core/app/static/utils/linters.py`
- **Size**: 1,710 bytes
- **Lines**: 62
- **Category**: python
- **Extension**: .py

---

## Original Source

```python
"""Linters for the package."""

import shutil
import subprocess
from pathlib import Path
from typing import (
    Literal,
)

from openbb_core.app.static.utils.console import Console
from openbb_core.env import Env


class Linters:
    """Run the linters for the Platform."""

    def __init__(self, directory: Path, verbose: bool = False) -> None:
        """Initialize the linters."""
        self.directory = directory
        self.verbose = verbose
        self.console = Console(verbose)

    def print_separator(self, symbol: str, length: int = 122):
        """Print a separator."""
        self.console.log(symbol * length)

    def run(
        self,
        linter: Literal["black", "ruff"],
        flags: list[str] | None = None,
    ):
        """Run linter with flags."""
        if shutil.which(linter):
            self.console.log(f"\n* {linter}")
            self.print_separator("^")

            command = [linter]
            if flags:
                command.extend(flags)  # type: ignore
            subprocess.run(  # noqa: S603
                command + list(self.directory.glob("*.py")), check=False
            )

            self.print_separator("-")
        else:
            self.console.log(f"\n* {linter} not found")

    def black(self):
        """Run black."""
        flags = ["--line-length", "122"]
        if not self.verbose and not Env().DEBUG_MODE:
            flags.append("--quiet")
        self.run(linter="black", flags=flags)

    def ruff(self):
        """Run ruff."""
        self.black()
        flags = ["check", "--fix"]
        if not self.verbose and not Env().DEBUG_MODE:
            flags.append("--silent")
        self.run(linter="ruff", flags=flags)

```



---

## High-Level Overview

This is a **python** file named `linters.py`.

**Python Module**

- **Classes** (1): Linters
- **Functions** (5): __init__, print_separator, run, black, ruff
- **Import Statements**: 2


---

## Detailed Analysis

### Python Code Structure

#### Classes

- **`Linters`**

#### Functions

- **`print_separator(self, symbol: str, length: int = 122)`**
- **`run(
        self,
        linter: Literal["black", "ruff"],
        flags: list[str] | None = None,
    )`**
- **`black(self)`**
- **`ruff(self)`**


---

## Related Files

The following files may be related based on imports and references:

**Imported Modules**:
- `Console`
- `Env`
- `Path`
- `openbb_core.app.static.utils.console`
- `openbb_core.env`
- `pathlib`
- `shutil`
- `subprocess`
- `typing`


---

## Performance & Security Notes

### Security Considerations

- ⚠️ Uses subprocess - validate input carefully


---

**Generated**: 2025-11-19T02:16:46.318664Z
**Generator**: World's Best Repo Book Generator v1.0

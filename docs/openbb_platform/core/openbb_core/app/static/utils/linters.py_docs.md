# Documentation: openbb_platform/core/openbb_core/app/static/utils/linters.py

## File Metadata
- **Path**: `openbb_platform/core/openbb_core/app/static/utils/linters.py`
- **Size**: 1,710 characters, 62 lines
- **Words**: 151
- **Extension**: .py
- **Classification**: Text file

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

## High-Level Overview

Linters for the package.

import shutil
import subprocess
from pathlib import Path
from typing import (
Literal,
)

from openbb_core.app.static.utils.console import Console
from openbb_core.env import Env


class Linters:
Run the linters for the Platform.
Initialize the linters.
self.directory = directory
self.verbose = verbose
self.console = Console(verbose)


## Detailed Structure

### Python File Structure

**Classes** (1):
`Linters`

**Functions** (5):
`__init__`, `print_separator`, `run`, `black`, `ruff`

**Imports** (9):
`shutil`, `subprocess`, `pathlib`, `Path`, `typing`, `openbb_core.app.static.utils.console`, `Console`, `openbb_core.env`, `Env`


## Key Components

**Class `Linters`**: Run the linters for the Platform.

## Usage & Examples

See source code for usage details.

## Related Files

- `shutil`
- `subprocess`
- `pathlib`
- `typing`
- `openbb_core.app.static.utils.console`
- `openbb_core.env`

## Notes
- Generated: 2025-11-18T07:54:35.499358
- Generator: World's Best Repo Book Generator v1.0.0

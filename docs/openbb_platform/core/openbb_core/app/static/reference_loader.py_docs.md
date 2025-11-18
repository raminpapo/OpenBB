# Documentation: openbb_platform/core/openbb_core/app/static/reference_loader.py

## File Metadata
- **Path**: `openbb_platform/core/openbb_core/app/static/reference_loader.py`
- **Size**: 1,727 characters, 55 lines
- **Words**: 154
- **Extension**: .py
- **Classification**: Text file

## Original Source

```python
"""ReferenceLoader class for loading reference data from a file."""

import json
from pathlib import Path

from openbb_core.app.model.abstract.singleton import SingletonMeta


class ReferenceLoader(metaclass=SingletonMeta):
    """ReferenceLoader class for loading the `reference.json` file."""

    def __init__(self, directory: Path | None = None):
        """
        Initialize the ReferenceLoader with a specific directory.

        If no directory is provided, a default directory will be used.

        Attributes
        ----------
        directory : Optional[Path]
            The directory from which to load the assets where the reference file lives.
        """

        reference_path = (
            directory.joinpath(
                "reference.json"
                if str(directory).endswith("/assets")
                else "assets/reference.json"
            )
            if directory
            else self._get_default_directory().joinpath("reference.json")
        )
        self.directory = Path(reference_path).parent.resolve()
        self._reference = self._load(reference_path)

    @property
    def reference(self) -> dict[str, dict]:
        """Get the reference data."""
        return self._reference

    def _get_default_directory(self) -> Path:
        """Get the default directory for loading references."""
        default_path = Path(__file__).parents[3].resolve() / "openbb" / "assets"

        return default_path

    def _load(self, file_path: Path):
        """Load the reference data from a file."""
        try:
            with open(file_path, encoding="utf-8") as f:
                data = json.load(f)
        except FileNotFoundError:
            data = {}
        return data

```

## High-Level Overview

ReferenceLoader class for loading reference data from a file.

import json
from pathlib import Path

from openbb_core.app.model.abstract.singleton import SingletonMeta


class ReferenceLoader(metaclass=SingletonMeta):
ReferenceLoader class for loading the `reference.json` file.

Initialize the ReferenceLoader with a specific directory.

If no directory is provided, a default directory will be used.

Attributes
----------
directory : Optional[Path]
The directory from which to load the assets where the reference file lives.


## Detailed Structure

### Python File Structure

**Classes** (3):
`for`, `ReferenceLoader`, `for`

**Functions** (4):
`__init__`, `reference`, `_get_default_directory`, `_load`

**Imports** (8):
`a`, `json`, `pathlib`, `Path`, `openbb_core.app.model.abstract.singleton`, `SingletonMeta`, `which`, `a`


## Key Components

**Class `for`**: ReferenceLoader class for loading the `reference.json` file.

## Usage & Examples

See source code for usage details.

## Related Files

- `json`
- `pathlib`
- `openbb_core.app.model.abstract.singleton`

## Notes
- Generated: 2025-11-18T07:54:35.493664
- Generator: World's Best Repo Book Generator v1.0.0

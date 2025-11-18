# Documentation: cookiecutter/openbb_cookiecutter/__init__.py

## File Metadata
- **Path**: `cookiecutter/openbb_cookiecutter/__init__.py`
- **Size**: 232 characters, 11 lines
- **Words**: 26
- **Extension**: .py
- **Classification**: Text file

## Original Source

```python
"""OpenBB Cookiecutter Template."""

from pathlib import Path

__version__ = "0.4.0"


def get_template_path() -> Path:
    """Return the path to the cookiecutter template directory."""
    return Path(__file__).parent / "template"

```

## High-Level Overview

OpenBB Cookiecutter Template.

from pathlib import Path

__version__ = "0.4.0"


def get_template_path() -> Path:
Return the path to the cookiecutter template directory.

## Detailed Structure

### Python File Structure

**Classes** (0):
None

**Functions** (1):
`get_template_path`

**Imports** (2):
`pathlib`, `Path`


## Key Components

No major components extracted.

## Usage & Examples

See source code for usage details.

## Related Files

- `pathlib`

## Notes
- Generated: 2025-11-18T07:54:34.737709
- Generator: World's Best Repo Book Generator v1.0.0

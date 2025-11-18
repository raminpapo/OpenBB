# Documentation: build/pypi/openbb_platform/nightly.py

## File Metadata
- **Path**: `build/pypi/openbb_platform/nightly.py`
- **Size**: 2,705 characters, 87 lines
- **Words**: 227
- **Extension**: .py
- **Classification**: Text file

## Original Source

```python
import subprocess
import sys
from pathlib import Path
from typing import Any, Dict

import toml

PLATFORM_PATH = Path(__file__).parent.parent.parent.parent.resolve() / "openbb_platform"
PYPROJECT = PLATFORM_PATH / "pyproject.toml"

SUB_PACKAGES = {}
DEPENDENCIES: Dict[str, Any] = {}
PLUGINS: Dict[str, Dict] = {
    "openbb_core_extension": {},
    "openbb_provider_extension": {},
    "openbb_obbject_extension": {},
}
CMD = [sys.executable, "-m", "poetry", "build"]


PYPROJECT_TOML = toml.load(PYPROJECT)
POETRY_DICT: Dict[str, dict] = PYPROJECT_TOML["tool"]["poetry"]
POETRY_DICT.pop("extras", None)


original_pyproject = PYPROJECT.read_text()


def gather_metadata(sub_path: str):
    """Gather metadata from the pyproject.toml files.

    Parameters
    ----------
    sub_path : str
        The path to the sub packages.
    """
    for path in PLATFORM_PATH.rglob(f"{sub_path}/**/pyproject.toml"):
        pyproject_toml = toml.load(path)
        poetry_dict: Dict[str, dict] = pyproject_toml["tool"]["poetry"]
        package_name = poetry_dict["packages"][0]["include"]

        for extension in list(PLUGINS.keys()):
            PLUGINS[extension].update(poetry_dict.get("plugins", {}).get(extension, {}))

        DEPENDENCIES.update(pyproject_toml["tool"]["poetry"]["dependencies"])
        SUB_PACKAGES[package_name] = path.relative_to(PLATFORM_PATH).parent.as_posix()


def build():
    """Build the Platform package."""
    for sub_path in ["core", "providers", "extensions", "obbject_extensions"]:
        gather_metadata(sub_path)

    # need to pop these from the dependencies
    DEPENDENCIES.pop("openbb-core", None)

    # add the sub packages
    for package_name, path in SUB_PACKAGES.items():
        POETRY_DICT["packages"].append({"include": package_name, "from": f"./{path}"})

    # add the plugins extensions
    for extension, plugins in PLUGINS.items():
        POETRY_DICT.setdefault("plugins", {}).setdefault(extension, {}).update(plugins)

    # update the dependencies and platform poetry dict
    POETRY_DICT["dependencies"] = DEPENDENCIES
    PYPROJECT_TOML["tool"]["poetry"] = POETRY_DICT

    temp_pyproject = toml.dumps(PYPROJECT_TOML)

    try:
        with open(PYPROJECT, "w", encoding="utf-8", newline="\n") as f:
            f.write(temp_pyproject)

        subprocess.run(CMD, cwd=PLATFORM_PATH, check=True)  # noqa: S603,PLW1510
    except (Exception, KeyboardInterrupt) as e:
        print(e)  # noqa: T201
        print("Restoring pyproject.toml")  # noqa: T201

    # we restore the original pyproject.toml
    with open(PYPROJECT, "w", encoding="utf-8", newline="\n") as f:
        f.write(original_pyproject)


if __name__ == "__main__":
    build()

```

## High-Level Overview

Gather metadata from the pyproject.toml files.

Parameters
----------
sub_path : str
The path to the sub packages.

Build the Platform package.

## Detailed Structure

### Python File Structure

**Classes** (0):
None

**Functions** (2):
`gather_metadata`, `build`

**Imports** (9):
`subprocess`, `sys`, `pathlib`, `Path`, `typing`, `Any`, `toml`, `the`, `the`


## Key Components

No major components extracted.

## Usage & Examples

This file can be run as a script. See the `__main__` block for entry point.

## Related Files

- `subprocess`
- `sys`
- `pathlib`
- `typing`
- `toml`

## Notes
- Generated: 2025-11-18T07:54:34.603449
- Generator: World's Best Repo Book Generator v1.0.0

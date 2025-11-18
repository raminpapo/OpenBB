# Documentation: cookiecutter/openbb_cookiecutter/template/hooks/post_gen_project.py

## File Metadata
- **Path**: `cookiecutter/openbb_cookiecutter/template/hooks/post_gen_project.py`
- **Size**: 907 characters, 32 lines
- **Words**: 94
- **Extension**: .py
- **Classification**: Text file

## Original Source

```python
"""OpenBB Platform Extension post-generation script."""

import re
import sys

MODULE_REGEX = r"^[_a-zA-Z][_a-zA-Z0-9]+$"

MODULE_NAME = "{{ cookiecutter.package_name }}"
PROVIDER_NAME = "{{ cookiecutter.provider_name }}" or ""
ROUTER_NAME = "{{ cookiecutter.router_name }}" or ""
OBBJECT_NAME = "{{ cookiecutter.obbject_name }}" or ""

if not re.match(MODULE_REGEX, MODULE_NAME):
    print(f"ERROR: {MODULE_NAME} is not a valid Python package name.")

    sys.exit(1)

if PROVIDER_NAME and not re.match(MODULE_REGEX, PROVIDER_NAME):
    print(f"ERROR: {PROVIDER_NAME} should be in lower snakecase.")

    sys.exit(1)

if ROUTER_NAME and not re.match(MODULE_REGEX, ROUTER_NAME):
    print(f"ERROR: {ROUTER_NAME} should be in lower snakecase.")

    sys.exit(1)

if OBBJECT_NAME and not re.match(MODULE_REGEX, OBBJECT_NAME):
    print(f"ERROR: {OBBJECT_NAME} should be in lower snakecase.")

    sys.exit(1)

```

## High-Level Overview

OpenBB Platform Extension post-generation script.

import re
import sys

MODULE_REGEX = r"^[_a-zA-Z][_a-zA-Z0-9]+$"

MODULE_NAME = "{{ cookiecutter.package_name }}"
PROVIDER_NAME = "{{ cookiecutter.provider_name }}" or ""
ROUTER_NAME = "{{ cookiecutter.router_name }}" or ""
OBBJECT_NAME = "{{ cookiecutter.obbject_name }}" or ""

if not re.match(MODULE_REGEX, MODULE_NAME):
print(f"ERROR: {MODULE_NAME} is not a valid Python package name.")

sys.exit(1)

if PROVIDER_NAME and not re.match(MODULE_REGEX, PROVIDER_NAME):
print(f"ERROR: {PROVIDER_NAME} should be in lower snakecase.")


## Detailed Structure

### Python File Structure

**Classes** (0):
None

**Functions** (0):
None

**Imports** (2):
`re`, `sys`


## Key Components

No major components extracted.

## Usage & Examples

See source code for usage details.

## Related Files

- `re`
- `sys`

## Notes
- Generated: 2025-11-18T07:54:34.740655
- Generator: World's Best Repo Book Generator v1.0.0

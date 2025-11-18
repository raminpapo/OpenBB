# Documentation: cookiecutter/openbb_cookiecutter/template/{{cookiecutter.project_tag}}/{{cookiecutter.package_name}}/routers/depends.py

## File Metadata
- **Path**: `cookiecutter/openbb_cookiecutter/template/{{cookiecutter.project_tag}}/{{cookiecutter.package_name}}/routers/depends.py`
- **Size**: 274 characters, 12 lines
- **Words**: 24
- **Extension**: .py
- **Classification**: Text file

## Original Source

```python
"""Router dependency injections."""

# pylint: disable=R0903

from typing import Annotated

import requests
from fastapi import Depends
from openbb_core.provider.utils.helpers import get_requests_session

Session = Annotated[requests.Session, Depends(get_requests_session)]

```

## High-Level Overview

Router dependency injections.

# pylint: disable=R0903

from typing import Annotated

import requests
from fastapi import Depends
from openbb_core.provider.utils.helpers import get_requests_session

Session = Annotated[requests.Session, Depends(get_requests_session)]


## Detailed Structure

### Python File Structure

**Classes** (0):
None

**Functions** (0):
None

**Imports** (7):
`typing`, `Annotated`, `requests`, `fastapi`, `Depends`, `openbb_core.provider.utils.helpers`, `get_requests_session`


## Key Components

No major components extracted.

## Usage & Examples

See source code for usage details.

## Related Files

- `typing`
- `requests`
- `fastapi`
- `openbb_core.provider.utils.helpers`

## Notes
- Generated: 2025-11-18T07:54:34.766486
- Generator: World's Best Repo Book Generator v1.0.0

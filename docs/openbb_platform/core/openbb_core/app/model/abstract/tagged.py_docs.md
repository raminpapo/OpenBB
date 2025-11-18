# Documentation: openbb_platform/core/openbb_core/app/model/abstract/tagged.py

## File Metadata
- **Path**: `openbb_platform/core/openbb_core/app/model/abstract/tagged.py`
- **Size**: 223 characters, 11 lines
- **Words**: 24
- **Extension**: .py
- **Classification**: Text file

## Original Source

```python
"""OpenBB Core App Abstract Model Tagged."""

from pydantic import BaseModel, Field
from uuid_extensions import uuid7str


class Tagged(BaseModel):
    """Model for Tagged."""

    id: str = Field(default_factory=uuid7str)

```

## High-Level Overview

OpenBB Core App Abstract Model Tagged.

from pydantic import BaseModel, Field
from uuid_extensions import uuid7str


class Tagged(BaseModel):
Model for Tagged.

## Detailed Structure

### Python File Structure

**Classes** (1):
`Tagged`

**Functions** (0):
None

**Imports** (4):
`pydantic`, `BaseModel`, `uuid_extensions`, `uuid7str`


## Key Components

**Class `Tagged`**: Model for Tagged.

## Usage & Examples

See source code for usage details.

## Related Files

- `pydantic`
- `uuid_extensions`

## Notes
- Generated: 2025-11-18T07:54:35.434896
- Generator: World's Best Repo Book Generator v1.0.0

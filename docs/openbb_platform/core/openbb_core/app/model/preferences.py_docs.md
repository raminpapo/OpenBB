# Documentation: openbb_platform/core/openbb_core/app/model/preferences.py

## File Metadata
- **Path**: `openbb_platform/core/openbb_core/app/model/preferences.py`
- **Size**: 1,249 characters, 36 lines
- **Words**: 126
- **Extension**: .py
- **Classification**: Text file

## Original Source

```python
"""Preferences for the OpenBB platform."""

from pathlib import Path
from typing import Literal

from pydantic import BaseModel, ConfigDict, Field, PositiveInt


class Preferences(BaseModel):
    """Preferences for the OpenBB platform."""

    cache_directory: str = str(Path.home() / "OpenBBUserData" / "cache")
    chart_style: Literal["dark", "light"] = "dark"
    data_directory: str = str(Path.home() / "OpenBBUserData")
    export_directory: str = str(Path.home() / "OpenBBUserData" / "exports")
    metadata: bool = True
    output_type: Literal[
        "OBBject", "dataframe", "polars", "numpy", "dict", "chart", "llm"
    ] = Field(
        default="OBBject",
        description="Python default output type.",
        validate_default=True,
    )
    request_timeout: PositiveInt = 60
    show_warnings: bool = False
    table_style: Literal["dark", "light"] = "dark"
    user_styles_directory: str = str(Path.home() / "OpenBBUserData" / "styles" / "user")

    model_config = ConfigDict(validate_assignment=True)

    def __repr__(self) -> str:
        """Return a string representation of the model."""
        return f"{self.__class__.__name__}\n\n" + "\n".join(
            f"{k}: {v}" for k, v in self.model_dump().items()
        )

```

## High-Level Overview

Preferences for the OpenBB platform.

from pathlib import Path
from typing import Literal

from pydantic import BaseModel, ConfigDict, Field, PositiveInt


class Preferences(BaseModel):
Preferences for the OpenBB platform.
Return a string representation of the model.
return f"{self.__class__.__name__}\n\n" + "\n".join(
f"{k}: {v}" for k, v in self.model_dump().items()
)


## Detailed Structure

### Python File Structure

**Classes** (1):
`Preferences`

**Functions** (1):
`__repr__`

**Imports** (6):
`pathlib`, `Path`, `typing`, `Literal`, `pydantic`, `BaseModel`


## Key Components

**Class `Preferences`**: Preferences for the OpenBB platform.

## Usage & Examples

See source code for usage details.

## Related Files

- `pathlib`
- `typing`
- `pydantic`

## Notes
- Generated: 2025-11-18T07:54:35.458071
- Generator: World's Best Repo Book Generator v1.0.0

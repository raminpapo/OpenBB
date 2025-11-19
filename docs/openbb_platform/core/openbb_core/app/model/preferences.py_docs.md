# File Documentation: preferences.py

## Metadata
- **Path**: `openbb_platform/core/openbb_core/app/model/preferences.py`
- **Size**: 1,249 bytes
- **Lines**: 36
- **Category**: python
- **Extension**: .py

---

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



---

## High-Level Overview

This is a **python** file named `preferences.py`.

**Python Module**

- **Classes** (1): Preferences
- **Functions** (1): __repr__
- **Import Statements**: 1


---

## Detailed Analysis

### Python Code Structure

#### Classes

- **`Preferences`**(BaseModel)


---

## Related Files

The following files may be related based on imports and references:

**Imported Modules**:
- `BaseModel`
- `Literal`
- `Path`
- `pathlib`
- `pydantic`
- `typing`


---

## Performance & Security Notes

No obvious security concerns detected in static analysis.


---

**Generated**: 2025-11-19T02:16:46.262196Z
**Generator**: World's Best Repo Book Generator v1.0

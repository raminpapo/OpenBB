# File Documentation: defaults.py

## Metadata
- **Path**: `openbb_platform/core/openbb_core/app/model/defaults.py`
- **Size**: 1,985 bytes
- **Lines**: 57
- **Category**: python
- **Extension**: .py

---

## Original Source

```python
"""Defaults model."""

from typing import Any
from warnings import warn

from openbb_core.app.model.abstract.warning import OpenBBWarning
from pydantic import BaseModel, ConfigDict, Field, model_validator


class Defaults(BaseModel):
    """Defaults."""

    model_config = ConfigDict(validate_assignment=True, populate_by_name=True)

    commands: dict[str, dict[str, Any]] = Field(
        default_factory=dict,
        alias="routes",
    )

    def __repr__(self) -> str:
        """Return string representation."""
        return f"{self.__class__.__name__}\n\n" + "\n".join(
            f"{k}: {v}" for k, v in self.model_dump().items()
        )

    @model_validator(mode="before")
    @classmethod
    def validate_before(cls, values: dict) -> dict:
        """Validate model (before)."""
        key = "commands"
        if "routes" in values:
            if not values.get("routes"):
                del values["routes"]
            show_warnings = values.get("preferences", {}).get("show_warnings")
            if show_warnings is False or show_warnings in ["False", "false"]:
                warn(
                    message="The 'routes' key is deprecated within 'defaults' of 'user_settings.json'."
                    + " Suppress this warning by updating the key to 'commands'.",
                    category=OpenBBWarning,
                )
                key = "routes"

        new_values: dict = {"commands": {}}
        for k, v in values.get(key, {}).items():
            clean_k = k.strip("/").replace("/", ".")
            provider = v.get("provider") if v else None
            if isinstance(provider, str):
                v["provider"] = [provider]
            new_values["commands"][clean_k] = v

        return new_values

    def update(self, incoming: "Defaults"):
        """Update current defaults."""
        incoming_commands = incoming.model_dump(exclude_none=True).get("commands", {})
        self.__dict__["commands"].update(incoming_commands)

```



---

## High-Level Overview

This is a **python** file named `defaults.py`.

**Python Module**

- **Classes** (1): Defaults
- **Functions** (3): __repr__, validate_before, update
- **Import Statements**: 1


---

## Detailed Analysis

### Python Code Structure

#### Classes

- **`Defaults`**(BaseModel)

#### Functions

- **`update(self, incoming: "Defaults")`**

#### Decorators Used

classmethod, model_validator


---

## Related Files

The following files may be related based on imports and references:

**Imported Modules**:
- `Any`
- `BaseModel`
- `OpenBBWarning`
- `openbb_core.app.model.abstract.warning`
- `pydantic`
- `typing`
- `warn`
- `warnings`


---

## Performance & Security Notes

No obvious security concerns detected in static analysis.


---

**Generated**: 2025-11-19T02:16:46.250862Z
**Generator**: World's Best Repo Book Generator v1.0

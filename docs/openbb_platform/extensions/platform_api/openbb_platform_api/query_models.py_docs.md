# File Documentation: query_models.py

## Metadata
- **Path**: `openbb_platform/extensions/platform_api/openbb_platform_api/query_models.py`
- **Size**: 1,754 bytes
- **Lines**: 62
- **Category**: python
- **Extension**: .py

---

## Original Source

```python
"""OpenBB Workspace Query Models."""

from typing import Any

from openbb_core.provider.abstract.data import Data
from pydantic import AliasGenerator, ConfigDict, Field, field_validator
from pydantic.alias_generators import to_snake


class OmniWidgetInput(Data):
    """Input for OmniWidget."""

    model_config = ConfigDict(
        extra="allow",
        alias_generator=AliasGenerator(to_snake),
        title="OmniWidget Input Data for POST Request.",
        json_schema_extra={
            "x-widget_config": {
                "$.type": "omni",
            }
        },
    )

    prompt: Any | None = Field(
        default=None,
        description="The prompt text or JSON object sent from Workspace.",
        json_schema_extra={
            "x-widget_config": {
                "type": "text",
                "value": "",
                "description": "Input prompt value for the OmniWidget.",
                "show": False,
            }
        },
    )

    @field_validator("prompt", mode="before")
    @classmethod
    def _validate_prompt(cls, v):
        """Validate and parse the prompt field."""
        # pylint: disable=import-outside-toplevel
        import json
        import re

        if not v or v == "":
            return None

        prompt = ""

        try:
            prompt = json.loads(v)
        except json.JSONDecodeError:
            # Try to fix common JSON errors like trailing commas
            try:
                # Remove trailing commas in objects and arrays
                cleaned_prompt = re.sub(r",(\s*[}\]])", r"\1", prompt)
                prompt = json.loads(cleaned_prompt)
            except json.JSONDecodeError:
                prompt = v

        return prompt if prompt != "" else None

```



---

## High-Level Overview

This is a **python** file named `query_models.py`.

**Python Module**

- **Classes** (1): OmniWidgetInput
- **Functions** (1): _validate_prompt
- **Import Statements**: 2


---

## Detailed Analysis

### Python Code Structure

#### Classes

- **`OmniWidgetInput`**(Data)

#### Functions

- **`_validate_prompt(cls, v)`**

#### Decorators Used

classmethod, field_validator


---

## Related Files

The following files may be related based on imports and references:

**Imported Modules**:
- `AliasGenerator`
- `Any`
- `Data`
- `json`
- `openbb_core.provider.abstract.data`
- `pydantic`
- `pydantic.alias_generators`
- `re`
- `to_snake`
- `typing`


---

## Performance & Security Notes

No obvious security concerns detected in static analysis.


---

**Generated**: 2025-11-19T02:16:47.188308Z
**Generator**: World's Best Repo Book Generator v1.0

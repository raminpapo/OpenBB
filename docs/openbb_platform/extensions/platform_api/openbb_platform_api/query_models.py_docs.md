# Documentation: openbb_platform/extensions/platform_api/openbb_platform_api/query_models.py

## File Metadata
- **Path**: `openbb_platform/extensions/platform_api/openbb_platform_api/query_models.py`
- **Size**: 1,754 characters, 62 lines
- **Words**: 159
- **Extension**: .py
- **Classification**: Text file

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

## High-Level Overview

OpenBB Workspace Query Models.

from typing import Any

from openbb_core.provider.abstract.data import Data
from pydantic import AliasGenerator, ConfigDict, Field, field_validator
from pydantic.alias_generators import to_snake


class OmniWidgetInput(Data):
Input for OmniWidget.
Validate and parse the prompt field.
# pylint: disable=import-outside-toplevel
import json
import re

if not v or v == "":
return None

prompt = ""

## Detailed Structure

### Python File Structure

**Classes** (1):
`OmniWidgetInput`

**Functions** (1):
`_validate_prompt`

**Imports** (11):
`typing`, `Any`, `openbb_core.provider.abstract.data`, `Data`, `pydantic`, `AliasGenerator`, `pydantic.alias_generators`, `to_snake`, `Workspace.`, `json`, `re`


## Key Components

**Class `OmniWidgetInput`**: Input for OmniWidget.

## Usage & Examples

See source code for usage details.

## Related Files

- `typing`
- `openbb_core.provider.abstract.data`
- `pydantic`
- `pydantic.alias_generators`
- `json`
- `re`

## Notes
- Generated: 2025-11-18T07:54:36.266548
- Generator: World's Best Repo Book Generator v1.0.0

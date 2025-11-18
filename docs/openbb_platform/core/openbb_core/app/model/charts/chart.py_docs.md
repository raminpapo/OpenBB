# Documentation: openbb_platform/core/openbb_core/app/model/charts/chart.py

## File Metadata
- **Path**: `openbb_platform/core/openbb_core/app/model/charts/chart.py`
- **Size**: 887 characters, 31 lines
- **Words**: 90
- **Extension**: .py
- **Classification**: Text file

## Original Source

```python
"""OpenBB Core Chart model."""

from typing import Any

from pydantic import BaseModel, ConfigDict, Field


class Chart(BaseModel):
    """Model for Chart."""

    content: dict[str, Any] | None = Field(
        default=None,
        description="Raw textual representation of the chart.",
    )
    format: str | None = Field(
        default=None,
        description="Complementary attribute to the `content` attribute. It specifies the format of the chart.",
    )
    fig: Any | None = Field(
        default=None,
        description="The figure object.",
        json_schema_extra={"exclude_from_api": True},
    )
    model_config = ConfigDict(validate_assignment=True)

    def __repr__(self) -> str:
        """Return string representation."""
        return f"{self.__class__.__name__}\n\n" + "\n".join(
            f"{k}: {v}" for k, v in self.model_dump().items()
        )

```

## High-Level Overview

OpenBB Core Chart model.

from typing import Any

from pydantic import BaseModel, ConfigDict, Field


class Chart(BaseModel):
Model for Chart.
Return string representation.
return f"{self.__class__.__name__}\n\n" + "\n".join(
f"{k}: {v}" for k, v in self.model_dump().items()
)


## Detailed Structure

### Python File Structure

**Classes** (1):
`Chart`

**Functions** (1):
`__repr__`

**Imports** (4):
`typing`, `Any`, `pydantic`, `BaseModel`


## Key Components

**Class `Chart`**: Model for Chart.

## Usage & Examples

See source code for usage details.

## Related Files

- `typing`
- `pydantic`

## Notes
- Generated: 2025-11-18T07:54:35.439604
- Generator: World's Best Repo Book Generator v1.0.0

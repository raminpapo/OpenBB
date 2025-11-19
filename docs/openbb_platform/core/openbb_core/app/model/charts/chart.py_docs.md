# File Documentation: chart.py

## Metadata
- **Path**: `openbb_platform/core/openbb_core/app/model/charts/chart.py`
- **Size**: 887 bytes
- **Lines**: 31
- **Category**: python
- **Extension**: .py

---

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



---

## High-Level Overview

This is a **python** file named `chart.py`.

**Python Module**

- **Classes** (1): Chart
- **Functions** (1): __repr__
- **Import Statements**: 1


---

## Detailed Analysis

### Python Code Structure

#### Classes

- **`Chart`**(BaseModel)


---

## Related Files

The following files may be related based on imports and references:

**Imported Modules**:
- `Any`
- `BaseModel`
- `pydantic`
- `typing`


---

## Performance & Security Notes

No obvious security concerns detected in static analysis.


---

**Generated**: 2025-11-19T02:16:46.277839Z
**Generator**: World's Best Repo Book Generator v1.0

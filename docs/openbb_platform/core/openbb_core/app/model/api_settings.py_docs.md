# File Documentation: api_settings.py

## Metadata
- **Path**: `openbb_platform/core/openbb_core/app/model/api_settings.py`
- **Size**: 1,833 bytes
- **Lines**: 56
- **Category**: python
- **Extension**: .py

---

## Original Source

```python
"""FastAPI configuration settings model."""

from pydantic import BaseModel, ConfigDict, Field, computed_field


class Cors(BaseModel):
    """Cors model for FastAPI configuration."""

    model_config = ConfigDict(frozen=True)

    allow_origins: list[str] = Field(default_factory=lambda: ["*"])
    allow_methods: list[str] = Field(default_factory=lambda: ["*"])
    allow_headers: list[str] = Field(default_factory=lambda: ["*"])


class Servers(BaseModel):
    """Servers model for FastAPI configuration."""

    model_config = ConfigDict(frozen=True)

    url: str = ""
    description: str = "Local OpenBB development server"


class APISettings(BaseModel):
    """Settings model for FastAPI configuration."""

    model_config = ConfigDict(frozen=True)

    version: str = "1"
    title: str = "OpenBB Platform API"
    description: str = "Investment research for everyone, anywhere."
    terms_of_service: str = "http://example.com/terms/"
    contact_name: str = "OpenBB Team"
    contact_url: str = "https://openbb.co"
    contact_email: str = "hello@openbb.co"
    license_name: str = "AGPLv3"
    license_url: str = "https://github.com/OpenBB-finance/OpenBB/blob/develop/LICENSE"
    servers: list[Servers] = Field(default_factory=lambda: [Servers()])
    cors: Cors = Field(default_factory=Cors)
    custom_headers: dict[str, str] | None = Field(
        default=None, description="Custom headers and respective default value."
    )

    @computed_field  # type: ignore[misc]
    @property
    def prefix(self) -> str:
        """Return the API prefix."""
        return f"/api/v{self.version}"

    def __repr__(self) -> str:
        """Return a string representation of the model."""
        return f"{self.__class__.__name__}\n\n" + "\n".join(
            f"{k}: {v}" for k, v in self.model_dump().items()
        )

```



---

## High-Level Overview

This is a **python** file named `api_settings.py`.

**Python Module**

- **Classes** (3): Cors, Servers, APISettings
- **Functions** (2): prefix, __repr__
- **Import Statements**: 1


---

## Detailed Analysis

### Python Code Structure

#### Classes

- **`Cors`**(BaseModel)
- **`Servers`**(BaseModel)
- **`APISettings`**(BaseModel)

#### Decorators Used

computed_field, openbb, property


---

## Related Files

The following files may be related based on imports and references:

**Imported Modules**:
- `BaseModel`
- `pydantic`


---

## Performance & Security Notes

No obvious security concerns detected in static analysis.


---

**Generated**: 2025-11-19T02:16:46.245501Z
**Generator**: World's Best Repo Book Generator v1.0

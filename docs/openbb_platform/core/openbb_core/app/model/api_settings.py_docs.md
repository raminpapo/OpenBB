# Documentation: openbb_platform/core/openbb_core/app/model/api_settings.py

## File Metadata
- **Path**: `openbb_platform/core/openbb_core/app/model/api_settings.py`
- **Size**: 1,833 characters, 56 lines
- **Words**: 172
- **Extension**: .py
- **Classification**: Text file

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

## High-Level Overview

FastAPI configuration settings model.

from pydantic import BaseModel, ConfigDict, Field, computed_field


class Cors(BaseModel):
Cors model for FastAPI configuration.
Servers model for FastAPI configuration.

model_config = ConfigDict(frozen=True)

url: str = ""
description: str = "Local OpenBB development server"


class APISettings(BaseModel):
Settings model for FastAPI configuration.
Return the API prefix.
return f"/api/v{self.version}"


## Detailed Structure

### Python File Structure

**Classes** (3):
`Cors`, `Servers`, `APISettings`

**Functions** (2):
`prefix`, `__repr__`

**Imports** (2):
`pydantic`, `BaseModel`


## Key Components

**Class `Cors`**: Cors model for FastAPI configuration.

**Class `Servers`**: Servers model for FastAPI configuration.

**Class `APISettings`**: Settings model for FastAPI configuration.

## Usage & Examples

See source code for usage details.

## Related Files

- `pydantic`

## Notes
- Generated: 2025-11-18T07:54:35.437854
- Generator: World's Best Repo Book Generator v1.0.0

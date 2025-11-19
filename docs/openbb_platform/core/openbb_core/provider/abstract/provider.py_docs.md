# File Documentation: provider.py

## Metadata
- **Path**: `openbb_platform/core/openbb_core/provider/abstract/provider.py`
- **Size**: 2,022 bytes
- **Lines**: 55
- **Category**: python
- **Extension**: .py

---

## Original Source

```python
"""Provider Abstract Class."""

from openbb_core.provider.abstract.fetcher import Fetcher


class Provider:
    """Serves as provider extension entry point and must be created by each provider."""

    # pylint: disable=too-many-arguments,too-many-positional-arguments
    def __init__(
        self,
        name: str,
        description: str,
        website: str | None = None,
        credentials: list[str] | None = None,
        fetcher_dict: dict[str, type[Fetcher]] | None = None,
        repr_name: str | None = None,
        deprecated_credentials: dict[str, str | None] | None = None,
        instructions: str | None = None,
    ) -> None:
        """Initialize the provider.

        Parameters
        ----------
        name : str
            Name of the provider.
        description : str
            Description of the provider.
        website : Optional[str]
            Website of the provider, by default None.
        credentials : Optional[List[str]]
            List of required credentials, by default None.
        fetcher_dict : Optional[Dict[str, Type[Fetcher]]]
            Dictionary of fetchers, by default None.
        repr_name: Optional[str]
            Full name of the provider, by default None.
        deprecated_credentials: Optional[Dict[str, Optional[str]]]
            Map of deprecated credentials to its current name, by default None.
        instructions: Optional[str]
            Instructions on how to setup the provider. For example, how to get an API key.
        """
        self.name = name
        self.description = description
        self.website = website
        self.fetcher_dict = fetcher_dict or {}
        if credentials is None:
            self.credentials: list = []
        else:
            self.credentials = []
            for c in credentials:
                self.credentials.append(f"{self.name.lower()}_{c}")
        self.repr_name = repr_name
        self.deprecated_credentials = deprecated_credentials
        self.instructions = instructions

```



---

## High-Level Overview

This is a **python** file named `provider.py`.

**Python Module**

- **Classes** (1): Provider
- **Functions** (1): __init__
- **Import Statements**: 1


---

## Detailed Analysis

### Python Code Structure

#### Classes

- **`Provider`**


---

## Related Files

The following files may be related based on imports and references:

**Imported Modules**:
- `Fetcher`
- `openbb_core.provider.abstract.fetcher`


---

## Performance & Security Notes

No obvious security concerns detected in static analysis.


---

**Generated**: 2025-11-19T02:16:46.334468Z
**Generator**: World's Best Repo Book Generator v1.0

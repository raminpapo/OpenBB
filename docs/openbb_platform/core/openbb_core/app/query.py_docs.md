# File Documentation: query.py

## Metadata
- **Path**: `openbb_platform/core/openbb_core/app/query.py`
- **Size**: 2,768 bytes
- **Lines**: 81
- **Category**: python
- **Extension**: .py

---

## Original Source

```python
"""Query class."""

import warnings
from dataclasses import asdict
from typing import Any

from openbb_core.app.model.abstract.warning import OpenBBWarning
from openbb_core.app.model.command_context import CommandContext
from openbb_core.app.provider_interface import (
    ExtraParams,
    ProviderChoices,
    ProviderInterface,
    StandardParams,
)


class Query:
    """Query class."""

    def __init__(
        self,
        cc: CommandContext,
        provider_choices: ProviderChoices,
        standard_params: StandardParams,
        extra_params: ExtraParams,
    ) -> None:
        """Initialize Query class."""
        self.cc = cc
        original = asdict(provider_choices)
        self.provider = original.get("provider")
        self.standard_params = standard_params
        self.extra_params = extra_params
        self.name = self.standard_params.__class__.__name__
        self.provider_interface = ProviderInterface()

    def filter_extra_params(
        self,
        extra_params: ExtraParams,
        provider_name: str,
    ) -> dict[str, Any]:
        """Filter extra params based on the provider and warn if not supported."""
        original = asdict(extra_params)
        filtered = {}

        query = extra_params.__class__.__name__
        fields = asdict(self.provider_interface.params[query]["extra"]())  # type: ignore

        for k, v in original.items():
            f = fields[k]
            providers = f.title.split(",") if hasattr(f, "title") else []

            # We only filter/warn if the value is not the default, because fastapi
            # Depends always sends the default value, even if it's not in the request.
            if v != f.default:
                if provider_name in providers:
                    filtered[k] = v
                else:
                    available = ", ".join(providers)
                    warnings.warn(
                        message=f"Parameter '{k}' is not supported by {provider_name}. Available for: {available}.",
                        category=OpenBBWarning,
                    )

        return filtered

    async def execute(self) -> Any:
        """Execute the query."""
        standard_dict = asdict(self.standard_params)
        extra_dict = (
            self.filter_extra_params(self.extra_params, self.provider) if self.extra_params else {}  # type: ignore
        )
        query_executor = self.provider_interface.create_executor()

        return await query_executor.execute(
            provider_name=self.provider,
            model_name=self.name,
            params={**standard_dict, **extra_dict},
            credentials=self.cc.user_settings.credentials.model_dump(),
            preferences=self.cc.user_settings.preferences.model_dump(),
        )

```



---

## High-Level Overview

This is a **python** file named `query.py`.

**Python Module**

- **Classes** (1): Query
- **Functions** (3): __init__, filter_extra_params, execute
- **Import Statements**: 1


---

## Detailed Analysis

### Python Code Structure

#### Classes

- **`Query`**


---

## Related Files

The following files may be related based on imports and references:

**Imported Modules**:
- `Any`
- `CommandContext`
- `OpenBBWarning`
- `asdict`
- `dataclasses`
- `openbb_core.app.model.abstract.warning`
- `openbb_core.app.model.command_context`
- `openbb_core.app.provider_interface`
- `typing`
- `warnings`


---

## Performance & Security Notes

No obvious security concerns detected in static analysis.


---

**Generated**: 2025-11-19T02:16:46.222088Z
**Generator**: World's Best Repo Book Generator v1.0

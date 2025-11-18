# Documentation: openbb_platform/core/openbb_core/app/query.py

## File Metadata
- **Path**: `openbb_platform/core/openbb_core/app/query.py`
- **Size**: 2,768 characters, 81 lines
- **Words**: 220
- **Extension**: .py
- **Classification**: Text file

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

## High-Level Overview

Query class.

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
Query class.
Initialize Query class.
self.cc = cc

## Detailed Structure

### Python File Structure

**Classes** (1):
`Query`

**Functions** (3):
`__init__`, `filter_extra_params`, `execute`

**Imports** (10):
`warnings`, `dataclasses`, `asdict`, `typing`, `Any`, `openbb_core.app.model.abstract.warning`, `OpenBBWarning`, `openbb_core.app.model.command_context`, `CommandContext`, `openbb_core.app.provider_interface`


## Key Components

**Class `Query`**: Query class.

## Usage & Examples

See source code for usage details.

## Related Files

- `warnings`
- `dataclasses`
- `typing`
- `openbb_core.app.model.abstract.warning`
- `openbb_core.app.model.command_context`
- `openbb_core.app.provider_interface`

## Notes
- Generated: 2025-11-18T07:54:35.468828
- Generator: World's Best Repo Book Generator v1.0.0

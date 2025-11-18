# Documentation: cli/openbb_cli/session.py

## File Metadata
- **Path**: `cli/openbb_cli/session.py`
- **Size**: 3,228 characters, 105 lines
- **Words**: 245
- **Extension**: .py
- **Classification**: Text file

## Original Source

```python
"""Settings module."""

import sys
from pathlib import Path

from openbb import obb
from openbb_charting.core.backend import create_backend, get_backend
from openbb_core.app.model.abstract.singleton import SingletonMeta
from openbb_core.app.model.charts.charting_settings import ChartingSettings
from openbb_core.app.model.user_settings import UserSettings as User
from prompt_toolkit import PromptSession

from openbb_cli.argparse_translator.obbject_registry import Registry
from openbb_cli.config.completer import CustomFileHistory
from openbb_cli.config.console import Console
from openbb_cli.config.constants import HIST_FILE_PROMPT
from openbb_cli.config.style import Style
from openbb_cli.models.settings import Settings


def _get_backend():
    """Get the Platform charting backend."""
    try:
        return get_backend()
    except ValueError:
        # backend might not be created yet
        charting_settings = ChartingSettings(
            system_settings=obb.system,  # type: ignore
            user_settings=obb.user,  # type: ignore
        )
        create_backend(charting_settings)
        get_backend().start(debug=charting_settings.debug_mode)  # type: ignore
        return get_backend()


class Session(metaclass=SingletonMeta):
    """Session class."""

    def __init__(self):
        """Initialize session."""

        self._obb = obb
        self._settings = Settings()
        self._style = Style(
            style=self._settings.RICH_STYLE,
            directory=Path(self._obb.user.preferences.user_styles_directory),  # type: ignore[union-attr]
        )
        self._console = Console(
            settings=self._settings, style=self._style.console_style
        )
        self._prompt_session = self._get_prompt_session()
        self._obbject_registry = Registry()

        self._backend = _get_backend()

    @property
    def user(self) -> User:
        """Get platform user."""
        return self._obb.user  # type: ignore[union-attr]

    @property
    def settings(self) -> Settings:
        """Get CLI settings."""
        return self._settings

    @property
    def style(self) -> Style:
        """Get CLI style."""
        return self._style

    @property
    def console(self) -> Console:
        """Get console."""
        return self._console

    @property
    def obbject_registry(self) -> Registry:
        """Get obbject registry."""
        return self._obbject_registry

    @property
    def prompt_session(self) -> PromptSession | None:
        """Get prompt session."""
        return self._prompt_session

    def _get_prompt_session(self) -> PromptSession | None:
        """Initialize prompt session."""
        try:
            if sys.stdin.isatty():
                prompt_session: PromptSession | None = PromptSession(
                    history=CustomFileHistory(str(HIST_FILE_PROMPT))
                )
            else:
                prompt_session = None
        except Exception:
            prompt_session = None

        return prompt_session

    def max_obbjects_exceeded(self) -> bool:
        """Check if max obbjects exceeded."""
        return (
            len(self.obbject_registry.all) >= self.settings.N_TO_KEEP_OBBJECT_REGISTRY
        )

```

## High-Level Overview

Settings module.

import sys
from pathlib import Path

from openbb import obb
from openbb_charting.core.backend import create_backend, get_backend
from openbb_core.app.model.abstract.singleton import SingletonMeta
from openbb_core.app.model.charts.charting_settings import ChartingSettings
from openbb_core.app.model.user_settings import UserSettings as User
from prompt_toolkit import PromptSession

from openbb_cli.argparse_translator.obbject_registry import Registry
from openbb_cli.config.completer import CustomFileHistory
from openbb_cli.config.console import Console
from openbb_cli.config.constants import HIST_FILE_PROMPT
from openbb_cli.config.style import Style
from openbb_cli.models.settings import Settings



## Detailed Structure

### Python File Structure

**Classes** (1):
`Session`

**Functions** (10):
`_get_backend`, `__init__`, `user`, `settings`, `style`, `console`, `obbject_registry`, `prompt_session`, `_get_prompt_session`, `max_obbjects_exceeded`

**Imports** (27):
`sys`, `pathlib`, `Path`, `openbb`, `obb`, `openbb_charting.core.backend`, `create_backend`, `openbb_core.app.model.abstract.singleton`, `SingletonMeta`, `openbb_core.app.model.charts.charting_settings`, `ChartingSettings`, `openbb_core.app.model.user_settings`, `UserSettings`, `prompt_toolkit`, `PromptSession`, `openbb_cli.argparse_translator.obbject_registry`, `Registry`, `openbb_cli.config.completer`, `CustomFileHistory`, `openbb_cli.config.console`


## Key Components

**Class `Session`**: Session class.

## Usage & Examples

See source code for usage details.

## Related Files

- `sys`
- `pathlib`
- `openbb`
- `openbb_charting.core.backend`
- `openbb_core.app.model.abstract.singleton`
- `openbb_core.app.model.charts.charting_settings`
- `openbb_core.app.model.user_settings`
- `prompt_toolkit`
- `openbb_cli.argparse_translator.obbject_registry`
- `openbb_cli.config.completer`

## Notes
- Generated: 2025-11-18T07:54:34.664493
- Generator: World's Best Repo Book Generator v1.0.0

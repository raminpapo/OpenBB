# File Documentation: dummy_backend.py

## Metadata
- **Path**: `openbb_platform/obbject_extensions/charting/openbb_charting/core/dummy_backend.py`
- **Size**: 1,655 bytes
- **Lines**: 56
- **Category**: python
- **Extension**: .py

---

## Original Source

```python
"""Dummy backend for charting to avoid import errors."""

import asyncio
from queue import Queue

import dotenv
from openbb_core.app.constants import OPENBB_DIRECTORY

SETTINGS_ENV_FILE = OPENBB_DIRECTORY / ".env"


class DummyBackend:
    """Dummy class to avoid import errors."""

    __version__ = "0.0.0"

    max_retries = 0
    outgoing: list[str] = []
    init_engine: list[str] = []
    daemon = True
    debug = False
    shell = False
    base = None
    recv: Queue = Queue()

    def __new__(cls, *args, **kwargs):  # pylint: disable=W0613
        """Create a singleton instance of the backend."""
        if not hasattr(cls, "instance"):
            cls.instance = super().__new__(cls)  # pylint: disable=E1120
        return cls.instance

    def __init__(self, daemon: bool = True, max_retries: int = 30):
        """Use cummy init to avoid import errors."""
        self.daemon = daemon
        self.max_retries = max_retries
        try:
            self.loop: asyncio.AbstractEventLoop = asyncio.get_event_loop()
        except RuntimeError:
            self.loop = asyncio.new_event_loop()
            asyncio.set_event_loop(self.loop)

        dotenv.set_key(SETTINGS_ENV_FILE, "PLOT_ENABLE_PYWRY", "0")

    def close(self, reset: bool = False):  # pylint: disable=W0613
        """Close the backend."""

    def start(self, debug: bool = False):  # pylint: disable=W0613
        """Start the backend."""

    def send_outgoing(self, outgoing: dict):
        """Send outgoing data to the backend."""

    async def check_backend(self):
        """Check backend method to avoid errors and revert to browser."""
        raise Exception

```



---

## High-Level Overview

This is a **python** file named `dummy_backend.py`.

**Python Module**

- **Classes** (2): DummyBackend, to
- **Functions** (6): __new__, __init__, close, start, send_outgoing, check_backend
- **Import Statements**: 4


---

## Detailed Analysis

### Python Code Structure

#### Classes

- **`DummyBackend`**

#### Functions

- **`__new__(cls, *args, **kwargs)`**
- **`__init__(self, daemon: bool = True, max_retries: int = 30)`**
- **`close(self, reset: bool = False)`**
- **`start(self, debug: bool = False)`**
- **`send_outgoing(self, outgoing: dict)`**
- **`check_backend(self)`**


---

## Related Files

The following files may be related based on imports and references:

**Imported Modules**:
- `OPENBB_DIRECTORY`
- `Queue`
- `asyncio`
- `dotenv`
- `errors.`
- `openbb_core.app.constants`
- `queue`


---

## Performance & Security Notes

No obvious security concerns detected in static analysis.


---

**Generated**: 2025-11-19T02:16:47.435112Z
**Generator**: World's Best Repo Book Generator v1.0

# File Documentation: cli.py

## Metadata
- **Path**: `cli/openbb_cli/cli.py`
- **Size**: 794 bytes
- **Lines**: 33
- **Category**: python
- **Extension**: .py

---

## Original Source

```python
"""OpenBB Platform CLI entry point."""

import logging
import sys

from openbb_cli.utils.utils import change_logging_sub_app, reset_logging_sub_app


def main():
    """Use the main entry point for the OpenBB Platform CLI."""
    print("Loading...\n")  # noqa: T201

    # pylint: disable=import-outside-toplevel
    from openbb_cli.config.setup import bootstrap
    from openbb_cli.controllers.cli_controller import launch

    bootstrap()

    dev = "--dev" in sys.argv[1:]
    debug = "--debug" in sys.argv[1:]

    launch(dev, debug)


if __name__ == "__main__":
    initial_logging_sub_app = change_logging_sub_app()
    try:
        main()
    except Exception:
        logging.exception("An unexpected error occurred")
    finally:
        reset_logging_sub_app(initial_logging_sub_app)

```



---

## High-Level Overview

This is a **python** file named `cli.py`.

**Python Module**

- **Functions** (1): main
- **Import Statements**: 2


---

## Detailed Analysis

### Python Code Structure


#### Functions

- **`main()`**


---

## Related Files

The following files may be related based on imports and references:

**Imported Modules**:
- `bootstrap`
- `change_logging_sub_app`
- `launch`
- `logging`
- `openbb_cli.config.setup`
- `openbb_cli.controllers.cli_controller`
- `openbb_cli.utils.utils`
- `sys`


---

## Performance & Security Notes

No obvious security concerns detected in static analysis.


---

**Generated**: 2025-11-19T02:15:18.813874Z
**Generator**: World's Best Repo Book Generator v1.0

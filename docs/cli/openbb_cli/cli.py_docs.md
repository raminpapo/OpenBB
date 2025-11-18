# Documentation: cli/openbb_cli/cli.py

## File Metadata
- **Path**: `cli/openbb_cli/cli.py`
- **Size**: 794 characters, 33 lines
- **Words**: 71
- **Extension**: .py
- **Classification**: Text file

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

## High-Level Overview

OpenBB Platform CLI entry point.

import logging
import sys

from openbb_cli.utils.utils import change_logging_sub_app, reset_logging_sub_app


def main():
Use the main entry point for the OpenBB Platform CLI.
pylint: disable=import-outside-toplevel

## Detailed Structure

### Python File Structure

**Classes** (0):
None

**Functions** (1):
`main`

**Imports** (8):
`logging`, `sys`, `openbb_cli.utils.utils`, `change_logging_sub_app`, `openbb_cli.config.setup`, `bootstrap`, `openbb_cli.controllers.cli_controller`, `launch`


## Key Components

No major components extracted.

## Usage & Examples

This file can be run as a script. See the `__main__` block for entry point.

## Related Files

- `logging`
- `sys`
- `openbb_cli.utils.utils`
- `openbb_cli.config.setup`
- `openbb_cli.controllers.cli_controller`

## Notes
- Generated: 2025-11-18T07:54:34.633277
- Generator: World's Best Repo Book Generator v1.0.0

# Documentation: openbb_platform/core/tests/app/static/utils/test_linters.py

## File Metadata
- **Path**: `openbb_platform/core/tests/app/static/utils/test_linters.py`
- **Size**: 849 characters, 46 lines
- **Words**: 59
- **Extension**: .py
- **Classification**: Text file

## Original Source

```python
"""Test linters.py file."""

# pylint: disable=redefined-outer-name

import pytest
from openbb_core.app.static.package_builder import (
    Linters,
)


@pytest.fixture(scope="module")
def tmp_package_dir(tmp_path_factory):
    """Return a temporary package directory."""
    return tmp_path_factory.mktemp("package")


@pytest.fixture(scope="module")
def linters(tmp_package_dir):
    """Return linters."""
    return Linters(tmp_package_dir)


def test_linters_init(linters):
    """Test linters init."""
    assert linters


def test_print_separator(linters):
    """Test print separator."""
    linters.print_separator(symbol="AAPL")


def test_run(linters):
    """Test run."""
    linters.run(linter="ruff")


def test_ruff(linters):
    """Test ruff."""
    linters.ruff()


def test_black(linters):
    """Test black."""
    linters.black()

```

## High-Level Overview

Test linters.py file.

# pylint: disable=redefined-outer-name

import pytest
from openbb_core.app.static.package_builder import (
Linters,
)


@pytest.fixture(scope="module")
def tmp_package_dir(tmp_path_factory):
Return a temporary package directory.
Return linters.
return Linters(tmp_package_dir)


def test_linters_init(linters):
Test linters init.
Test print separator.

## Detailed Structure

### Python File Structure

**Classes** (0):
None

**Functions** (7):
`tmp_package_dir`, `linters`, `test_linters_init`, `test_print_separator`, `test_run`, `test_ruff`, `test_black`

**Imports** (2):
`pytest`, `openbb_core.app.static.package_builder`


## Key Components

No major components extracted.

## Usage & Examples

See source code for usage details.

## Related Files

- `pytest`
- `openbb_core.app.static.package_builder`

## Notes
- Generated: 2025-11-18T07:54:35.862894
- Generator: World's Best Repo Book Generator v1.0.0

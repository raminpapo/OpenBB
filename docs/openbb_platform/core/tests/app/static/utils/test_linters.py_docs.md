# File Documentation: test_linters.py

## Metadata
- **Path**: `openbb_platform/core/tests/app/static/utils/test_linters.py`
- **Size**: 849 bytes
- **Lines**: 46
- **Category**: python
- **Extension**: .py

---

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



---

## High-Level Overview

This is a **python** file named `test_linters.py`.

**Python Module**

- **Functions** (7): tmp_package_dir, linters, test_linters_init, test_print_separator, test_run, test_ruff, test_black
- **Import Statements**: 1


---

## Detailed Analysis

### Python Code Structure


#### Functions

- **`tmp_package_dir(tmp_path_factory)`**
- **`linters(tmp_package_dir)`**
- **`test_linters_init(linters)`**
- **`test_print_separator(linters)`**
- **`test_run(linters)`**
- **`test_ruff(linters)`**
- **`test_black(linters)`**

#### Decorators Used

pytest


---

## Related Files

The following files may be related based on imports and references:

**Imported Modules**:
- `openbb_core.app.static.package_builder`
- `pytest`


---

## Performance & Security Notes

No obvious security concerns detected in static analysis.


---

**Generated**: 2025-11-19T02:16:46.705956Z
**Generator**: World's Best Repo Book Generator v1.0

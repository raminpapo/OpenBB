# File Documentation: test_session.py

## Metadata
- **Path**: `cli/tests/test_session.py`
- **Size**: 1,316 bytes
- **Lines**: 46
- **Category**: python
- **Extension**: .py

---

## Original Source

```python
"Test the Session class."

from unittest.mock import MagicMock, patch

import pytest
from openbb_cli.models.settings import Settings
from openbb_cli.session import Session, sys

# pylint: disable=redefined-outer-name, unused-argument, protected-access


def mock_isatty(return_value):
    """Mock the isatty method."""
    original_isatty = sys.stdin.isatty
    sys.stdin.isatty = MagicMock(return_value=return_value)  # type: ignore
    return original_isatty


@pytest.fixture
def session():
    """Session fixture."""
    return Session()


def test_session_initialization(session):
    """Test the initialization of the Session class."""
    assert session.settings is not None
    assert session.style is not None
    assert session.console is not None
    assert session.obbject_registry is not None
    assert isinstance(session.settings, Settings)


@patch("sys.stdin.isatty", return_value=True)
def test_get_prompt_session_true(mock_isatty, session):
    "Test get_prompt_session method."
    prompt_session = session._get_prompt_session()
    assert prompt_session is not None


@patch("sys.stdin.isatty", return_value=False)
def test_get_prompt_session_false(mock_isatty, session):
    "Test get_prompt_session method."
    prompt_session = session._get_prompt_session()
    assert prompt_session is None

```



---

## High-Level Overview

This is a **python** file named `test_session.py`.

**Python Module**

- **Functions** (5): mock_isatty, session, test_session_initialization, test_get_prompt_session_true, test_get_prompt_session_false
- **Import Statements**: 1


---

## Detailed Analysis

### Python Code Structure


#### Functions

- **`mock_isatty(return_value)`**
- **`session()`**
- **`test_session_initialization(session)`**
- **`test_get_prompt_session_true(mock_isatty, session)`**
- **`test_get_prompt_session_false(mock_isatty, session)`**

#### Decorators Used

patch, pytest


---

## Related Files

The following files may be related based on imports and references:

**Imported Modules**:
- `MagicMock`
- `Session`
- `Settings`
- `openbb_cli.models.settings`
- `openbb_cli.session`
- `pytest`
- `unittest.mock`


---

## Performance & Security Notes

No obvious security concerns detected in static analysis.


---

**Generated**: 2025-11-19T02:16:44.934131Z
**Generator**: World's Best Repo Book Generator v1.0

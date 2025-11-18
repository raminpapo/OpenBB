# Documentation: cli/tests/test_session.py

## File Metadata
- **Path**: `cli/tests/test_session.py`
- **Size**: 1,316 characters, 46 lines
- **Words**: 112
- **Extension**: .py
- **Classification**: Text file

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

## High-Level Overview

pylint: disable=redefined-outer-name, unused-argument, protected-access
Mock the isatty method.
original_isatty = sys.stdin.isatty
sys.stdin.isatty = MagicMock(return_value=return_value)  # type: ignore
return original_isatty


@pytest.fixture
def session():
Session fixture.
Test the initialization of the Session class.
assert session.settings is not None
assert session.style is not None
assert session.console is not None
assert session.obbject_registry is not None
assert isinstance(session.settings, Settings)


@patch("sys.stdin.isatty", return_value=True)
def test_get_prompt_session_true(mock_isatty, session):

## Detailed Structure

### Python File Structure

**Classes** (0):
None

**Functions** (5):
`mock_isatty`, `session`, `test_session_initialization`, `test_get_prompt_session_true`, `test_get_prompt_session_false`

**Imports** (7):
`unittest.mock`, `MagicMock`, `pytest`, `openbb_cli.models.settings`, `Settings`, `openbb_cli.session`, `Session`


## Key Components

No major components extracted.

## Usage & Examples

See source code for usage details.

## Related Files

- `unittest.mock`
- `pytest`
- `openbb_cli.models.settings`
- `openbb_cli.session`

## Notes
- Generated: 2025-11-18T07:54:34.731108
- Generator: World's Best Repo Book Generator v1.0.0

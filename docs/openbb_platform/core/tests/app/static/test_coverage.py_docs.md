# Documentation: openbb_platform/core/tests/app/static/test_coverage.py

## File Metadata
- **Path**: `openbb_platform/core/tests/app/static/test_coverage.py`
- **Size**: 1,173 characters, 47 lines
- **Words**: 90
- **Extension**: .py
- **Classification**: Text file

## Original Source

```python
"""Test the coverage.py file."""

# pylint: disable=redefined-outer-name

import pytest
from openbb_core.app.command_runner import CommandRunner
from openbb_core.app.static.app_factory import BaseApp
from openbb_core.app.static.coverage import Coverage


@pytest.fixture(scope="module")
def app():
    """Return a BaseApp instance."""
    return BaseApp(command_runner=CommandRunner())


@pytest.fixture(scope="module")
def coverage(app):
    """Return coverage."""
    return Coverage(app)  # Pass the BaseApp instance to Coverage


def test_coverage_init(coverage):
    """Test coverage init."""
    assert coverage


def test_coverage_providers(coverage):
    """Test coverage providers."""
    provider_coverage = coverage.providers
    assert provider_coverage
    assert isinstance(provider_coverage, dict)


def test_coverage_commands(coverage):
    """Test coverage commands."""
    command_coverage = coverage.commands
    assert command_coverage
    assert isinstance(command_coverage, dict)


def test_coverage_reference(coverage):
    """Test coverage reference."""
    reference = coverage.reference
    assert reference
    assert isinstance(reference, dict)

```

## High-Level Overview

Test the coverage.py file.

# pylint: disable=redefined-outer-name

import pytest
from openbb_core.app.command_runner import CommandRunner
from openbb_core.app.static.app_factory import BaseApp
from openbb_core.app.static.coverage import Coverage


@pytest.fixture(scope="module")
def app():
Return a BaseApp instance.
Return coverage.
return Coverage(app)  # Pass the BaseApp instance to Coverage


def test_coverage_init(coverage):
Test coverage init.
Test coverage providers.

## Detailed Structure

### Python File Structure

**Classes** (0):
None

**Functions** (6):
`app`, `coverage`, `test_coverage_init`, `test_coverage_providers`, `test_coverage_commands`, `test_coverage_reference`

**Imports** (7):
`pytest`, `openbb_core.app.command_runner`, `CommandRunner`, `openbb_core.app.static.app_factory`, `BaseApp`, `openbb_core.app.static.coverage`, `Coverage`


## Key Components

No major components extracted.

## Usage & Examples

See source code for usage details.

## Related Files

- `pytest`
- `openbb_core.app.command_runner`
- `openbb_core.app.static.app_factory`
- `openbb_core.app.static.coverage`

## Notes
- Generated: 2025-11-18T07:54:35.856550
- Generator: World's Best Repo Book Generator v1.0.0

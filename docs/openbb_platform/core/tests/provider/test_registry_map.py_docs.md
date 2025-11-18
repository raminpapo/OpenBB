# Documentation: openbb_platform/core/tests/provider/test_registry_map.py

## File Metadata
- **Path**: `openbb_platform/core/tests/provider/test_registry_map.py`
- **Size**: 1,168 characters, 42 lines
- **Words**: 96
- **Extension**: .py
- **Classification**: Text file

## Original Source

```python
"""Test the registry map."""

# pylint: disable=W0621

import pytest
from openbb_core.provider.registry_map import RegistryMap


@pytest.fixture
def load_registry_map():
    """Mock the registry map."""
    return RegistryMap()


def test_get_credentials(load_registry_map):
    """Test if the _get_credentials method behaves as expected."""
    required_creds = load_registry_map.credentials

    assert "fmp" in required_creds
    assert required_creds["fmp"] == ["fmp_api_key"]


def test_get_available_providers(load_registry_map):
    """Test if the _get_available_providers method behaves as expected."""
    available_providers = load_registry_map.available_providers

    assert "fmp" in available_providers
    assert len(available_providers) > 0


def test_map_and_models(load_registry_map):
    """Test if the _get_map method behaves as expected."""
    standard_extra, original_models = (
        load_registry_map.standard_extra,
        load_registry_map.original_models,
    )
    models = load_registry_map.models

    assert "EquityHistorical" in standard_extra
    assert "EquityHistorical" in original_models
    assert "EquityHistorical" in models

```

## High-Level Overview

Test the registry map.

# pylint: disable=W0621

import pytest
from openbb_core.provider.registry_map import RegistryMap


@pytest.fixture
def load_registry_map():
Mock the registry map.
Test if the _get_credentials method behaves as expected.
required_creds = load_registry_map.credentials

assert "fmp" in required_creds
assert required_creds["fmp"] == ["fmp_api_key"]


def test_get_available_providers(load_registry_map):
Test if the _get_available_providers method behaves as expected.

## Detailed Structure

### Python File Structure

**Classes** (0):
None

**Functions** (4):
`load_registry_map`, `test_get_credentials`, `test_get_available_providers`, `test_map_and_models`

**Imports** (3):
`pytest`, `openbb_core.provider.registry_map`, `RegistryMap`


## Key Components

No major components extracted.

## Usage & Examples

See source code for usage details.

## Related Files

- `pytest`
- `openbb_core.provider.registry_map`

## Notes
- Generated: 2025-11-18T07:54:35.884639
- Generator: World's Best Repo Book Generator v1.0.0

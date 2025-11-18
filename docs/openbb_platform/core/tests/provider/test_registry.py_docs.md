# Documentation: openbb_platform/core/tests/provider/test_registry.py

## File Metadata
- **Path**: `openbb_platform/core/tests/provider/test_registry.py`
- **Size**: 932 characters, 31 lines
- **Words**: 75
- **Extension**: .py
- **Classification**: Text file

## Original Source

```python
"""Test the Registry."""

from openbb_core.provider.abstract.provider import Provider
from openbb_core.provider.registry import Registry, RegistryLoader


def test_registry():
    """Test the registry."""
    registry = Registry()
    assert registry.providers == {}

    mock_provider = Provider(name="TestProvider", description="Just a test provider.")
    registry.include_provider(mock_provider)

    assert "testprovider" in registry.providers
    assert registry.providers["testprovider"] == mock_provider


def test_registry_loader_integration():
    """Execute the loading process."""
    core_providers = ["fmp", "polygon", "fred", "benzinga", "intrinio"]
    registry = RegistryLoader.from_extensions()

    assert len(registry.providers) > 0

    for provider in core_providers:
        assert provider in registry.providers

    for provider in registry.providers.values():
        assert isinstance(provider, Provider)

```

## High-Level Overview

Test the Registry.

from openbb_core.provider.abstract.provider import Provider
from openbb_core.provider.registry import Registry, RegistryLoader


def test_registry():
Test the registry.
Execute the loading process.
core_providers = ["fmp", "polygon", "fred", "benzinga", "intrinio"]
registry = RegistryLoader.from_extensions()

assert len(registry.providers) > 0

for provider in core_providers:
assert provider in registry.providers

for provider in registry.providers.values():
assert isinstance(provider, Provider)


## Detailed Structure

### Python File Structure

**Classes** (0):
None

**Functions** (2):
`test_registry`, `test_registry_loader_integration`

**Imports** (4):
`openbb_core.provider.abstract.provider`, `Provider`, `openbb_core.provider.registry`, `Registry`


## Key Components

No major components extracted.

## Usage & Examples

See source code for usage details.

## Related Files

- `openbb_core.provider.abstract.provider`
- `openbb_core.provider.registry`

## Notes
- Generated: 2025-11-18T07:54:35.883565
- Generator: World's Best Repo Book Generator v1.0.0

# File Documentation: test_registry.py

## Metadata
- **Path**: `openbb_platform/core/tests/provider/test_registry.py`
- **Size**: 932 bytes
- **Lines**: 31
- **Category**: python
- **Extension**: .py

---

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



---

## High-Level Overview

This is a **python** file named `test_registry.py`.

**Python Module**

- **Functions** (2): test_registry, test_registry_loader_integration
- **Import Statements**: 1


---

## Detailed Analysis

### Python Code Structure


#### Functions

- **`test_registry()`**
- **`test_registry_loader_integration()`**


---

## Related Files

The following files may be related based on imports and references:

**Imported Modules**:
- `Provider`
- `Registry`
- `openbb_core.provider.abstract.provider`
- `openbb_core.provider.registry`


---

## Performance & Security Notes

No obvious security concerns detected in static analysis.


---

**Generated**: 2025-11-19T02:16:46.708931Z
**Generator**: World's Best Repo Book Generator v1.0

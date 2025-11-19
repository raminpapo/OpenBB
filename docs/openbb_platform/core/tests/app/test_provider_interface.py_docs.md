# File Documentation: test_provider_interface.py

## Metadata
- **Path**: `openbb_platform/core/tests/app/test_provider_interface.py`
- **Size**: 2,166 bytes
- **Lines**: 81
- **Category**: python
- **Extension**: .py

---

## Original Source

```python
"""Test provider interface."""

# pylint: disable=redefined-outer-name

import pytest
from openbb_core.app.provider_interface import (
    ProviderChoices,
    ProviderInterface,
)


@pytest.fixture(scope="module")
def provider_interface():
    """Set up provider_interface."""
    return ProviderInterface()


def test_init(provider_interface):
    """Test init."""
    assert provider_interface


def test_map(provider_interface):
    """Test map."""
    provider_interface_map = provider_interface.map
    assert isinstance(provider_interface_map, dict)
    assert len(provider_interface_map) > 0
    assert "EquityHistorical" in provider_interface_map


def test_credentials(provider_interface):
    """Test required credentials."""
    credentials = provider_interface.credentials
    assert isinstance(credentials, dict)
    assert len(credentials) > 0


def test_model_providers(provider_interface):
    """Test model providers."""
    model_providers = provider_interface.model_providers
    assert isinstance(model_providers, dict)
    assert len(model_providers) > 0


def test_params(provider_interface):
    """Test params."""
    params = provider_interface.params
    assert isinstance(params, dict)
    assert len(params) > 0
    assert "EquityHistorical" in params


def test_data(provider_interface):
    """Test data."""
    data = provider_interface.data
    assert isinstance(data, dict)
    assert len(data) > 0
    assert "EquityHistorical" in data


def test_available_providers(provider_interface):
    """Test providers literal."""
    available_providers = provider_interface.available_providers
    assert isinstance(available_providers, list)
    assert len(available_providers) > 0
    assert "openbb" not in available_providers


def test_provider_choices(provider_interface):
    """Test provider choices."""
    provider_choices = provider_interface.provider_choices
    assert isinstance(provider_choices, type(ProviderChoices))


def test_models(provider_interface):
    """Test models."""
    models = provider_interface.models
    assert isinstance(models, list)
    assert len(models) > 0
    assert "EquityHistorical" in models

```



---

## High-Level Overview

This is a **python** file named `test_provider_interface.py`.

**Python Module**

- **Functions** (10): provider_interface, test_init, test_map, test_credentials, test_model_providers, test_params, test_data, test_available_providers, test_provider_choices, test_models
- **Import Statements**: 1


---

## Detailed Analysis

### Python Code Structure


#### Functions

- **`provider_interface()`**
- **`test_init(provider_interface)`**
- **`test_map(provider_interface)`**
- **`test_credentials(provider_interface)`**
- **`test_model_providers(provider_interface)`**
- **`test_params(provider_interface)`**
- **`test_data(provider_interface)`**
- **`test_available_providers(provider_interface)`**
- **`test_provider_choices(provider_interface)`**
- **`test_models(provider_interface)`**

#### Decorators Used

pytest


---

## Related Files

The following files may be related based on imports and references:

**Imported Modules**:
- `openbb_core.app.provider_interface`
- `pytest`


---

## Performance & Security Notes

No obvious security concerns detected in static analysis.


---

**Generated**: 2025-11-19T02:16:46.641219Z
**Generator**: World's Best Repo Book Generator v1.0

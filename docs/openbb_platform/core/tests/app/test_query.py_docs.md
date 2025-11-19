# File Documentation: test_query.py

## Metadata
- **Path**: `openbb_platform/core/tests/app/test_query.py`
- **Size**: 3,166 bytes
- **Lines**: 134
- **Category**: python
- **Extension**: .py

---

## Original Source

```python
"""Test the Query class."""

# pylint: disable=redefined-outer-name

from dataclasses import dataclass
from unittest.mock import MagicMock, patch

import pytest
from openbb_core.app.model.command_context import CommandContext
from openbb_core.app.provider_interface import (
    ExtraParams,
    ProviderChoices,
    StandardParams,
)
from openbb_core.app.query import Query
from pydantic import BaseModel, ConfigDict


class MockBaseModel(BaseModel):
    """Mock QueryParams class."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)


def create_mock_query():
    """Mock query."""

    class EquityHistorical:
        """Mock EquityHistorical class."""

        start_date = "2020-01-01"
        end_date = "2020-01-05"
        symbol = "AAPL"

    return EquityHistorical()


def create_mock_extra_params():
    """Mock ExtraParams dataclass."""

    @dataclass
    class EquityHistorical:
        """Mock ExtraParams dataclass."""

        sort: str = "desc"

    return EquityHistorical()


@pytest.fixture(scope="module")
def query():
    """Set up query."""
    return Query(
        cc=CommandContext(),
        provider_choices=ProviderChoices(provider="fmp"),
        standard_params=StandardParams(),
        extra_params=ExtraParams(),
    )


def test_init(query):
    """Test init."""
    assert query


@pytest.fixture
def mock_registry():
    """Mock registry."""
    with patch(
        "openbb_core.app.provider_interface.ProviderInterface"
    ) as mock_get_provider_interface:
        mock_registry = MagicMock()
        mock_get_provider_interface.return_value.build_registry.return_value = (
            mock_registry
        )
        yield mock_registry


@pytest.fixture
def query_instance():
    """Set up query."""
    standard_params = create_mock_query()
    extra_params = create_mock_extra_params()

    cc = CommandContext()
    setattr(
        cc.user_settings.credentials,
        "fmp_api_key",
        "1234",  # pylint: disable=no-member
    )

    return Query(
        cc=cc,
        provider_choices=ProviderChoices(provider="fmp"),
        standard_params=standard_params,
        extra_params=extra_params,
    )


def test_filter_extra_params(query):
    """Test filter_extra_params."""
    extra_params = create_mock_extra_params()
    extra_params = query.filter_extra_params(extra_params, "fmp")

    assert isinstance(extra_params, dict)
    assert len(extra_params) == 0


def test_filter_extra_params_wrong_param(query):
    """Test filter_extra_params."""

    @dataclass
    class EquityHistorical:
        """Mock ExtraParams dataclass."""

        sort: str = "desc"
        limit: int = 4

    extra_params = EquityHistorical()

    extra = query.filter_extra_params(extra_params, "fmp")
    assert isinstance(extra, dict)
    assert len(extra) == 0


@pytest.mark.asyncio
async def test_execute_method_fake_credentials(query_instance: Query, mock_registry):
    """Test execute method without setting credentials."""
    mock_fetch_result = MockBaseModel()
    mock_registry.fetch.return_value = mock_fetch_result

    with pytest.raises(Exception):
        await query_instance.execute()

```



---

## High-Level Overview

This is a **python** file named `test_query.py`.

**Python Module**

- **Classes** (5): from, MockBaseModel, EquityHistorical, class, class
- **Functions** (9): create_mock_query, create_mock_extra_params, query, test_init, mock_registry, query_instance, test_filter_extra_params, test_filter_extra_params_wrong_param, test_execute_method_fake_credentials
- **Import Statements**: 2


---

## Detailed Analysis

### Python Code Structure

#### Classes

- **`MockBaseModel`**(BaseModel)
- **`EquityHistorical`**
- **`EquityHistorical`**
- **`EquityHistorical`**

#### Functions

- **`create_mock_query()`**
- **`create_mock_extra_params()`**
- **`query()`**
- **`test_init(query)`**
- **`mock_registry()`**
- **`query_instance()`**
- **`test_filter_extra_params(query)`**
- **`test_filter_extra_params_wrong_param(query)`**
- **`test_execute_method_fake_credentials(query_instance: Query, mock_registry)`**

#### Decorators Used

dataclass, pytest


---

## Related Files

The following files may be related based on imports and references:

**Imported Modules**:
- `BaseModel`
- `CommandContext`
- `MagicMock`
- `Query`
- `dataclass`
- `dataclasses`
- `openbb_core.app.model.command_context`
- `openbb_core.app.provider_interface`
- `openbb_core.app.query`
- `pydantic`
- `pytest`
- `unittest.mock`


---

## Performance & Security Notes

No obvious security concerns detected in static analysis.


---

**Generated**: 2025-11-19T02:16:46.642619Z
**Generator**: World's Best Repo Book Generator v1.0

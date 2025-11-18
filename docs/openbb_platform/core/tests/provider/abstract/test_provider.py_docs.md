# Documentation: openbb_platform/core/tests/provider/abstract/test_provider.py

## File Metadata
- **Path**: `openbb_platform/core/tests/provider/abstract/test_provider.py`
- **Size**: 1,605 characters, 46 lines
- **Words**: 130
- **Extension**: .py
- **Classification**: Text file

## Original Source

```python
"""Test the Provider."""

from openbb_core.provider.abstract.fetcher import Fetcher
from openbb_core.provider.abstract.provider import Provider


def test_provider_initialization():
    """Test the basic initialization of the Provider class."""
    provider = Provider(name="TestProvider", description="A simple test provider.")

    assert provider.name == "TestProvider"
    assert provider.description == "A simple test provider."
    assert provider.website is None
    assert provider.credentials == []
    assert provider.fetcher_dict == {}


def test_provider_with_optional_parameters():
    """Test the initialization of the Provider class with optional parameters."""
    provider = Provider(
        name="TestProvider",
        description="A simple test provider.",
        website="https://testprovider.example.com",
        credentials=["api_key"],
        fetcher_dict={"fetcher1": Fetcher},
    )

    assert provider.name == "TestProvider"
    assert provider.description == "A simple test provider."
    assert provider.website == "https://testprovider.example.com"
    assert provider.credentials == ["testprovider_api_key"]
    assert provider.fetcher_dict == {"fetcher1": Fetcher}


def test_provider_credentials_formatting():
    """Test the formatting of required credentials."""
    credentials = ["key1", "key2"]
    provider = Provider(
        name="TestProvider",
        description="A simple test provider.",
        credentials=credentials,
    )

    expected_credentials = ["testprovider_key1", "testprovider_key2"]
    assert provider.credentials == expected_credentials

```

## High-Level Overview

Test the Provider.

from openbb_core.provider.abstract.fetcher import Fetcher
from openbb_core.provider.abstract.provider import Provider


def test_provider_initialization():
Test the basic initialization of the Provider class.
Test the initialization of the Provider class with optional parameters.
provider = Provider(
name="TestProvider",
description="A simple test provider.",
website="https://testprovider.example.com",
credentials=["api_key"],
fetcher_dict={"fetcher1": Fetcher},
)

assert provider.name == "TestProvider"
assert provider.description == "A simple test provider."
assert provider.website == "https://testprovider.example.com"

## Detailed Structure

### Python File Structure

**Classes** (1):
`with`

**Functions** (3):
`test_provider_initialization`, `test_provider_with_optional_parameters`, `test_provider_credentials_formatting`

**Imports** (4):
`openbb_core.provider.abstract.fetcher`, `Fetcher`, `openbb_core.provider.abstract.provider`, `Provider`


## Key Components

**Class `with`**: No documentation

## Usage & Examples

See source code for usage details.

## Related Files

- `openbb_core.provider.abstract.fetcher`
- `openbb_core.provider.abstract.provider`

## Notes
- Generated: 2025-11-18T07:54:35.878202
- Generator: World's Best Repo Book Generator v1.0.0

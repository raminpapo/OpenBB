# Documentation: cookiecutter/openbb_cookiecutter/template/{{cookiecutter.project_tag}}/{{cookiecutter.package_name}}/providers/{{cookiecutter.provider_name}}/__init__.py

## File Metadata
- **Path**: `cookiecutter/openbb_cookiecutter/template/{{cookiecutter.project_tag}}/{{cookiecutter.package_name}}/providers/{{cookiecutter.provider_name}}/__init__.py`
- **Size**: 1,138 characters, 23 lines
- **Words**: 86
- **Extension**: .py
- **Classification**: Text file

## Original Source

```python
"""{{ cookiecutter.package_name }} OpenBB Platform Provider."""

from openbb_core.provider.abstract.provider import Provider
from {{cookiecutter.package_name}}.providers.{{cookiecutter.provider_name}}.models.example import ExampleFetcher
from {{cookiecutter.package_name}}.providers.{{cookiecutter.provider_name}}.models.ohlc_example import {{cookiecutter.provider_name.replace('_', ' ').title().replace(' ', '')}}EquityHistoricalFetcher



{{cookiecutter.provider_name}}_provider = Provider(
    name="{{cookiecutter.provider_name}}",
    description="Data provider for {{cookiecutter.project_name}}.",
    # Only add 'credentials' if they are needed.
    # For multiple login details, list them all here.
    # credentials=["api_key"],
    website="https://{{cookiecutter.project_tag}}.com",
    # Here, we list out the fetchers showing what our provider can get.
    # The dictionary key is the fetcher's name, used in the `../routers/router.py`.
    fetcher_dict={
        "EquityHistorical": {{cookiecutter.provider_name.replace('_', ' ').title().replace(' ', '')}}EquityHistoricalFetcher,
        "Example": ExampleFetcher,
    }
)

```

## High-Level Overview

{{ cookiecutter.package_name }} OpenBB Platform Provider.

from openbb_core.provider.abstract.provider import Provider
from {{cookiecutter.package_name}}.providers.{{cookiecutter.provider_name}}.models.example import ExampleFetcher
from {{cookiecutter.package_name}}.providers.{{cookiecutter.provider_name}}.models.ohlc_example import {{cookiecutter.provider_name.replace('_', ' ').title().replace(' ', '')}}EquityHistoricalFetcher



{{cookiecutter.provider_name}}_provider = Provider(
name="{{cookiecutter.provider_name}}",
description="Data provider for {{cookiecutter.project_name}}.",
# Only add 'credentials' if they are needed.
# For multiple login details, list them all here.
# credentials=["api_key"],
website="https://{{cookiecutter.project_tag}}.com",
# Here, we list out the fetchers showing what our provider can get.
# The dictionary key is the fetcher's name, used in the `../routers/router.py`.
fetcher_dict={
"EquityHistorical": {{cookiecutter.provider_name.replace('_', ' ').title().replace(' ', '')}}EquityHistoricalFetcher,
"Example": ExampleFetcher,

## Detailed Structure

### Python File Structure

**Classes** (0):
None

**Functions** (0):
None

**Imports** (3):
`openbb_core.provider.abstract.provider`, `Provider`, `ExampleFetcher`


## Key Components

No major components extracted.

## Usage & Examples

See source code for usage details.

## Related Files

- `openbb_core.provider.abstract.provider`
- `ExampleFetcher`

## Notes
- Generated: 2025-11-18T07:54:34.755296
- Generator: World's Best Repo Book Generator v1.0.0

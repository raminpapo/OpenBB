# File Documentation: __init__.py

## Metadata
- **Path**: `cookiecutter/openbb_cookiecutter/template/{{cookiecutter.project_tag}}/{{cookiecutter.package_name}}/providers/{{cookiecutter.provider_name}}/__init__.py`
- **Size**: 1,138 bytes
- **Lines**: 23
- **Category**: python
- **Extension**: .py

---

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



---

## High-Level Overview

This is a **python** file named `__init__.py`.

**Python Module**

- **Import Statements**: 2


---

## Detailed Analysis

### Python Code Structure



---

## Related Files

The following files may be related based on imports and references:

**Imported Modules**:
- `ExampleFetcher`
- `Provider`
- `openbb_core.provider.abstract.provider`


---

## Performance & Security Notes

No obvious security concerns detected in static analysis.


---

**Generated**: 2025-11-19T02:16:44.958601Z
**Generator**: World's Best Repo Book Generator v1.0

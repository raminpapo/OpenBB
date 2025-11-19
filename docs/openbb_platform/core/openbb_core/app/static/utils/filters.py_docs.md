# File Documentation: filters.py

## Metadata
- **Path**: `openbb_platform/core/openbb_core/app/static/utils/filters.py`
- **Size**: 2,679 bytes
- **Lines**: 67
- **Category**: python
- **Extension**: .py

---

## Original Source

```python
"""OpenBB filters."""

from typing import Any

from openbb_core.app.utils import check_single_item, convert_to_basemodel


def filter_inputs(
    data_processing: bool = False,
    info: dict[str, dict[str, Any]] | None = None,
    **kwargs,
) -> dict:
    """Filter command inputs."""
    for key, value in kwargs.items():
        if data_processing and key == "data":
            kwargs[key] = convert_to_basemodel(value)

    if info:
        # Here we check if list items are passed and multiple items allowed for
        # the given provider/input combination. In that case we transform the list
        # into a comma-separated string
        provider = kwargs.get("provider_choices", {}).get("provider")
        for field, properties in info.items():
            for p in ("standard_params", "extra_params"):
                if field in kwargs.get(p, {}):
                    current = kwargs[p][field]
                    new = (
                        ",".join(map(str, current))
                        if isinstance(current, list)
                        else current
                    )

                    provider_properties = properties.get(provider, {})
                    if isinstance(provider_properties, dict):
                        multiple_items_allowed = provider_properties.get(
                            "multiple_items_allowed"
                        )
                    elif isinstance(provider_properties, list):
                        # For backwards compatibility, before this was a list
                        multiple_items_allowed = (
                            "multiple_items_allowed" in provider_properties
                        )
                    else:
                        multiple_items_allowed = True

                    if not multiple_items_allowed:
                        check_single_item(
                            new,
                            f"{field} -> multiple items not allowed for '{provider}'",
                        )

                    kwargs[p][field] = new
                    break
    else:
        provider = kwargs.get("provider_choices", {}).get("provider")
        for param_category in ("standard_params", "extra_params"):
            if param_category in kwargs:
                for field, value in kwargs[param_category].items():
                    if isinstance(value, list):
                        kwargs[param_category][field] = ",".join(map(str, value))
                    check_single_item(
                        kwargs[param_category][field],
                        f"{field} -> multiple items not allowed for '{provider}'",
                    )

    return kwargs

```



---

## High-Level Overview

This is a **python** file named `filters.py`.

**Python Module**

- **Functions** (1): filter_inputs
- **Import Statements**: 1


---

## Detailed Analysis

### Python Code Structure



---

## Related Files

The following files may be related based on imports and references:

**Imported Modules**:
- `Any`
- `check_single_item`
- `openbb_core.app.utils`
- `typing`


---

## Performance & Security Notes

No obvious security concerns detected in static analysis.


---

**Generated**: 2025-11-19T02:16:46.316874Z
**Generator**: World's Best Repo Book Generator v1.0

# File Documentation: index_views.py

## Metadata
- **Path**: `openbb_platform/extensions/index/openbb_index/index_views.py`
- **Size**: 567 bytes
- **Lines**: 23
- **Category**: python
- **Extension**: .py

---

## Original Source

```python
"""Views for the index Extension."""

from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from openbb_charting.core.openbb_figure import (
        OpenBBFigure,
    )


class IndexViews:
    """Index Views."""

    @staticmethod
    def index_price_historical(  # noqa: PLR0912
        **kwargs,
    ) -> tuple["OpenBBFigure", dict[str, Any]]:
        """Index Price Historical Chart."""
        # pylint: disable=import-outside-toplevel
        from openbb_charting.charts.price_historical import price_historical

        return price_historical(**kwargs)

```



---

## High-Level Overview

This is a **python** file named `index_views.py`.

**Python Module**

- **Classes** (1): IndexViews
- **Functions** (1): index_price_historical
- **Import Statements**: 2


---

## Detailed Analysis

### Python Code Structure

#### Classes

- **`IndexViews`**

#### Decorators Used

staticmethod


---

## Related Files

The following files may be related based on imports and references:

**Imported Modules**:
- `TYPE_CHECKING`
- `openbb_charting.charts.price_historical`
- `openbb_charting.core.openbb_figure`
- `price_historical`
- `typing`


---

## Performance & Security Notes

No obvious security concerns detected in static analysis.


---

**Generated**: 2025-11-19T02:16:47.066331Z
**Generator**: World's Best Repo Book Generator v1.0

# File Documentation: currency_views.py

## Metadata
- **Path**: `openbb_platform/extensions/currency/openbb_currency/currency_views.py`
- **Size**: 582 bytes
- **Lines**: 23
- **Category**: python
- **Extension**: .py

---

## Original Source

```python
"""Views for the Currency Extension."""

from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from openbb_charting.core.openbb_figure import (
        OpenBBFigure,
    )


class CurrencyViews:
    """Currency Views."""

    @staticmethod
    def currency_price_historical(  # noqa: PLR0912
        **kwargs,
    ) -> tuple["OpenBBFigure", dict[str, Any]]:
        """Currency Price Historical Chart."""
        # pylint: disable=import-outside-toplevel
        from openbb_charting.charts.price_historical import price_historical

        return price_historical(**kwargs)

```



---

## High-Level Overview

This is a **python** file named `currency_views.py`.

**Python Module**

- **Classes** (1): CurrencyViews
- **Functions** (1): currency_price_historical
- **Import Statements**: 2


---

## Detailed Analysis

### Python Code Structure

#### Classes

- **`CurrencyViews`**

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

**Generated**: 2025-11-19T02:16:46.787514Z
**Generator**: World's Best Repo Book Generator v1.0

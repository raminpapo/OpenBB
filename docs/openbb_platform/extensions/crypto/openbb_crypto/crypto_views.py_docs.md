# File Documentation: crypto_views.py

## Metadata
- **Path**: `openbb_platform/extensions/crypto/openbb_crypto/crypto_views.py`
- **Size**: 572 bytes
- **Lines**: 23
- **Category**: python
- **Extension**: .py

---

## Original Source

```python
"""Views for the crypto Extension."""

from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from openbb_charting.core.openbb_figure import (
        OpenBBFigure,
    )


class CryptoViews:
    """Crypto Views."""

    @staticmethod
    def crypto_price_historical(  # noqa: PLR0912
        **kwargs,
    ) -> tuple["OpenBBFigure", dict[str, Any]]:
        """Crypto Price Historical Chart."""
        # pylint: disable=import-outside-toplevel
        from openbb_charting.charts.price_historical import price_historical

        return price_historical(**kwargs)

```



---

## High-Level Overview

This is a **python** file named `crypto_views.py`.

**Python Module**

- **Classes** (1): CryptoViews
- **Functions** (1): crypto_price_historical
- **Import Statements**: 2


---

## Detailed Analysis

### Python Code Structure

#### Classes

- **`CryptoViews`**

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

**Generated**: 2025-11-19T02:16:46.762004Z
**Generator**: World's Best Repo Book Generator v1.0

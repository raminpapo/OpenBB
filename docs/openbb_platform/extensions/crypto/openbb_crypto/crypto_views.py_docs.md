# Documentation: openbb_platform/extensions/crypto/openbb_crypto/crypto_views.py

## File Metadata
- **Path**: `openbb_platform/extensions/crypto/openbb_crypto/crypto_views.py`
- **Size**: 572 characters, 23 lines
- **Words**: 47
- **Extension**: .py
- **Classification**: Text file

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

## High-Level Overview

Views for the crypto Extension.

from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
from openbb_charting.core.openbb_figure import (
OpenBBFigure,
)


class CryptoViews:
Crypto Views.
Crypto Price Historical Chart.
# pylint: disable=import-outside-toplevel
from openbb_charting.charts.price_historical import price_historical

return price_historical(**kwargs)


## Detailed Structure

### Python File Structure

**Classes** (1):
`CryptoViews`

**Functions** (1):
`crypto_price_historical`

**Imports** (5):
`typing`, `TYPE_CHECKING`, `openbb_charting.core.openbb_figure`, `openbb_charting.charts.price_historical`, `price_historical`


## Key Components

**Class `CryptoViews`**: Crypto Views.

## Usage & Examples

See source code for usage details.

## Related Files

- `typing`
- `openbb_charting.core.openbb_figure`
- `openbb_charting.charts.price_historical`

## Notes
- Generated: 2025-11-18T07:54:35.917356
- Generator: World's Best Repo Book Generator v1.0.0

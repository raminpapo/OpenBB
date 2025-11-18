# Documentation: openbb_platform/extensions/currency/openbb_currency/currency_views.py

## File Metadata
- **Path**: `openbb_platform/extensions/currency/openbb_currency/currency_views.py`
- **Size**: 582 characters, 23 lines
- **Words**: 47
- **Extension**: .py
- **Classification**: Text file

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

## High-Level Overview

Views for the Currency Extension.

from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
from openbb_charting.core.openbb_figure import (
OpenBBFigure,
)


class CurrencyViews:
Currency Views.
Currency Price Historical Chart.
# pylint: disable=import-outside-toplevel
from openbb_charting.charts.price_historical import price_historical

return price_historical(**kwargs)


## Detailed Structure

### Python File Structure

**Classes** (1):
`CurrencyViews`

**Functions** (1):
`currency_price_historical`

**Imports** (5):
`typing`, `TYPE_CHECKING`, `openbb_charting.core.openbb_figure`, `openbb_charting.charts.price_historical`, `price_historical`


## Key Components

**Class `CurrencyViews`**: Currency Views.

## Usage & Examples

See source code for usage details.

## Related Files

- `typing`
- `openbb_charting.core.openbb_figure`
- `openbb_charting.charts.price_historical`

## Notes
- Generated: 2025-11-18T07:54:35.938364
- Generator: World's Best Repo Book Generator v1.0.0

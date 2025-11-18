# Documentation: openbb_platform/extensions/index/openbb_index/index_views.py

## File Metadata
- **Path**: `openbb_platform/extensions/index/openbb_index/index_views.py`
- **Size**: 567 characters, 23 lines
- **Words**: 47
- **Extension**: .py
- **Classification**: Text file

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

## High-Level Overview

Views for the index Extension.

from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
from openbb_charting.core.openbb_figure import (
OpenBBFigure,
)


class IndexViews:
Index Views.
Index Price Historical Chart.
# pylint: disable=import-outside-toplevel
from openbb_charting.charts.price_historical import price_historical

return price_historical(**kwargs)


## Detailed Structure

### Python File Structure

**Classes** (1):
`IndexViews`

**Functions** (1):
`index_price_historical`

**Imports** (5):
`typing`, `TYPE_CHECKING`, `openbb_charting.core.openbb_figure`, `openbb_charting.charts.price_historical`, `price_historical`


## Key Components

**Class `IndexViews`**: Index Views.

## Usage & Examples

See source code for usage details.

## Related Files

- `typing`
- `openbb_charting.core.openbb_figure`
- `openbb_charting.charts.price_historical`

## Notes
- Generated: 2025-11-18T07:54:36.163541
- Generator: World's Best Repo Book Generator v1.0.0

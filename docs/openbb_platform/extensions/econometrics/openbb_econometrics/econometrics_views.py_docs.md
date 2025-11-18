# Documentation: openbb_platform/extensions/econometrics/openbb_econometrics/econometrics_views.py

## File Metadata
- **Path**: `openbb_platform/extensions/econometrics/openbb_econometrics/econometrics_views.py`
- **Size**: 1,368 characters, 40 lines
- **Words**: 127
- **Extension**: .py
- **Classification**: Text file

## Original Source

```python
"""Views for the Econometrics Extension."""

from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from openbb_charting.core.openbb_figure import (
        OpenBBFigure,
    )


class EconometricsViews:
    """Econometrics Views."""

    @staticmethod
    def econometrics_correlation_matrix(  # noqa: PLR0912
        **kwargs,
    ) -> tuple["OpenBBFigure", dict[str, Any]]:
        """Correlation Matrix Chart.

        Parameters
        ----------
        data : Union[list[Data], DataFrame]
            Input dataset.
        method : Literal["pearson", "kendall", "spearman"]
            Method to use for correlation calculation. Default is "pearson".
                pearson : standard correlation coefficient
                kendall : Kendall Tau correlation coefficient
                spearman : Spearman rank correlation
        colorscale : str
            Plotly colorscale to use for the heatmap. Default is "RdBu".
        title : str
            Title of the chart. Default is "Asset Correlation Matrix".
        layout_kwargs : Dict[str, Any]
            Additional keyword arguments to apply with figure.update_layout(), by default None.
        """
        # pylint: disable=import-outside-toplevel
        from openbb_charting.charts.correlation_matrix import correlation_matrix

        return correlation_matrix(**kwargs)  # type: ignore

```

## High-Level Overview

Views for the Econometrics Extension.

from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
from openbb_charting.core.openbb_figure import (
OpenBBFigure,
)


class EconometricsViews:
Econometrics Views.
Correlation Matrix Chart.

Parameters
----------
data : Union[list[Data], DataFrame]
Input dataset.
method : Literal["pearson", "kendall", "spearman"]
Method to use for correlation calculation. Default is "pearson".

## Detailed Structure

### Python File Structure

**Classes** (1):
`EconometricsViews`

**Functions** (1):
`econometrics_correlation_matrix`

**Imports** (5):
`typing`, `TYPE_CHECKING`, `openbb_charting.core.openbb_figure`, `openbb_charting.charts.correlation_matrix`, `correlation_matrix`


## Key Components

**Class `EconometricsViews`**: Econometrics Views.

## Usage & Examples

See source code for usage details.

## Related Files

- `typing`
- `openbb_charting.core.openbb_figure`
- `openbb_charting.charts.correlation_matrix`

## Notes
- Generated: 2025-11-18T07:54:36.008519
- Generator: World's Best Repo Book Generator v1.0.0

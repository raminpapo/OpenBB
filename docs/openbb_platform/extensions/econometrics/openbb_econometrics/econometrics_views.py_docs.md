# File Documentation: econometrics_views.py

## Metadata
- **Path**: `openbb_platform/extensions/econometrics/openbb_econometrics/econometrics_views.py`
- **Size**: 1,368 bytes
- **Lines**: 40
- **Category**: python
- **Extension**: .py

---

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



---

## High-Level Overview

This is a **python** file named `econometrics_views.py`.

**Python Module**

- **Classes** (1): EconometricsViews
- **Functions** (1): econometrics_correlation_matrix
- **Import Statements**: 2


---

## Detailed Analysis

### Python Code Structure

#### Classes

- **`EconometricsViews`**

#### Decorators Used

staticmethod


---

## Related Files

The following files may be related based on imports and references:

**Imported Modules**:
- `TYPE_CHECKING`
- `correlation_matrix`
- `openbb_charting.charts.correlation_matrix`
- `openbb_charting.core.openbb_figure`
- `typing`


---

## Performance & Security Notes

No obvious security concerns detected in static analysis.


---

**Generated**: 2025-11-19T02:16:46.876332Z
**Generator**: World's Best Repo Book Generator v1.0

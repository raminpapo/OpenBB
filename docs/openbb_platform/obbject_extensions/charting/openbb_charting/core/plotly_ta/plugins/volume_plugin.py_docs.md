# File Documentation: volume_plugin.py

## Metadata
- **Path**: `openbb_platform/obbject_extensions/charting/openbb_charting/core/plotly_ta/plugins/volume_plugin.py`
- **Size**: 3,547 bytes
- **Lines**: 126
- **Category**: python
- **Extension**: .py

---

## Original Source

```python
"""Volume technical indicators."""

import pandas as pd

from openbb_charting.core.openbb_figure import OpenBBFigure
from openbb_charting.core.plotly_ta.base import (
    PltTA,
    indicator,
)
from openbb_charting.core.plotly_ta.data_classes import (
    columns_regex,
)


class Volume(PltTA):
    """Volume technical indicators."""

    __subplots__ = ["ad", "adosc", "obv"]

    # Useless super delegation
    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)

    @indicator()
    def plot_ad(self, fig: OpenBBFigure, df_ta: pd.DataFrame, subplot_row: int):
        """Add ad to plotly figure."""
        ad_col = columns_regex(df_ta, "AD")[0]
        fig.add_scatter(
            name="AD",
            mode="lines",
            line=dict(width=1.5, color=fig.theme.get_colors()[1]),
            x=df_ta.index,
            y=df_ta[ad_col].values,
            opacity=0.9,
            row=subplot_row,
            col=1,
            secondary_y=False,
        )

        fig.add_hline(
            y=0,
            fillcolor="white",
            opacity=1,
            layer="below",
            line=dict(color="white", dash="dash", width=2),
            row=subplot_row,
            col=1,
            secondary_y=False,
        )

        fig.add_annotation(
            xref=f"x{subplot_row} domain",
            yref=f"y{subplot_row + 1} domain",
            text="<b>AD</b>",
            x=0,
            xanchor="right",
            xshift=-6,
            y=0.98,
            font_size=14,
            font_color=fig.theme.get_colors()[1],
        )
        fig["layout"][f"yaxis{subplot_row + 1}"].update(nticks=3, autorange=True)

        return fig, subplot_row + 1

    @indicator()
    def plot_adosc(self, fig: OpenBBFigure, df_ta: pd.DataFrame, subplot_row: int):
        """Add adosc to plotly figure."""
        ad_col = columns_regex(df_ta, "ADOSC")[0]
        fig.add_scatter(
            name="ADOSC",
            mode="lines",
            line=dict(width=1.5, color=fig.theme.get_colors()[1]),
            x=df_ta.index,
            y=df_ta[ad_col].values,
            opacity=0.9,
            row=subplot_row,
            col=1,
            secondary_y=False,
        )

        fig.add_annotation(
            xref=f"x{subplot_row} domain",
            yref=f"y{subplot_row + 1} domain",
            text="<b>ADOSC</b>",
            x=0,
            xanchor="right",
            xshift=-6,
            y=0.98,
            font_size=14,
            font_color=fig.theme.get_colors()[1],
        )

        return fig, subplot_row + 1

    @indicator()
    def plot_obv(self, fig: OpenBBFigure, df_ta: pd.DataFrame, subplot_row: int):
        """Add obv to plotly figure."""
        obv_col = columns_regex(df_ta, "OBV")[0]
        fig.add_scatter(
            name="OBV",
            mode="lines",
            line=dict(width=1.5, color=fig.theme.get_colors()[1]),
            x=df_ta.index,
            y=df_ta[obv_col].values,
            opacity=0.9,
            row=subplot_row,
            col=1,
            secondary_y=False,
        )

        fig.add_annotation(
            xref=f"x{subplot_row} domain",
            yref=f"y{subplot_row + 1} domain",
            text="<b>OBV</b>",
            x=0,
            xanchor="right",
            xshift=-6,
            y=0.98,
            font_size=14,
            font_color=fig.theme.get_colors()[1],
        )
        fig["layout"][f"yaxis{subplot_row + 1}"].update(nticks=5, autorange=True)

        return fig, subplot_row + 1

```



---

## High-Level Overview

This is a **python** file named `volume_plugin.py`.

**Python Module**

- **Classes** (1): Volume
- **Functions** (4): __init__, plot_ad, plot_adosc, plot_obv
- **Import Statements**: 1


---

## Detailed Analysis

### Python Code Structure

#### Classes

- **`Volume`**(PltTA)

#### Functions

- **`__init__(self, *args, **kwargs)`**
- **`plot_ad(self, fig: OpenBBFigure, df_ta: pd.DataFrame, subplot_row: int)`**
- **`plot_adosc(self, fig: OpenBBFigure, df_ta: pd.DataFrame, subplot_row: int)`**
- **`plot_obv(self, fig: OpenBBFigure, df_ta: pd.DataFrame, subplot_row: int)`**

#### Decorators Used

indicator


---

## Related Files

The following files may be related based on imports and references:

**Imported Modules**:
- `OpenBBFigure`
- `openbb_charting.core.openbb_figure`
- `openbb_charting.core.plotly_ta.base`
- `openbb_charting.core.plotly_ta.data_classes`
- `pandas`


---

## Performance & Security Notes

No obvious security concerns detected in static analysis.


---

**Generated**: 2025-11-19T02:16:48.216816Z
**Generator**: World's Best Repo Book Generator v1.0

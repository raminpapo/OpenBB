# File Documentation: to_chart.py

## Metadata
- **Path**: `openbb_platform/obbject_extensions/charting/openbb_charting/core/to_chart.py`
- **Size**: 2,393 bytes
- **Lines**: 69
- **Category**: python
- **Extension**: .py

---

## Original Source

```python
"""Module containing the to_chart function."""

from typing import TYPE_CHECKING, Any, Union

if TYPE_CHECKING:
    from openbb_charting.core.plotly_ta.data_classes import ChartIndicators  # noqa
    from openbb_charting.core.openbb_figure import OpenBBFigure  # noqa
    from pandas import DataFrame, Series  # noqa


def to_chart(  # pylint: disable=R0917
    data: Union["DataFrame", "Series"],
    indicators: Union["ChartIndicators", dict[str, dict[str, Any]]] | None = None,
    symbol: str = "",
    candles: bool = True,
    volume: bool = True,
    prepost: bool = False,
    volume_ticks_x: int = 7,
) -> tuple["OpenBBFigure", dict[str, Any]]:
    """Return the plotly json representation of the chart.

    This function is used so it can be called at the module level and used out of the box,
    which allows some more flexibility, ease of use and doesn't require the user to know
    about the PlotlyTA class.

    Parameters
    ----------
    data : Union[DataFrame, Series]
        Data to be plotted.
    indicators : Optional[Union[ChartIndicators, Dict[str, Dict[str, Any]]]], optional
        Indicators to be plotted, by default None
    symbol : str, optional
        Symbol to be plotted, by default ""
    candles : bool, optional
        If True, candles will be plotted, by default True
    volume : bool, optional
        If True, volume will be plotted, by default True
    prepost : bool, optional
        If True, prepost will be plotted, by default False
    volume_ticks_x : int, optional
        Volume ticks, by default 7

    Returns
    -------
    Tuple[OpenBBFigure, Dict[str, Any]]
        Tuple containing the OpenBBFigure and the plotly json representation of the chart.
    """
    # pylint: disable=import-outside-toplevel
    from openbb_charting.core.plotly_ta.ta_class import PlotlyTA

    try:
        ta = PlotlyTA()
        fig = ta.plot(  # type: ignore
            df_stock=data,
            indicators=indicators,
            symbol=symbol,
            candles=candles,
            volume=volume,
            prepost=prepost,
            volume_ticks_x=volume_ticks_x,
        )
        content = fig.show(external=True).to_plotly_json()

        return fig, content
    except Exception as e:
        raise Exception(
            f"Failed to convert results to chart. Ensure the provided data is a valid time series. {e}"
        ) from e

```



---

## High-Level Overview

This is a **python** file named `to_chart.py`.

**Python Module**

- **Classes** (1): import
- **Functions** (1): to_chart
- **Import Statements**: 5


---

## Detailed Analysis

### Python Code Structure



---

## Related Files

The following files may be related based on imports and references:

**Imported Modules**:
- `ChartIndicators`
- `DataFrame`
- `OpenBBFigure`
- `PlotlyTA`
- `TYPE_CHECKING`
- `openbb_charting.core.openbb_figure`
- `openbb_charting.core.plotly_ta.data_classes`
- `openbb_charting.core.plotly_ta.ta_class`
- `pandas`
- `typing`


---

## Performance & Security Notes

No obvious security concerns detected in static analysis.


---

**Generated**: 2025-11-19T02:16:47.849541Z
**Generator**: World's Best Repo Book Generator v1.0

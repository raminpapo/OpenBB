# File Documentation: statistics.py

## Metadata
- **Path**: `openbb_platform/extensions/quantitative/openbb_quantitative/statistics.py`
- **Size**: 1,327 bytes
- **Lines**: 46
- **Category**: python
- **Extension**: .py

---

## Original Source

```python
"""Statistics Functions."""

from numpy import (
    mean as mean_np,
    ndarray,
    std,
    var as var_np,
)
from pandas import DataFrame, Series
from scipy import stats

# Because python is weird and these being the same name as the fastapi router functions
# which overwrites the function signature, we add the _ after the function name


def kurtosis_(data: DataFrame | Series | ndarray) -> float:
    """Get Kurtosis.

    It is a measure of the "tailedness" of the probability distribution of a real-valued random variable.
    """
    return stats.kurtosis(data)


def skew_(data: DataFrame | Series | ndarray) -> float:
    """Get Skewness.

    It is a measure of the asymmetry of the probability distribution of a
    real-valued random variable about its mean.
    """
    return stats.skew(data)


def mean_(data: DataFrame | Series | ndarray) -> float:
    """Get Mean which is the average of the numbers."""
    return mean_np(data)


def std_dev_(data: DataFrame | Series | ndarray) -> float:
    """Get Standard deviation that is a measure of the amount of variation or dispersion of a set of values."""
    return std(data)


def var_(data: DataFrame | Series | ndarray) -> float:
    """Get Variance that is a measure of the amount of variation or dispersion of a set of values."""
    return var_np(data)

```



---

## High-Level Overview

This is a **python** file named `statistics.py`.

**Python Module**

- **Functions** (5): kurtosis_, skew_, mean_, std_dev_, var_
- **Import Statements**: 1


---

## Detailed Analysis

### Python Code Structure



---

## Related Files

The following files may be related based on imports and references:

**Imported Modules**:
- `DataFrame`
- `numpy`
- `pandas`
- `scipy`
- `stats`


---

## Performance & Security Notes

No obvious security concerns detected in static analysis.


---

**Generated**: 2025-11-19T02:16:47.261264Z
**Generator**: World's Best Repo Book Generator v1.0

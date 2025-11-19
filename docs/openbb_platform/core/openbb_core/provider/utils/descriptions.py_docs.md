# File Documentation: descriptions.py

## Metadata
- **Path**: `openbb_platform/core/openbb_core/provider/utils/descriptions.py`
- **Size**: 1,166 bytes
- **Lines**: 30
- **Category**: python
- **Extension**: .py

---

## Original Source

```python
"""Common descriptions for model fields."""

QUERY_DESCRIPTIONS = {
    "symbol": "Symbol to get data for.",
    "start_date": "Start date of the data, in YYYY-MM-DD format.",
    "end_date": "End date of the data, in YYYY-MM-DD format.",
    "interval": "Time interval of the data to return.",
    "period": "Time period of the data to return.",
    "date": "A specific date to get data for.",
    "limit": "The number of data entries to return.",
    "country": "The country to get data.",
    "countries": "The country or countries to get data.",
    "units": "The unit of measurement for the data.",
    "frequency": "The frequency of the data.",
}

DATA_DESCRIPTIONS = {
    "symbol": "Symbol representing the entity requested in the data.",
    "cik": "Central Index Key (CIK) for the requested entity.",
    "date": "The date of the data.",
    "open": "The open price.",
    "high": "The high price.",
    "low": "The low price.",
    "close": "The close price.",
    "volume": "The trading volume.",
    "adj_close": "The adjusted close price.",
    "vwap": "Volume Weighted Average Price over the period.",
    "prev_close": "The previous close price.",
}

```



---

## High-Level Overview

This is a **python** file named `descriptions.py`.

**Python Module**



---

## Detailed Analysis

### Python Code Structure



---

## Related Files

The following files may be related based on imports and references:

*No direct imports detected.*


---

## Performance & Security Notes

No obvious security concerns detected in static analysis.


---

**Generated**: 2025-11-19T02:16:46.604306Z
**Generator**: World's Best Repo Book Generator v1.0

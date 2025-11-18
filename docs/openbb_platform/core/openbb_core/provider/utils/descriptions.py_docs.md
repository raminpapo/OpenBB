# Documentation: openbb_platform/core/openbb_core/provider/utils/descriptions.py

## File Metadata
- **Path**: `openbb_platform/core/openbb_core/provider/utils/descriptions.py`
- **Size**: 1,166 characters, 30 lines
- **Words**: 159
- **Extension**: .py
- **Classification**: Text file

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

## High-Level Overview

Common descriptions for model fields.

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

## Detailed Structure

### Python File Structure

**Classes** (0):
None

**Functions** (0):
None

**Imports** (0):
None


## Key Components

No major components extracted.

## Usage & Examples

See source code for usage details.

## Related Files

No direct file references found.

## Notes
- Generated: 2025-11-18T07:54:35.768177
- Generator: World's Best Repo Book Generator v1.0.0

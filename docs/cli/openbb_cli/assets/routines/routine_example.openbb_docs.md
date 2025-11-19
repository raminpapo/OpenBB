# File Documentation: routine_example.openbb

## Metadata
- **Path**: `cli/openbb_cli/assets/routines/routine_example.openbb`
- **Size**: 439 bytes
- **Lines**: 21
- **Category**: text
- **Extension**: .openbb

---

## Original Source

```
# Go into the equity context
equity

# Get the company's profile
profile --symbol aapl

# Get company's statements
fundamental
balance --symbol aapl
cash --symbol aapl
transcript --symbol aapl --year 2023

# Load company's historical data
../price
historical --symbol aapl

# Get its performance
performance --symbol aapl

# Export the candle as an image and the historical data into a csv
historical --symbol aapl --chart --export csv,jpg
```



---

## High-Level Overview

This is a **text** file named `routine_example.openbb`.

This file contains 21 lines of code/text.


---

## Detailed Analysis

This file contains code or text data. See the original source above for full details.


---

## Related Files

The following files may be related based on imports and references:

*No direct imports detected.*


---

## Performance & Security Notes

No obvious security concerns detected in static analysis.


---

**Generated**: 2025-11-19T02:15:18.829230Z
**Generator**: World's Best Repo Book Generator v1.0

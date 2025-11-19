# File Documentation: profitable_low_price_sales.ini

## Metadata
- **Path**: `openbb_platform/providers/finviz/openbb_finviz/utils/presets/profitable_low_price_sales.ini`
- **Size**: 396 bytes
- **Lines**: 22
- **Category**: config
- **Extension**: .ini

---

## Original Source

```
# Author of preset: OpenBB
# Description: Profitable companies with high sales growth, low P/S, and decent trading volume.

[General]

Order = Price/Sales
Ascend = true

[Descriptive]

Market Cap. = +Mid (over $2bln)
Average Volume = Over 1M

[Fundamental]

P/S = Under 10
Sales growthqtr over qtr = High (>25%)
Sales growthpast 5 years = Over 30%
Net Profit Margin = Positive (>0%)

[Technical]

```



---

## High-Level Overview

This is a **config** file named `profitable_low_price_sales.ini`.

**Configuration File**

This file contains configuration settings for the project.


---

## Detailed Analysis

### Configuration Structure

This configuration file defines settings and parameters for the project.


---

## Related Files

The following files may be related based on imports and references:

*No direct imports detected.*


---

## Performance & Security Notes

No obvious security concerns detected in static analysis.


---

**Generated**: 2025-11-19T02:16:50.451572Z
**Generator**: World's Best Repo Book Generator v1.0

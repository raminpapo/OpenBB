# File Documentation: fastgrowths.ini

## Metadata
- **Path**: `openbb_platform/providers/finviz/openbb_finviz/utils/presets/fastgrowths.ini`
- **Size**: 694 bytes
- **Lines**: 24
- **Category**: config
- **Extension**: .ini

---

## Original Source

```
# Author of preset: mmistroni@gmail.com
# Description: Fastest growth watch list. Again, from Medium article https://medium.com/the-investors-handbook/the-best-finviz-screens-for-growth-investors-72795f507b91
#
[General]
Order = Market Cap.

[Descriptive]
Market Cap. = +Mid (over $2bln)
Average Volume = Over 200K
Price = Over $10
[Fundamental]
EPS growththis year = Over 20%
EPS growthnext year = Over 20%
EPS growthqtr over qtr = Over 20%
Sales growthqtr over qtr = Over 20%
Return on Equity = Over +20%
Gross Margin = Over 20%

[Technical]
20-Day Simple Moving Average = Price above SMA20
50-Day Simple Moving Average = Price above SMA50
200-Day Simple Moving Average = Price above SMA200


```



---

## High-Level Overview

This is a **config** file named `fastgrowths.ini`.

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

**Generated**: 2025-11-19T02:16:50.439961Z
**Generator**: World's Best Repo Book Generator v1.0

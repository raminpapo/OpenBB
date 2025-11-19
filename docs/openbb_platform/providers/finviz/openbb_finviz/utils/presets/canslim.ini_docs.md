# File Documentation: canslim.ini

## Metadata
- **Path**: `openbb_platform/providers/finviz/openbb_finviz/utils/presets/canslim.ini`
- **Size**: 909 bytes
- **Lines**: 28
- **Category**: config
- **Extension**: .ini

---

## Original Source

```
# Author of preset: mmistroni@gmail.com
# Description: Canslim stocks are ones that are likely to explode , cfr https://en.wikipedia.org/wiki/CAN_SLIM
# Params picked from  https://medium.com/the-investors-handbook/the-best-finviz-screens-for-growth-investors-72795f507b91
# This config add some extra filters to make the list more robust

[General]

Order = Market Cap.

[Descriptive]
Average Volume =  Over 200K
Float =  Under 50M

[Fundamental]
EPS growththis year = Over 20%
EPS growthnext year = Over 20%
EPS growthqtr over qtr = Over 20%
Sales growthqtr over qtr = Over 20%
EPS growthpast 5 years = Over 20%
Gross Margin = Positive (>0%)
Return on Equity = Positive (>0%)
InstitutionalOwnership = Over 20%

[Technical]
20-Day Simple Moving Average = Price above SMA20
50-Day Simple Moving Average = Price above SMA50
200-Day Simple Moving Average = Price above SMA200
52-Week High/Low = 0-10% below High
```



---

## High-Level Overview

This is a **config** file named `canslim.ini`.

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

**Generated**: 2025-11-19T02:16:50.433162Z
**Generator**: World's Best Repo Book Generator v1.0

# File Documentation: growth_stocks.ini

## Metadata
- **Path**: `openbb_platform/providers/finviz/openbb_finviz/utils/presets/growth_stocks.ini`
- **Size**: 538 bytes
- **Lines**: 24
- **Category**: config
- **Extension**: .ini

---

## Original Source

```
# Author of preset: JohnnyDankseed
# Description: Growth Stocks

[General]
Order = PEG (Price/Earnings/Growth)
Signal = Top Gainers

[Descriptive]
Market Cap. = +Micro (over $50mln)
Average Volume = Over 300K
Country = USA
Price = Over $10

[Fundamental]
EPS growthnext 5 years = Over 15%
Debt/Equity = Under 0.5
PEG = Under 2
EPS growththis year = Over 15%
EPS growthqtr over qtr = Over 15%
EPS growthpast 5 years = Over 15%

[Technical]
20-Day Simple Moving Average = SMA20 above SMA200
50-Day Simple Moving Average = SMA50 above SMA200
```



---

## High-Level Overview

This is a **config** file named `growth_stocks.ini`.

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

**Generated**: 2025-11-19T02:16:50.442787Z
**Generator**: World's Best Repo Book Generator v1.0

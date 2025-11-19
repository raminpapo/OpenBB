# File Documentation: newhigh.ini

## Metadata
- **Path**: `openbb_platform/providers/finviz/openbb_finviz/utils/presets/newhigh.ini`
- **Size**: 833 bytes
- **Lines**: 29
- **Category**: config
- **Extension**: .ini

---

## Original Source

```
# Author of preset: mmistroni@gmail.com
# Description: Custom filters for new highs. Copied from an interesting Medium article
# https://medium.com/the-investors-handbook/the-best-finviz-screens-for-growth-investors-72795f507b91

[General]

Order = Market Cap.

[Descriptive]
Market Cap. = +Small (over $300mln)
Average Volume = Over 200K
Relative Volume = Over 1
Price = Over $10
[Fundamental]
EPS growththis year = Positive (>0%)
EPS growthnext year = Positive (>0%)
EPS growthqtr over qtr = Positive (>0%)
Sales growthqtr over qtr = Positive (>0%)
Return on Equity = Positive (>0%)
[Technical]
Performance = Today Up
20-Day Simple Moving Average = Price above SMA20
50-Day Simple Moving Average = Price above SMA50
200-Day Simple Moving Average = Price above SMA200
Change = Up
Change from Open =  Up
52-Week High/Low = New High


```



---

## High-Level Overview

This is a **config** file named `newhigh.ini`.

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

**Generated**: 2025-11-19T02:16:50.450191Z
**Generator**: World's Best Repo Book Generator v1.0

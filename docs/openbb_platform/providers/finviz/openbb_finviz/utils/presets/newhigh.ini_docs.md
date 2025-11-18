# Documentation: openbb_platform/providers/finviz/openbb_finviz/utils/presets/newhigh.ini

## File Metadata
- **Path**: `openbb_platform/providers/finviz/openbb_finviz/utils/presets/newhigh.ini`
- **Size**: 833 characters, 29 lines
- **Words**: 121
- **Extension**: .ini
- **Classification**: Text file

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

## High-Level Overview

This is a .ini file containing 29 lines of code.

## Detailed Structure

Standard text file.

## Key Components

No major components extracted.

## Usage & Examples

See source code for usage details.

## Related Files

No direct file references found.

## Notes
- Generated: 2025-11-18T07:54:39.205483
- Generator: World's Best Repo Book Generator v1.0.0

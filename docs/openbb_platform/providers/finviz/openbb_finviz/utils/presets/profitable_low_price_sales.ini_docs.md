# Documentation: openbb_platform/providers/finviz/openbb_finviz/utils/presets/profitable_low_price_sales.ini

## File Metadata
- **Path**: `openbb_platform/providers/finviz/openbb_finviz/utils/presets/profitable_low_price_sales.ini`
- **Size**: 396 characters, 22 lines
- **Words**: 64
- **Extension**: .ini
- **Classification**: Text file

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

## High-Level Overview

This is a .ini file containing 22 lines of code.

## Detailed Structure

Standard text file.

## Key Components

No major components extracted.

## Usage & Examples

See source code for usage details.

## Related Files

No direct file references found.

## Notes
- Generated: 2025-11-18T07:54:39.206963
- Generator: World's Best Repo Book Generator v1.0.0

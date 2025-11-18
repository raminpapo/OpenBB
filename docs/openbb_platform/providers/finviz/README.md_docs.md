# Documentation: openbb_platform/providers/finviz/README.md

## File Metadata
- **Path**: `openbb_platform/providers/finviz/README.md`
- **Size**: 3,047 characters, 112 lines
- **Words**: 379
- **Extension**: .md
- **Classification**: Text file

## Original Source

```markdown
# OpenBB Finviz Data Provider Extension

This extension integrates the [Finviz](https://finviz.com/) data provider into the OpenBB Platform.

It will install, [finvizfinance](https://github.com/lit26/finvizfinance/), to power the functions.

## Installation

To install the extension:

```bash
pip install openbb-finviz
```

## Endpoints

- obb.equity.compare.groups
- obb.equity.estimates.price_target
- obb.equity.fundamental.metrics
- obb.equity.profile
- obb.equity.price.performance
- obb.equity.screener

## Screener

The screener is a faithful replication of the public-facing stock screener - https://finviz.com/screener.ashx?

Some options are directly accessible through the function parameters, all others are exposed via `presets` or `filters_dict`.
The filters list below are exposed in the function, with choices visible in the docstring:

- `exchange`
- `index`
- `sector`
- `industry`
- `mktcap`
- `recommendation` (analyst's mean score from 1-5)
- `signal` (same as the "Signal" on the Finviz page)

When the function is run without any parameters, it will default to the "top_gainers" signal.

```python
res = obb.equity.screener(provider="finviz")
```

### Metric

The `metric` parameter defines the type of data fields to return. Choices are:

- `overview`
- `ownership`
- `performance`
- `technical`
- `valuation`

Default is, "overview".

```
res = obb.equity.screener(provider="finviz", metric="performance")
```

### Preset Files

Presets can be created and customized in the "OpenBBUserData" folder. Template and default presets are created on the first run of the function.

Files are loaded on runtime, changes are effective without restarting the Python interpreter.

The `preset` parameter will override all others, except `metric` and `limit`.

Run the function to create the template and default presets in your `OpenBBUserData` folder.

Presets from the legacy OpenBB Terminal will continue to work, simply move your presets into the folder below.

```python
res = obb.equity.screener(provider="finviz", index="nasdaq")
```

Then find the presets here: `$HOME/OpenBBUserData/presets/finviz`

```python
res = obb.equity.screener(provider="finviz", preset="short_squeeze")
```

### Filters Dict

The `filters_dict` parameter acts as an alternative to `preset`, accepting a dictionary or JSON encoded string.

```python
res = obb.equity.screener(provider="finviz", filters_dict={"Index": "NASDAQ 100"})
```

Or as a JSON:

```python
res = obb.equity.screener(provider="finviz", filters_dict='{"Index": "NASDAQ 100"}')
```

When using the Fast API, this is sent in the request body.

### Error Messages

All parameters are validated, incorrect keys and choices will raise an error with information to help correct. For example:

```python
obb.equity.screener(provider="finviz", filters_dict='{"Index": "NASDAQ"}')
```

```console
Invalid filter option 'NASDAQ'. Possible filter options: ['Any', 'S&P 500', 'NASDAQ 100', 'DJIA', 'RUSSELL 2000']
```

Read the OpenBB Platform documentation [here](https://docs.openbb.co)

```

## High-Level Overview

This is a .md file containing 112 lines of code.

## Detailed Structure

Standard text file.

## Key Components

No major components extracted.

## Usage & Examples

See source code for usage details.

## Related Files

No direct file references found.

## Notes
- Generated: 2025-11-18T07:54:39.154526
- Generator: World's Best Repo Book Generator v1.0.0

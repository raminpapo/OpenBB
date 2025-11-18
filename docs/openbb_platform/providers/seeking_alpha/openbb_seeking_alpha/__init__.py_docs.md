# Documentation: openbb_platform/providers/seeking_alpha/openbb_seeking_alpha/__init__.py

## File Metadata
- **Path**: `openbb_platform/providers/seeking_alpha/openbb_seeking_alpha/__init__.py`
- **Size**: 847 characters, 24 lines
- **Words**: 56
- **Extension**: .py
- **Classification**: Text file

## Original Source

```python
"""Seeking Alpha Provider module."""

from openbb_core.provider.abstract.provider import Provider
from openbb_seeking_alpha.models.calendar_earnings import SACalendarEarningsFetcher
from openbb_seeking_alpha.models.forward_eps_estimates import (
    SAForwardEpsEstimatesFetcher,
)
from openbb_seeking_alpha.models.forward_sales_estimates import (
    SAForwardSalesEstimatesFetcher,
)

seeking_alpha_provider = Provider(
    name="seeking_alpha",
    website="https://seekingalpha.com",
    description="""Seeking Alpha is a data provider with access to news, analysis, and
real-time alerts on stocks.""",
    fetcher_dict={
        "CalendarEarnings": SACalendarEarningsFetcher,
        "ForwardEpsEstimates": SAForwardEpsEstimatesFetcher,
        "ForwardSalesEstimates": SAForwardSalesEstimatesFetcher,
    },
    repr_name="Seeking Alpha",
)

```

## High-Level Overview

Seeking Alpha Provider module.

from openbb_core.provider.abstract.provider import Provider
from openbb_seeking_alpha.models.calendar_earnings import SACalendarEarningsFetcher
from openbb_seeking_alpha.models.forward_eps_estimates import (
SAForwardEpsEstimatesFetcher,
)
from openbb_seeking_alpha.models.forward_sales_estimates import (
SAForwardSalesEstimatesFetcher,
)

seeking_alpha_provider = Provider(
name="seeking_alpha",
website="https://seekingalpha.com",
description="""Seeking Alpha is a data provider with access to news, analysis, and
real-time alerts on stocks.""",
fetcher_dict={
"CalendarEarnings": SACalendarEarningsFetcher,
"ForwardEpsEstimates": SAForwardEpsEstimatesFetcher,
"ForwardSalesEstimates": SAForwardSalesEstimatesFetcher,

## Detailed Structure

### Python File Structure

**Classes** (0):
None

**Functions** (0):
None

**Imports** (6):
`openbb_core.provider.abstract.provider`, `Provider`, `openbb_seeking_alpha.models.calendar_earnings`, `SACalendarEarningsFetcher`, `openbb_seeking_alpha.models.forward_eps_estimates`, `openbb_seeking_alpha.models.forward_sales_estimates`


## Key Components

No major components extracted.

## Usage & Examples

See source code for usage details.

## Related Files

- `openbb_core.provider.abstract.provider`
- `openbb_seeking_alpha.models.calendar_earnings`
- `openbb_seeking_alpha.models.forward_eps_estimates`
- `openbb_seeking_alpha.models.forward_sales_estimates`

## Notes
- Generated: 2025-11-18T07:54:41.651439
- Generator: World's Best Repo Book Generator v1.0.0

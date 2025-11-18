# Documentation: openbb_platform/providers/congress_gov/openbb_congress_gov/__init__.py

## File Metadata
- **Path**: `openbb_platform/providers/congress_gov/openbb_congress_gov/__init__.py`
- **Size**: 1,185 characters, 30 lines
- **Words**: 109
- **Extension**: .py
- **Classification**: Text file

## Original Source

```python
"""Congress.gov Provider Module."""

from openbb_congress_gov.models.bill_info import CongressBillInfoFetcher
from openbb_congress_gov.models.bill_text import CongressBillTextFetcher
from openbb_congress_gov.models.congress_bills import CongressBillsFetcher
from openbb_core.provider.abstract.provider import Provider

congress_gov_provider = Provider(
    name="congress_gov",
    website="https://api.congress.gov",
    description="""The Congress.gov API provides legislative data from the U.S.
Congress, including bills, summaries, and related information. The Federal
Register API provides access to presidential documents and regulations.""",
    credentials=["api_key"],
    fetcher_dict={
        "CongressBills": CongressBillsFetcher,
        "CongressBillInfo": CongressBillInfoFetcher,
        "CongressBillText": CongressBillTextFetcher,
    },
    repr_name="Congress.gov",
    instructions="""To get a Congress.gov API key:

1. Go to https://api.congress.gov/sign-up/
2. Fill out the registration form with your information
3. Agree to the terms of service
4. You will receive an API key via email

The API key is free and provides access to all Congress.gov data.""",
)

```

## High-Level Overview

Congress.gov Provider Module.

from openbb_congress_gov.models.bill_info import CongressBillInfoFetcher
from openbb_congress_gov.models.bill_text import CongressBillTextFetcher
from openbb_congress_gov.models.congress_bills import CongressBillsFetcher
from openbb_core.provider.abstract.provider import Provider

congress_gov_provider = Provider(
name="congress_gov",
website="https://api.congress.gov",
description="""The Congress.gov API provides legislative data from the U.S.
Congress, including bills, summaries, and related information. The Federal
Register API provides access to presidential documents and regulations.""",
credentials=["api_key"],
fetcher_dict={
"CongressBills": CongressBillsFetcher,
"CongressBillInfo": CongressBillInfoFetcher,
"CongressBillText": CongressBillTextFetcher,
},
repr_name="Congress.gov",

## Detailed Structure

### Python File Structure

**Classes** (0):
None

**Functions** (0):
None

**Imports** (9):
`openbb_congress_gov.models.bill_info`, `CongressBillInfoFetcher`, `openbb_congress_gov.models.bill_text`, `CongressBillTextFetcher`, `openbb_congress_gov.models.congress_bills`, `CongressBillsFetcher`, `openbb_core.provider.abstract.provider`, `Provider`, `the`


## Key Components

No major components extracted.

## Usage & Examples

See source code for usage details.

## Related Files

- `openbb_congress_gov.models.bill_info`
- `openbb_congress_gov.models.bill_text`
- `openbb_congress_gov.models.congress_bills`
- `openbb_core.provider.abstract.provider`

## Notes
- Generated: 2025-11-18T07:54:37.594955
- Generator: World's Best Repo Book Generator v1.0.0

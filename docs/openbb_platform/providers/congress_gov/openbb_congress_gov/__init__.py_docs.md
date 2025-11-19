# File Documentation: __init__.py

## Metadata
- **Path**: `openbb_platform/providers/congress_gov/openbb_congress_gov/__init__.py`
- **Size**: 1,185 bytes
- **Lines**: 30
- **Category**: python
- **Extension**: .py

---

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



---

## High-Level Overview

This is a **python** file named `__init__.py`.

**Python Module**

- **Import Statements**: 1


---

## Detailed Analysis

### Python Code Structure



---

## Related Files

The following files may be related based on imports and references:

**Imported Modules**:
- `CongressBillInfoFetcher`
- `CongressBillTextFetcher`
- `CongressBillsFetcher`
- `Provider`
- `openbb_congress_gov.models.bill_info`
- `openbb_congress_gov.models.bill_text`
- `openbb_congress_gov.models.congress_bills`
- `openbb_core.provider.abstract.provider`


---

## Performance & Security Notes

No obvious security concerns detected in static analysis.


---

**Generated**: 2025-11-19T02:16:48.685732Z
**Generator**: World's Best Repo Book Generator v1.0

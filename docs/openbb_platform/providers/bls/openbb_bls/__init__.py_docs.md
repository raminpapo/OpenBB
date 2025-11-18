# Documentation: openbb_platform/providers/bls/openbb_bls/__init__.py

## File Metadata
- **Path**: `openbb_platform/providers/bls/openbb_bls/__init__.py`
- **Size**: 967 characters, 22 lines
- **Words**: 100
- **Extension**: .py
- **Classification**: Text file

## Original Source

```python
"""BLS Provider Module."""

from openbb_bls.models.search import BlsSearchFetcher
from openbb_bls.models.series import BlsSeriesFetcher
from openbb_core.provider.abstract.provider import Provider

bls_provider = Provider(
    name="bls",
    website="https://www.bls.gov/developers/api_signature_v2.htm",
    description="The Bureau of Labor Statistics' (BLS) Public Data Application Programming Interface (API)"
    + " gives the public access to economic data from all BLS programs."
    + " It is the Bureau's hope that talented developers and programmers will use the BLS Public Data API to create"
    + " original, inventive applications with published BLS data.",
    credentials=["api_key"],
    fetcher_dict={
        "BlsSearch": BlsSearchFetcher,
        "BlsSeries": BlsSeriesFetcher,
    },
    repr_name="Bureau of Labor Statistics' (BLS) Public Data API",
    instructions="Sign up for a free API key here: https://data.bls.gov/registrationEngine/",
)

```

## High-Level Overview

BLS Provider Module.

from openbb_bls.models.search import BlsSearchFetcher
from openbb_bls.models.series import BlsSeriesFetcher
from openbb_core.provider.abstract.provider import Provider

bls_provider = Provider(
name="bls",
website="https://www.bls.gov/developers/api_signature_v2.htm",
description="The Bureau of Labor Statistics' (BLS) Public Data Application Programming Interface (API)"
+ " gives the public access to economic data from all BLS programs."
+ " It is the Bureau's hope that talented developers and programmers will use the BLS Public Data API to create"
+ " original, inventive applications with published BLS data.",
credentials=["api_key"],
fetcher_dict={
"BlsSearch": BlsSearchFetcher,
"BlsSeries": BlsSeriesFetcher,
},
repr_name="Bureau of Labor Statistics' (BLS) Public Data API",
instructions="Sign up for a free API key here: https://data.bls.gov/registrationEngine/",

## Detailed Structure

### Python File Structure

**Classes** (0):
None

**Functions** (0):
None

**Imports** (7):
`openbb_bls.models.search`, `BlsSearchFetcher`, `openbb_bls.models.series`, `BlsSeriesFetcher`, `openbb_core.provider.abstract.provider`, `Provider`, `all`


## Key Components

No major components extracted.

## Usage & Examples

See source code for usage details.

## Related Files

- `openbb_bls.models.search`
- `openbb_bls.models.series`
- `openbb_core.provider.abstract.provider`

## Notes
- Generated: 2025-11-18T07:54:37.337316
- Generator: World's Best Repo Book Generator v1.0.0

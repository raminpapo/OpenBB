# File Documentation: __init__.py

## Metadata
- **Path**: `openbb_platform/providers/bls/openbb_bls/__init__.py`
- **Size**: 967 bytes
- **Lines**: 22
- **Category**: python
- **Extension**: .py

---

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
- `BlsSearchFetcher`
- `BlsSeriesFetcher`
- `Provider`
- `openbb_bls.models.search`
- `openbb_bls.models.series`
- `openbb_core.provider.abstract.provider`


---

## Performance & Security Notes

No obvious security concerns detected in static analysis.


---

**Generated**: 2025-11-19T02:16:48.351513Z
**Generator**: World's Best Repo Book Generator v1.0

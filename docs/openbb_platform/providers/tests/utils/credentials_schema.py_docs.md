# File Documentation: credentials_schema.py

## Metadata
- **Path**: `openbb_platform/providers/tests/utils/credentials_schema.py`
- **Size**: 450 bytes
- **Lines**: 13
- **Category**: python
- **Extension**: .py

---

## Original Source

```python
"""Provider credentials schema used for unit test."""

test_credentials: dict[str, tuple[str, str]] = {
    "benzinga": ("token", "MOCK_TOKEN"),
    "alpha_vantage": ("apikey", "MOCK_API_KEY"),
    "fmp": ("apikey", "MOCK_API_KEY"),
    "polygon": ("apiKey", "MOCK_API_KEY"),
    "nasdaq": ("x-api-token", "MOCK_API_KEY"),
    "fred": ("api_key", "MOCK_API_KEY"),
    "intrinio": ("api_key", "MOCK_API_KEY"),
    "tiingo": ("token", "MOCK_TOKEN"),
}

```



---

## High-Level Overview

This is a **python** file named `credentials_schema.py`.

**Python Module**



---

## Detailed Analysis

### Python Code Structure



---

## Related Files

The following files may be related based on imports and references:

*No direct imports detected.*


---

## Performance & Security Notes

No obvious security concerns detected in static analysis.


---

**Generated**: 2025-11-19T02:16:52.985989Z
**Generator**: World's Best Repo Book Generator v1.0

# Documentation: openbb_platform/providers/tests/utils/credentials_schema.py

## File Metadata
- **Path**: `openbb_platform/providers/tests/utils/credentials_schema.py`
- **Size**: 450 characters, 13 lines
- **Words**: 38
- **Extension**: .py
- **Classification**: Text file

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

## High-Level Overview

Provider credentials schema used for unit test.

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


## Detailed Structure

### Python File Structure

**Classes** (0):
None

**Functions** (0):
None

**Imports** (0):
None


## Key Components

No major components extracted.

## Usage & Examples

See source code for usage details.

## Related Files

No direct file references found.

## Notes
- Generated: 2025-11-18T07:54:41.704807
- Generator: World's Best Repo Book Generator v1.0.0

# Documentation: openbb_platform/providers/intrinio/tests/record/http/test_intrinio_fetchers/test_intrinio_price_target_consensus_fetcher_urllib3_v2.yaml

## File Metadata
- **Path**: `openbb_platform/providers/intrinio/tests/record/http/test_intrinio_fetchers/test_intrinio_price_target_consensus_fetcher_urllib3_v2.yaml`
- **Size**: 1,143 characters, 39 lines
- **Words**: 62
- **Extension**: .yaml
- **Classification**: Text file

## Original Source

```yaml
interactions:
- request:
    body: null
    headers:
      Accept:
      - application/json
      Accept-Encoding:
      - gzip, deflate
      Connection:
      - keep-alive
    method: GET
    uri: https://api-v2.intrinio.com/zacks/target_price_consensuses?api_key=MOCK_API_KEY&identifier=AAPL&page_size=10000
  response:
    body:
      string: !!binary |
        H4sIAHo7fWYAA1yQX0vDMBTFv8q4z11J/1ht3qboHM6tiMOBSIjppQtrk5Kk6hz77ks2RTBPueeX
        nHvu3YPjpkHHeiMFMqGVRWUHixbo6x6cFFs0QGEyqeYQgdBdz9WOKd5hUKtqfjuaLW48kqoerDM7
        1hg99EwN3fvpZ1KWnm5kswGaXl7EJIJWfwJNijzcO+TKgySJ8zyJwDquam5qVuOH5E7qAIs4J0UE
        TjveAs38s05bxwwKVI7V3IUsKUnzMSnGaQ7BtZZnXxKaGC4t1kDV0Lan9mj+yp+ZgO5BejHUbLEu
        pt9Lb/R/Ab+D932Lo5kSsddalF66f1lVD0/ksVquru6m6+vnrAxJhNx6SPzJUpKUGRwOb94Gv/zK
        eYPnEIcjAAAA//8DANXI/92HAQAA
    headers:
      Connection:
      - keep-alive
      Content-Encoding:
      - gzip
      Content-Type:
      - application/json
      Date:
      - Thu, 27 Jun 2024 10:14:18 GMT
      Transfer-Encoding:
      - chunked
      Vary:
      - Origin,Accept-Encoding
    status:
      code: 200
      message: OK
version: 1

```

## High-Level Overview

This is a .yaml file containing 39 lines of code.

## Detailed Structure

Standard text file.

## Key Components

No major components extracted.

## Usage & Examples

See source code for usage details.

## Related Files

No direct file references found.

## Notes
- Generated: 2025-11-18T07:54:40.272828
- Generator: World's Best Repo Book Generator v1.0.0

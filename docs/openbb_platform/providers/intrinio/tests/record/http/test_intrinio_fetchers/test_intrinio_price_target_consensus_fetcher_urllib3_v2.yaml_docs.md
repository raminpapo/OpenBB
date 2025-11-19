# File Documentation: test_intrinio_price_target_consensus_fetcher_urllib3_v2.yaml

## Metadata
- **Path**: `openbb_platform/providers/intrinio/tests/record/http/test_intrinio_fetchers/test_intrinio_price_target_consensus_fetcher_urllib3_v2.yaml`
- **Size**: 1,143 bytes
- **Lines**: 39
- **Category**: config
- **Extension**: .yaml

---

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



---

## High-Level Overview

This is a **config** file named `test_intrinio_price_target_consensus_fetcher_urllib3_v2.yaml`.

**Configuration File**

This file contains configuration settings for the project.


---

## Detailed Analysis

### Configuration Structure

This configuration file defines settings and parameters for the project.


---

## Related Files

The following files may be related based on imports and references:

*No direct imports detected.*


---

## Performance & Security Notes

No obvious security concerns detected in static analysis.


---

**Generated**: 2025-11-19T02:16:51.580063Z
**Generator**: World's Best Repo Book Generator v1.0

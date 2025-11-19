# File Documentation: test_fmp_historical_employees_fetcher_urllib3_v2.yaml

## Metadata
- **Path**: `openbb_platform/providers/fmp/tests/record/http/test_fmp_fetchers/test_fmp_historical_employees_fetcher_urllib3_v2.yaml`
- **Size**: 1,622 bytes
- **Lines**: 57
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
    uri: https://financialmodelingprep.com/stable/historical-employee-count?apikey=MOCK_API_KEY&limit=1&symbol=AAPL
  response:
    body:
      string: !!binary |
        H4sIAAAAAAAAA12Qy07DMBBF9/0KK2scP1JFNLuIbhAIEOoOsTDONLEaP+S4DRHi34kTEipG8ubc
        O3M987ZB6Gt8CCXdoD9smxQoKcuXx+RmplKdIqJjZZyyXbYIQkpwQRgJB6UhejjlW8wYpgzRvKCs
        yPLF7MArWz0fX8FZH1Yz3WF+uyZZ7YQZnsQ8rXSuBXRvZLoYjtbrw+AmlVH8sHLVKlPvRfj3i0UH
        7Vo7ANzZs4nZLN+O2/yKnT17OTU2IbiuIKTv+7QDmdb2QkovG3WBjkBVC08qEQSZz0D+LsLjOMav
        EY7LTRArU8Fn2gSdjIHfm/cfuku9qHIBAAA=
    headers:
      Access-Control-Allow-Credentials:
      - 'true'
      Access-Control-Allow-Headers:
      - X-Requested-With, content-type, auth-token, Authorization, stripe-signature,
        APPS, publicauthkey, privateauthkey
      Access-Control-Allow-Methods:
      - GET, POST, OPTIONS
      Access-Control-Allow-Origin:
      - '*'
      Access-Control-Max-Age:
      - '3600'
      Connection:
      - keep-alive
      Content-Encoding:
      - gzip
      Content-Type:
      - application/json; charset=utf-8
      Date:
      - Tue, 23 Sep 2025 03:08:35 GMT
      Etag:
      - W/"172-gd7iRRwhH24qRvKXp0NtrKTg+Oo"
      Server:
      - nginx/1.18.0 (Ubuntu)
      Transfer-Encoding:
      - chunked
      Vary:
      - Accept-Encoding
      X-Frame-Options:
      - SAMEORIGIN
      X-Powered-By:
      - Express
    status:
      code: 200
      message: OK
version: 1

```



---

## High-Level Overview

This is a **config** file named `test_fmp_historical_employees_fetcher_urllib3_v2.yaml`.

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

**Generated**: 2025-11-19T02:16:50.887693Z
**Generator**: World's Best Repo Book Generator v1.0

# File Documentation: test_fmp_etf_equity_exposure_fetcher_urllib3_v2.yaml

## Metadata
- **Path**: `openbb_platform/providers/fmp/tests/record/http/test_fmp_fetchers/test_fmp_etf_equity_exposure_fetcher_urllib3_v2.yaml`
- **Size**: 1,302 bytes
- **Lines**: 49
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
    uri: https://financialmodelingprep.com/stable/etf/asset-exposure?apikey=MOCK_API_KEY&symbol=CNST
  response:
    body:
      string: "[\n  {\n    \"symbol\": \"PQSG\",\n    \"asset\": \"CNST\",\n    \"sharesNumber\":
        720,\n    \"weightPercentage\": 0.16,\n    \"marketValue\": 20656.33\n  }\n]"
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
      Content-Length:
      - '137'
      Content-Type:
      - application/json; charset=utf-8
      Date:
      - Tue, 23 Sep 2025 03:08:48 GMT
      Etag:
      - W/"89-i2xjiWdGr1iM6E7Wx99Rw/ogJQo"
      Server:
      - nginx/1.18.0 (Ubuntu)
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

This is a **config** file named `test_fmp_etf_equity_exposure_fetcher_urllib3_v2.yaml`.

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

**Generated**: 2025-11-19T02:16:50.865593Z
**Generator**: World's Best Repo Book Generator v1.0

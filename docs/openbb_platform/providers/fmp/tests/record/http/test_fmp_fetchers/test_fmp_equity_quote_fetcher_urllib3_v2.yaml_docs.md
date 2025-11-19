# File Documentation: test_fmp_equity_quote_fetcher_urllib3_v2.yaml

## Metadata
- **Path**: `openbb_platform/providers/fmp/tests/record/http/test_fmp_fetchers/test_fmp_equity_quote_fetcher_urllib3_v2.yaml`
- **Size**: 1,610 bytes
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
    uri: https://financialmodelingprep.com/stable/quote?apikey=MOCK_API_KEY&symbol=AAPL
  response:
    body:
      string: !!binary |
        H4sIAAAAAAAAA12Qu07DMBSG9z6FlbmyfIljh80qQ5EqVMSIGEw4SiPiOErSQIR4d+LELqWDl+87
        /s/lZYPQ9/wQSvrJvrk6uUOJ1sdDsl1pYywsrG1rQA9NgaNpu6rwiokMExVgcTJNCUfoCmgGU3qf
        Yk5yIf8VzJgSLOKv0dVnu0KqMkHzPIh3Mx3cp2+SKkzZH91X5Sn0znjAE5gu8oxgeoXXEJrlmEVs
        TfcBw860s+CKEM4kkZQRcr2eHktBfB5LsWIyvXFz9SIpllzkIlj4uiyZPOrne/0UT+ZaaMIy/BIF
        Y+XO/a52/XLNVOAYNFQW+sFYPyKVQgk/H53dz+b1Fw2v2Pu5AQAA
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
      - Tue, 23 Sep 2025 03:08:38 GMT
      Etag:
      - W/"1b9-Y0olwV4IWG5k9+ZadKCVZLhK6Pc"
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

This is a **config** file named `test_fmp_equity_quote_fetcher_urllib3_v2.yaml`.

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

**Generated**: 2025-11-19T02:16:50.859241Z
**Generator**: World's Best Repo Book Generator v1.0

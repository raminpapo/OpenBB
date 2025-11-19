# File Documentation: test_fmp_price_performance_fetcher_urllib3_v2.yaml

## Metadata
- **Path**: `openbb_platform/providers/fmp/tests/record/http/test_fmp_fetchers/test_fmp_price_performance_fetcher_urllib3_v2.yaml`
- **Size**: 1,768 bytes
- **Lines**: 59
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
    uri: https://financialmodelingprep.com/stable/stock-price-change?apikey=MOCK_API_KEY&symbol=AAPL%2CSPY%2CBTCUSD
  response:
    body:
      string: !!binary |
        H4sIAAAAAAAAA3WSPU/DMBCG9/6KKHN7uk/bx1boCFKlwlAhBhAjFQMMVIj/zsWJo0aCIcuj15d7
        Xvtx1XXf8XVd/3E+vby/9Vddv93ub/v1SGkXREHQLU/IBpSBzIu31F0gYlBR0onJwDiDInvLpZrL
        IMxWJnb+fA1ogGTSGB2HnABmnXMysJQhWdbUVqk5dkAhmZfBgRYU4ILKEz09fw1Zd6UEHmMt+M/6
        L//D/rjQR9AsRJf6FH/UIpf6AiJpNpCpEUbPLTbaF2Ap3Foa7UkBzX2edxxrQstzsOrnAuSaGhv1
        kaAUp6U+q0BAW9prDE2kLv+6X9/fPBx2C/0NgpfY5NJ/o6CcuXVSCxhYcV3cPyGYFWxnawMiQEmk
        nZ0aKPHGNM0Dq61B4uzNoTagAU0wNVgr8IRx10nn07UCLRy95ninbaXWQqKUhTH+aVFmfQirp1/j
        CHm0CwMAAA==
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
      - Tue, 23 Sep 2025 03:08:44 GMT
      Etag:
      - W/"30b-ITJ/yRUuZHc/0BzZS9ayy5q9zFk"
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

This is a **config** file named `test_fmp_price_performance_fetcher_urllib3_v2.yaml`.

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

**Generated**: 2025-11-19T02:16:50.909419Z
**Generator**: World's Best Repo Book Generator v1.0

# File Documentation: test_fmp_equity_peers_fetcher_urllib3_v2.yaml

## Metadata
- **Path**: `openbb_platform/providers/fmp/tests/record/http/test_fmp_fetchers/test_fmp_equity_peers_fetcher_urllib3_v2.yaml`
- **Size**: 1,588 bytes
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
    uri: https://financialmodelingprep.com/stable/stock-peers?apikey=MOCK_API_KEY&symbol=AAPL
  response:
    body:
      string: !!binary |
        H4sIAAAAAAAAA33RQUvDMBQH8Ps+xaPnEpI0SROvG4zB2IbFDRUPWe2huPaFtBOr+N2NUy+22SGX
        /wv8eP/3OAP4CA8g6YbmiKfkBpLl7nabpD9piY2z7bCxTXUZ4c5jCqu2JH8/nK/L7xknWv9GzUs/
        ty5kQkpDBaU05J/plFVsNzGrwBa7aYtJItV/jGlNtckZu6rdx7UBlh7PDuboHXrb19iOljQkz0Zw
        bjgzQgvOVZTe3z2sIvT+/F6/XVMzko2q5YpRoUTGouJhvSgi4qGy3h5PFSyq10B0sO6fRyWriY7D
        Obk0ly1nT1/kRcP/PQIAAA==
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
      - W/"23d-YEAJEs+QJhYRxkodIT+3w+pF/Kk"
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

This is a **config** file named `test_fmp_equity_peers_fetcher_urllib3_v2.yaml`.

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

**Generated**: 2025-11-19T02:16:50.855817Z
**Generator**: World's Best Repo Book Generator v1.0

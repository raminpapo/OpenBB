# File Documentation: test_fmp_equity_screener_fetcher_urllib3_v2.yaml

## Metadata
- **Path**: `openbb_platform/providers/fmp/tests/record/http/test_fmp_fetchers/test_fmp_equity_screener_fetcher_urllib3_v2.yaml`
- **Size**: 1,806 bytes
- **Lines**: 58
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
    uri: https://financialmodelingprep.com/stable/company-screener?apikey=MOCK_API_KEY&betaLowerThan=0.5&includeAllShareClasses=false&industry=Oil+%26+Gas+Midstream&isActivelyTrading=true&isEtf=false&isFund=false&limit=2&sector=Energy
  response:
    body:
      string: !!binary |
        H4sIAAAAAAAAA9WRPU/DMBiE9/4KKwNTiZq2oRVbKAExkCIlAxJicOy3qVXHjvxRESH+O04aBwGC
        GQYvd4+tO9/TBKFXdxAKdFuXkgeXKEizq/OHJCy2wfRkEVk3WLQZrqH3RakYrQDdCeKRGqsDmA1u
        HDAbNA3ESHW6AapqPcsEtdqotnO2jKMzdIs1umfUiYBrj5VgcPdauIgGpVGMdAnmy3A9SBxrkwhh
        Mb9mR0ZBUOdH4WIVD8BRctvHjmOfC17IHouq71JIJYWRKDeSHFDqnS9kvpfK+PpF/vjxMVYMRTbJ
        WE+nZuekHeYaRu3G9tE+iwkx7Ai8LRSmTFTON8qCc9+mPw6T/Zlhvq8SLX+f5WLlgXGW+Xr2n3aZ
        PL8DZ/rENTMDAAA=
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
      - Tue, 23 Sep 2025 03:08:39 GMT
      Etag:
      - W/"333-qXQUkRxytzxamHIGMrPaI4swz08"
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

This is a **config** file named `test_fmp_equity_screener_fetcher_urllib3_v2.yaml`.

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

**Generated**: 2025-11-19T02:16:50.860705Z
**Generator**: World's Best Repo Book Generator v1.0

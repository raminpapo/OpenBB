# File Documentation: test_fmp_treasury_rates_fetcher_urllib3_v2.yaml

## Metadata
- **Path**: `openbb_platform/providers/fmp/tests/record/http/test_fmp_fetchers/test_fmp_treasury_rates_fetcher_urllib3_v2.yaml`
- **Size**: 1,767 bytes
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
    uri: https://financialmodelingprep.com/stable/treasury-rates?apikey=MOCK_API_KEY&from=2023-01-01&to=2023-01-10
  response:
    body:
      string: !!binary |
        H4sIAAAAAAAAA42Uy2rDMBBF9/kK4XVi9BzJ/ZXSRaCBbtpCyaaU/ntdzRjuoDHOIptj+WZ0fKXn
        k3M/68+56fV6v01Pboo+posPl+CnMz95//y4v4X1WZ5zQBY7o4gsdVYTMuqsFWHft+sXx9UMiNMi
        ov+wNC+ISkc1AqodUcV4zyxgPrMFWWJW84p+z/sy/GLISBUZj1+aIcNwkWAITqNlcBEQiQt8kV0Q
        jS5GFQVfFBVqClFBdKSCLBWqA6KiIGMVZLiouEvphfpuu73AbYoLzBIXSrXIwCpuMtQfiIx6JKNY
        Mh50QcikF7hxcdFw1o4yjs9hAVexi1FFw1MjKrRqP4rdjkg7UpENFUYtsnFdaD1SC3We92qR1Kis
        AlexCnX1sAvdOj+2Z3OBY4iLFo5cJMNFMK4LU4Zxd1oy8GNK2kO1wFXSC8NFHVzk2Ru9aL0Xp5c/
        5fFi40oGAAA=
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
      - Tue, 23 Sep 2025 03:08:33 GMT
      Etag:
      - W/"64a-ZC8CGBkjfc40G90jP0L5IvaaFL8"
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

This is a **config** file named `test_fmp_treasury_rates_fetcher_urllib3_v2.yaml`.

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

**Generated**: 2025-11-19T02:16:50.921324Z
**Generator**: World's Best Repo Book Generator v1.0

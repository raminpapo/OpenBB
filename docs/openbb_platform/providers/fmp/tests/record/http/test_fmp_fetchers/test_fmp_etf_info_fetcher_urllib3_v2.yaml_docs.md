# File Documentation: test_fmp_etf_info_fetcher_urllib3_v2.yaml

## Metadata
- **Path**: `openbb_platform/providers/fmp/tests/record/http/test_fmp_fetchers/test_fmp_etf_info_fetcher_urllib3_v2.yaml`
- **Size**: 2,159 bytes
- **Lines**: 64
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
    uri: https://financialmodelingprep.com/stable/etf/info?apikey=MOCK_API_KEY&symbol=IOO
  response:
    body:
      string: !!binary |
        H4sIAAAAAAAAA5VUTVPbMBC98ys0OWP5I/4gubUhtMyUYYaEHspwEPIm0aBIrlZOSDv975XsOHDA
        1D1krOw+vd19b+2HM0J+ux8hIzxsn7QcTcno+vZ2dN4GFduCD4nFhhlA8kXqJyZJHEVkvrzqUCUg
        N6KyQisPXm6AvH+BIMAzEquJNYw/E+uRagdot6AscRdqaZHoFWHKJUp4IVxvK41Q+qBnkcysIeCs
        EpZJ8Yv5omTdVoGftbACkHaNCRRNR/eLNE+TiyIrkqTLMUSwM+keHjH3Vw9dDoHXxv2f1Sgqnz5d
        P42st4ILCS17F93DEwrbBDfWVjgNw/1+TwU2YlA3S8g3YWX0ChBd40xiCMoHyppbDJPxpBgX4REf
        tGMFbuwA7Kor4o4zJwpTh8asVuhT8qUChXDndXHpiKZvx8V7p6m5YYqtwSvuEEWST8ZZPMnzDrhb
        f9eybnx3/UR50YmpODQeX7J2xCRyjcVJEGWv67JziTie0Kh4Dc1qY0DxQ6vVZQfeaFkKtcaZrptO
        4ig5ZuqqdCXKT7atkmRBNAmSZBln0yibxhmN8uTHG6+sNvhNoIc/NMFuqY99lzVa05T/zFBwcuPY
        jXDiHzk65TTWxk8W0zw/Jv6cf0zonNjWSvB2DxdgdoJDH+8FzdLBvAqdB4bMDlw6etlDOaHxf1Ne
        wsrtiNhBD2dO88lAzrkCsz708IxpUQzkuRKKKe4s+ZeEcUSzod58BSbthrvXo9ePNBvIdd2eP1ia
        lBZDnbhzjZE5Wv8evU8W0WSoBUvgG6Wl7rUhzWgxHkh2b4VsPqG9faWnIZvn45k/Pf4FVlx6+0gG
        AAA=
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
      - Tue, 23 Sep 2025 03:08:42 GMT
      Etag:
      - W/"648-WeMcFFuxsFW70AT4IZ8DRchPbqc"
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

This is a **config** file named `test_fmp_etf_info_fetcher_urllib3_v2.yaml`.

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

**Generated**: 2025-11-19T02:16:50.868969Z
**Generator**: World's Best Repo Book Generator v1.0

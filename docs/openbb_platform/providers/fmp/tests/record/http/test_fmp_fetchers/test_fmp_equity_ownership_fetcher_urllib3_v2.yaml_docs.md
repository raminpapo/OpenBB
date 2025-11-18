# Documentation: openbb_platform/providers/fmp/tests/record/http/test_fmp_fetchers/test_fmp_equity_ownership_fetcher_urllib3_v2.yaml

## File Metadata
- **Path**: `openbb_platform/providers/fmp/tests/record/http/test_fmp_fetchers/test_fmp_equity_ownership_fetcher_urllib3_v2.yaml`
- **Size**: 2,174 characters, 63 lines
- **Words**: 105
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
    uri: https://financialmodelingprep.com/stable/institutional-ownership/extract-analytics/holder?apikey=MOCK_API_KEY&limit=1&page=0&quarter=2&symbol=AAPL&year=2025
  response:
    body:
      string: !!binary |
        H4sIAAAAAAAAA32UXW+bMBSG7/srUK4H8ge28e4iknaVWoKStLuYduEGJ7FKILNNq2jaf68hdQp0
        GxISOu/j4/ccH/PjKgh+uzcIJoWwcvI1mCCASAhoiMHky1nZqOdWAO6BAHHAvbBVpap2s8HCJITQ
        66p6kcbWOhOHjnicZjcP0+UsuFkuHvLgNks9aU6Hp7psmek0v7tE5abRyp78+mme3837y+zpKBfb
        1TvWIunifrw6bYw6dgVglmAMwaUwsxdamrVL0sqrbz5+bGwqynLVyp3SfQyKOsjKzpTZaGlVXbXQ
        7DqbfTBFY6w+rZUtuwzzu3m6Xi6y2zRwDvOH9Xy58vCrVLu9dVQcMYDQe7QUxn73CokoItQfx15U
        O3lbXdQQRBzh+K9yLvXGWRW71kYIaRTDGL+TB6GfpX0UZdOK7mAJoBxjzFjPw/0AwhBCwihFmMDR
        fkMwRIASwFDC2dhYDxy6oxHF1O99PpusOTxJ7UQYQ8IxSkDc87YaMwAwDhLARzuOOeKycU7+Qw2M
        wQgkvtpfjdBW6nlV5Fptur4BEkHvWrzsunguVNG2i0XUm1Emk68uthWlkZfYqi6LRWNH8fq1ktrs
        u7HlEQEQ9qpeDEQcIzwqpA+ACJIk+RcwKpN+NGXvfLm77QBVt5Ukfi63Shs7LQpZnO88cHceh/hy
        549Sb2t9ENXmPAaYERZDBBH4DAyP3/UKk/7458NUmMcJZQzBT6M+BN2AIo6p+1n5xiiT1k1lZXFd
        6yFrdSMd8+fq5xteoxBVCgUAAA==
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
      - Tue, 23 Sep 2025 03:08:25 GMT
      Etag:
      - W/"50a-H+27fii31AZpmffqSs5XAK/JwTk"
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

## High-Level Overview

This is a .yaml file containing 63 lines of code.

## Detailed Structure

Standard text file.

## Key Components

No major components extracted.

## Usage & Examples

See source code for usage details.

## Related Files

No direct file references found.

## Notes
- Generated: 2025-11-18T07:54:39.570066
- Generator: World's Best Repo Book Generator v1.0.0

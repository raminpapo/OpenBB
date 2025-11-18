# Documentation: openbb_platform/providers/fmp/tests/record/http/test_fmp_fetchers/test_fmp_etf_sectors_fetcher_urllib3_v2.yaml

## File Metadata
- **Path**: `openbb_platform/providers/fmp/tests/record/http/test_fmp_fetchers/test_fmp_etf_sectors_fetcher_urllib3_v2.yaml`
- **Size**: 1,621 characters, 57 lines
- **Words**: 99
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
    uri: https://financialmodelingprep.com/stable/etf/sector-weightings?apikey=MOCK_API_KEY&symbol=IOO
  response:
    body:
      string: !!binary |
        H4sIAAAAAAAAA52STU/DMAyG7/sVUc+T1bK03TgyhtgBDfFxQjuEzGstpY6UpEMV4r8TEFzDwiEX
        x3psvY9fZkK8xydE4afh1ZriUhTb3a6Y/xRRB+u+ilfKkxZ3KqAjZfxvwxtS14d7dBo5qA5jawVN
        Ez8/5mez13YYRiatAlkWj+hOpDE1Ygm1zB3BfhzQifWkTZxkEvQVVP+lX+MR2dMJE/gGmlUefsPo
        uimBXEDb5iFviBXraPKcuKsS6kylt6hM6LVyqSSWIOs87JYPow9/XaCENlPgQ1xXbHyI553glnCR
        ae4Jdc/W2KQ9WUO7yOM+BzIUKGmtBPmdwmz/CYYUDGTmAwAA
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
      - Tue, 23 Sep 2025 03:08:43 GMT
      Etag:
      - W/"3e6-mX9CPZ79gCzyKisUhJmCIafXKs4"
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

This is a .yaml file containing 57 lines of code.

## Detailed Structure

Standard text file.

## Key Components

No major components extracted.

## Usage & Examples

See source code for usage details.

## Related Files

No direct file references found.

## Notes
- Generated: 2025-11-18T07:54:39.592364
- Generator: World's Best Repo Book Generator v1.0.0

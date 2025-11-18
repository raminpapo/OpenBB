# Documentation: openbb_platform/providers/fmp/tests/record/http/test_fmp_fetchers/test_fmp_historical_market_cap_fetcher_urllib3_v2.yaml

## File Metadata
- **Path**: `openbb_platform/providers/fmp/tests/record/http/test_fmp_fetchers/test_fmp_historical_market_cap_fetcher_urllib3_v2.yaml`
- **Size**: 1,751 characters, 58 lines
- **Words**: 100
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
    uri: https://financialmodelingprep.com/stable/historical-market-capitalization?apikey=MOCK_API_KEY&from=2024-01-01&limit=5000&symbol=AAPL&to=2024-01-31
  response:
    body:
      string: !!binary |
        H4sIAAAAAAAAA52Vu0oEQRBF8/2KYeJdqPfDbDE1MBeDETfSRdFNRPx3e1CzmsAKOumCQ1F1+vbd
        bpo+x5mm+f3j/PDyPF9N8/F4ezPvf24fl8tpvSMgOQAeGP8q5+Xt6XS5Xl5HmUIgOENMAEb5a/9v
        LtTctERHI5Iel7LkprKbuENEk2s114RTAlGpydWam8iqoNnmygZ3NByZBM29EVdcBhh7k/ShRZNL
        db/hICg4VOtxccsHRFF3ZWtyo+aCjVEYOjXngF6/CxQW9P58sfY3xotzZ+73W+8tTEjNxbv+4kbu
        aK6zRYWuDxu5YyFovPbd40LtWeiaZOhtf6H2LDQcwTi7/kKdO55IPFICup5BnTsxyp5kkt1+y9yh
        4DHh8WlEN89gw1/NFEbw373t7r8BXevZVToHAAA=
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
      - Tue, 23 Sep 2025 03:08:50 GMT
      Etag:
      - W/"73a-MDe9BxWD2CL5roRSOp6aLuALx48"
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

This is a .yaml file containing 58 lines of code.

## Detailed Structure

Standard text file.

## Key Components

No major components extracted.

## Usage & Examples

See source code for usage details.

## Related Files

No direct file references found.

## Notes
- Generated: 2025-11-18T07:54:39.605079
- Generator: World's Best Repo Book Generator v1.0.0

# Documentation: openbb_platform/providers/tmx/tests/record/http/test_tmx_fetchers/test_tmx_price_target_consensus_fetcher_urllib3_v2.yaml

## File Metadata
- **Path**: `openbb_platform/providers/tmx/tests/record/http/test_tmx_fetchers/test_tmx_price_target_consensus_fetcher_urllib3_v2.yaml`
- **Size**: 1,900 characters, 58 lines
- **Words**: 130
- **Extension**: .yaml
- **Classification**: Text file

## Original Source

```yaml
interactions:
- request:
    body: '{"operationName": "getCompanyAnalysts", "variables": {"symbol": "SHOP",
      "datatype": "equity"}, "query": "query getCompanyAnalysts(\n  $symbol: String!\n  $dataType:
      String,\n) {\n  analysts: getCompanyAnalysts(\n    datatype: $dataType,\n    symbol:
      $symbol\n  ) {\n    totalAnalysts\n    priceTarget\n      {\n        highPriceTarget\n        lowPriceTarget\n        priceTarget\n        priceTargetUpside\n    }\n    consensusAnalysts\n      {\n      consensus\n      buy\n      sell\n      hold\n    }\n  }\n}"}'
    headers:
      Accept:
      - '*/*'
      Content-Type:
      - application/json
      authority:
      - app-money.tmx.com
      locale:
      - en
      referer:
      - https://money.tmx.com/en/quote/SHOP
    method: POST
    uri: https://app-money.tmx.com/graphql
  response:
    body:
      string: '{"data":{"analysts":{"totalAnalysts":31,"priceTarget":{"highPriceTarget":131.5272,"lowPriceTarget":86.314725,"priceTarget":104.947745,"priceTargetUpside":18.63},"consensusAnalysts":{"consensus":"Buy","buy":17,"sell":0,"hold":14}}}}

        '
    headers:
      Access-Control-Allow-Origin:
      - '*'
      Connection:
      - keep-alive
      Content-Length:
      - '232'
      Content-Security-Policy:
      - frame-ancestors 'none'; default-src 'self'
      Content-Type:
      - application/json; charset=utf-8
      Date:
      - Thu, 27 Jun 2024 10:16:01 GMT
      Etag:
      - W/"e8-x7zZy8+wO8c5e0cKfkZlBO8BLBw"
      Strict-Transport-Security:
      - max-age=15552000; includeSubDomains
      Vary:
      - Origin, Accept-Encoding
      X-Content-Type-Options:
      - nosniff
      X-DNS-Prefetch-Control:
      - 'off'
      X-Download-Options:
      - noopen
      X-Frame-Options:
      - SAMEORIGIN
      X-XSS-Protection:
      - 1; mode=block
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
- Generated: 2025-11-18T07:54:43.139590
- Generator: World's Best Repo Book Generator v1.0.0

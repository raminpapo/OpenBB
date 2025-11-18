# Documentation: openbb_platform/providers/federal_reserve/tests/record/http/test_federal_reserve_fetchers/test_federal_reserve_overnight_bank_funding_rate_fetcher_urllib3_v2.yaml

## File Metadata
- **Path**: `openbb_platform/providers/federal_reserve/tests/record/http/test_federal_reserve_fetchers/test_federal_reserve_overnight_bank_funding_rate_fetcher_urllib3_v2.yaml`
- **Size**: 1,732 characters, 61 lines
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
    uri: https://markets.newyorkfed.org/api/rates/unsecured/obfr/search.json?startDate=2024-06-01&endDate=2024-06-06
  response:
    body:
      string: !!binary |
        H4sIAAAAAAAEA6pWUCpKTQtKLEktVrJSiFaoVlBKTUtLTS7JLEt1SSxJVbJSUDIyMDLRNTDTNTBT
        0lFQKqksAIv6O7kFKSnoKBWkFiWn5pWAjFCyUjDVMzZCCAZA5DJzUg3Bckam2OSMTMGSxobYJM2h
        ksbYJC0tITotFXSUyvJzSnNTPfOcMnNyMvPzQN4xsgDZV5RallmcmZ/nmZeSmZxYkl8E8pOSQq0O
        fs+aDlbPWuDwrDlIgkzPmgw1z1oYKOgokelZ46HmWXN8yRgwhViFWgD5Rz99xgMAAA==
    headers:
      Access-Control-Allow-Headers:
      - Content-Type,Content-Disposition
      Access-Control-Allow-Methods:
      - OPTIONS,GET
      Access-Control-Allow-Origin:
      - '*'
      Access-Control-Expose-Headers:
      - Content-Disposition
      Cache-Control:
      - no-store
      Connection:
      - keep-alive
      Content-Encoding:
      - gzip
      Content-Length:
      - '220'
      Content-Type:
      - application/json; charset=utf-8
      Date:
      - Thu, 27 Jun 2024 10:22:37 GMT
      Pragma:
      - no-cache
      Vary:
      - Accept-Encoding
      strict-transport-security:
      - max-age=31536000; includeSubDomains
      x-amz-apigw-id:
      - aBaJFF_RiYcFrCQ=
      x-amzn-requestid:
      - 1ca86d24-755a-4112-a2d6-7755eacd57ec
      x-amzn-trace-id:
      - Root=1-667d3d6d-bbbfce79698eea6b630f7dbe;Parent=316f2a5810eaac9b;Sampled=0;lineage=e7c0e2ee:0
      x-frame-options:
      - SAMEORIGIN
      x-xss-protection:
      - 1; mode=block
    status:
      code: 200
      message: OK
version: 1

```

## High-Level Overview

This is a .yaml file containing 61 lines of code.

## Detailed Structure

Standard text file.

## Key Components

No major components extracted.

## Usage & Examples

See source code for usage details.

## Related Files

No direct file references found.

## Notes
- Generated: 2025-11-18T07:54:38.549994
- Generator: World's Best Repo Book Generator v1.0.0

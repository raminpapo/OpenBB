# Documentation: openbb_platform/providers/intrinio/tests/record/http/test_intrinio_fetchers/test_intrinio_forward_pe_fetcher_urllib3_v2.yaml

## File Metadata
- **Path**: `openbb_platform/providers/intrinio/tests/record/http/test_intrinio_fetchers/test_intrinio_forward_pe_fetcher_urllib3_v2.yaml`
- **Size**: 1,803 characters, 71 lines
- **Words**: 117
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
    uri: https://api-v2.intrinio.com/zacks/forward_pe/AAPL?api_key=MOCK_API_KEY
  response:
    body:
      string: !!binary |
        H4sIAHs7fWYAA2TOvQqDMBSG4VspZ9agJybUbFI6FKTkDg5B0yL1J8RIkdJ7bxw6ZfmG91m+D4Sh
        e1kPCppGt5BBt0zOzDvNZrJH1bq9nm73S6TN9SbYno6NhAVWeSFzlNEei38b35OztFvjS1AcGT8n
        gKCwZgVPgEcQrJQJVKDmbRyTLtL+JG/CsPwfIBN1BmN8uwYKYSLrVlCSVfz7AwAA//8DAJhm1Wb4
        AAAA
    headers:
      Connection:
      - keep-alive
      Content-Encoding:
      - gzip
      Content-Type:
      - application/json
      Date:
      - Thu, 27 Jun 2024 10:14:19 GMT
      Transfer-Encoding:
      - chunked
      Vary:
      - Origin,Accept-Encoding
    status:
      code: 200
      message: OK
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
    uri: https://api-v2.intrinio.com/zacks/forward_pe/MSFT?api_key=MOCK_API_KEY
  response:
    body:
      string: !!binary |
        H4sIAHs7fWYAA2TOsQqDMBgE4Fcp/6xB/yS2ZhWEDsWi7iFoKtKqIaYUKX33xqFDyXLDfXDcG9zY
        3bUFAZembCGCbpmMmjc5q0nv7bmoq6Yq20NR1VfvT9Mrp3u5p3dMkMVJFmPm7bbYl7K9NFpuWtkU
        BD0RhgGgB0Zo0FMQmBN6DIB5YASzALiHhPC/qUFa5cbldwEJzSN4+Lurk85NUpsVRJoSzj9fAAAA
        //8DANw+WDX/AAAA
    headers:
      Connection:
      - keep-alive
      Content-Encoding:
      - gzip
      Content-Type:
      - application/json
      Date:
      - Thu, 27 Jun 2024 10:14:19 GMT
      Transfer-Encoding:
      - chunked
      Vary:
      - Origin,Accept-Encoding
    status:
      code: 200
      message: OK
version: 1

```

## High-Level Overview

This is a .yaml file containing 71 lines of code.

## Detailed Structure

Standard text file.

## Key Components

No major components extracted.

## Usage & Examples

See source code for usage details.

## Related Files

No direct file references found.

## Notes
- Generated: 2025-11-18T07:54:40.222751
- Generator: World's Best Repo Book Generator v1.0.0

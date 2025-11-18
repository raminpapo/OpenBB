# Documentation: openbb_platform/providers/intrinio/tests/record/http/test_intrinio_fetchers/test_intrinio_fred_series_fetcher_urllib3_v2.yaml

## File Metadata
- **Path**: `openbb_platform/providers/intrinio/tests/record/http/test_intrinio_fetchers/test_intrinio_fred_series_fetcher_urllib3_v2.yaml`
- **Size**: 1,252 characters, 40 lines
- **Words**: 63
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
    uri: https://api-v2.intrinio.com/indices/economic/$GDP/historical_data/level?api_key=MOCK_API_KEY&end_date=2023-09-20&page_size=100000&start_date=2022-09-20
  response:
    body:
      string: !!binary |
        H4sIAGc7fWYAA2SRy27CMBREfyWyuiSR7TxIsqNCYodQ201bVZFJDHXl2OAHIkL5995AQZDufMfH
        o7njE/oW1mkjaiarhjmGys8TggNHJaKYxiGehpigCTow6UGk04zgiNC8n4y4ZMThLI4wof848shl
        OYmjDJNHjoYEj7gE51GC0zE3zpcWRRJlcdF/TZBQDT+i8oREAzhM1XL7TpZbwG3XrrUE9WkxX8Gs
        WDtYLoy2Npjrllsn6mBldONrB/e1Vk4orhwqlZdyELxypruOfjeEqjaG7z1XNeho75lx3MgOnktm
        XXVhmnNykoaEhpS+kbhMSUnyCGP8AaReW24OzAmtKuvAAXBSJNNbcfcAVze3aw+WM6sV/CZrfrx1
        7Tkyev1TZRfMzjpvgplSnsngZSgTFlDCWSCfhZRgbQO9gR6kZMaiHvrhR1ft2JZfFu5/AQAA//8D
        AF1gUZ85AgAA
    headers:
      Connection:
      - keep-alive
      Content-Encoding:
      - gzip
      Content-Type:
      - application/json
      Date:
      - Thu, 27 Jun 2024 10:13:59 GMT
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

This is a .yaml file containing 40 lines of code.

## Detailed Structure

Standard text file.

## Key Components

No major components extracted.

## Usage & Examples

See source code for usage details.

## Related Files

No direct file references found.

## Notes
- Generated: 2025-11-18T07:54:40.225492
- Generator: World's Best Repo Book Generator v1.0.0

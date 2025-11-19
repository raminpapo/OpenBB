# File Documentation: test_intrinio_fred_series_fetcher_urllib3_v2.yaml

## Metadata
- **Path**: `openbb_platform/providers/intrinio/tests/record/http/test_intrinio_fetchers/test_intrinio_fred_series_fetcher_urllib3_v2.yaml`
- **Size**: 1,252 bytes
- **Lines**: 40
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



---

## High-Level Overview

This is a **config** file named `test_intrinio_fred_series_fetcher_urllib3_v2.yaml`.

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

**Generated**: 2025-11-19T02:16:51.530049Z
**Generator**: World's Best Repo Book Generator v1.0

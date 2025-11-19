# File Documentation: test_fred_commercial_paper_fetcher_urllib3_v2.yaml

## Metadata
- **Path**: `openbb_platform/providers/fred/tests/record/http/test_fred_fetchers/test_fred_commercial_paper_fetcher_urllib3_v2.yaml`
- **Size**: 3,164 bytes
- **Lines**: 102
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
    uri: https://api.stlouisfed.org/fred/series/observations?api_key=MOCK_API_KEY&file_type=json&limit=100000&observation_end=2024-02-01&observation_start=2024-01-01&series_id=RIFSPPAAAD30NB
  response:
    body:
      string: !!binary |
        H4sIAAAAAAAEA6pWKkpNzCnJzE2NLy5JLCpRslIyMjAy0TUw0zUyV9JByKbmpaDL5ScVpxaVJZZk
        5uehaTbUNTBU0lFCVoCs3wgiXZqXWVKsZKWUk5kHUlxaUlBaEl9SWZCqZGWoo5SWmZMK5SllFeeD
        lRSlpBbFJ1UqWaEYnZJYkqqko1ScX1QSnw9SomSllFicrKSjlJxfmleiZGVkoqOUn5ZWnFqiZGWg
        o5STmZtZomRlaAACKK4sVrKKpiREwC6BhSA0EMoSc0pTlayU9JRqdahptpGSjhLMbFM9Y3MqG2+M
        arwZlY03QTXelMrGm6IaT+3AsUA1ntqut0Q1nsphb2iAajyVA8cQlPOREiaVA8cQLd1T23jklEPl
        LGtoRtuAB5XXSAFP7WSDluhNqJtlDWmb6I1Qk42JIXVdb4RWXFI5VRqhFZdUjloj5ERP/brECC3d
        UznlGKGlHCqHvTFacUlt49GKS6oGDrShhVQoAGaqVBtbCwCzHM3B9QkAAA==
    headers:
      Cache-Control:
      - max-age=0, no-cache
      Connection:
      - keep-alive
      Content-Encoding:
      - gzip
      Content-Length:
      - '385'
      Content-Type:
      - application/json; charset=UTF-8
      Date:
      - Thu, 27 Jun 2024 10:13:27 GMT
      Expires:
      - Thu, 27 Jun 2024 10:13:27 GMT
      Last-Modified:
      - Wed, 26 Jun 2024 17:04:19 GMT
      Pragma:
      - no-cache
      Server:
      - Apache
      Strict-Transport-Security:
      - max-age=86400
      Vary:
      - Accept-Encoding
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
    uri: https://api.stlouisfed.org/fred/series?api_key=MOCK_API_KEY&file_type=json&series_id=RIFSPPAAAD30NB
  response:
    body:
      string: !!binary |
        H4sIAAAAAAAEA6pWKkpNzCnJzE2NLy5JLCpRslIyMjAy0TUw0zUyV9JByKbmpaDLFacWZaYWFytZ
        RVcrZYJkgzzdggMCHB0dXYwN/JyQdZNsdklmSU6qkpWSsYGuS2KlgqOjgmNxcWqJrlNicnZqioJz
        fm5ualFyZmKOQkBiQWqRgmdeSWpRanGJQlBiSaqSjlJ+UnFqUVliSWZ+HpLHDAx1QcgITQGa30yV
        dJTSilILS1PzkiuVrJRcEjNzKpHF4osz8sFB5aKko1Sal1lSrGSlFJBalJyaVwITgatRVdJRKk5N
        LM7PS8yJT0zJKi0uyQWps1Lyyy9RCIbK5FQqOILlUlOwq4eb5xfsqKSjlJNYXBJfWpCSWJIKCnl4
        nJkpGBpZGZhYGVrqGoD8UZBfUJqTWJRZUqlkZWipo5SXX5IKcq1bfpFCbn5RqkJmXlp+US44oHQU
        CnJSE4tTFYpTUxUySkoKrGL0Y/TLy8v10lJTUosSc4pSQYGaqpeeXxajX5QKVgxYcYx+ckGMfmJS
        fmmJXkZJrp5SbWwtAIB0s0JWAgAA
    headers:
      Cache-Control:
      - max-age=0, no-cache
      Connection:
      - keep-alive
      Content-Encoding:
      - gzip
      Content-Length:
      - '420'
      Content-Type:
      - application/json; charset=UTF-8
      Date:
      - Thu, 27 Jun 2024 10:13:27 GMT
      Expires:
      - Thu, 27 Jun 2024 10:13:27 GMT
      Last-Modified:
      - Wed, 26 Jun 2024 17:04:19 GMT
      Pragma:
      - no-cache
      Server:
      - Apache
      Strict-Transport-Security:
      - max-age=86400
      Vary:
      - Accept-Encoding
    status:
      code: 200
      message: OK
version: 1

```



---

## High-Level Overview

This is a **config** file named `test_fred_commercial_paper_fetcher_urllib3_v2.yaml`.

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

**Generated**: 2025-11-19T02:16:51.076746Z
**Generator**: World's Best Repo Book Generator v1.0

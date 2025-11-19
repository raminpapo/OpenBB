# File Documentation: test_imf_direction_of_trade_fetcher_urllib3_v2.yaml

## Metadata
- **Path**: `openbb_platform/providers/imf/tests/record/http/test_imf_fetchers/test_imf_direction_of_trade_fetcher_urllib3_v2.yaml`
- **Size**: 1,939 bytes
- **Lines**: 56
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
    uri: http://dataservices.imf.org/REST/SDMX_JSON.svc/CompactData/DOT/A.US.TXG_FOB_USD.W00+B0?startPeriod=2020-01-01&endPeriod=2023-12-31
  response:
    body:
      string: !!binary |
        H4sIAAAAAAAEA6SSX6+aQBDFv4qhL216gWVBUJ5EwZZExPKnsfaBbGFUEgHDUrUx97t3Fm3uNU2T
        m/Rxz57fmZmdvUqzpjqyvHNZxyT7Kk0u1aHm9oWXki3tu+5oq+r5fFbOutK0O5USoqnrYBHne6iY
        XNa8Y3UO0tMLWLwB7P28tHkfs2hy1pVN/QjGbrDua7bAm59tDlwVUrBQbxRXTzQjagWcsx0MRK8c
        m21hV/Ku/aXworr0/IO9j7ghyoUXPYZUgeNzaE8lllHKatuD+e1pVDdM3uoTmf1w4hX/Zx4M+Qys
        gFYsxXcxKtcLTaNkLBcFMWVDHxGZWflQHm1Nczg2iAHWFqkEeIfuLTtwsZZVC0fWQoESJdSQkack
        0Ua2MbIJQX8MdXGrMimFS5sJdckqEJXFd7APrN4hDzXa33Vw6fDgB3Pp+UmaNXWHv0dY08hHff/y
        Ze7PiFACBzjumxrQ8HGgDd5jKx8GJtVlk1IiPWNQBDmUp9eNbDYbUcHFzcTQ9U+Ai3gliaKiv5pj
        7L1ugW4O/94jNhNDWwIi36/SZB55XxB2UJ5E3jxzIs/BcxoLwV+6/sxJwgiVZP0pm4fTLI1dcTUL
        02XiRSsnSv4wUyIu0qWfZEG6SJAxhZD4gYdkFDhCWmnfUAx/3Mv3lysv8kMX/ZTQPiOcxtlXZ5F6
        QtN1a2golmVpODl2/BeiYeDkAbHo+Her9G7DMAwDAXSX1AHBo/jtskUqj8LdLbuMICCFBzjw+MgE
        BdJyk5HfzDBkKqlCXTahsYS8wpzCWcVfffR79ntQ9Hv/5+dpUqhUlZGyMmqz7KKKsEgBmUfx367C
        bphGFdAhm1kLrMxeZiCfZxnjkj26+wT887SyqwUAAA==
    headers:
      Cache-Control:
      - private
      Connection:
      - Keep-Alive
      Content-Encoding:
      - gzip
      Content-Length:
      - '658'
      Content-Type:
      - application/json; charset=utf-8
      Date:
      - Fri, 20 Sep 2024 22:48:00 GMT
      Set-Cookie: null
      Vary:
      - Accept-Encoding
      X-Content-Type-Options:
      - nosniff
      X-Frame-Options:
      - SAMEORIGIN
      X-Permitted-Cross-Domain-Policies:
      - none
      X-XSS-Protection:
      - 1; mode=block
    status:
      code: 200
      message: OK
version: 1

```



---

## High-Level Overview

This is a **config** file named `test_imf_direction_of_trade_fetcher_urllib3_v2.yaml`.

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

**Generated**: 2025-11-19T02:16:51.349734Z
**Generator**: World's Best Repo Book Generator v1.0

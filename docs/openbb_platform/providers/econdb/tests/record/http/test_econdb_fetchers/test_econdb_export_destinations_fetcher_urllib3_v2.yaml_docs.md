# File Documentation: test_econdb_export_destinations_fetcher_urllib3_v2.yaml

## Metadata
- **Path**: `openbb_platform/providers/econdb/tests/record/http/test_econdb_fetchers/test_econdb_export_destinations_fetcher_urllib3_v2.yaml`
- **Size**: 1,884 bytes
- **Lines**: 61
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
    uri: https://www.econdb.com/widgets/top-trade-items/data/?country=US&split_by=country
  response:
    body:
      string: !!binary |
        H4sIAAAAAAAAA3XRXU/CMBQG4L/S7JoL2NaNcafgByJoHDMmhouyVV1S2qU9SySE/25booldTnbT
        nj475017ijqhwEQz8n6KQDNpOmW43YLu+YhEcOzcLjJct9xErtKC8KU1ayXh353SQBpuoJUMWiU9
        +lAKpALvStXrms9ItSFzdbAzGk6WEri+eCbI1tdKsHvbpjZkwYDtmc0x+pvsA9aq8S1fmeg5ObRC
        2AakKhcOSnbAD5vWdIId3fmeaVepGfBPpX1prnoJdnneOWqHX8b9lp24cv8MW89InFKan0fkH1+/
        oTzJ8mnI5xuMTyZpTkP+8IxxWsRZqKsVqpNpHOrVC66zQe/FDarjdBLqzSOm03GchvoaTZIUyeAK
        l+gVJlM66F3eoTobvuYtniShxSA3eidxno9DfY++TjzOBkmWW1zTJNRP8MW1QbNTmhbnnf1+AMFP
        oscFBAAA
    headers:
      CF-Cache-Status:
      - DYNAMIC
      CF-RAY:
      - 8b9ea0585b382d3c-YVR
      Cache-Control:
      - max-age=900
      Connection:
      - keep-alive
      Content-Encoding:
      - gzip
      Content-Type:
      - application/json
      Date:
      - Tue, 27 Aug 2024 19:56:42 GMT
      Expires:
      - Tue, 27 Aug 2024 20:11:42 GMT
      NEL:
      - '{"success_fraction":0,"report_to":"cf-nel","max_age":604800}'
      Referrer-Policy:
      - same-origin
      Report-To:
      - '{"endpoints":[{"url":"https:\/\/a.nel.cloudflare.com\/report\/v4?s=Qv%2Fm9wBrsOOXrNxkgFKyvcwWSvrkUU5NErV3efQCtStbotvUpdeNjSokum2HdjRpZpIuFluPSusDKnXJh%2BrYKSShNoFVulTvkqsxx5vxT9T%2FO0KnHfgUma2KHO6qmro2TMHkRR1wEQHAdHSN"}],"group":"cf-nel","max_age":604800}'
      Server:
      - cloudflare
      Transfer-Encoding:
      - chunked
      Vary:
      - Accept-Encoding
      - Origin
      X-Content-Type-Options:
      - nosniff
      X-Frame-Options:
      - DENY
    status:
      code: 200
      message: OK
version: 1

```



---

## High-Level Overview

This is a **config** file named `test_econdb_export_destinations_fetcher_urllib3_v2.yaml`.

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

**Generated**: 2025-11-19T02:16:49.324084Z
**Generator**: World's Best Repo Book Generator v1.0

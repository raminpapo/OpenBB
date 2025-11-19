# File Documentation: test_oecd_country_interest_rates_fetcher_urllib3_v2.yaml

## Metadata
- **Path**: `openbb_platform/providers/oecd/tests/record/http/test_oecd_fetchers/test_oecd_country_interest_rates_fetcher_urllib3_v2.yaml`
- **Size**: 2,234 bytes
- **Lines**: 45
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
      - application/vnd.sdmx.data+csv; charset=utf-8
      Accept-Encoding:
      - gzip, deflate
      Connection:
      - keep-alive
    method: GET
    uri: https://sdmx.oecd.org/public/rest/data/OECD.SDD.STES,DSD_KEI@DF_KEI,4.0/GBR.M.IRLT....?detail=dataonly&dimensionAtObservation=TIME_PERIOD&endPeriod=2024-01&startPeriod=2023-01
  response:
    body:
      string: "DATAFLOW,REF_AREA,FREQ,MEASURE,UNIT_MEASURE,ACTIVITY,ADJUSTMENT,TRANSFORMATION,TIME_PERIOD,OBS_VALUE,OBS_STATUS,UNIT_MULT,DECIMALS,BASE_PER\r\nOECD.SDD.STES:DSD_KEI@DF_KEI(4.0),GBR,M,IRLT,PA,_Z,_Z,_Z,2023-03,3.5638,,,,\r\nOECD.SDD.STES:DSD_KEI@DF_KEI(4.0),GBR,M,IRLT,PA,_Z,_Z,_Z,2023-02,3.5553,,,,\r\nOECD.SDD.STES:DSD_KEI@DF_KEI(4.0),GBR,M,IRLT,PA,_Z,_Z,_Z,2023-01,3.5115,,,,\r\nOECD.SDD.STES:DSD_KEI@DF_KEI(4.0),GBR,M,IRLT,PA,_Z,_Z,_Z,2024-01,3.9319,,,,\r\nOECD.SDD.STES:DSD_KEI@DF_KEI(4.0),GBR,M,IRLT,PA,_Z,_Z,_Z,2023-12,3.8622,,,,\r\nOECD.SDD.STES:DSD_KEI@DF_KEI(4.0),GBR,M,IRLT,PA,_Z,_Z,_Z,2023-11,4.2721,,,,\r\nOECD.SDD.STES:DSD_KEI@DF_KEI(4.0),GBR,M,IRLT,PA,_Z,_Z,_Z,2023-10,4.5695,,,,\r\nOECD.SDD.STES:DSD_KEI@DF_KEI(4.0),GBR,M,IRLT,PA,_Z,_Z,_Z,2023-09,4.4199,,,,\r\nOECD.SDD.STES:DSD_KEI@DF_KEI(4.0),GBR,M,IRLT,PA,_Z,_Z,_Z,2023-08,4.5298,,,,\r\nOECD.SDD.STES:DSD_KEI@DF_KEI(4.0),GBR,M,IRLT,PA,_Z,_Z,_Z,2023-07,4.4372,,,,\r\nOECD.SDD.STES:DSD_KEI@DF_KEI(4.0),GBR,M,IRLT,PA,_Z,_Z,_Z,2023-06,4.3659,,,,\r\nOECD.SDD.STES:DSD_KEI@DF_KEI(4.0),GBR,M,IRLT,PA,_Z,_Z,_Z,2023-05,3.9621,,,,\r\nOECD.SDD.STES:DSD_KEI@DF_KEI(4.0),GBR,M,IRLT,PA,_Z,_Z,_Z,2023-04,3.6503,,,,\r\n"
    headers:
      Accept-Ranges:
      - values
      Cache-Control:
      - no-store,no-cache
      Content-Encoding:
      - gzip
      Content-Language:
      - en,en-US
      Content-Type:
      - application/vnd.sdmx.data+csv; charset=utf-8
      Date:
      - Wed, 31 Jul 2024 22:54:54 GMT
      Pragma:
      - no-cache
      Strict-Transport-Security:
      - max-age=2592000
      Transfer-Encoding:
      - chunked
      Vary:
      - Accept,Accept-Encoding,Accept-Encoding
      X-Server-Node:
      - Server 1
      api-supported-versions:
      - '1'
    status:
      code: 200
      message: OK
version: 1

```



---

## High-Level Overview

This is a **config** file named `test_oecd_country_interest_rates_fetcher_urllib3_v2.yaml`.

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

**Generated**: 2025-11-19T02:16:51.825483Z
**Generator**: World's Best Repo Book Generator v1.0

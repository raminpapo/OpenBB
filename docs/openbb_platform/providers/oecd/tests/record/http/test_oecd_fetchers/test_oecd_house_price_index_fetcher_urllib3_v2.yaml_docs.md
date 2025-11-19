# File Documentation: test_oecd_house_price_index_fetcher_urllib3_v2.yaml

## Metadata
- **Path**: `openbb_platform/providers/oecd/tests/record/http/test_oecd_fetchers/test_oecd_house_price_index_fetcher_urllib3_v2.yaml`
- **Size**: 2,967 bytes
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
    uri: https://sdmx.oecd.org/public/rest/data/OECD.SDD.TPS,DSD_RHPI_TARGET@DF_RHPI_TARGET,1.0/COU.GBR.Q.RHPI.IX....?detail=dataonly&dimensionAtObservation=TIME_PERIOD&endPeriod=2024-04&startPeriod=2020-01
  response:
    body:
      string: "DATAFLOW,REF_AREA_TYPE,REF_AREA,FREQ,MEASURE,UNIT_MEASURE,ADJUSTMENT,TRANSFORMATION,VINTAGE,DWELLINGS,TIME_PERIOD,OBS_VALUE,OBS_STATUS,UNIT_MULT,DECIMALS,BASE_PER\r\nOECD.SDD.TPS:DSD_RHPI_TARGET@DF_RHPI_TARGET(1.0),COU,GBR,Q,RHPI,IX,N,_Z,_T,_T,2020-Q3,120.812,,,,\r\nOECD.SDD.TPS:DSD_RHPI_TARGET@DF_RHPI_TARGET(1.0),COU,GBR,Q,RHPI,IX,N,_Z,_T,_T,2022-Q1,136.43,,,,\r\nOECD.SDD.TPS:DSD_RHPI_TARGET@DF_RHPI_TARGET(1.0),COU,GBR,Q,RHPI,IX,N,_Z,_T,_T,2020-Q4,124.248,,,,\r\nOECD.SDD.TPS:DSD_RHPI_TARGET@DF_RHPI_TARGET(1.0),COU,GBR,Q,RHPI,IX,N,_Z,_T,_T,2021-Q1,126.185,,,,\r\nOECD.SDD.TPS:DSD_RHPI_TARGET@DF_RHPI_TARGET(1.0),COU,GBR,Q,RHPI,IX,N,_Z,_T,_T,2021-Q2,128.433,,,,\r\nOECD.SDD.TPS:DSD_RHPI_TARGET@DF_RHPI_TARGET(1.0),COU,GBR,Q,RHPI,IX,N,_Z,_T,_T,2021-Q3,130.745,,,,\r\nOECD.SDD.TPS:DSD_RHPI_TARGET@DF_RHPI_TARGET(1.0),COU,GBR,Q,RHPI,IX,N,_Z,_T,_T,2021-Q4,133.186,,,,\r\nOECD.SDD.TPS:DSD_RHPI_TARGET@DF_RHPI_TARGET(1.0),COU,GBR,Q,RHPI,IX,N,_Z,_T,_T,2022-Q2,139.995,,,,\r\nOECD.SDD.TPS:DSD_RHPI_TARGET@DF_RHPI_TARGET(1.0),COU,GBR,Q,RHPI,IX,N,_Z,_T,_T,2022-Q3,145.294,,,,\r\nOECD.SDD.TPS:DSD_RHPI_TARGET@DF_RHPI_TARGET(1.0),COU,GBR,Q,RHPI,IX,N,_Z,_T,_T,2022-Q4,145.455,,,,\r\nOECD.SDD.TPS:DSD_RHPI_TARGET@DF_RHPI_TARGET(1.0),COU,GBR,Q,RHPI,IX,N,_Z,_T,_T,2023-Q1,141.858,,,,\r\nOECD.SDD.TPS:DSD_RHPI_TARGET@DF_RHPI_TARGET(1.0),COU,GBR,Q,RHPI,IX,N,_Z,_T,_T,2023-Q2,141.215,,,,\r\nOECD.SDD.TPS:DSD_RHPI_TARGET@DF_RHPI_TARGET(1.0),COU,GBR,Q,RHPI,IX,N,_Z,_T,_T,2023-Q3,143.72,,,,\r\nOECD.SDD.TPS:DSD_RHPI_TARGET@DF_RHPI_TARGET(1.0),COU,GBR,Q,RHPI,IX,N,_Z,_T,_T,2023-Q4,142.468,,,,\r\nOECD.SDD.TPS:DSD_RHPI_TARGET@DF_RHPI_TARGET(1.0),COU,GBR,Q,RHPI,IX,N,_Z,_T,_T,2024-Q1,142.179,,,,\r\nOECD.SDD.TPS:DSD_RHPI_TARGET@DF_RHPI_TARGET(1.0),COU,GBR,Q,RHPI,IX,N,_Z,_T,_T,2020-Q1,117.108,,,,\r\nOECD.SDD.TPS:DSD_RHPI_TARGET@DF_RHPI_TARGET(1.0),COU,GBR,Q,RHPI,IX,N,_Z,_T,_T,2020-Q2,117.326,,,,\r\n"
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
      - Thu, 27 Jun 2024 10:14:42 GMT
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

This is a **config** file named `test_oecd_house_price_index_fetcher_urllib3_v2.yaml`.

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

**Generated**: 2025-11-19T02:16:51.831364Z
**Generator**: World's Best Repo Book Generator v1.0

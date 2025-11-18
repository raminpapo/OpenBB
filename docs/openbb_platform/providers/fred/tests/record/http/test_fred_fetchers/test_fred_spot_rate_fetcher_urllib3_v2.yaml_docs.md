# Documentation: openbb_platform/providers/fred/tests/record/http/test_fred_fetchers/test_fred_spot_rate_fetcher_urllib3_v2.yaml

## File Metadata
- **Path**: `openbb_platform/providers/fred/tests/record/http/test_fred_fetchers/test_fred_spot_rate_fetcher_urllib3_v2.yaml`
- **Size**: 1,837 characters, 45 lines
- **Words**: 85
- **Extension**: .yaml
- **Classification**: Text file

## Original Source

```yaml
interactions:
- request:
    body: null
    headers:
      Accept:
      - '*/*'
      Accept-Encoding:
      - gzip, deflate
      Connection:
      - keep-alive
    method: GET
    uri: https://api.stlouisfed.org/fred/series/observations?api_key=MOCK_API_KEY&file_type=json&observation_end=2023-06-06&observation_start=2023-01-01&series_id=HQMCB10YR
  response:
    body:
      string: '{"realtime_start":"2024-06-27","realtime_end":"2024-06-27","observation_start":"2023-01-01","observation_end":"2023-06-06","units":"lin","output_type":1,"file_type":"json","order_by":"observation_date","sort_order":"asc","count":6,"offset":0,"limit":100000,"observations":[{"realtime_start":"2024-06-27","realtime_end":"2024-06-27","date":"2023-01-01","value":"4.98"},{"realtime_start":"2024-06-27","realtime_end":"2024-06-27","date":"2023-02-01","value":"5.13"},{"realtime_start":"2024-06-27","realtime_end":"2024-06-27","date":"2023-03-01","value":"5.18"},{"realtime_start":"2024-06-27","realtime_end":"2024-06-27","date":"2023-04-01","value":"4.92"},{"realtime_start":"2024-06-27","realtime_end":"2024-06-27","date":"2023-05-01","value":"5.09"},{"realtime_start":"2024-06-27","realtime_end":"2024-06-27","date":"2023-06-01","value":"5.22"}]}'
    headers:
      Cache-Control:
      - max-age=0, no-cache
      Connection:
      - keep-alive
      Content-Encoding:
      - gzip
      Content-Length:
      - '286'
      Content-Type:
      - application/json; charset=UTF-8
      Date:
      - Thu, 27 Jun 2024 10:13:28 GMT
      Expires:
      - Thu, 27 Jun 2024 10:13:28 GMT
      Last-Modified:
      - Fri, 07 Jun 2024 19:03:01 GMT
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

## High-Level Overview

This is a .yaml file containing 45 lines of code.

## Detailed Structure

Standard text file.

## Key Components

No major components extracted.

## Usage & Examples

See source code for usage details.

## Related Files

No direct file references found.

## Notes
- Generated: 2025-11-18T07:54:39.833167
- Generator: World's Best Repo Book Generator v1.0.0

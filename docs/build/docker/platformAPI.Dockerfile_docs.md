# Documentation: build/docker/platformAPI.Dockerfile

## File Metadata
- **Path**: `build/docker/platformAPI.Dockerfile`
- **Size**: 184 characters, 11 lines
- **Words**: 19
- **Extension**: .Dockerfile
- **Classification**: Text file

## Original Source

```
FROM python:3.10-slim-bookworm

WORKDIR /app

RUN pip install "openbb[all]"
RUN pip install openbb-platform-api

EXPOSE 6900

ENTRYPOINT ["openbb-api", "--host", "0.0.0.0", "--login"]

```

## High-Level Overview

This is a .Dockerfile file containing 11 lines of code.

## Detailed Structure

Standard text file.

## Key Components

No major components extracted.

## Usage & Examples

See source code for usage details.

## Related Files

No direct file references found.

## Notes
- Generated: 2025-11-18T07:54:34.601453
- Generator: World's Best Repo Book Generator v1.0.0

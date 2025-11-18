# Documentation: build/docker/platform.dockerfile

## File Metadata
- **Path**: `build/docker/platform.dockerfile`
- **Size**: 1,272 characters, 48 lines
- **Words**: 150
- **Extension**: .dockerfile
- **Classification**: Text file

## Original Source

```
# ---- Base Python ----
    FROM python:3.11-slim-bullseye AS base

    # set work directory
    WORKDIR /openbb

    # set environment variables
    ENV PYTHONDONTWRITEBYTECODE 1
    ENV PYTHONUNBUFFERED 1

    # install dependencies
    RUN apt-get update \
        && apt-get install -y --no-install-recommends build-essential openssh-client curl \
        && apt-get clean \
        && rm -rf /var/lib/apt/lists/*

    # install toml and poetry
    RUN pip install toml poetry

    # ---- Copy Files/Build ----
    FROM base AS builder

    WORKDIR /openbb

    # install Rust
    RUN curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh -s -- -y \
        && apt-get update \
        && apt-get install -y --no-install-recommends libwebkit2gtk-4.0-dev \
        && apt-get clean \
        && rm -rf /var/lib/apt/lists/*

    # add Rust to PATH
    ENV PATH="/root/.cargo/bin:${PATH}"

    COPY ./openbb_platform ./openbb_platform

    # Install the Platform
    RUN pip install /openbb/openbb_platform[all]
    RUN pip install openbb-devtools

    # ---- Copy Files ----
    FROM base

    COPY --from=builder /usr/local /usr/local

    # Launch the API
    CMD ["uvicorn", "openbb_core.api.rest_api:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]

```

## High-Level Overview

This is a .dockerfile file containing 48 lines of code.

## Detailed Structure

Standard text file.

## Key Components

No major components extracted.

## Usage & Examples

See source code for usage details.

## Related Files

No direct file references found.

## Notes
- Generated: 2025-11-18T07:54:34.600592
- Generator: World's Best Repo Book Generator v1.0.0

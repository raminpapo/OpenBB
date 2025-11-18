# Documentation: openbb_platform/providers/README.md

## File Metadata
- **Path**: `openbb_platform/providers/README.md`
- **Size**: 770 characters, 30 lines
- **Words**: 82
- **Extension**: .md
- **Classification**: Text file

## Original Source

```markdown
# Providers

In this folder you can find the providers that were created or are supported by OpenBB.

## Recommended structure

Every provider is located within a directory, with the following structure:

```{.bash}
openbb_platform
└───providers
    └───<provider_name>
        |   README.md
        │   pyproject.toml
        │   poetry.lock
        |───tests
        └───openbb_<provider_name>
            │   __init__.py
            |───models
            |   |───<some model>.py
            |   └───...
            └───utils
                |───<some helper>.py
                └───...
```

The models define the data structures that are used to query the provider endpoints and store the response data.

See [CONTRIBUTING file](../CONTRIBUTING.md) for more details

```

## High-Level Overview

This is a .md file containing 30 lines of code.

## Detailed Structure

Standard text file.

## Key Components

No major components extracted.

## Usage & Examples

See source code for usage details.

## Related Files

No direct file references found.

## Notes
- Generated: 2025-11-18T07:54:37.237608
- Generator: World's Best Repo Book Generator v1.0.0

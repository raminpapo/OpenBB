# Documentation: .github/labeler.yml

## File Metadata
- **Path**: `.github/labeler.yml`
- **Size**: 471 characters, 28 lines
- **Words**: 44
- **Extension**: .yml
- **Classification**: Text file

## Original Source

```yaml
version: 2
appendOnly: true
labels:
  - label: "platform"
    files:
      - "openbb_platform/.*"

  - label: "v4"
    files:
      - "openbb_platform/.*"

  - label: "enhancement"
    branch: "^feature/.*"

  - label: "bug"
    branch: "^hotfix/.*"

  - label: "bug"
    branch: "^bugfix/.*"

  - label: "excel"
    files:
      - "website/content/excel/.*"

  - label: "breaking_change"
    files:
      - "openbb_platform/core/openbb_core/provider/standard_models/.*"

```

## High-Level Overview

This is a .yml file containing 28 lines of code.

## Detailed Structure

Standard text file.

## Key Components

No major components extracted.

## Usage & Examples

See source code for usage details.

## Related Files

No direct file references found.

## Notes
- Generated: 2025-11-18T07:54:34.555943
- Generator: World's Best Repo Book Generator v1.0.0

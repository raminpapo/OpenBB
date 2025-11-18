# Documentation: desktop/src-tauri/tauri.linux.conf.json

## File Metadata
- **Path**: `desktop/src-tauri/tauri.linux.conf.json`
- **Size**: 531 characters, 30 lines
- **Words**: 38
- **Extension**: .json
- **Classification**: Text file

## Original Source

```json
{
  "bundle": {
    "targets": "all",
    "resources": [],
    "category": "Finance",
    "linux": {
      "deb": {
        "depends": [
          "libwebkit2gtk-4.1-0",
          "libgtk-3-0",
          "libssl3",
          "libcairo-gobject2",
          "libgdk-pixbuf-2.0-0",
          "libpango-1.0-0",
          "libatk1.0-0",
          "libglib2.0-0",
          "libssl-dev"
        ]
      },
      "rpm": {
        "depends": [
          "webkit2gtk4.1",
          "gtk3",
          "openssl"
        ]
      }
    }
  }
}

```

## High-Level Overview

This is a .json file containing 30 lines of code.

## Detailed Structure

Standard text file.

## Key Components

No major components extracted.

## Usage & Examples

See source code for usage details.

## Related Files

No direct file references found.

## Notes
- Generated: 2025-11-18T07:54:35.116631
- Generator: World's Best Repo Book Generator v1.0.0

# File Documentation: desktop.json

## Metadata
- **Path**: `desktop/src-tauri/capabilities/desktop.json`
- **Size**: 1,722 bytes
- **Lines**: 73
- **Category**: config
- **Extension**: .json

---

## Original Source

```json
{
  "identifier": "desktop-capability",
  "platforms": [
    "macOS",
    "windows",
    "linux"
  ],
  "windows": [
    "*"
  ],
  "permissions": [
    "core:default",
    "opener:allow-default-urls",
    "shell:allow-open",
    "shell:allow-execute",
    "shell:allow-spawn",
    "fs:read-all",
    "fs:write-all",
    "fs:write-files",
    "fs:allow-unwatch",
    "log:default",
    {
      "identifier": "opener:allow-open-path",
      "allow": [
        {
          "path": "**"
        }
      ]
    },
    "dialog:default",
    "fs:default",
    {
      "identifier": "fs:allow-exists",
      "allow": [
        {
          "path": "**"
        }
      ]
    },
    "fs:scope-home-recursive",
    "fs:allow-copy-file",
    "fs:allow-create",
    "fs:allow-exists",
    "fs:allow-mkdir",
    "fs:allow-read-dir",
    "fs:allow-read-file",
    "fs:allow-remove",
    "fs:allow-rename",
    "fs:allow-watch",
    "fs:allow-write-file",
    "fs:scope-localdata-recursive",
    "fs:scope-log",
    "fs:allow-appconfig-read-recursive",
    "fs:allow-appconfig-write-recursive",
    "fs:allow-app-read-recursive",
    "fs:allow-app-write-recursive",
    "fs:allow-applocaldata-read-recursive",
    "fs:allow-applocaldata-write-recursive",
    "fs:allow-applog-read-recursive",
    "fs:allow-applog-write-recursive",
    "fs:allow-appcache-read-recursive",
    "fs:allow-appcache-write-recursive",
    "fs:allow-cache-read-recursive",
    "fs:allow-cache-write-recursive",
    "fs:allow-temp-read-recursive",
    "fs:allow-temp-write-recursive",
    "fs:allow-data-write-recursive",
    "fs:allow-data-read-recursive",
    "fs:allow-config-read-recursive",
    "fs:allow-config-write-recursive",
    "updater:default"
  ]
}
```



---

## High-Level Overview

This is a **config** file named `desktop.json`.

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

**Generated**: 2025-11-19T02:16:45.413284Z
**Generator**: World's Best Repo Book Generator v1.0

# Documentation: desktop/src-tauri/src/utils/autostart/mod.rs

## File Metadata
- **Path**: `desktop/src-tauri/src/utils/autostart/mod.rs`
- **Size**: 165 characters, 9 lines
- **Words**: 18
- **Extension**: .rs
- **Classification**: Text file

## Original Source

```rust
#[cfg(target_os = "macos")]
pub mod macos_autostart;

#[cfg(target_os = "linux")]
pub mod linux_autostart;

#[cfg(target_os = "windows")]
pub mod windows_autostart;

```

## High-Level Overview

This is a .rs file containing 9 lines of code.

## Detailed Structure

Standard text file.

## Key Components

No major components extracted.

## Usage & Examples

See source code for usage details.

## Related Files

No direct file references found.

## Notes
- Generated: 2025-11-18T07:54:35.103408
- Generator: World's Best Repo Book Generator v1.0.0

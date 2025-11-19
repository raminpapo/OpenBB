# File Documentation: sign.ps1

## Metadata
- **Path**: `desktop/src-tauri/scripts/sign.ps1`
- **Size**: 1,138 bytes
- **Lines**: 22
- **Category**: text
- **Extension**: .ps1

---

## Original Source

```
# Download and set up CodeSignTool
$toolDir = Join-Path $env:GITHUB_WORKSPACE "codesigntool"
New-Item -ItemType Directory -Force -Path $toolDir
$zipPath = Join-Path $toolDir "CodeSignTool.zip"
Invoke-WebRequest -Uri "https://github.com/SSLcom/CodeSignTool/releases/download/v1.3.1/CodeSignTool-v1.3.1-windows.zip" -OutFile $zipPath
Expand-Archive -Path $zipPath -DestinationPath $toolDir -Force
$codeSignToolPath = Join-Path $toolDir "CodeSignTool.bat"

# Find all binaries in the root of the release directory
$targetDir = Join-Path $env:GITHUB_WORKSPACE "desktop/target/x86_64-pc-windows-msvc/release"
$filesToSign = Get-ChildItem -Path $targetDir -Include *.exe, *.dll

# Sign each file individually
foreach ($file in $filesToSign) {
    Write-Host "Signing $($file.FullName)..."
    & $codeSignToolPath sign -username="$($env:ESIGNER_USERNAME)" -password="$($env:ESIGNER_PASSWORD)" -credential_id="$($env:ESIGNER_CREDENTIAL_ID)" -totp_secret="$($env:ESIGNER_TOTP_SECRET)" -file_path="$($file.FullName)" -malware_block="true"
    if ($LASTEXITCODE -ne 0) {
        Write-Error "Failed to sign $($file.FullName)"
        exit 1
    }
}

```



---

## High-Level Overview

This is a **text** file named `sign.ps1`.

This file contains 22 lines of code/text.


---

## Detailed Analysis

This file contains code or text data. See the original source above for full details.


---

## Related Files

The following files may be related based on imports and references:

*No direct imports detected.*


---

## Performance & Security Notes

No obvious security concerns detected in static analysis.


---

**Generated**: 2025-11-19T02:16:45.417489Z
**Generator**: World's Best Repo Book Generator v1.0

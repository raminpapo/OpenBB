# Documentation: desktop/src/components/ShowVersion.tsx

## File Metadata
- **Path**: `desktop/src/components/ShowVersion.tsx`
- **Size**: 793 characters, 33 lines
- **Words**: 94
- **Extension**: .tsx
- **Classification**: Text file

## Original Source

```tsx
import { useState, useEffect } from "react";
import { getVersion } from "@tauri-apps/api/app";

let cachedVersion: string | null = null;

const safeGetVersion = async (): Promise<string> => {
  if (cachedVersion !== null) return cachedVersion;
  try {
    cachedVersion = await getVersion();
    return cachedVersion;
  } catch (error) {
    console.error("Failed to get version:", error);
    cachedVersion = "";
    return "";
  }
};

export default function ShowVersion() {
  const [version, setVersion] = useState<string>(cachedVersion ?? "");

  useEffect(() => {
    if (cachedVersion !== null) return;
    safeGetVersion().then(setVersion);
  }, []);

  if (!version) return null;

  return (
    <div className="body-xs-regular text-theme-secondary">
      v{version}
    </div>
  );
}
```

## High-Level Overview

This is a .tsx file containing 33 lines of code.

## Detailed Structure

### JavaScript/TypeScript Structure

**Classes**: 0
**Functions**: 2
**Imports**: 2


## Key Components

No major components extracted.

## Usage & Examples

See source code for usage details.

## Related Files

No direct file references found.

## Notes
- Generated: 2025-11-18T07:54:35.145830
- Generator: World's Best Repo Book Generator v1.0.0

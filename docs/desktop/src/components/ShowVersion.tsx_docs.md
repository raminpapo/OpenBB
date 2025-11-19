# File Documentation: ShowVersion.tsx

## Metadata
- **Path**: `desktop/src/components/ShowVersion.tsx`
- **Size**: 793 bytes
- **Lines**: 33
- **Category**: javascript
- **Extension**: .tsx

---

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



---

## High-Level Overview

This is a **javascript** file named `ShowVersion.tsx`.

This file contains 33 lines of code/text.


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

**Generated**: 2025-11-19T02:16:45.053887Z
**Generator**: World's Best Repo Book Generator v1.0

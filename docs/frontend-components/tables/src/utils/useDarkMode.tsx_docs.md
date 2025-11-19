# File Documentation: useDarkMode.tsx

## Metadata
- **Path**: `frontend-components/tables/src/utils/useDarkMode.tsx`
- **Size**: 430 bytes
- **Lines**: 15
- **Category**: javascript
- **Extension**: .tsx

---

## Original Source

```tsx
import { useState, useEffect } from "react";

export default function useDarkMode(initialTheme: "dark" | "light") {
  const [theme, setTheme] = useState(initialTheme);
  const colorTheme = theme === "dark" ? "light" : "dark";

  useEffect(() => {
    const root = window.document.documentElement;
    root.classList.remove(colorTheme);
    root.classList.add(theme);
  }, [theme, colorTheme]);

  return [colorTheme, setTheme];
}

```



---

## High-Level Overview

This is a **javascript** file named `useDarkMode.tsx`.

This file contains 15 lines of code/text.


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

**Generated**: 2025-11-19T02:16:46.107278Z
**Generator**: World's Best Repo Book Generator v1.0

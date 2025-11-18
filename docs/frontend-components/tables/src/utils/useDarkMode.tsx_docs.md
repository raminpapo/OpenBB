# Documentation: frontend-components/tables/src/utils/useDarkMode.tsx

## File Metadata
- **Path**: `frontend-components/tables/src/utils/useDarkMode.tsx`
- **Size**: 430 characters, 15 lines
- **Words**: 46
- **Extension**: .tsx
- **Classification**: Text file

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

## High-Level Overview

This is a .tsx file containing 15 lines of code.

## Detailed Structure

### JavaScript/TypeScript Structure

**Classes**: 0
**Functions**: 3
**Imports**: 1


## Key Components

No major components extracted.

## Usage & Examples

See source code for usage details.

## Related Files

No direct file references found.

## Notes
- Generated: 2025-11-18T07:54:35.366615
- Generator: World's Best Repo Book Generator v1.0.0

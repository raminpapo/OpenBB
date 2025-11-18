# Documentation: frontend-components/tables/src/utils/useClickOutside.tsx

## File Metadata
- **Path**: `frontend-components/tables/src/utils/useClickOutside.tsx`
- **Size**: 728 characters, 23 lines
- **Words**: 72
- **Extension**: .tsx
- **Classification**: Text file

## Original Source

```tsx
import { RefObject, useEffect } from "react";

export default function useOnClickOutside(
  ref: RefObject<HTMLElement>,
  handler: (event: MouseEvent | TouchEvent) => void
) {
  useEffect(() => {
    const listener = (event: MouseEvent | TouchEvent) => {
      // Do nothing if clicking ref's element or descendent elements
      if (!ref.current || ref.current.contains(event.target as Node)) {
        return;
      }
      handler(event);
    };
    document.addEventListener("mousedown", listener);
    document.addEventListener("touchstart", listener);
    return () => {
      document.removeEventListener("mousedown", listener);
      document.removeEventListener("touchstart", listener);
    };
  }, [ref, handler]);
}

```

## High-Level Overview

Do nothing if clicking ref's element or descendent elements

## Detailed Structure

### JavaScript/TypeScript Structure

**Classes**: 0
**Functions**: 2
**Imports**: 1


## Key Components

No major components extracted.

## Usage & Examples

See source code for usage details.

## Related Files

No direct file references found.

## Notes
- Generated: 2025-11-18T07:54:35.365208
- Generator: World's Best Repo Book Generator v1.0.0

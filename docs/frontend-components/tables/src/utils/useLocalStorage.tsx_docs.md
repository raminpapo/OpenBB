# Documentation: frontend-components/tables/src/utils/useLocalStorage.tsx

## File Metadata
- **Path**: `frontend-components/tables/src/utils/useLocalStorage.tsx`
- **Size**: 1,484 characters, 43 lines
- **Words**: 192
- **Extension**: .tsx
- **Classification**: Text file

## Original Source

```tsx
import { useState } from "react";

export default function useLocalStorage(key: string, initialValue: any, validateFn?: (value: any) => any) {
  // State to store our value
  // Pass initial state function to useState so logic is only executed once
  const [storedValue, setStoredValue] = useState(() => {
    if (typeof window === "undefined") {
      return initialValue;
    }
    try {
      // Get from local storage by key
      const item = window.localStorage.getItem(key);
      // Parse stored json or if none return initialValue
      return item ?
        validateFn ? validateFn(JSON.parse(item)) :
          JSON.parse(item) : initialValue;
    } catch (error) {
      // If error also return initialValue
      console.log(error);
      return initialValue;
    }
  });
  // Return a wrapped version of useState's setter function that ...
  // ... persists the new value to localStorage.
  const setValue = (value: any) => {
    try {
      // Allow value to be a function so we have same API as useState
      const valueToStore =
        value instanceof Function ? value(storedValue) : value;
      // Save state
      setStoredValue(valueToStore);
      // Save to local storage
      if (typeof window !== "undefined") {
        window.localStorage.setItem(key, JSON.stringify(valueToStore));
      }
    } catch (error) {
      // A more advanced implementation would handle the error case
      console.log(error);
    }
  };
  return [storedValue, setValue];
}

```

## High-Level Overview

State to store our value
Pass initial state function to useState so logic is only executed once
Get from local storage by key
Parse stored json or if none return initialValue
If error also return initialValue
Return a wrapped version of useState's setter function that ...
... persists the new value to localStorage.
Allow value to be a function so we have same API as useState
Save state
Save to local storage
A more advanced implementation would handle the error case

## Detailed Structure

### JavaScript/TypeScript Structure

**Classes**: 0
**Functions**: 4
**Imports**: 1


## Key Components

No major components extracted.

## Usage & Examples

See source code for usage details.

## Related Files

No direct file references found.

## Notes
- Generated: 2025-11-18T07:54:35.367972
- Generator: World's Best Repo Book Generator v1.0.0

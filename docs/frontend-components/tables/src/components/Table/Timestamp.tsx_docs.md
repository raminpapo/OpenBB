# File Documentation: Timestamp.tsx

## Metadata
- **Path**: `frontend-components/tables/src/components/Table/Timestamp.tsx`
- **Size**: 1,336 bytes
- **Lines**: 49
- **Category**: javascript
- **Extension**: .tsx

---

## Original Source

```tsx
import { useEffect, useState } from "react";

export default function Timestamp() {
  const [counter, setCounter] = useState(0);
  useEffect(() => {
    const interval = setInterval(() => {
      setCounter((counter) => counter + 10);
    }, 10000);
    return () => clearInterval(interval);
  }, []);

  const minutesPassed = Math.floor(counter / 60);

  return (
    <div className="lg:flex gap-2 items-center bg-grey-200 dark:bg-grey-800 rounded p-2 text-xs hidden">
      <svg
        xmlns="http://www.w3.org/2000/svg"
        width="16"
        height="16"
        fill="none"
        viewBox="0 0 16 16"
      >
        <g
          strokeLinecap="round"
          strokeLinejoin="round"
          clipPath="url(#clip0_106_4278)"
        >
          <path
            stroke="currentColor"
            d="M7.646 1.28a6.667 6.667 0 11-4.311 1.94M8 4.333V8l2 1.333"
          ></path>
          <path
            stroke="currentColor"
            d="M.701 3.693l3.22-.863.776 2.898"
          ></path>
        </g>
        <defs>
          <clipPath id="clip0_106_4278">
            <path fill="currentColor" d="M0 0H16V16H0z"></path>
          </clipPath>
        </defs>
      </svg>
      <span className="whitespace-nowrap">
        {minutesPassed > 0 ? `${minutesPassed} min ago` : "Just now"}
      </span>
    </div>
  );
}

```



---

## High-Level Overview

This is a **javascript** file named `Timestamp.tsx`.

This file contains 49 lines of code/text.


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

**Generated**: 2025-11-19T02:16:46.090129Z
**Generator**: World's Best Repo Book Generator v1.0

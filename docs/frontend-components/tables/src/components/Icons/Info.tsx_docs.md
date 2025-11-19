# File Documentation: Info.tsx

## Metadata
- **Path**: `frontend-components/tables/src/components/Icons/Info.tsx`
- **Size**: 686 bytes
- **Lines**: 33
- **Category**: javascript
- **Extension**: .tsx

---

## Original Source

```tsx
import type { SVGProps } from "react";
interface SVGRProps {
  title?: string;
  titleId?: string;
}

const InfoIcon = ({
  title,
  titleId,
  ...props
}: SVGProps<SVGSVGElement> & SVGRProps) => (
  <svg
    viewBox="0 0 24 24"
    width={24}
    height={24}
    fill="none"
    xmlns="http://www.w3.org/2000/svg"
    aria-labelledby={titleId}
    {...props}
  >
    {title ? <title id={titleId}>{title}</title> : null}
    <path
      d="M12 22c5.523 0 10-4.477 10-10S17.523 2 12 2 2 6.477 2 12s4.477 10 10 10ZM12 16v-4M12 8h.01"
      stroke="currentColor"
      strokeWidth={1.5}
      strokeLinecap="round"
      strokeLinejoin="round"
    />
  </svg>
);

export default InfoIcon;

```



---

## High-Level Overview

This is a **javascript** file named `Info.tsx`.

This file contains 33 lines of code/text.


---

## Detailed Analysis

This file contains code or text data. See the original source above for full details.


---

## Related Files

The following files may be related based on imports and references:

**Imported Modules**:
- `type`


---

## Performance & Security Notes

No obvious security concerns detected in static analysis.


---

**Generated**: 2025-11-19T02:16:46.076444Z
**Generator**: World's Best Repo Book Generator v1.0

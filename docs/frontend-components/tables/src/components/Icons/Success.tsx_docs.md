# File Documentation: Success.tsx

## Metadata
- **Path**: `frontend-components/tables/src/components/Icons/Success.tsx`
- **Size**: 804 bytes
- **Lines**: 40
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

const SuccessIcon = ({
  title,
  titleId,
  ...props
}: SVGProps<SVGSVGElement> & SVGRProps) => (
  <svg
    width={18}
    height={18}
    viewBox="0 0 18 18"
    fill="none"
    xmlns="http://www.w3.org/2000/svg"
    aria-labelledby={titleId}
    {...props}
  >
    {title ? <title id={titleId}>{title}</title> : null}
    <path
      d="M16.5 8.31V9a7.5 7.5 0 1 1-4.447-6.855"
      stroke="currentColor"
      strokeWidth={1.5}
      strokeLinecap="round"
      strokeLinejoin="round"
    />
    <path
      d="M16.5 3 9 10.508l-2.25-2.25"
      stroke="currentColor"
      strokeWidth={1.5}
      strokeLinecap="round"
      strokeLinejoin="round"
    />
  </svg>
);

export default SuccessIcon;

```



---

## High-Level Overview

This is a **javascript** file named `Success.tsx`.

This file contains 40 lines of code/text.


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

**Generated**: 2025-11-19T02:16:46.077951Z
**Generator**: World's Best Repo Book Generator v1.0

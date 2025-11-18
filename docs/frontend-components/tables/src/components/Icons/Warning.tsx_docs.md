# Documentation: frontend-components/tables/src/components/Icons/Warning.tsx

## File Metadata
- **Path**: `frontend-components/tables/src/components/Icons/Warning.tsx`
- **Size**: 742 characters, 33 lines
- **Words**: 80
- **Extension**: .tsx
- **Classification**: Text file

## Original Source

```tsx
import type { SVGProps } from "react";
interface SVGRProps {
  title?: string;
  titleId?: string;
}

const WarningIcon = ({
  title,
  titleId,
  ...props
}: SVGProps<SVGSVGElement> & SVGRProps) => (
  <svg
    viewBox="0 0 18 18"
    width={18}
    height={18}
    fill="none"
    xmlns="http://www.w3.org/2000/svg"
    aria-labelledby={titleId}
    {...props}
  >
    {title ? <title id={titleId}>{title}</title> : null}
    <path
      d="M7.718 2.895 1.366 13.5a1.5 1.5 0 0 0 1.282 2.25h12.705a1.5 1.5 0 0 0 1.283-2.25L10.283 2.895a1.5 1.5 0 0 0-2.565 0v0ZM9 6.75v3M9 12.75h.008"
      stroke="currentColor"
      strokeWidth={1.5}
      strokeLinecap="round"
      strokeLinejoin="round"
    />
  </svg>
);

export default WarningIcon;

```

## High-Level Overview

This is a .tsx file containing 33 lines of code.

## Detailed Structure

### JavaScript/TypeScript Structure

**Classes**: 0
**Functions**: 1
**Imports**: 1


## Key Components

No major components extracted.

## Usage & Examples

See source code for usage details.

## Related Files

- `type`

## Notes
- Generated: 2025-11-18T07:54:35.328246
- Generator: World's Best Repo Book Generator v1.0.0

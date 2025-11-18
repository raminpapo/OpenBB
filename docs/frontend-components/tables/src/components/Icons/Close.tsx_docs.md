# Documentation: frontend-components/tables/src/components/Icons/Close.tsx

## File Metadata
- **Path**: `frontend-components/tables/src/components/Icons/Close.tsx`
- **Size**: 496 characters, 29 lines
- **Words**: 53
- **Extension**: .tsx
- **Classification**: Text file

## Original Source

```tsx
import type { SVGProps } from "react";
interface SVGRProps {
  title?: string;
  titleId?: string;
}

const CloseIcon = ({
  title,
  titleId,
  ...props
}: SVGProps<SVGSVGElement> & SVGRProps) => (
  <svg
    xmlns="http://www.w3.org/2000/svg"
    fill="none"
    viewBox="0 0 24 24"
    stroke="currentColor"
    strokeWidth={1.5}
    {...props}
  >
    <path
      strokeLinecap="round"
      strokeLinejoin="round"
      d="M6 18L18 6M6 6l12 12"
    />
  </svg>
);

export default CloseIcon;

```

## High-Level Overview

This is a .tsx file containing 29 lines of code.

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
- Generated: 2025-11-18T07:54:35.323409
- Generator: World's Best Repo Book Generator v1.0.0

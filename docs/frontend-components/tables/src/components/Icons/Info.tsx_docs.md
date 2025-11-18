# Documentation: frontend-components/tables/src/components/Icons/Info.tsx

## File Metadata
- **Path**: `frontend-components/tables/src/components/Icons/Info.tsx`
- **Size**: 686 characters, 33 lines
- **Words**: 74
- **Extension**: .tsx
- **Classification**: Text file

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
- Generated: 2025-11-18T07:54:35.325824
- Generator: World's Best Repo Book Generator v1.0.0

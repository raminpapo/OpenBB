# Documentation: frontend-components/tables/src/components/Icons/Success.tsx

## File Metadata
- **Path**: `frontend-components/tables/src/components/Icons/Success.tsx`
- **Size**: 804 characters, 40 lines
- **Words**: 73
- **Extension**: .tsx
- **Classification**: Text file

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

## High-Level Overview

This is a .tsx file containing 40 lines of code.

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
- Generated: 2025-11-18T07:54:35.326958
- Generator: World's Best Repo Book Generator v1.0.0

# Documentation: frontend-components/tables/src/components/Table/InderterminateCheckbox.tsx

## File Metadata
- **Path**: `frontend-components/tables/src/components/Table/InderterminateCheckbox.tsx`
- **Size**: 589 characters, 27 lines
- **Words**: 61
- **Extension**: .tsx
- **Classification**: Text file

## Original Source

```tsx
import { HTMLProps, useEffect, useRef } from "react";

function IndeterminateCheckbox({
  indeterminate,
  className = "",
  ...rest
}: { indeterminate?: boolean } & HTMLProps<HTMLInputElement>) {
  const ref = useRef<HTMLInputElement>(null!);

  useEffect(() => {
    if (typeof indeterminate === "boolean") {
      ref.current.indeterminate = !rest.checked && indeterminate;
    }
  }, [ref, indeterminate]);

  return (
    <input
      type="checkbox"
      ref={ref}
      className={className + " cursor-pointer"}
      {...rest}
    />
  );
}

export default IndeterminateCheckbox;

```

## High-Level Overview

This is a .tsx file containing 27 lines of code.

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
- Generated: 2025-11-18T07:54:35.340934
- Generator: World's Best Repo Book Generator v1.0.0

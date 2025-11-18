# Documentation: frontend-components/plotly/src/utils/utils.ts

## File Metadata
- **Path**: `frontend-components/plotly/src/utils/utils.ts`
- **Size**: 301 characters, 14 lines
- **Words**: 39
- **Extension**: .ts
- **Classification**: Text file

## Original Source

```typescript
// @ts-nocheck

export const non_blocking = (func: Function, delay: number) => {
  let timeout: number;
  return function () {
    // @ts-ignore
    const context = this;
    const args = arguments;
    clearTimeout(timeout);
    timeout = setTimeout(() => func.apply(context, args), delay);
  };
};


```

## High-Level Overview

@ts-nocheck
@ts-ignore

## Detailed Structure

### JavaScript/TypeScript Structure

**Classes**: 0
**Functions**: 3
**Imports**: 0


## Key Components

No major components extracted.

## Usage & Examples

See source code for usage details.

## Related Files

No direct file references found.

## Notes
- Generated: 2025-11-18T07:54:35.303341
- Generator: World's Best Repo Book Generator v1.0.0

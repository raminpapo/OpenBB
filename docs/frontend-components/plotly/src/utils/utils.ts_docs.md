# File Documentation: utils.ts

## Metadata
- **Path**: `frontend-components/plotly/src/utils/utils.ts`
- **Size**: 301 bytes
- **Lines**: 14
- **Category**: javascript
- **Extension**: .ts

---

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



---

## High-Level Overview

This is a **javascript** file named `utils.ts`.

This file contains 14 lines of code/text.


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

**Generated**: 2025-11-19T02:16:46.043622Z
**Generator**: World's Best Repo Book Generator v1.0

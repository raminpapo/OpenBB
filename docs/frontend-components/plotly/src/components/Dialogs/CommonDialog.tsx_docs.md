# File Documentation: CommonDialog.tsx

## Metadata
- **Path**: `frontend-components/plotly/src/components/Dialogs/CommonDialog.tsx`
- **Size**: 1,196 bytes
- **Lines**: 44
- **Category**: javascript
- **Extension**: .tsx

---

## Original Source

```tsx
import * as DialogPrimitive from "@radix-ui/react-dialog";
import CloseIcon from "../Icons/Close";
import { ReactNode } from "react";

export const styleDialog = {
  margin: "2px 0px 2px 10px",
  padding: "5px 2px 2px 5px",
};

export default function CommonDialog({
  open,
  close,
  title,
  description,
  children,
}: {
  open: boolean;
  close: () => void;
  title: string;
  description: string;
  children: ReactNode;
}) {
  return (
    <DialogPrimitive.Root open={open} onOpenChange={close}>
      <DialogPrimitive.Overlay onClick={close} className="_modal-overlay" />
      <DialogPrimitive.Content className="_modal">
        <DialogPrimitive.Title className="_modal-title">
          {title}
        </DialogPrimitive.Title>
        <DialogPrimitive.Description className="_modal_description">
          {description}
        </DialogPrimitive.Description>
        <DialogPrimitive.Close>
          <CloseIcon />
        </DialogPrimitive.Close>
        {children}
        <DialogPrimitive.Close className="_modal-close" onClick={close}>
          <CloseIcon className="w-6 h-6" />
        </DialogPrimitive.Close>
      </DialogPrimitive.Content>
    </DialogPrimitive.Root>
  );
}

```



---

## High-Level Overview

This is a **javascript** file named `CommonDialog.tsx`.

This file contains 44 lines of code/text.


---

## Detailed Analysis

This file contains code or text data. See the original source above for full details.


---

## Related Files

The following files may be related based on imports and references:

**Imported Modules**:
- `CloseIcon`


---

## Performance & Security Notes

No obvious security concerns detected in static analysis.


---

**Generated**: 2025-11-19T02:16:46.018433Z
**Generator**: World's Best Repo Book Generator v1.0

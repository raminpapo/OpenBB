# Documentation: frontend-components/plotly/src/components/Dialogs/CommonDialog.tsx

## File Metadata
- **Path**: `frontend-components/plotly/src/components/Dialogs/CommonDialog.tsx`
- **Size**: 1,196 characters, 44 lines
- **Words**: 93
- **Extension**: .tsx
- **Classification**: Text file

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

## High-Level Overview

This is a .tsx file containing 44 lines of code.

## Detailed Structure

### JavaScript/TypeScript Structure

**Classes**: 0
**Functions**: 2
**Imports**: 3


## Key Components

No major components extracted.

## Usage & Examples

See source code for usage details.

## Related Files

- `CloseIcon`

## Notes
- Generated: 2025-11-18T07:54:35.265017
- Generator: World's Best Repo Book Generator v1.0.0

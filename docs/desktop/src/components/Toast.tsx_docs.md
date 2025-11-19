# File Documentation: Toast.tsx

## Metadata
- **Path**: `desktop/src/components/Toast.tsx`
- **Size**: 1,419 bytes
- **Lines**: 56
- **Category**: javascript
- **Extension**: .tsx

---

## Original Source

```tsx
import React from "react";
import { Button } from "@openbb/ui-pro";
import CustomIcon from "../components/Icon";

interface ToastProps {
  title: string;
  children: React.ReactNode;
  onClose: () => void;
  buttonText?: string;
  onButtonClick?: () => void;
}


const Toast: React.FC<ToastProps> = ({
  title,
  children,
  onClose,
  buttonText,
  onButtonClick,
}) => {
  return (
    <div className="toast-container">
      <div className="flex-col">
        <div className="flex flex-1 items-center justify-between">
          <div className="flex flex1 gap-2 items-start">
            <CustomIcon id="info" className="toast-info-icon w-5 h-5"/>
            <div className="body-sm-bold">{title}</div>
          </div>
          <Button
            type="button"
            variant="icon"
            onClick={onClose}
          >
            <span className="items-end body-lg-bold">x</span>
          </Button>
        </div>
        <div className="flex-1 mt-2 body-sm-medium justify-left mr-5 pr-10">{children}</div>
        {buttonText && onButtonClick && (
          <div className="mt-5 mr-5 flex justify-end">
            <Button
              type="button"
              className="button-toast"
              onClick={onButtonClick}
              size="xs"
            >
              {buttonText}
            </Button>
          </div>
        )}
      </div>
    </div>
  );
};

export default Toast;

```



---

## High-Level Overview

This is a **javascript** file named `Toast.tsx`.

This file contains 56 lines of code/text.


---

## Detailed Analysis

This file contains code or text data. See the original source above for full details.


---

## Related Files

The following files may be related based on imports and references:

**Imported Modules**:
- `CustomIcon`
- `React`


---

## Performance & Security Notes

No obvious security concerns detected in static analysis.


---

**Generated**: 2025-11-19T02:16:45.054912Z
**Generator**: World's Best Repo Book Generator v1.0

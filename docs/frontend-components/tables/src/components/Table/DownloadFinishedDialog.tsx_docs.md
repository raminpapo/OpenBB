# File Documentation: DownloadFinishedDialog.tsx

## Metadata
- **Path**: `frontend-components/tables/src/components/Table/DownloadFinishedDialog.tsx`
- **Size**: 2,388 bytes
- **Lines**: 81
- **Category**: javascript
- **Extension**: .tsx

---

## Original Source

```tsx
import * as DialogPrimitive from "@radix-ui/react-dialog";
import CloseIcon from "../Icons/Close";

export default function DownloadFinishedDialog({
  open,
  close,
}: {
  open: boolean;
  close: () => void;
}) {
  const userHomeDir = window.download_path || "~/OpenBBUserData/exports";
  return (
    <DialogPrimitive.Root open={open} onOpenChange={close}>
      <div id="loading" className="saving">
        <div id="loading_text" className="loading_text" />
        <div id="loader" className="loader" />
      </div>
      <DialogPrimitive.Overlay onClick={close} className="_modal-overlay" />
      <DialogPrimitive.Content className="_modal">
        <DialogPrimitive.Close>
          <CloseIcon />
        </DialogPrimitive.Close>
        <DialogPrimitive.Close
          className="_modal-close"
          onClick={close}
          style={{ float: "right", marginTop: 20 }}
        >
          <CloseIcon className="w-6 h-6" />
        </DialogPrimitive.Close>
        <DialogPrimitive.Title className="_modal-title">
          Success
        </DialogPrimitive.Title>
        <div
          id="popup_title"
          className="popup_content"
          style={{ padding: "0px 2px 2px 5px", marginTop: 5 }}
        >
          <div
            style={{
              display: "flex",
              flexDirection: "column",
              gap: 0,
              fontSize: 14,
            }}
          >
            <div>
              <label htmlFor="title_text">
                <b>{window.title}</b> has been downloaded to
                <br />
                <br />
                <a
                  style={{ color: "#FFDD00", marginTop: 15 }}
                  href={`${userHomeDir}`}
                  onClick={(e) => {
                    e.preventDefault();
                    window.pywry.open_file(userHomeDir);
                  }}
                >
                  {userHomeDir}
                </a>
              </label>
            </div>
          </div>
          <div style={{ float: "right", marginTop: 20 }}>
            <button
              className="_btn"
              style={{
                padding: "8px 16px",
                width: "100%",
              }}
              onClick={close}
            >
              Close
            </button>
          </div>
        </div>
      </DialogPrimitive.Content>
    </DialogPrimitive.Root>
  );
}

```



---

## High-Level Overview

This is a **javascript** file named `DownloadFinishedDialog.tsx`.

This file contains 81 lines of code/text.


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

**Generated**: 2025-11-19T02:16:46.083289Z
**Generator**: World's Best Repo Book Generator v1.0

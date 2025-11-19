# File Documentation: AlertDialog.tsx

## Metadata
- **Path**: `frontend-components/plotly/src/components/Dialogs/AlertDialog.tsx`
- **Size**: 847 bytes
- **Lines**: 43
- **Category**: javascript
- **Extension**: .tsx

---

## Original Source

```tsx
import CommonDialog from "../Dialogs/CommonDialog";

export default function AlertDialog({
	title,
	content,
	open,
	close,
}: {
	title: string;
	content: string;
	open: boolean;
	close: () => void;
}) {
	return (
		<CommonDialog title={title} description="" open={open} close={close}>
			<div
				id="popup_title"
				className="popup_content"
				style={{ padding: "0px 2px 2px 5px", marginTop: 5 }}
			>
				<div style={{ display: "flex", flexDirection: "column", gap: 0 }}>
					<div>
						<label htmlFor="title_text">{content}</label>
					</div>
				</div>
				<div style={{ float: "right", marginTop: 20 }}>
					<button
						type="button"
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
		</CommonDialog>
	);
}

```



---

## High-Level Overview

This is a **javascript** file named `AlertDialog.tsx`.

This file contains 43 lines of code/text.


---

## Detailed Analysis

This file contains code or text data. See the original source above for full details.


---

## Related Files

The following files may be related based on imports and references:

**Imported Modules**:
- `CommonDialog`


---

## Performance & Security Notes

No obvious security concerns detected in static analysis.


---

**Generated**: 2025-11-19T02:16:46.016991Z
**Generator**: World's Best Repo Book Generator v1.0

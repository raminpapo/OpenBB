# Documentation: frontend-components/plotly/src/components/Dialogs/AlertDialog.tsx

## File Metadata
- **Path**: `frontend-components/plotly/src/components/Dialogs/AlertDialog.tsx`
- **Size**: 847 characters, 43 lines
- **Words**: 86
- **Extension**: .tsx
- **Classification**: Text file

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

## High-Level Overview

This is a .tsx file containing 43 lines of code.

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

- `CommonDialog`

## Notes
- Generated: 2025-11-18T07:54:35.263376
- Generator: World's Best Repo Book Generator v1.0.0

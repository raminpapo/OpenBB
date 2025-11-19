# File Documentation: ChangeColor.tsx

## Metadata
- **Path**: `frontend-components/plotly/src/components/ChangeColor.tsx`
- **Size**: 2,547 bytes
- **Lines**: 96
- **Category**: javascript
- **Extension**: .tsx

---

## Original Source

```tsx
//@ts-nocheck
import { useEffect, useState } from "react";

export default function ChangeColor({
  open,
  onColorChange,
}: {
  open: boolean;
  onColorChange: (color: string) => void;
}) {
  const [active, setActive] = useState(false);

  function onChangeColor(color) {
    onColorChange(color);
  }

  if (open && !active) {
    setActive(true);
  }
  if (!open && active) {
    setActive(false);
  }

  useEffect(() => {
    if (active) {
      let color_picker = document.getElementById("changecolor");
      color_picker.style.display = "block";
      color_picker.style.width = null;
      dragElement(color_picker);

      function dragElement(elmnt) {
        let pos1 = 0,
          pos2 = 0,
          pos3 = 0,
          pos4 = 0;
        if (document.getElementById(elmnt.id + "_header")) {
          // if present, the header is where you move the DIV from:
          document.getElementById(elmnt.id + "_header").onmousedown =
            dragMouseDown;
        } else {
          // otherwise, move the DIV from anywhere inside the DIV:
          elmnt.onmousedown = dragMouseDown;
        }

        function dragMouseDown(e) {
          e = e || window.event;
          e.preventDefault();
          // get the mouse cursor position at startup:
          pos3 = e.clientX;
          pos4 = e.clientY;
          document.onmouseup = closeDragElement;
          // call a function whenever the cursor moves:
          document.onmousemove = elementDrag;
        }

        function elementDrag(e) {
          e = e || window.event;
          e.preventDefault();
          // calculate the new cursor position:
          pos1 = pos3 - e.clientX;
          pos2 = pos4 - e.clientY;
          pos3 = e.clientX;
          pos4 = e.clientY;
          // set the element's new position:
          elmnt.style.top = elmnt.offsetTop - pos2 + "px";
          elmnt.style.left = elmnt.offsetLeft - pos1 + "px";
        }

        function closeDragElement() {
          // stop moving when mouse button is released:
          document.onmouseup = null;
          document.onmousemove = null;
        }
      }
    } else {
      document.getElementById("changecolor").style.display = "none";
    }
  }, [active]);

  return (
    <div id="changecolor">
      <div id="changecolor_header">
        <input
          type="color"
          id="picked_color"
          value="#00ACFF"
          onChange={(e) => {
            let color = e.target.value;
            onChangeColor(color);
          }}
        />
      </div>
    </div>
  );
}

```



---

## High-Level Overview

This is a **javascript** file named `ChangeColor.tsx`.

This file contains 96 lines of code/text.


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

**Generated**: 2025-11-19T02:16:46.007899Z
**Generator**: World's Best Repo Book Generator v1.0

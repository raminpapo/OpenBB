# File Documentation: Export.tsx

## Metadata
- **Path**: `frontend-components/tables/src/components/Table/Export.tsx`
- **Size**: 1,275 bytes
- **Lines**: 57
- **Category**: javascript
- **Extension**: .tsx

---

## Original Source

```tsx
import { useState } from "react";
import { downloadData, downloadImage } from "../../utils/utils";
import * as RadioGroup from "@radix-ui/react-radio-group";
import useLocalStorage from "../../utils/useLocalStorage";
import { EXPORT_TYPES } from ".";
import Select from "../Select";

export default function Export({
  columns,
  data,
  type,
  setType,
  downloadFinished,
}: {
  columns: any;
  data: any;
  type: any;
  setType: any;
  downloadFinished: (change: boolean) => void;
}) {
  const onExport = () => {
    switch (type) {
      case "csv":
        downloadData("csv", columns, data, downloadFinished);
        break;
      case "png":
        downloadImage("table", downloadFinished);
        break;
    }
  };
  return (
    <div className="flex gap-2 items-center">
      <Select
        labelType="row"
        value={type}
        onChange={(value) => {
          setType(value);
        }}
        label="Type"
        placeholder="Select type"
        groups={[
          {
            label: "Type",
            items: EXPORT_TYPES.map((type) => ({
              label: type,
              value: type,
            })),
          },
        ]}
      />
      <button onClick={onExport} className="_btn">
        Export
      </button>
    </div>
  );
}

```



---

## High-Level Overview

This is a **javascript** file named `Export.tsx`.

This file contains 57 lines of code/text.


---

## Detailed Analysis

This file contains code or text data. See the original source above for full details.


---

## Related Files

The following files may be related based on imports and references:

**Imported Modules**:
- `Select`
- `useLocalStorage`


---

## Performance & Security Notes

No obvious security concerns detected in static analysis.


---

**Generated**: 2025-11-19T02:16:46.084616Z
**Generator**: World's Best Repo Book Generator v1.0

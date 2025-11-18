# Documentation: frontend-components/tables/src/components/Table/Export.tsx

## File Metadata
- **Path**: `frontend-components/tables/src/components/Table/Export.tsx`
- **Size**: 1,275 characters, 57 lines
- **Words**: 123
- **Extension**: .tsx
- **Classification**: Text file

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

## High-Level Overview

This is a .tsx file containing 57 lines of code.

## Detailed Structure

### JavaScript/TypeScript Structure

**Classes**: 0
**Functions**: 2
**Imports**: 6


## Key Components

No major components extracted.

## Usage & Examples

See source code for usage details.

## Related Files

- `useLocalStorage`
- `Select`

## Notes
- Generated: 2025-11-18T07:54:35.336509
- Generator: World's Best Repo Book Generator v1.0.0

# File Documentation: Pagination.tsx

## Metadata
- **Path**: `frontend-components/tables/src/components/Table/Pagination.tsx`
- **Size**: 3,487 bytes
- **Lines**: 116
- **Category**: javascript
- **Extension**: .tsx

---

## Original Source

```tsx
import clsx from "clsx";
import Select from "../Select";
import { DEFAULT_ROWS_PER_PAGE } from ".";

export function validatePageSize(pageSize: any) {
  if (typeof pageSize !== "number") {
    if (typeof pageSize === "string" && pageSize.includes("All")) {
      return pageSize;
    }
    return DEFAULT_ROWS_PER_PAGE;
  }
  if (pageSize < 1) {
    return DEFAULT_ROWS_PER_PAGE;
  }
  return pageSize;
}

export default function Pagination({
  table,
  currentPage,
  setCurrentPage,
}: {
  table: any;
  currentPage: number;
  setCurrentPage: (value: number) => void;
}) {
  const totalRows = table.getFilteredRowModel().rows.length || 0;

  return (
    <div className="hidden md:flex items-center gap-3">
      <Select
        value={currentPage}
        onChange={(value) => {
          const newValue = validatePageSize(value);
          setCurrentPage(newValue);
          if (newValue.toString().includes("All")) table.setPageSize(totalRows);
          else table.setPageSize(newValue);
        }}
        labelType="row"
        label="Rows per page"
        placeholder="Select rows per page"
        groups={[
          {
            label: "Rows per page", // TODO: generate number automatically
            items: [10, 20, 30, 40, 50, `All (${totalRows})`].map(
              (pageSize) => ({
                label: `${pageSize}`,
                value: pageSize,
              })
            ),
          },
        ]}
      />
      <span className="flex items-center gap-1">
        <strong>{table.getState().pagination.pageIndex + 1}</strong>
        of
        <strong>{table.getPageCount()}</strong>
      </span>
      {/*<span className="flex items-center gap-1">
          | Go to page:
          <input
            type="number"
            defaultValue={table.getState().pagination.pageIndex + 1}
            onChange={(e) => {
              const page = e.target.value ? Number(e.target.value) - 1 : 0;
              table.setPageIndex(page);
            }}
            className="_input"
          />
          </span>*/}
      <div className="hidden mdl:block">
        <button
          className={clsx("px-2", {
            "text-grey-400 dark:text-grey-700": !table.getCanPreviousPage(),
            "dark:text-white": table.getCanPreviousPage(),
          })}
          onClick={() => table.setPageIndex(0)}
          disabled={!table.getCanPreviousPage()}
        >
          {"<<"}
        </button>
        <button
          className={clsx("px-2", {
            "text-grey-400 dark:text-grey-700": !table.getCanPreviousPage(),
            "dark:text-white": table.getCanPreviousPage(),
          })}
          onClick={() => table.previousPage()}
          disabled={!table.getCanPreviousPage()}
        >
          {"<"}
        </button>
        <button
          className={clsx("px-2", {
            "text-grey-400 dark:text-grey-700": !table.getCanNextPage(),
            "dark:text-white": table.getCanNextPage(),
          })}
          onClick={() => table.nextPage()}
          disabled={!table.getCanNextPage()}
        >
          {">"}
        </button>
        <button
          className={clsx("px-2", {
            "text-grey-400 dark:text-grey-700": !table.getCanNextPage(),
            "dark:text-white": table.getCanNextPage(),
          })}
          onClick={() => table.setPageIndex(table.getPageCount() - 1)}
          disabled={!table.getCanNextPage()}
        >
          {">>"}
        </button>
      </div>
    </div>
  );
}

```



---

## High-Level Overview

This is a **javascript** file named `Pagination.tsx`.

This file contains 116 lines of code/text.


---

## Detailed Analysis

This file contains code or text data. See the original source above for full details.


---

## Related Files

The following files may be related based on imports and references:

**Imported Modules**:
- `Select`
- `clsx`


---

## Performance & Security Notes

No obvious security concerns detected in static analysis.


---

**Generated**: 2025-11-19T02:16:46.088878Z
**Generator**: World's Best Repo Book Generator v1.0

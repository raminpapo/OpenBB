# File Documentation: DebouncedInput.tsx

## Metadata
- **Path**: `frontend-components/tables/src/components/Table/DebouncedInput.tsx`
- **Size**: 1,585 bytes
- **Lines**: 62
- **Category**: javascript
- **Extension**: .tsx

---

## Original Source

```tsx
import { FC, useEffect, useState } from "react";

type Props = {
  value: string | number;
  onChange: (value: string | number) => void;
  debounce?: number;
} & Omit<React.InputHTMLAttributes<HTMLInputElement>, "onChange">;

const DebouncedInput: FC<Props> = ({
  value: initialValue,
  onChange,
  debounce = 500,
  ...props
}) => {
  const [value, setValue] = useState<number | string>(initialValue);

  const handleInputChange = (event: React.ChangeEvent<HTMLInputElement>) =>
    setValue(event.target.value);

  useEffect(() => {
    setValue(initialValue);
  }, [initialValue]);

  useEffect(() => {
    const timeout = setTimeout(() => {
      onChange(value);
    }, debounce);

    return () => clearTimeout(timeout);
  }, [value]);

  return (
    <div className="relative group">
      <div className="absolute inset-y-0 left-0 flex items-center pl-3 pointer-events-none">
        <svg
          aria-hidden="true"
          className="w-5 h-5 text-grey-600"
          fill="none"
          stroke="currentColor"
          viewBox="0 0 24 24"
          xmlns="http://www.w3.org/2000/svg"
        >
          <path
            strokeLinecap="round"
            strokeLinejoin="round"
            strokeWidth="2"
            d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z"
          ></path>
        </svg>
      </div>
      <input
        {...props}
        className="bg-grey-900 h-[36px] border-[1.5px] border-grey-700 rounded p-3 pl-10 max-w-[216px]"
        value={value}
        onChange={handleInputChange}
      />
    </div>
  );
};

export default DebouncedInput;

```



---

## High-Level Overview

This is a **javascript** file named `DebouncedInput.tsx`.

This file contains 62 lines of code/text.


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

**Generated**: 2025-11-19T02:16:46.082003Z
**Generator**: World's Best Repo Book Generator v1.0

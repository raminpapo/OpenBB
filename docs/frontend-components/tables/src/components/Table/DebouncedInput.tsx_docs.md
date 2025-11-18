# Documentation: frontend-components/tables/src/components/Table/DebouncedInput.tsx

## File Metadata
- **Path**: `frontend-components/tables/src/components/Table/DebouncedInput.tsx`
- **Size**: 1,585 characters, 62 lines
- **Words**: 145
- **Extension**: .tsx
- **Classification**: Text file

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

## High-Level Overview

This is a .tsx file containing 62 lines of code.

## Detailed Structure

### JavaScript/TypeScript Structure

**Classes**: 0
**Functions**: 2
**Imports**: 1


## Key Components

No major components extracted.

## Usage & Examples

See source code for usage details.

## Related Files

No direct file references found.

## Notes
- Generated: 2025-11-18T07:54:35.333329
- Generator: World's Best Repo Book Generator v1.0.0

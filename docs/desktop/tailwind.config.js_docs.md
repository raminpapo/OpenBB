# Documentation: desktop/tailwind.config.js

## File Metadata
- **Path**: `desktop/tailwind.config.js`
- **Size**: 296 characters, 17 lines
- **Words**: 31
- **Extension**: .js
- **Classification**: Text file

## Original Source

```javascript
/** @type {import('tailwindcss').Config} */
import conf from "@openbb/ui-pro/tailwind.config";
export default {
  presets: [conf],
  content: [
    "./index.html",
    "./src/**/*.{js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {},
    container: {
      center: true,
    },
  },
  plugins: [],
}

```

## High-Level Overview

@type {import('tailwindcss').Config} */

## Detailed Structure

### JavaScript/TypeScript Structure

**Classes**: 0
**Functions**: 0
**Imports**: 1


## Key Components

No major components extracted.

## Usage & Examples

See source code for usage details.

## Related Files

- `conf`

## Notes
- Generated: 2025-11-18T07:54:35.222612
- Generator: World's Best Repo Book Generator v1.0.0

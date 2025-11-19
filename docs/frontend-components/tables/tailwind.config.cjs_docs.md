# File Documentation: tailwind.config.cjs

## Metadata
- **Path**: `frontend-components/tables/tailwind.config.cjs`
- **Size**: 840 bytes
- **Lines**: 32
- **Category**: text
- **Extension**: .cjs

---

## Original Source

```
/** @type {import('tailwindcss').Config} */
module.exports = {
  darkMode: "class",
  content: ["./index.html", "./src/**/*.{js,ts,jsx,tsx}"],
  theme: {
    extend: {
      screens: {
        smh: { raw: "(max-height: 450px)" },
        mdl: { raw: "(min-width: 890px)" },
      },
      colors: {
        "grey-50": "#f6f6f6ff",
        "grey-100": "#eaeaeaff",
        "grey-200": "#dcdcdcff",
        "grey-300": "#c8c8c8ff",
        "grey-400": "#a2a2a2ff",
        "grey-500": "#808080ff",
        "grey-600": "#5a5a5aff",
        "grey-700": "#474747ff",
        "grey-800": "#2a2a2aff",
        "grey-850": "#131313ff",
        "grey-900": "#070707ff",
        "burgundy-300": "#B47DA0",
        "burgundy-400": "#9B5181",
        "burgundy-500": "#822661",
        "burgundy-900": "#340F27",
      },
    },
  },
  plugins: [],
};

```



---

## High-Level Overview

This is a **text** file named `tailwind.config.cjs`.

This file contains 32 lines of code/text.


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

**Generated**: 2025-11-19T02:16:46.061759Z
**Generator**: World's Best Repo Book Generator v1.0

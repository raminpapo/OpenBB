# File Documentation: eslint.config.mjs

## Metadata
- **Path**: `desktop/eslint.config.mjs`
- **Size**: 2,086 bytes
- **Lines**: 81
- **Category**: text
- **Extension**: .mjs

---

## Original Source

```
import js from "@eslint/js";
import tseslint from "typescript-eslint";
import react from "eslint-plugin-react";

export default [
  {
    ignores: [
      "dist/",
      "target/",
      "node_modules/",
      "*.js",
      "*.cjs",
      "*.mjs",
      "*.d.ts",
      "src-tauri/",
      ".vscode/",
      ".tanstack/"
    ]
  },
  js.configs.recommended,
  ...tseslint.configs.recommended,
  {
    files: ["**/*.ts", "**/*.tsx", "**/*.js", "**/*.jsx"],
    plugins: { "@typescript-eslint": tseslint.plugin },
    languageOptions: {
      parser: tseslint.parser,
      parserOptions: {
        project: "./tsconfig.json",
      },
      globals: {
        window: "readonly",
        document: "readonly",
        console: "readonly",
        setTimeout: "readonly",
        clearTimeout: "readonly",
        setInterval: "readonly",
        clearInterval: "readonly",
        Event: "readonly",
        CustomEvent: "readonly",
        Node: "readonly",
        HTMLElement: "readonly",
        HTMLInputElement: "readonly",
        ResizeObserver: "readonly",
        MutationObserver: "readonly",
        AbortController: "readonly",
        URL: "readonly",
        Headers: "readonly",
        Response: "readonly",
        CSS: "readonly",
        self: "readonly",
        navigator: "readonly",
        sessionStorage: "readonly",
        requestAnimationFrame: "readonly",
        cancelAnimationFrame: "readonly",
        NodeFilter: "readonly",
        DocumentFragment: "readonly",
        IntersectionObserver: "readonly",
      }
    },
  },
  {
    files: ["src/components/BackendLogsPage.tsx", "src/routes/backends.tsx"],
    rules: {
      "no-control-regex": "off",
    },
  },
  {
    plugins: { react },
    files: ["**/*.jsx", "**/*.tsx"],
    settings: { react: { version: "detect" } },
    rules: {
      // Add custom React rules here if needed
    },
  },
  {
    files: ["**/*.test.ts", "**/*.test.tsx", "**/*.spec.ts", "**/*.spec.tsx", "**/tests/**/*.ts", "**/tests/**/*.tsx"],
    rules: {
      "@typescript-eslint/no-explicit-any": "off",
    },
  },
];
```



---

## High-Level Overview

This is a **text** file named `eslint.config.mjs`.

This file contains 81 lines of code/text.


---

## Detailed Analysis

This file contains code or text data. See the original source above for full details.


---

## Related Files

The following files may be related based on imports and references:

**Imported Modules**:
- `js`
- `react`
- `tseslint`


---

## Performance & Security Notes

No obvious security concerns detected in static analysis.


---

**Generated**: 2025-11-19T02:16:44.994599Z
**Generator**: World's Best Repo Book Generator v1.0

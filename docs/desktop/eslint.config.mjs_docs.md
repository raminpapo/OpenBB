# Documentation: desktop/eslint.config.mjs

## File Metadata
- **Path**: `desktop/eslint.config.mjs`
- **Size**: 2,086 characters, 81 lines
- **Words**: 164
- **Extension**: .mjs
- **Classification**: Text file

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

## High-Level Overview

This is a .mjs file containing 81 lines of code.

## Detailed Structure

Standard text file.

## Key Components

No major components extracted.

## Usage & Examples

See source code for usage details.

## Related Files

- `js`
- `tseslint`
- `react`

## Notes
- Generated: 2025-11-18T07:54:34.787816
- Generator: World's Best Repo Book Generator v1.0.0

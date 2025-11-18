# Documentation: desktop/tsconfig.json

## File Metadata
- **Path**: `desktop/tsconfig.json`
- **Size**: 842 characters, 30 lines
- **Words**: 65
- **Extension**: .json
- **Classification**: Text file

## Original Source

```json
{
  "compilerOptions": {
    "target": "ES2020",
    "useDefineForClassFields": true,
    "lib": ["ES2020", "DOM", "DOM.Iterable"],
    "module": "ESNext",
    "skipLibCheck": true,
    "moduleResolution": "bundler",
    "allowImportingTsExtensions": true,
    "resolveJsonModule": true,
    "isolatedModules": true,
    "noEmit": true,
    "jsx": "react-jsx",
    "strict": true,
    "noImplicitAny": true,
    "strictNullChecks": true,
    "noUnusedLocals": true,
    "noUnusedParameters": true,
    "noFallthroughCasesInSwitch": true,
    "forceConsistentCasingInFileNames": true,
    "esModuleInterop": true,
    "baseUrl": ".",
    "paths": {
      "*": ["*", "src/*"],
      "~/*": ["./src/*"]
    }
  },
  "include": ["src/**/*.ts", "src/**/*.tsx", "src/**/*.js", "src/**/*.jsx"],
  "references": [{ "path": "./tsconfig.node.json" }]
}
```

## High-Level Overview

This is a .json file containing 30 lines of code.

## Detailed Structure

Standard text file.

## Key Components

No major components extracted.

## Usage & Examples

See source code for usage details.

## Related Files

No direct file references found.

## Notes
- Generated: 2025-11-18T07:54:35.223364
- Generator: World's Best Repo Book Generator v1.0.0

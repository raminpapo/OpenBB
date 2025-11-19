# File Documentation: vite.config.ts

## Metadata
- **Path**: `desktop/vite.config.ts`
- **Size**: 1,515 bytes
- **Lines**: 63
- **Category**: javascript
- **Extension**: .ts

---

## Original Source

```typescript
import path from "node:path";
import { tanstackRouter } from "@tanstack/router-vite-plugin";
import react from "@vitejs/plugin-react";
import { defineConfig } from "vite";
import { viteStaticCopy } from "vite-plugin-static-copy";
import svgr from "vite-plugin-svgr";

const host = process.env.TAURI_DEV_HOST;

export default defineConfig(async () => ({
    resolve: {
        alias: {
            "~": path.resolve(__dirname, "./src"),
        },
    },
    plugins: [
        react(),
        svgr(),
        viteStaticCopy({
            targets: [{ src: "./node_modules/@openbb/ui-pro/dist/assets", dest: "" }],
        }),
        tanstackRouter(),
    ],

    base: "./",
    build: {
        outDir: "dist",
        emptyOutDir: true,
        sourcemap: true,
        chunkSizeWarningLimit: 1000, // Increase chunk size warning limit to 1MB
        rollupOptions: {
			output: {
				manualChunks(id: string) {
				if (id.includes('node_modules')) {
					if (id.includes('@openbb')) {
					return 'vendor-openbb';
					}
					if (id.includes('@tanstack')) {
					return 'vendor-tanstack';
					}
					return 'vendor';
				}
				}
			}
		}
    },
    clearScreen: false,
    server: {
        port: 1470,
        strictPort: true,
        host: host || false,
        hmr: host
            ? {
                    protocol: "ws",
                    host,
                    port: 1421,
                }
            : undefined,
        watch: {
            ignored: ["**/src-tauri/**"],
        },
    },
}));
```



---

## High-Level Overview

This is a **javascript** file named `vite.config.ts`.

This file contains 63 lines of code/text.


---

## Detailed Analysis

This file contains code or text data. See the original source above for full details.


---

## Related Files

The following files may be related based on imports and references:

**Imported Modules**:
- `path`
- `react`
- `svgr`


---

## Performance & Security Notes

No obvious security concerns detected in static analysis.


---

**Generated**: 2025-11-19T02:16:45.020733Z
**Generator**: World's Best Repo Book Generator v1.0

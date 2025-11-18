# Documentation: desktop/src/tests/setup.ts

## File Metadata
- **Path**: `desktop/src/tests/setup.ts`
- **Size**: 226 characters, 11 lines
- **Words**: 20
- **Extension**: .ts
- **Classification**: Text file

## Original Source

```typescript
import '@testing-library/jest-dom';

// Mock ResizeObserver
const ResizeObserverMock = vi.fn(() => ({
  observe: vi.fn(),
  unobserve: vi.fn(),
  disconnect: vi.fn(),
}));

vi.stubGlobal('ResizeObserver', ResizeObserverMock);

```

## High-Level Overview

Mock ResizeObserver

## Detailed Structure

### JavaScript/TypeScript Structure

**Classes**: 0
**Functions**: 1
**Imports**: 0


## Key Components

No major components extracted.

## Usage & Examples

See source code for usage details.

## Related Files

No direct file references found.

## Notes
- Generated: 2025-11-18T07:54:35.219317
- Generator: World's Best Repo Book Generator v1.0.0

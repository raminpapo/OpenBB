# Documentation: desktop/src/tests/routes/jupyter-logs.test.tsx

## File Metadata
- **Path**: `desktop/src/tests/routes/jupyter-logs.test.tsx`
- **Size**: 1,809 characters, 49 lines
- **Words**: 173
- **Extension**: .tsx
- **Classification**: Text file

## Original Source

```tsx
/// <reference types="vitest/globals" />
import { render, screen } from '@testing-library/react';
import { vi } from 'vitest';
import React from 'react';

// Mock @tanstack/react-router to match the real API
vi.mock('@tanstack/react-router', () => ({
  createFileRoute: vi.fn(() => (opts: any) => ({
    ...opts,
    options: opts,
  })),
}));

// Mock the JupyterLogsPage component
vi.mock('../../components/JupyterLogsPage', () => ({
  __esModule: true,
  default: vi.fn(() => <div>Mocked JupyterLogsPage</div>),
}));

// Import after mocks so Route uses the mocks
import { Route as JupyterLogsRoute } from '../../routes/jupyter-logs';

describe('JupyterLogs Route', () => {
  const JupyterLogsWrapperComponent = JupyterLogsRoute.options.component as React.ComponentType;

  beforeEach(() => {
    vi.clearAllMocks();
    // Clean up body class for each test
    document.body.classList.remove('jupyter-logs-view');
  });

  test('renders JupyterLogsWrapper and JupyterLogsPage component', () => {
    render(<JupyterLogsWrapperComponent />);
    expect(screen.getByText(/Mocked JupyterLogsPage/i)).toBeInTheDocument();
  });

  test('adds and removes "jupyter-logs-view" class to body on mount and unmount', () => {
    const { unmount } = render(<JupyterLogsWrapperComponent />);
    expect(document.body.classList.contains('jupyter-logs-view')).toBe(true);
    unmount();
    expect(document.body.classList.contains('jupyter-logs-view')).toBe(false);
  });

  test('validates search parameters correctly', () => {
    const validateSearch = JupyterLogsRoute.options.validateSearch as (search: Record<string, unknown>) => Record<string, unknown>;
    expect(validateSearch({ env: 'some-env' })).toEqual({ environment: 'some-env' });
    expect(validateSearch({})).toEqual({ environment: null });
  });
});
```

## High-Level Overview

<reference types="vitest/globals" />
Mock @tanstack/react-router to match the real API
Mock the JupyterLogsPage component
Import after mocks so Route uses the mocks
Clean up body class for each test

## Detailed Structure

### JavaScript/TypeScript Structure

**Classes**: 2
**Functions**: 2
**Imports**: 4


## Key Components

No major components extracted.

## Usage & Examples

See source code for usage details.

## Related Files

- `React`

## Notes
- Generated: 2025-11-18T07:54:35.214058
- Generator: World's Best Repo Book Generator v1.0.0

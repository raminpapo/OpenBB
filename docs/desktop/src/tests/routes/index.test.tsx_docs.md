# File Documentation: index.test.tsx

## Metadata
- **Path**: `desktop/src/tests/routes/index.test.tsx`
- **Size**: 3,644 bytes
- **Lines**: 110
- **Category**: javascript
- **Extension**: .tsx

---

## Original Source

```tsx
/// <reference types="vitest/globals" />
import { render, screen, waitFor, act } from '@testing-library/react';
import { vi } from 'vitest';
import { invoke } from '@tauri-apps/api/core';
import { listen } from '@tauri-apps/api/event';
import { Route as IndexRoute } from '../../routes/index'; // Import the Route object
import React from 'react'; // Import React for ComponentType

// Mock @tauri-apps/api/core
vi.mock('@tauri-apps/api/core', () => ({
  invoke: vi.fn(),
}));

// Mock @tauri-apps/api/event
vi.mock('@tauri-apps/api/event', () => ({
  listen: vi.fn(() => Promise.resolve(vi.fn())),
}));

describe('Index Route', () => {
  const originalLocation = window.location;
  const IndexComponent = IndexRoute.options.component as React.ComponentType;

  // No global timeout configuration here. Tests should pass within default timeout.

  beforeAll(() => {
    // Mock window.location.href
    Object.defineProperty(window, 'location', {
      writable: true,
      value: { href: '' },
    });
  });

  afterAll(() => {
    // Restore original window.location
    Object.defineProperty(window, 'location', {
      writable: true,
      value: originalLocation,
    });
  });

  beforeEach(() => {
    vi.clearAllMocks();
    window.location.href = ''; // Reset href for each test
    vi.mocked(invoke).mockClear();
    vi.mocked(listen).mockClear();
    localStorage.clear(); // Clear localStorage for each test
  });

  test('displays loading message initially', () => {
    render(<IndexComponent />);
    expect(screen.getByText(/Starting OpenBB Platform/i)).toBeInTheDocument();
    expect(screen.getByText(/Checking installation status.../i)).toBeInTheDocument();
  });

  test('redirects to /environments if installed via event', async () => {
    const unlistenMock = vi.fn();
    vi.mocked(listen).mockImplementation(async (eventName, handler) => {
      if (eventName === 'installation-status') {
        // Trigger the handler immediately within act
        void await act(async () => {
          handler({ payload: true } as any);
          await Promise.resolve(); // flush microtasks if handler is async
        });
      }
      return Promise.resolve(unlistenMock);
    });
    vi.mocked(invoke).mockImplementation((cmd) => {
      if (cmd === 'get_installation_state') {
        return Promise.resolve({ is_installed: true });
      }
      return Promise.resolve(undefined);
    });

    await act(async () => { // Wrap render in act
      render(<IndexComponent />);
      await Promise.resolve(); // Flush microtasks after render
    });

    await waitFor(() => expect(window.location.href).toBe('/environments'));
    expect(vi.mocked(invoke)).not.toHaveBeenCalledWith('get_installation_state');
  });

  test('redirects to /setup if not installed via event', async () => {
    const unlistenMock = vi.fn();
    vi.mocked(listen).mockImplementation(async (eventName, handler) => {
      if (eventName === 'installation-status') {
        await act(async () => {
          handler({ payload: false } as any);
        });
      }
      return Promise.resolve(unlistenMock);
    });
    vi.mocked(invoke).mockImplementation((cmd) => {
      if (cmd === 'get_installation_state') {
        return Promise.resolve({ is_installed: false });
      }
      return Promise.resolve(undefined);
    });

    await act(async () => { // Wrap render in act
      render(<IndexComponent />);
      await Promise.resolve(); // Flush microtasks after render
    });

    await waitFor(() => expect(window.location.href).toBe('/setup'));
    expect(vi.mocked(invoke)).not.toHaveBeenCalledWith('get_installation_state');
  });

});

```



---

## High-Level Overview

This is a **javascript** file named `index.test.tsx`.

This file contains 110 lines of code/text.


---

## Detailed Analysis

This file contains code or text data. See the original source above for full details.


---

## Related Files

The following files may be related based on imports and references:

**Imported Modules**:
- `React`


---

## Performance & Security Notes

No obvious security concerns detected in static analysis.


---

**Generated**: 2025-11-19T02:16:45.111557Z
**Generator**: World's Best Repo Book Generator v1.0

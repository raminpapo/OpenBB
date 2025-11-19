# File Documentation: SearchBar.test.tsx

## Metadata
- **Path**: `desktop/src/tests/components/SearchBar.test.tsx`
- **Size**: 3,323 bytes
- **Lines**: 90
- **Category**: javascript
- **Extension**: .tsx

---

## Original Source

```tsx
import { render, screen, fireEvent } from '@testing-library/react';
import { vi } from 'vitest';
import SearchBar from '../../components/SearchBar';
import React from 'react';

describe('SearchBar', () => {
  const mockSetSearchTerm = vi.fn();
  const mockSetCaseSensitive = vi.fn();
  const mockSetSearchVisible = vi.fn();
  const mockPrevMatch = vi.fn();
  const mockNextMatch = vi.fn();
  const searchInputRef = React.createRef<HTMLInputElement>();

  const defaultProps = {
    searchTerm: '',
    setSearchTerm: mockSetSearchTerm,
    caseSensitive: false,
    setCaseSensitive: mockSetCaseSensitive,
    searchVisible: true,
    setSearchVisible: mockSetSearchVisible,
    prevMatch: mockPrevMatch,
    nextMatch: mockNextMatch,
    currentMatchIndex: 0,
    totalMatches: 0,
    searchInputRef: searchInputRef,
  };

  it('renders nothing when searchVisible is false', () => {
    render(<SearchBar {...defaultProps} searchVisible={false} />);
    expect(screen.queryByPlaceholderText('Search logs...')).toBeNull();
  });

  it('renders the search bar when searchVisible is true', () => {
    render(<SearchBar {...defaultProps} />);
    expect(screen.getByPlaceholderText('Search logs...')).toBeInTheDocument();
  });

  it('calls setSearchTerm on input change', () => {
    render(<SearchBar {...defaultProps} />);
    const input = screen.getByPlaceholderText('Search logs...');
    fireEvent.change(input, { target: { value: 'test' } });
    expect(mockSetSearchTerm).toHaveBeenCalledWith('test');
  });

  it('toggles case sensitivity on button click', () => {
    render(<SearchBar {...defaultProps} />);
    const caseSensitiveButton = screen.getByText('aa');
    fireEvent.click(caseSensitiveButton);
    expect(mockSetCaseSensitive).toHaveBeenCalledWith(true);
  });

  it('calls prevMatch on previous match button click', () => {
    render(<SearchBar {...defaultProps} totalMatches={5} />);
    const prevMatchButton = screen.getByText('↑');
    fireEvent.click(prevMatchButton);
    expect(mockPrevMatch).toHaveBeenCalled();
  });

  it('calls nextMatch on next match button click', () => {
    render(<SearchBar {...defaultProps} totalMatches={5} />);
    const nextMatchButton = screen.getByText('↓');
    fireEvent.click(nextMatchButton);
    expect(mockNextMatch).toHaveBeenCalled();
  });

  it('displays the correct match count', () => {
    render(<SearchBar {...defaultProps} currentMatchIndex={2} totalMatches={5} />);
    expect(screen.getByText('3/5')).toBeInTheDocument();
  });

  it('displays 0/0 when there are no matches', () => {
    render(<SearchBar {...defaultProps} />);
    expect(screen.getByText('0/0')).toBeInTheDocument();
  });

  it('disables prev/next buttons when there are no matches', () => {
    render(<SearchBar {...defaultProps} />);
    expect(screen.getByText('↑').closest('button')).toBeDisabled();
    expect(screen.getByText('↓').closest('button')).toBeDisabled();
  });

  it('calls setSearchVisible and setSearchTerm on close button click', () => {
    render(<SearchBar {...defaultProps} searchTerm="test" />);
    const closeButton = screen.getByRole('button', { name: /close search/i });
    fireEvent.click(closeButton);
    expect(mockSetSearchVisible).toHaveBeenCalledWith(false);
    expect(mockSetSearchTerm).toHaveBeenCalledWith('');
  });
});

```



---

## High-Level Overview

This is a **javascript** file named `SearchBar.test.tsx`.

This file contains 90 lines of code/text.


---

## Detailed Analysis

This file contains code or text data. See the original source above for full details.


---

## Related Files

The following files may be related based on imports and references:

**Imported Modules**:
- `React`
- `SearchBar`


---

## Performance & Security Notes

No obvious security concerns detected in static analysis.


---

**Generated**: 2025-11-19T02:16:45.100501Z
**Generator**: World's Best Repo Book Generator v1.0

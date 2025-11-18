# Documentation: desktop/src/styles/jupyter-logs.css

## File Metadata
- **Path**: `desktop/src/styles/jupyter-logs.css`
- **Size**: 1,816 characters, 74 lines
- **Words**: 218
- **Extension**: .css
- **Classification**: Text file

## Original Source

```css
/* Clean slate - only target critical alignment issues */
body.jupyter-logs-view {
  overflow-y: hidden !important; /* Only vertical scrolling */
  overflow-x: hidden !important; /* No horizontal scrollbar */
}

body.jupyter-logs-view main.flex.flex-col.items-center {
  align-items: flex-start !important;
  padding-left: 0 !important;
  padding-right: 0 !important;
  width: 100% !important;
}

/* Ensure log content containers use full width */
body.jupyter-logs-view main > div {
  max-width: 100% !important;
  width: 100% !important;
}

/* Content section - starts after header with no overlap */
.jupyter-logs-content-section {
  position: relative !important;
  width: 100% !important;
  padding-bottom: 5px !important; /* Add some bottom padding for scrolling */
  padding-top: 5px !important;
  margin: 0 !important;
}

/* Target any potential horizontal scrollbars */
body.jupyter-logs-view div,
body.jupyter-logs-view pre,
body.jupyter-logs-view code {
  overflow-x: hidden !important; /* No horizontal scrolling */
  max-width: 100% !important; /* Prevent content from exceeding container width */
  white-space: pre-wrap !important; /* Ensure text wraps */
  word-break: break-word !important; /* Break long words if needed */
}


.search-container-fixed {
  position: fixed;
  top: 55px;
  left: 18px;
  justify-items: center;
}

/* Make header taller on log pages */
header.logs-page-header {
  min-height: 92px !important;
}

.search-help-container {
  position: fixed;
  top: 65px;
  left: 0;
  right: 0;
  z-index: 50;
  display: flex;
  justify-content: center;
  align-items: flex-start;
}


/* Search highlight styles */
.search-highlight {
  background-color: #ffd90080;
  color: var(--text-primary);
}

.search-highlight-current {
  background-color: #ff8c00;
  color: var(--text-primary);
}

```

## High-Level Overview

Clean slate - only target critical alignment issues */
Ensure log content containers use full width */
Content section - starts after header with no overlap */
Target any potential horizontal scrollbars */
Make header taller on log pages */

## Detailed Structure

Standard text file.

## Key Components

No major components extracted.

## Usage & Examples

See source code for usage details.

## Related Files

No direct file references found.

## Notes
- Generated: 2025-11-18T07:54:35.186823
- Generator: World's Best Repo Book Generator v1.0.0

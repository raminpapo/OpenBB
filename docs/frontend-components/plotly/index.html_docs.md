# Documentation: frontend-components/plotly/index.html

## File Metadata
- **Path**: `frontend-components/plotly/index.html`
- **Size**: 1,476 characters, 41 lines
- **Words**: 157
- **Extension**: .html
- **Classification**: Text file

## Original Source

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <meta name="color-scheme" content="dark light" />
    <title>OpenBB Interactive Charts</title>
    <script>
      if (
        // check if user had saved dark as their
        // theme when accessing page before
        localStorage.theme === "dark" ||
        // or user's requesting dark color
        // scheme through operating system
        (!("theme" in localStorage) &&
          window.matchMedia("(prefers-color-scheme: dark)").matches)
      ) {
        // then if we have access to the document and the element
        // we add the dark class to the html element and
        // store the dark value in the localStorage
        if (document && document.documentElement) {
          document.documentElement.classList.add("dark");
          localStorage.setItem("theme", "dark");
        }
      } else {
        // else if we have access to the document and the element
        // we remove the dark class to the html element and
        // store the value light in the localStorage
        if (document && document.documentElement) {
          document.documentElement.classList.remove("dark");
          localStorage.setItem("theme", "light");
        }
      }
    </script>
  </head>
  <body>
    <div id="root" class="h-full"></div>
    <script type="module" src="/src/main.tsx"></script>
  </body>
</html>

```

## High-Level Overview

check if user had saved dark as their
theme when accessing page before
or user's requesting dark color
scheme through operating system
then if we have access to the document and the element
we add the dark class to the html element and
store the dark value in the localStorage
else if we have access to the document and the element
we remove the dark class to the html element and
store the value light in the localStorage

## Detailed Structure

Standard text file.

## Key Components

No major components extracted.

## Usage & Examples

See source code for usage details.

## Related Files

No direct file references found.

## Notes
- Generated: 2025-11-18T07:54:35.238881
- Generator: World's Best Repo Book Generator v1.0.0

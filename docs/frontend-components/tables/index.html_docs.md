# File Documentation: index.html

## Metadata
- **Path**: `frontend-components/tables/index.html`
- **Size**: 1,407 bytes
- **Lines**: 40
- **Category**: web
- **Extension**: .html

---

## Original Source

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>OpenBB Interactive Tables</title>
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
    <div id="root"></div>
    <script type="module" src="/src/main.tsx"></script>
  </body>
</html>

```



---

## High-Level Overview

This is a **web** file named `index.html`.

This file contains 40 lines of code/text.


---

## Detailed Analysis

This file contains code or text data. See the original source above for full details.


---

## Related Files

The following files may be related based on imports and references:

*No direct imports detected.*


---

## Performance & Security Notes

No obvious security concerns detected in static analysis.


---

**Generated**: 2025-11-19T02:16:46.045462Z
**Generator**: World's Best Repo Book Generator v1.0

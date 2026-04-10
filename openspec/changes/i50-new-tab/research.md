## Codebase Context

The repository is a simple demonstration site currently containing:
- `/home/runner/work/euclide-testbed/euclide-testbed/hello-world.html` — the only existing HTML page, displaying "Hello World" with night sky styling and cursor lamp effect
- `/home/runner/work/euclide-testbed/euclide-testbed/docs/` — documentation directory with architecture.md, testing.md, setup.md, and metrics.md
- `/home/runner/work/euclide-testbed/euclide-testbed/README.md` — project README

The codebase is minimal, with no existing multi-page navigation or tab functionality.

**Confidence:** Confident

## Patterns and Conventions

Based on the existing hello-world.html file:
- **File structure:** Single-file HTML with inline CSS and JavaScript (hello-world.html:1-71)
- **Styling approach:** Inline `<style>` tags within the HTML `<head>` (hello-world.html:7-51)
- **Color palette:** Night sky theme with dark blues (#0a192f, #1e3a5f), purples (#2d1b69), and light text (#fff9e6) (hello-world.html:15, 21)
- **JavaScript placement:** Inline `<script>` tags at end of `<body>` (hello-world.html:56-68)
- **Viewport:** Full viewport height layouts using `min-height: 100vh` and flexbox centering (hello-world.html:11-14)

The repository follows a simple, self-contained approach with no build system, frameworks, or external dependencies.

**Confidence:** Confident

## Integration Points

Given the current single-page structure, integration options include:

1. **Standalone page approach:** Create a separate HTML file with no integration to hello-world.html
2. **Navigation links:** Add navigation elements to both pages to link between them
3. **Tabbed interface:** Implement a tab-switching mechanism within a single or shared navigation structure

Since the product issue states "add new tab", the most likely integration point would be adding navigation elements to existing and new pages, or implementing a client-side tab interface.

**Risk:** The product issue is ambiguous about whether "tab" means a browser tab (separate page) or an in-page tab interface. Design decision required.

**Confidence:** Likely (for navigation approach), Unclear (for specific tab implementation)

## Reusable Assets

From hello-world.html:
- Color scheme variables could be extracted: `#0a192f`, `#1e3a5f`, `#2d1b69` (background), `#fff9e6` (text) (hello-world.html:15, 21)
- CSS patterns for full-viewport centering (hello-world.html:8-18)
- Night sky gradient pattern (hello-world.html:15)
- Text shadow glow effect (hello-world.html:24)
- Cursor lamp overlay technique (hello-world.html:30-50, 56-68)

These patterns can be replicated or adapted for consistency across pages.

**Confidence:** Confident

## Risks and Unknowns

- **Ambiguous requirement:** "add new tab" could mean:
  - A new browser tab (separate HTML page)
  - An in-page tabbed interface
  - A navigation menu item
  → **Confidence:** Unclear — design decision required

- **Navigation pattern:** No existing navigation structure to follow
  → **Confidence:** Unclear — design must choose approach

- **Content for new tab:** Product issue doesn't specify what content the new tab should display
  → **Confidence:** Unclear — design decision required

## Ecosystem Research

<!-- Not applicable: This is a brownfield change extending an existing static HTML site. No new libraries or technologies are being introduced. -->

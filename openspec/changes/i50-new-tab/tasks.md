## 1. About Page Creation

- [ ] 1.1 Create about.html with HTML5 structure _(AC: specs/new-tab/spec.md § Requirement: About page HTML structure)_
  - **Files**: `/home/runner/work/euclide-testbed/euclide-testbed/about.html` (new file)
  - **Action**: Create a new HTML5 file with DOCTYPE, html, head, and body tags. Set title to "About". Include viewport meta tag for basic responsiveness.
  - **Verify**: Open about.html in a browser and verify it loads without errors
  - **Done**: about.html exists with valid HTML5 structure

- [ ] 1.2 Add About heading and content _(AC: specs/new-tab/spec.md § Requirement: About page content)_
  - **Files**: `/home/runner/work/euclide-testbed/euclide-testbed/about.html`
  - **Action**: Add an `<h1>` element with text "About" and a paragraph describing the site (e.g., "This is a demonstration site showcasing multi-page navigation with a beautiful night sky theme.")
  - **Verify**: Open about.html and verify the heading and text are visible
  - **Done**: About page displays "About" heading with descriptive content

- [ ] 1.3 Apply night sky theme styling to About page _(AC: specs/new-tab/spec.md § Requirement: Visual consistency with existing page)_
  - **Files**: `/home/runner/work/euclide-testbed/euclide-testbed/about.html`
  - **Action**: Add inline CSS in `<style>` tag matching hello-world.html: gradient background with colors #0a192f, #1e3a5f, #2d1b69; text color #fff9e6; full viewport height with flexbox centering; text shadow glow effect
  - **Verify**: Open about.html and compare visually with hello-world.html for color consistency
  - **Done**: About page uses the same night sky color scheme and styling as hello-world.html

- [ ] 1.4 Add cursor lamp effect to About page _(AC: specs/new-tab/spec.md § Requirement: Cursor lamp effect)_
  - **Files**: `/home/runner/work/euclide-testbed/euclide-testbed/about.html`
  - **Action**: Copy the lamp overlay CSS (hello-world.html:30-50) and JavaScript (hello-world.html:56-68) to about.html. Include the lamp-overlay div element.
  - **Verify**: Open about.html and move the mouse to see the cursor lamp effect
  - **Done**: Cursor lamp effect works on about.html

## 2. Navigation Implementation

- [ ] 2.1 Add navigation to hello-world.html _(AC: specs/new-tab/spec.md § Requirement: Navigation on both pages)_
  - **Files**: `/home/runner/work/euclide-testbed/euclide-testbed/hello-world.html`
  - **Action**: Add a `<nav>` element with links to "Home" (hello-world.html) and "About" (about.html). Style the nav with the night sky theme: position at top, use background rgba with transparency, light text color, horizontal layout with padding.
  - **Verify**: Open hello-world.html and click the "About" link to navigate to about.html
  - **Done**: Navigation bar appears on hello-world.html with working links

- [ ] 2.2 Add navigation to about.html _(AC: specs/new-tab/spec.md § Requirement: Navigation on both pages)_
  - **Files**: `/home/runner/work/euclide-testbed/euclide-testbed/about.html`
  - **Action**: Add the same `<nav>` element and styling from hello-world.html to about.html
  - **Verify**: Open about.html and click the "Home" link to navigate back to hello-world.html
  - **Done**: Navigation bar appears on about.html with working links

## 3. Documentation and design

- [ ] 3.1 Update README.md _(AC: specs/new-tab/spec.md § Scenario: User navigates to the About page)_
  - **Files**: `/home/runner/work/euclide-testbed/euclide-testbed/README.md`
  - **Action**: Update the description to mention both pages. Update the Quickstart section to mention opening either hello-world.html or about.html in a browser.
  - **Verify**: Read README.md to confirm it accurately describes the multi-page structure
  - **Done**: README reflects the addition of the About page and navigation

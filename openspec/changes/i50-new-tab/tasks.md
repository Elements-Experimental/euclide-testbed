## 1. Create About Page

- [ ] 1.1 Create about.html with HTML5 structure _(AC: specs/new-tab-page/spec.md § Requirement: HTML page structure)_
  - **Files**: `about.html` (new file in repository root)
  - **Action**: Create about.html with DOCTYPE, html, head, and body tags. Include meta charset and viewport tags in head. Set page title to "About - euclide-testbed".
  - **Verify**: Open about.html in a browser and verify it loads without errors
  - **Done**: Valid HTML5 structure is in place

- [ ] 1.2 Add night sky color scheme styling _(AC: specs/new-tab-page/spec.md § Requirement: Night sky color theme consistency)_
  - **Files**: `about.html`
  - **Action**: Add inline CSS in style tag using the same color palette as hello-world.html: background gradient with #0a192f, #1e3a5f, #2d1b69; text color #fff9e6. Apply flexbox layout (min-height: 100vh, centered content).
  - **Verify**: Open about.html and verify colors match hello-world.html
  - **Done**: Page displays with night sky colors matching hello-world.html

- [ ] 1.3 Add about content _(AC: specs/new-tab-page/spec.md § Requirement: About content)_
  - **Files**: `about.html`
  - **Action**: Add content describing the euclide-testbed project. Include a heading and paragraph(s) explaining that this is a demonstration repository.
  - **Verify**: Open about.html and verify content is displayed
  - **Done**: About content is visible on the page

## 2. Add Navigation Links

- [ ] 2.1 Add navigation link from hello-world.html to about.html _(AC: specs/new-tab-page/spec.md § Requirement: Navigation to and from hello world page)_
  - **Files**: `hello-world.html`
  - **Action**: Add a navigation link to about.html. Style it to match the night sky theme with color #fff9e6 and hover effects. Position it appropriately on the page (e.g., top-right or bottom).
  - **Verify**: Open hello-world.html and click the link to verify it navigates to about.html
  - **Done**: Link from hello-world.html to about.html works

- [ ] 2.2 Add navigation link from about.html to hello-world.html _(AC: specs/new-tab-page/spec.md § Requirement: Navigation to and from hello world page)_
  - **Files**: `about.html`
  - **Action**: Add a navigation link back to hello-world.html. Style it consistently with the link in hello-world.html.
  - **Verify**: Open about.html and click the link to verify it navigates to hello-world.html
  - **Done**: Link from about.html to hello-world.html works

## 3. Documentation and design

- [ ] 3.1 Update README.md to reference the new page _(AC: specs/new-tab-page/spec.md § Scenario: User opens the about page in a browser)_
  - **Files**: `README.md`
  - **Action**: Update README.md to mention about.html alongside hello-world.html in the Quickstart section or add a new section listing available pages.
  - **Verify**: Read README.md to confirm both pages are documented
  - **Done**: README.md references both HTML pages

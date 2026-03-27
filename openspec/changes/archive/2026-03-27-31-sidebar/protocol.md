## Setup

- [ ] Open `hello-world.html` in a web browser (Chrome, Firefox, or Safari)

## 1. Sidebar Visibility and Structure

### Step 1.1 — Sidebar is present and positioned on the left <!-- HUMAN CHECKPOINT -->

- [ ] Verify that a sidebar is visible on the left side of the page
- **Expected**: The sidebar should be visible on the left edge of the page with a dark, semi-transparent background
_(AC: specs/sidebar/spec.md § Scenario: User opens the page and sees the sidebar)_

### Step 1.2 — Sidebar contains "About" heading and content <!-- HUMAN CHECKPOINT -->

- [ ] Check that the sidebar contains an "About" heading
- [ ] Read the content below the heading
- **Expected**: The sidebar should contain an "About" heading (styled with light text) and a paragraph explaining that this is a testbed project for demonstrating web development concepts and the OpenSpec workflow
_(AC: specs/sidebar/spec.md § Scenario: About field contains project description)_

## 2. Sidebar Styling

### Step 2.1 — Sidebar width is 250px <!-- HUMAN CHECKPOINT -->

- [ ] Use browser developer tools (F12) to inspect the `#sidebar` element
- [ ] Check the computed width property
- **Expected**: The sidebar width should be exactly 250px
_(AC: specs/sidebar/spec.md § Requirement: Sidebar width)_

### Step 2.2 — Sidebar has night sky theme colors <!-- HUMAN CHECKPOINT -->

- [ ] Inspect the sidebar's background color using developer tools
- **Expected**: The sidebar background should use `rgba(10, 10, 40, 0.7)` or similar dark blue/purple color with opacity ≤ 0.8, matching the night sky aesthetic
_(AC: specs/sidebar/spec.md § Scenario: Sidebar displays with night sky styling)_

## 3. Layout and Main Content

### Step 3.1 — Main content remains visible alongside sidebar <!-- HUMAN CHECKPOINT -->

- [ ] Verify that the "Hello World" heading is still visible to the right of the sidebar
- [ ] Check that the heading appears centered in its available space (not the entire viewport)
- **Expected**: The "Hello World" heading should be visible and properly positioned in the main content area to the right of the sidebar, centered within that area
_(AC: specs/sidebar/spec.md § Scenario: Main content remains visible alongside sidebar)_

### Step 3.2 — Layout uses flexbox structure <!-- HUMAN CHECKPOINT -->

- [ ] Use developer tools to inspect the body element
- [ ] Check the display property
- **Expected**: The body should have `display: flex`, creating a horizontal layout with the sidebar and main content area
_(AC: specs/sidebar/spec.md § Requirement: Layout adjustment)_

## 4. Cursor Lamp Effect

### Step 4.1 — Cursor lamp effect works over sidebar <!-- HUMAN CHECKPOINT -->

- [ ] Move the mouse cursor over the sidebar area
- **Expected**: A subtle light effect should follow the cursor, illuminating the area beneath it
_(AC: specs/sidebar/spec.md § Scenario: Cursor lamp effect works with sidebar)_

### Step 4.2 — Cursor lamp effect works over main content <!-- HUMAN CHECKPOINT -->

- [ ] Move the mouse cursor over the main content area (where "Hello World" is displayed)
- **Expected**: The cursor lamp effect should continue to work, illuminating areas under the cursor just as it did before the sidebar was added
_(AC: specs/sidebar/spec.md § Scenario: Cursor lamp effect works with sidebar)_

### Step 4.3 — Cursor lamp overlay has correct z-index <!-- HUMAN CHECKPOINT -->

- [ ] Use developer tools to inspect the `#lamp-overlay` element
- [ ] Check the z-index property
- **Expected**: The lamp overlay should have `z-index: 2` and cover the entire viewport while remaining non-interactive (`pointer-events: none`)
_(AC: specs/sidebar/spec.md § Requirement: Cursor lamp effect preservation)_

## 5. Cleanup

- [ ] Close the browser tab

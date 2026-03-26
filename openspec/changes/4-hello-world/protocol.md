## Setup

- [ ] Ensure you have a modern web browser (Chrome, Firefox, Safari, or Edge)
- [ ] Navigate to the repository root directory

## 1. Basic Page Rendering

### Step 1.1 — Open page directly in browser <!-- HUMAN CHECKPOINT -->

- [ ] Double-click `index.html` in the file explorer, or drag it into a browser window
- **Expected**: The page opens and displays content without errors
_(AC: specs/hello-world/spec.md § Scenario: Page works without dependencies)_

### Step 1.2 — Verify Hello World text <!-- HUMAN CHECKPOINT -->

- [ ] View the page content
- **Expected**: The exact text "Hello World" (no comma, correct capitalization) is displayed prominently on the page
_(AC: specs/hello-world/spec.md § Scenario: User opens the hello world page)_

## 2. Visual Styling

### Step 2.1 — Verify warm color palette <!-- HUMAN CHECKPOINT -->

- [ ] Observe the page background colors
- **Expected**: The background uses warm colors (oranges, reds, yellows) visible as a gradient from orange to yellow tones
_(AC: specs/hello-world/spec.md § Scenario: Page uses warm color palette)_

### Step 2.2 — Verify text readability <!-- HUMAN CHECKPOINT -->

- [ ] Check the "Hello World" text against the background
- **Expected**: The text is legible with good contrast (white text with a subtle shadow)
_(AC: specs/hello-world/spec.md § Requirement: Warm Color Scheme)_

### Step 2.3 — Verify centered layout <!-- HUMAN CHECKPOINT -->

- [ ] Observe the position of the "Hello World" text on the page
- **Expected**: The text is centered both horizontally and vertically in the browser viewport
_(AC: specs/hello-world/spec.md § Scenario: Content is centered on the page)_

## 3. HTML Structure

### Step 3.1 — Verify HTML validity <!-- HUMAN CHECKPOINT -->

- [ ] Right-click the page and select "View Page Source" (or Ctrl/Cmd+U)
- **Expected**: The HTML has proper structure with DOCTYPE, html, head (with title), and body tags
_(AC: specs/hello-world/spec.md § Requirement: Self-Contained HTML)_

### Step 3.2 — Verify self-containment <!-- HUMAN CHECKPOINT -->

- [ ] Check the page source for external file references
- **Expected**: All styles are inline (in a `<style>` tag), no external CSS or JS files are referenced
_(AC: specs/hello-world/spec.md § Scenario: Page works without dependencies)_

## 4. Cross-Browser Verification

### Step 4.1 — Test in different browsers <!-- HUMAN CHECKPOINT -->

- [ ] If possible, open `index.html` in at least one additional browser
- **Expected**: The page renders consistently with the same warm colors and centered text
_(AC: specs/hello-world/spec.md § Scenario: Page works without dependencies)_

## 5. Cleanup

- [ ] Close all browser windows used for testing

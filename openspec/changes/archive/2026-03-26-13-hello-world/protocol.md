## Setup

- [ ] Ensure you have a web browser installed (Chrome, Firefox, Safari, or Edge)

## 1. HTML Structure Validation

### Step 1.1 — Verify HTML file exists <!-- HUMAN CHECKPOINT -->

- [ ] Navigate to the `src/` directory in the repository
- [ ] Confirm that `index.html` file exists at `src/index.html`
- **Expected**: The file `src/index.html` exists in the repository
_(AC: specs/hello-world/spec.md § Scenario: HTML structure is valid)_

### Step 1.2 — Inspect HTML structure <!-- HUMAN CHECKPOINT -->

- [ ] Open `src/index.html` in a text editor
- [ ] Verify the file contains:
  - `<!DOCTYPE html>` declaration at the top
  - `<html>` opening and closing tags
  - `<head>` section with `<meta charset="UTF-8">` and `<title>Hello World</title>`
  - `<body>` section with "Hello World" text content
- **Expected**: All required HTML5 structural elements are present with correct metadata
_(AC: specs/hello-world/spec.md § Scenario: HTML structure is valid)_

## 2. Browser Display Verification

### Step 2.1 — Open HTML file in browser <!-- HUMAN CHECKPOINT -->

- [ ] Open `src/index.html` in a web browser (double-click the file or use File > Open in your browser)
- [ ] Observe the page loads without errors
- **Expected**: The page loads successfully with no console errors or loading failures
_(AC: specs/hello-world/spec.md § Scenario: User opens the HTML file in a browser)_

### Step 2.2 — Verify displayed content <!-- HUMAN CHECKPOINT -->

- [ ] Look at the rendered page content in the browser
- [ ] Confirm the visible text in the body is exactly "Hello World"
- [ ] Verify the browser tab/window title shows "Hello World"
- **Expected**: The page body displays exactly "Hello World" with no additional UI elements or decorations
_(AC: specs/hello-world/spec.md § Scenario: Page displays correct content)_

## 3. Cross-Browser Compatibility (Optional)

### Step 3.1 — Test in multiple browsers <!-- HUMAN CHECKPOINT -->

- [ ] Open `src/index.html` in at least one additional browser (if available)
- [ ] Verify the page displays "Hello World" correctly
- **Expected**: The page displays consistently across different browsers

## 4. Cleanup

- [ ] Close all browser windows/tabs used for testing

## Setup

- [ ] Open a modern web browser (Chrome, Firefox, Safari, or Edge)
- [ ] Navigate to or open the hello-world.html file

## 1. Cursor Lamp Visual Effect

### Step 1.1 — Verify lamp appears and follows cursor <!-- HUMAN CHECKPOINT -->

- [ ] Move your cursor slowly across different areas of the page
- **Expected**: A radial light gradient should follow your cursor position in real-time, creating a "spotlight" or "lamp" effect
_(AC: specs/cursor-lamp/spec.md § Scenario: User moves cursor across the page)_

### Step 1.2 — Check visual integration with night sky theme <!-- HUMAN CHECKPOINT -->

- [ ] Observe the lamp effect as it moves across the night sky background
- **Expected**: The lamp's center should be noticeably brighter than the surrounding area, and the light should fade smoothly into the existing dark blue/purple background colors without harsh transitions
_(AC: specs/cursor-lamp/spec.md § Scenario: Lamp effect integrates with background)_

### Step 1.3 — Test lamp radius and intensity <!-- HUMAN CHECKPOINT -->

- [ ] Move the cursor to various positions and observe the size of the illuminated area
- **Expected**: The lamp should illuminate a reasonable area (approximately 200-400px diameter) around the cursor with a smooth gradient falloff

## 2. Interaction and Functionality

### Step 2.1 — Verify non-interference with content <!-- HUMAN CHECKPOINT -->

- [ ] Try to select the "Hello World" text with your cursor
- [ ] Right-click on the page to open the context menu
- **Expected**: Text selection should work normally, and all mouse interactions should function as expected without the lamp overlay blocking them
_(AC: specs/cursor-lamp/spec.md § Scenario: Lamp does not block content)_

### Step 2.2 — Test cursor entering and leaving page <!-- HUMAN CHECKPOINT -->

- [ ] Move your cursor off the page (outside the browser window content area)
- [ ] Move your cursor back onto the page from different edges (top, bottom, left, right)
- **Expected**: The lamp effect should disappear when the cursor leaves and reappear smoothly at the cursor position when it re-enters the page
_(AC: specs/cursor-lamp/spec.md § Scenario: Cursor leaves and re-enters page)_

### Step 2.3 — Test initial page load <!-- HUMAN CHECKPOINT -->

- [ ] Refresh the page (F5 or Ctrl+R / Cmd+R)
- [ ] As soon as the page loads, move your cursor
- **Expected**: The lamp effect should be immediately functional after page load, appearing as soon as the cursor moves
_(AC: specs/cursor-lamp/spec.md § Scenario: Page loads with lamp functionality)_

## 3. Performance and Smoothness

### Step 3.1 — Test smooth tracking <!-- HUMAN CHECKPOINT -->

- [ ] Move your cursor rapidly in circles and across the page
- [ ] Move your cursor slowly in straight lines
- **Expected**: The lamp should track cursor movement smoothly without lag, jitter, or visible delays in both fast and slow movements
_(AC: specs/cursor-lamp/spec.md § Requirement: Cursor position tracking)_

## 4. Cleanup

- [ ] Close the browser tab/window (no cleanup required for this static page)

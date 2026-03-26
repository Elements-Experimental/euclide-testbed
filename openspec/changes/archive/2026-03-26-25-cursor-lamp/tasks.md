## 1. HTML Structure

- [x] 1.1 Add overlay div element to hello-world.html with appropriate id/class for lamp effect _(AC: specs/cursor-lamp/spec.md § Requirement: Non-intrusive overlay)_

## 2. CSS Styling

- [x] 2.1 Add CSS for lamp overlay with pointer-events: none to avoid blocking interactions _(AC: specs/cursor-lamp/spec.md § Requirement: Non-intrusive overlay)_
- [x] 2.2 Implement radial-gradient with CSS custom properties for dynamic positioning _(AC: specs/cursor-lamp/spec.md § Requirement: Radial light effect)_
- [x] 2.3 Configure gradient colors to integrate with existing night sky theme _(AC: specs/cursor-lamp/spec.md § Requirement: Visual integration with night sky theme)_

## 3. JavaScript Implementation

- [x] 3.1 Add mousemove event listener to track cursor position _(AC: specs/cursor-lamp/spec.md § Requirement: Cursor position tracking)_
- [x] 3.2 Update CSS custom properties (--mouse-x, --mouse-y) based on cursor position _(AC: specs/cursor-lamp/spec.md § Scenario: User moves cursor across the page)_
- [x] 3.3 Ensure smooth real-time tracking of cursor movement _(AC: specs/cursor-lamp/spec.md § Scenario: User moves cursor across the page)_

## 4. Testing and Verification

- [x] 4.1 Verify lamp effect follows cursor smoothly across entire page _(AC: specs/cursor-lamp/spec.md § Scenario: User moves cursor across the page)_
- [x] 4.2 Test that lamp integrates visually with night sky background _(AC: specs/cursor-lamp/spec.md § Scenario: Lamp effect integrates with background)_
- [x] 4.3 Confirm text selection and other interactions work properly _(AC: specs/cursor-lamp/spec.md § Scenario: Lamp does not block content)_
- [x] 4.4 Test cursor leaving and re-entering page boundary _(AC: specs/cursor-lamp/spec.md § Scenario: Cursor leaves and re-enters page)_

## 5. Documentation and design

- [x] 5.1 Relevant docs in `docs/` updated (API, data model, or feature docs as applicable)

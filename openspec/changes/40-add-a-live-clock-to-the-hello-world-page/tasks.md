## 1. Clock HTML Structure

- [ ] 1.1 Add clock div element to hello-world.html _(AC: specs/live-clock/spec.md § Requirement: Clock element display)_
  - **Files**: hello-world.html
  - **Action**: Add a `<div id="clock"></div>` element in the body after the `<h1>Hello World</h1>` element (around line 55)
  - **Verify**: Open hello-world.html in browser and inspect DOM to confirm clock div exists
  - **Done**: Clock div element is present in the DOM positioned after the h1 element

## 2. Clock Styling

- [ ] 2.1 Add CSS styling for clock element _(AC: specs/live-clock/spec.md § Requirement: Visual integration with night sky theme)_
  - **Files**: hello-world.html
  - **Action**: Add CSS rules in the existing `<style>` tag (around line 7-51) for `#clock` selector with: light color (white/light yellow), text-shadow for glow effect, monospace font-family, center text-align, appropriate font-size (smaller than h1), and z-index: 1 for positioning above lamp overlay
  - **Verify**: Open hello-world.html in browser and verify clock element has proper styling (light colored, glowing text effect, monospace font)
  - **Done**: Clock is styled consistently with night sky theme and "Hello World" heading

- [ ] 2.2 Position clock below main heading _(AC: specs/live-clock/spec.md § Requirement: Non-obstructive positioning)_
  - **Files**: hello-world.html
  - **Action**: Add CSS positioning properties to `#clock` to place it below the h1 with appropriate margin-top for spacing
  - **Verify**: Open hello-world.html in browser and confirm clock appears centered below "Hello World" with proper spacing
  - **Done**: Clock is positioned below heading without obstructing any existing content

## 3. Clock Functionality

- [ ] 3.1 Implement time formatting function _(AC: specs/live-clock/spec.md § Requirement: Clock element display)_
  - **Files**: hello-world.html
  - **Action**: Add JavaScript in the existing `<script>` tag (around line 56-68) to create a function that formats current time as HH:MM:SS with leading zeros using `new Date()`, `getHours()`, `getMinutes()`, `getSeconds()`, and `padStart(2, '0')`
  - **Verify**: Add console.log call to the function and verify in browser console that it outputs properly formatted time string
  - **Done**: Function returns time string in HH:MM:SS format with leading zeros

- [ ] 3.2 Implement clock update mechanism _(AC: specs/live-clock/spec.md § Requirement: Automatic time updates)_
  - **Files**: hello-world.html
  - **Action**: Add JavaScript to select the clock element, create an update function that sets clock's textContent to formatted current time, call update function immediately on page load, and use `setInterval` to call update function every 1000ms
  - **Verify**: Open hello-world.html in browser and observe that clock displays current time and updates every second
  - **Done**: Clock displays current time and automatically updates every second

## 4. Integration Testing

- [ ] 4.1 Verify clock works with existing features _(AC: specs/live-clock/spec.md § Scenario: Clock does not interfere with cursor lamp)_
  - **Files**: hello-world.html
  - **Action**: Test the page to ensure clock works alongside cursor lamp effect, heading remains visible, and all three elements (heading, clock, lamp) function correctly together
  - **Verify**: Open hello-world.html, move cursor to verify lamp effect works, observe clock updates, confirm no visual or functional conflicts
  - **Done**: Clock, heading, and cursor lamp all work together without interference

## 5. Documentation and design

- [ ] 5.1 Relevant docs in `docs/` updated (API, data model, or feature docs as applicable)
  - **Files**: README.md
  - **Action**: Update README.md to mention the live clock feature in the description or quickstart section
  - **Verify**: Read README.md and confirm live clock is documented
  - **Done**: Documentation reflects the live clock feature

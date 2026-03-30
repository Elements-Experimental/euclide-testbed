## 1. HTML Structure

- [ ] 1.1 Add clock div element to the page _(AC: specs/live-clock/spec.md § Requirement: Clock element display)_
  - **Files**: `hello-world.html`
  - **Action**: Add `<div id="clock"></div>` as a sibling to the `<h1>` heading within the `<body>` tag, after the lamp overlay div
  - **Verify**: Open hello-world.html in browser; inspect DOM to confirm clock div exists with id="clock"
  - **Done**: Clock div element is present in the HTML structure

## 2. CSS Styling

- [ ] 2.1 Add clock positioning and layout styles _(AC: specs/live-clock/spec.md § Requirement: Non-interfering positioning)_
  - **Files**: `hello-world.html`
  - **Action**: Within the `<style>` tag, add a `#clock` rule with `position: fixed; top: 20px; right: 20px; z-index: 1;` to position the clock in the top-right corner above the lamp overlay
  - **Verify**: Open hello-world.html in browser; clock should appear in top-right corner without overlapping heading
  - **Done**: Clock is positioned in the top-right corner and does not interfere with other elements

- [ ] 2.2 Add clock typography and color styles _(AC: specs/live-clock/spec.md § Requirement: Visual style consistency)_
  - **Files**: `hello-world.html`
  - **Action**: In the `#clock` CSS rule, add `color: #fff9e6; font-family: 'Courier New', Courier, monospace; font-size: 1.5rem; text-shadow: 0 0 20px rgba(255, 249, 230, 0.5);` to match the page aesthetic with monospace font
  - **Verify**: Open hello-world.html in browser; clock text should have light cream color, glow effect, and monospace font
  - **Done**: Clock styling is consistent with the night sky theme and uses monospace font

## 3. JavaScript Clock Logic

- [ ] 3.1 Add clock update function _(AC: specs/live-clock/spec.md § Requirement: Automatic time updates)_
  - **Files**: `hello-world.html`
  - **Action**: Within the `<script>` tag, add a `updateClock()` function that: (1) creates a new Date object, (2) extracts hours/minutes/seconds with `padStart(2, '0')` for leading zeros, (3) formats as "HH:MM:SS", (4) updates the textContent of the clock element
  - **Verify**: Add `console.log` to the function; open browser console and verify function outputs correctly formatted time
  - **Done**: Clock update function correctly formats time as HH:MM:SS with leading zeros

- [ ] 3.2 Initialize clock with immediate update and interval _(AC: specs/live-clock/spec.md § Requirement: Clock element display, Automatic time updates)_
  - **Files**: `hello-world.html`
  - **Action**: In the `<script>` tag after the updateClock function, add: (1) call `updateClock()` immediately to display initial time, (2) call `setInterval(updateClock, 1000)` to update every second
  - **Verify**: Open hello-world.html in browser; clock should display current time immediately and update every second
  - **Done**: Clock displays on page load and updates every second automatically

## 4. Documentation and Design

- [ ] 4.1 Document the live clock feature _(AC: Implementation complete)_
  - **Files**: `README.md` (if exists at repository root)
  - **Action**: If README.md exists, add a brief mention of the live clock feature under the hello-world page description; if no README exists, skip this task
  - **Verify**: Check if README.md exists; if it does, verify live clock is mentioned
  - **Done**: Documentation reflects the live clock feature (or confirmed README doesn't exist)

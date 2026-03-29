## Context

The hello-world.html page currently exists as a single HTML file with:
- A "Hello World" heading centered on the page (hello-world.html:55)
- A night sky themed gradient background (hello-world.html:15)
- An interactive cursor lamp effect that follows mouse movement (hello-world.html:30-67)
- All styling is inline CSS within a `<style>` tag
- All JavaScript is inline within a `<script>` tag

## Goals / Non-Goals

**Goals:**
- Add a live clock that displays current time in HH:MM:SS format
- Clock updates automatically every second
- Clock styling integrates with existing night sky theme
- Clock positioned to not obstruct "Hello World" heading or interfere with cursor lamp
- Implementation uses vanilla JavaScript (consistent with existing code)
- All code remains in single HTML file (no external files)

**Non-Goals:**
- Date display (only time)
- 12-hour format or AM/PM indicators
- Timezone selection or conversion
- Clock customization controls (pause, format switching)
- Analog clock face
- Multiple clock instances

## Decisions

### Clock Positioning
Place the clock below the "Hello World" heading. This avoids interfering with the centered main heading while keeping both elements visible together. The clock will also be centered horizontally for visual balance.

### Time Format
Use 24-hour HH:MM:SS format (e.g., "14:35:27"). This is unambiguous and internationally recognized. The format includes seconds to demonstrate the live updating behavior clearly.

### Update Mechanism
Use `setInterval` with 1000ms (1 second) interval to update the clock. This is the standard approach for real-time clock displays and provides smooth second-by-second updates.

### Styling Approach
Style the clock to complement the night sky theme:
- Use light colors matching the "Hello World" text (white or light yellow)
- Apply similar text shadow for glowing effect
- Use a monospace font for the time display to ensure digits don't shift as they change
- Size smaller than the main heading to maintain visual hierarchy

### DOM Structure
Add a single `<div id="clock">` element after the `<h1>` in the HTML body. The JavaScript will select this element and update its `textContent` every second.

### ADR Links
No architectural decisions requiring ADR documentation.

## Risks / Trade-offs

**Risk**: Clock may drift slightly over time if browser tab is backgrounded (browsers throttle `setInterval` in inactive tabs).
**Mitigation**: Using `new Date()` on each update ensures we always show current system time, even if the interval timing drifts.

**Trade-off**: Adding JavaScript increases page complexity, but the implementation is minimal and follows patterns already established by the cursor lamp effect.

## External references (if applicable)

None. Implementation uses standard Web APIs (Date, setInterval, DOM manipulation).

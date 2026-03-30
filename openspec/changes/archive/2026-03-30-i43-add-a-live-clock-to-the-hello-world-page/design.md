## Context

The hello-world.html page currently displays:
- A centered "Hello World" heading (4rem, #fff9e6 color with glow)
- A night sky gradient background (blues and purples)
- A cursor lamp overlay effect that follows the mouse

The page uses a single HTML file with embedded CSS and JavaScript, following a minimal dependency approach. The clock will be added as a new element that coexists with these existing features without external libraries.

## Goals / Non-Goals

**Goals:**
- Add a live clock element displaying HH:MM:SS format that updates every second
- Position the clock to avoid interfering with the centered heading or cursor lamp
- Maintain visual consistency with the night sky theme and existing typography
- Keep the implementation lightweight using vanilla JavaScript

**Non-Goals:**
- Timezone selection or multiple timezone displays
- Date display
- 12-hour format or AM/PM indicators
- Analog clock visualization
- Clock customization UI
- Mobile-specific optimizations

## Decisions

### Clock Positioning
Position the clock in the **top-right corner** using fixed positioning.

**Rationale:**
- Top-right is conventional for clocks in UIs (status bars, dashboards)
- Fixed positioning ensures visibility regardless of scroll state
- Corner placement keeps it away from the centered heading
- Adequate padding from edges prevents overlap with browser chrome

**Implementation:** `position: fixed; top: 20px; right: 20px;` with `z-index: 1` to stay above the lamp overlay.

### Font Choice
Use **monospace font family** for the clock display.

**Rationale:**
- Monospace fonts are conventional for digital time displays
- Fixed-width characters prevent layout shift when digits change (e.g., 1 vs 8)
- Creates visual distinction from the serif/sans-serif heading, signaling different content type
- Common monospace stacks: `'Courier New', Courier, monospace` provide good cross-browser support

**Implementation:** `font-family: 'Courier New', Courier, monospace;`

### Font Size
Set clock font size to **1.5rem**.

**Rationale:**
- Heading is 4rem — clock should be significantly smaller to avoid competing for attention
- 1.5rem is readable but unobtrusive
- Maintains visual hierarchy: heading (primary) > clock (secondary information)
- Proportional to typical viewport sizes

### Visual Effects
Apply the **same text color and glow effect** as the heading.

**Rationale:**
- Color consistency: `#fff9e6` matches the light accent used throughout
- Glow effect: `text-shadow: 0 0 20px rgba(255, 249, 230, 0.5)` creates cohesion with heading
- Maintains the atmospheric night sky aesthetic
- Ensures readability against the dark gradient background

### Time Update Implementation
Use `setInterval(updateClock, 1000)` with an immediate initial call.

**Rationale:**
- `setInterval` is the standard approach for periodic updates in JavaScript
- 1000ms interval matches the one-second update requirement
- Initial call ensures clock displays immediately on page load (no one-second delay)
- Function approach (`updateClock`) keeps code organized and testable

**Implementation:**
```javascript
function updateClock() {
  const now = new Date();
  const hours = String(now.getHours()).padStart(2, '0');
  const minutes = String(now.getMinutes()).padStart(2, '0');
  const seconds = String(now.getSeconds()).padStart(2, '0');
  document.getElementById('clock').textContent = `${hours}:${minutes}:${seconds}`;
}
updateClock(); // Initial call
setInterval(updateClock, 1000);
```

### HTML Structure
Add a single `<div id="clock"></div>` element as a sibling to the heading.

**Rationale:**
- Minimal DOM addition follows existing pattern
- ID selector enables efficient JavaScript updates
- Div is semantically neutral — clock is presentational, not structural content
- Placement within body but separate from heading preserves layout independence

### ADR Links

No architectural decisions requiring ADR documentation. This is a localized enhancement using established patterns.

## Risks / Trade-offs

**Timer accuracy:**
- `setInterval` may drift over time due to JavaScript event loop delays
- For a UI clock, this is acceptable — clock will self-correct on each update from system time
- Trade-off: Simplicity vs. perfect timer precision (simplicity chosen)

**Fixed positioning on small screens:**
- On very small viewports, top-right clock might overlap heading if heading grows
- Current design assumes typical desktop/tablet viewport sizes
- Trade-off: Responsive complexity vs. stated scope (mobile optimization out of scope per issue)

**No accessibility considerations:**
- Clock has no ARIA labels or screen reader support
- Trade-off: Accessibility vs. stated scope (not in acceptance criteria; can be added later)

**Browser local time only:**
- Clock shows whatever timezone/time the user's system is set to
- No server sync means time could be incorrect if system time is wrong
- Trade-off: Simplicity vs. accuracy (simplicity chosen per requirements)

## External references

None. This is a self-contained enhancement to an existing HTML file with no external design assets or API schemas.

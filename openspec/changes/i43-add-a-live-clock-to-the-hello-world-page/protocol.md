## Setup

- [ ] Open a modern web browser (Chrome, Firefox, Safari, or Edge)
- [ ] Navigate to or open the hello-world.html file

## 1. Clock Display and Functionality

### Step 1.1 — Verify clock is visible and positioned correctly <!-- HUMAN CHECKPOINT -->

- **Built**: A live clock element positioned in the top-right corner of the page
- [ ] Load the hello-world.html page and locate the clock in the top-right corner
- **Expected**: The clock should be visible in the top-right corner (20px from top and right edges), displaying time in HH:MM:SS format (e.g., "14:23:47")

### Step 1.2 — Verify clock updates every second <!-- HUMAN CHECKPOINT -->

- **Built**: JavaScript that updates the clock display every second using setInterval
- [ ] Watch the clock for at least 10 seconds
- **Expected**: The seconds should increment by one every second, and minutes/hours should roll over correctly (e.g., 59 seconds → 00 seconds, minute increments)

### Step 1.3 — Verify time format is correct <!-- HUMAN CHECKPOINT -->

- **Built**: Time formatting using padStart to ensure two-digit display
- [ ] Check that all time components (hours, minutes, seconds) are displayed with two digits
- **Expected**: Single-digit values should have a leading zero (e.g., "09:05:03" not "9:5:3")

## 2. Visual Style and Integration

### Step 2.1 — Check clock styling matches page aesthetic <!-- HUMAN CHECKPOINT -->

- **Built**: CSS styling for the clock using the same color palette and glow effects as the heading
- [ ] Observe the clock's color, font, and glow effect
- **Expected**: The clock should use a light cream color (#fff9e6) with a subtle glow effect, consistent with the "Hello World" heading but with a monospace font for better readability

### Step 2.2 — Verify clock doesn't interfere with existing elements <!-- HUMAN CHECKPOINT -->

- **Built**: Clock positioned with z-index: 2 and fixed positioning to stay out of the way
- [ ] Move your cursor across the entire page, including over the clock area
- [ ] Check that the "Hello World" heading remains centered and visible
- **Expected**: The lamp overlay should work normally, the heading should remain centered, and the clock should stay visible above the lamp overlay without blocking any interactive elements

### Step 2.3 — Test clock visibility with lamp overlay <!-- HUMAN CHECKPOINT -->

- **Built**: Clock z-index set higher than lamp overlay to ensure visibility
- [ ] Move your cursor directly under and around the clock area
- **Expected**: The clock should remain clearly visible and readable even when the lamp overlay is directly behind it

## 3. Responsiveness and Edge Cases

### Step 3.1 — Test page refresh <!-- HUMAN CHECKPOINT -->

- **Built**: updateClock() is called immediately on page load before setInterval starts
- [ ] Refresh the page (F5 or Ctrl+R / Cmd+R)
- **Expected**: The clock should display the correct current time immediately upon page load, not wait for the first second to pass

### Step 3.2 — Test in different window sizes <!-- HUMAN CHECKPOINT -->

- **Built**: Fixed positioning ensures clock stays in top-right corner regardless of viewport size
- [ ] Resize the browser window to various sizes (full screen, half screen, narrow window)
- **Expected**: The clock should always remain in the top-right corner, maintaining its 20px spacing from the edges

## 4. Cleanup

- [ ] Close the browser tab/window (no cleanup required for this static page)

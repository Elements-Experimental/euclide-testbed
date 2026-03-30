## Setup

- [ ] Open hello-world.html in a web browser

## 1. Clock Display and Positioning

### Step 1.1 — Clock appears on page load <!-- HUMAN CHECKPOINT -->

- **Built**: A clock div element with fixed positioning in the top-right corner
- [ ] Open hello-world.html in a browser
- **Expected**: A clock displaying time in HH:MM:SS format appears in the top-right corner
_(AC: specs/live-clock/spec.md § Scenario: Clock displays on page load)_

### Step 1.2 — Clock positioning does not interfere with content <!-- HUMAN CHECKPOINT -->

- **Built**: Clock is positioned in the top-right corner using fixed positioning with appropriate z-index
- [ ] Observe the clock position relative to the "Hello World" heading
- [ ] Move the mouse cursor around the page to activate the lamp effect
- **Expected**: The clock remains in the top-right corner, does not overlap the centered heading, and the cursor lamp effect works normally without being blocked by the clock
_(AC: specs/live-clock/spec.md § Scenario: Clock does not interfere with existing elements)_

## 2. Clock Functionality

### Step 2.1 — Clock updates every second <!-- HUMAN CHECKPOINT -->

- **Built**: JavaScript function that updates the clock every second using setInterval
- [ ] Observe the clock for at least 5 seconds
- **Expected**: The seconds value increments by 1 each second, and the clock continuously updates to show the current time
_(AC: specs/live-clock/spec.md § Scenario: Clock updates every second)_

### Step 2.2 — Clock displays correct time format <!-- HUMAN CHECKPOINT -->

- **Built**: Time formatting logic that pads hours, minutes, and seconds with leading zeros
- [ ] Observe the time displayed in the clock
- **Expected**: Time is displayed in HH:MM:SS format with two digits for hours (00-23), minutes (00-59), and seconds (00-59), separated by colons
_(AC: specs/live-clock/spec.md § Scenario: Clock shows correct time format)_

## 3. Clock Visual Styling

### Step 3.1 — Clock styling matches page theme <!-- HUMAN CHECKPOINT -->

- **Built**: CSS styling for the clock with night sky theme colors and monospace font
- [ ] Observe the clock's visual appearance
- **Expected**: Clock text is displayed in #fff9e6 color with a subtle glow effect (text-shadow), uses a monospace font (Courier New), and has good contrast against the night sky gradient background
_(AC: specs/live-clock/spec.md § Scenario: Clock styling matches page theme)_

### Step 3.2 — Clock position remains fixed <!-- HUMAN CHECKPOINT -->

- **Built**: Fixed positioning CSS that keeps the clock in place regardless of user interaction
- [ ] Move the cursor around the entire page
- [ ] Try scrolling (if applicable)
- **Expected**: The clock remains fixed in the top-right corner and does not move or reposition based on cursor movement or scrolling
_(AC: specs/live-clock/spec.md § Scenario: Clock positioning remains fixed)_

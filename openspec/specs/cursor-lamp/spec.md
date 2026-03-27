## ADDED Requirements

### Requirement: Cursor position tracking
The page must track the user's cursor position in real-time as it moves across the page.

### Requirement: Radial light effect
A radial gradient light effect must follow the cursor position, creating a "lamp" or "spotlight" effect that illuminates the area around the cursor.

### Requirement: Visual integration with night sky theme
The lamp effect must integrate seamlessly with the existing night sky color scheme, with the light center being brighter/lighter and gradually fading to the dark background colors.

### Requirement: Non-intrusive overlay
The lamp effect must not interfere with any existing content or user interactions on the page (e.g., it should not block text selection or clicks).

## Scenarios

#### Scenario: User moves cursor across the page
- **GIVEN** the hello world page is open in a browser
- **WHEN** the user moves their cursor across the page
- **THEN** a radial light gradient should follow the cursor position in real-time
- **AND** the light should illuminate the area around the cursor with a smooth gradient

#### Scenario: Lamp effect integrates with background
- **GIVEN** the hello world page is displayed with its night sky background
- **WHEN** the cursor lamp is active
- **THEN** the lamp's center should be brighter than the surrounding area
- **AND** the light should fade smoothly into the existing dark blue/purple background colors

#### Scenario: Page loads in dark state
- **GIVEN** a user opens the hello world page
- **WHEN** the page finishes loading and the cursor has not yet entered the viewport
- **THEN** the page should display a fully dark overlay (no lamp visible)
- **AND** the night sky background and text content should remain readable beneath the overlay

#### Scenario: Page loads with lamp functionality
- **GIVEN** a user opens the hello world page
- **WHEN** the page finishes loading
- **THEN** the cursor lamp effect should be ready and functional
- **AND** the lamp should appear as soon as the user moves their cursor for the first time

#### Scenario: Lamp does not block content
- **GIVEN** the hello world page is displayed with the cursor lamp effect
- **WHEN** the user attempts to interact with page content (e.g., select text)
- **THEN** the lamp overlay should not interfere with the interaction
- **AND** all existing functionality should work as expected

#### Scenario: Cursor leaves and re-enters page
- **GIVEN** the cursor lamp is active on the page
- **WHEN** the user moves their cursor outside the page boundary
- **THEN** the lamp should disappear immediately (overlay returns to fully dark)
- **WHEN** the user moves their cursor back into the page
- **THEN** the lamp effect should reappear at the cursor's new entry position
- **AND** the effect should continue to track cursor movement smoothly

## Out of scope

- Touch/mobile device support (lamp follows touch)
- Multiple simultaneous light sources
- Customizable lamp color, size, or intensity controls
- Click to place static lamps
- Lamp effect persistence across page reloads
- Animation effects (pulse, flicker, etc.)
- Performance optimization for very old browsers
- Keyboard navigation alternative for accessibility

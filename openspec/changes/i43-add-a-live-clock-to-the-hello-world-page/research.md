## Codebase Context

**Relevant files:**
- `hello-world.html` — The existing hello world page that will be modified to add the clock

**Current implementation:**
- Single HTML file with embedded CSS and JavaScript
- Night sky gradient background using `linear-gradient(135deg, #0a192f 0%, #1e3a5f 50%, #2d1b69 100%)`
- Centered `<h1>` heading with color `#fff9e6` and text shadow glow effect
- Cursor lamp overlay implemented with CSS custom properties (`--mouse-x`, `--mouse-y`) and JavaScript event listeners
- No external dependencies — pure vanilla HTML/CSS/JavaScript

**Confidence:** Confident (based on hello-world.html:1-70)

## Patterns and Conventions

**Styling approach:**
- All CSS is embedded in a `<style>` tag within the `<head>` (hello-world.html:7-50)
- Uses modern CSS features: flexbox for centering, CSS custom properties for dynamic values, fixed positioning for overlays
- Color palette: dark blues and purples for background, light cream (`#fff9e6`) for text with glow effects

**JavaScript approach:**
- All JavaScript is embedded in a `<script>` tag before closing `</body>` (hello-world.html:56-68)
- Uses vanilla JavaScript with modern DOM APIs (`getElementById`, `addEventListener`, `classList`)
- Event-driven approach for interactivity (mousemove, mouseleave events)

**HTML structure:**
- Semantic HTML5 with proper DOCTYPE
- Minimal DOM structure — only elements needed for functionality
- Z-index layering: lamp overlay at z-index 0 (background), heading at z-index 1 (foreground)

**Confidence:** Confident (based on hello-world.html structure)

## Integration Points

**HTML integration:**
- New clock element will be added as a sibling to the `<h1>` heading and `#lamp-overlay` div within `<body>`
- Must be positioned using CSS to avoid overlapping with existing elements

**CSS integration:**
- Clock styles will be added to the existing `<style>` block
- Must use the same color palette (`#fff9e6`) and glow effects (text-shadow) for consistency
- Needs appropriate z-index to layer correctly with lamp overlay and heading

**JavaScript integration:**
- Clock update logic will be added to the existing `<script>` block
- Will use `setInterval` for periodic updates (standard JavaScript timing pattern)
- No interaction with existing lamp effect JavaScript — independent functionality

**Confidence:** Confident (clear separation of concerns in current implementation)

## Reusable Assets

**Color values:**
- Text color: `#fff9e6` (used for heading — hello-world.html:21)
- Text glow effect: `text-shadow: 0 0 20px rgba(255, 249, 230, 0.5)` (hello-world.html:24)
- Background gradient colors: `#0a192f`, `#1e3a5f`, `#2d1b69` (hello-world.html:15)

**Layout patterns:**
- Fixed positioning with `position: fixed` for overlays (hello-world.html:31)
- Centering with flexbox: `display: flex; justify-content: center; align-items: center` (hello-world.html:12-14)
- Z-index layering pattern established (0 for background effects, 1 for content)

**JavaScript patterns:**
- DOM element selection via `getElementById`
- Event listeners for user interactions
- CSS custom property manipulation via `style.setProperty`

**Confidence:** Confident (existing patterns can be directly applied)

## Risks and Unknowns

**Clock positioning choice:**
- Clock could be positioned in corner (top-right, top-left, bottom-right, bottom-left) or along an edge
- Issue acceptance criteria states "does not interfere with the lamp overlay or the centered heading layout" but doesn't specify preferred position
- **Decision needed:** Which corner or position to use
- **Confidence:** Unclear → Design must specify position

**Font choice for clock:**
- Current heading uses Arial (`font-family: Arial, sans-serif` — hello-world.html:16)
- Clock could use same font or a monospace font (common for digital clocks)
- Issue doesn't specify font requirements
- **Decision needed:** Use Arial for consistency or monospace for clock aesthetic
- **Confidence:** Likely → Design should specify; monospace is conventional for digital time displays

**Clock size:**
- No specification in requirements for clock font size
- Must be visible but not dominate the page (heading is 4rem — hello-world.html:22)
- **Decision needed:** Clock font size relative to heading
- **Confidence:** Likely → Design should specify reasonable size

**Glow effect intensity:**
- Heading has text-shadow glow; should clock match this intensity or be more subtle?
- **Decision needed:** Whether to match or reduce glow effect
- **Confidence:** Likely → Design should specify

## Ecosystem Research

This section is not applicable — this is a brownfield change to an existing HTML file using established vanilla JavaScript/CSS patterns. No new technologies or libraries are being introduced. The codebase patterns are clear from hello-world.html.

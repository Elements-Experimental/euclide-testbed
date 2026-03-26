## Context

The hello-world.html page exists with a night sky-themed gradient background (dark blues and purples) and centered white/light yellow text. The page currently has no interactive elements. This enhancement will add a cursor-following light effect to create a more immersive experience.

## Goals / Non-Goals

**Goals:**
- Create a smooth, performant cursor-following radial gradient effect
- Maintain the existing night sky aesthetic and color scheme
- Use vanilla JavaScript for simplicity and no external dependencies
- Ensure the effect works across modern browsers
- Make the lamp effect visually pleasing with appropriate size and intensity

**Non-Goals:**
- Mobile/touch device support (cursor-based interaction only)
- Multiple light sources or click-to-place lamps
- Customizable lamp colors or sizes via UI controls
- Animation effects beyond the cursor movement
- Accessibility enhancements for the interactive feature

## Decisions

### Implementation Approach
Use a JavaScript mousemove event listener to track cursor position and update a CSS radial-gradient background overlay. The overlay will be positioned using CSS custom properties updated via JavaScript for smooth performance.

### Technical Details
- Add a `<div>` overlay element with pointer-events: none to avoid interfering with interactions
- Use CSS `radial-gradient` with a transparent center fading to the dark background color
- Update gradient position via CSS custom properties (--mouse-x, --mouse-y) for better performance than direct style manipulation
- Lamp radius: 250px with smooth falloff
- Light center color: cool blue-white `rgba(200, 220, 255, 0.15)` fading to transparent, overlaid on the dark background
- Initial state: overlay is fully opaque (dark) on load; lamp only appears on first `mousemove`
- Cursor exit: listen for `mouseleave` on the document and hide the lamp (restore full dark overlay)

### ADR Links
<!-- No architectural decisions required for this simple enhancement -->

## Risks / Trade-offs

- **Performance:** mousemove events fire frequently; mitigate with requestAnimationFrame if needed
- **Browser compatibility:** CSS custom properties and radial gradients are well-supported in modern browsers but may not work in very old browsers (acceptable trade-off)
- **Visual distraction:** The lamp effect might be distracting for some users, but enhances the immersive quality for most

## External references (if applicable)

<!-- None -->

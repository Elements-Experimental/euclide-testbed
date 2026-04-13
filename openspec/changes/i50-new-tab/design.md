## Context

The project currently has one standalone HTML page (hello-world.html). This change adds a second HTML page to demonstrate a multi-page structure. The new page should maintain visual consistency with the existing night sky theme while providing distinct content.

## Goals / Non-Goals

**Goals:**
- Create a new standalone HTML page with valid HTML5 structure
- Use the same night sky color palette as hello-world.html for visual consistency
- Provide distinct content that differentiates it from the hello world page
- Make the new page discoverable (link from hello-world.html)
- Update documentation to reference the new page

**Non-Goals:**
- Complex navigation systems or menus
- JavaScript frameworks or build systems
- Server-side rendering or backend integration
- Responsive design beyond basic viewport handling
- Duplication of the cursor lamp effect (unless it adds value)

## Decisions

### Page Name and Content
The new page will be named `about.html` and will contain information about the project. This provides meaningful content while keeping the scope simple.

### Visual Design
- Reuse the night sky color palette from hello-world.html: `#0a192f`, `#1e3a5f`, `#2d1b69` (gradients), `#fff9e6` (text)
- Use similar layout structure (full viewport, centered content, flexbox)
- Apply text glow effect for consistency
- Do not include the cursor lamp effect (keep it unique to hello-world.html)

### Navigation
Add simple navigation links:
- hello-world.html will link to about.html
- about.html will link back to hello-world.html
- Links styled to match the night sky theme

### File Location
Place `about.html` in the repository root, alongside hello-world.html

### ADR Links
No ADRs required for this simple implementation.

## Risks / Trade-offs

- Adding hardcoded navigation links between pages means any future pages require manual updates to all existing pages. This is acceptable for a small project but doesn't scale well.
- Inline CSS in each page means style changes require updates to multiple files. However, this maintains the simplicity and self-contained nature of each page, which is appropriate for a demo project.

## External references (if applicable)

None

## Context

The repository currently has a single HTML page (hello-world.html). The product issue requests "add new tab" without specifying the exact nature or content of the tab. The existing page uses inline CSS/JS with a night sky theme.

## Goals / Non-Goals

**Goals:**
- Create a new HTML page accessible from the existing hello-world.html page
- Implement simple navigation to allow switching between pages
- Maintain visual consistency with the existing night sky theme
- Keep the implementation simple and self-contained (no frameworks or build tools)

**Non-Goals:**
- Complex single-page application (SPA) framework
- Server-side routing or backend logic
- Advanced tab state management or deep linking
- Mobile-responsive navigation (beyond basic HTML)
- Complex animations or transitions

## Decisions

### Navigation Pattern: Simple HTML Links

Use basic HTML anchor tags to navigate between pages. This is the simplest approach and requires no JavaScript framework. Each page will have navigation links to other pages.

**Rationale:** Maintains the simplicity of the current codebase. No build tools or frameworks needed.

### New Page Content: "About" Page

The new tab will be an "About" page with placeholder content describing the site. This provides a clear purpose and demonstrates multi-page navigation.

**Rationale:** Simple, understandable content that doesn't require external resources or complexity.

### Visual Consistency

The new page will:
- Use the same color palette as hello-world.html (#0a192f, #1e3a5f, #2d1b69 for background, #fff9e6 for text)
- Maintain the same night sky gradient background
- Use consistent typography and styling
- Include the same cursor lamp effect for visual continuity

**Rationale:** Provides a cohesive user experience across pages.

### Navigation Placement

Add a simple navigation bar at the top of both pages with links to "Home" (hello-world.html) and "About" (about.html).

**Rationale:** Standard web pattern, easy to implement, doesn't interfere with existing content.

### File Naming

The new page will be named `about.html` and placed in the repository root alongside `hello-world.html`.

**Rationale:** Follows the flat structure of the existing project and uses a clear, descriptive name.

### ADR Links

<!-- No ADRs required for this simple implementation -->

## Risks / Trade-offs

- **Simple navigation means full page reloads:** This is acceptable for a small demo site but wouldn't scale for larger applications.
- **Code duplication:** Navigation HTML and CSS will be duplicated across pages. For this small project, it's acceptable. A larger project would benefit from templating or components.
- **No active state styling:** The current page won't be visually distinguished in the navigation. This is acceptable for a minimal implementation but could be enhanced later.

## External references (if applicable)

<!-- None -->

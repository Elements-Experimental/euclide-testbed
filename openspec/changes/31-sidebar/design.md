## Context

The current application consists of a single HTML page (`hello-world.html`) with a centered "Hello World" message and a night sky-themed background with a cursor lamp effect. The page uses a gradient background (dark blues and purples) with light-colored text.

## Goals / Non-Goals

**Goals:**
- Add a sidebar to the existing page with an "about" section
- Maintain the existing night sky aesthetic and cursor lamp effect
- Ensure the sidebar is visually integrated with the current design
- Provide clear information about the project's purpose
- Keep the sidebar simple and unobtrusive

**Non-Goals:**
- Collapsible/toggleable sidebar functionality
- Multiple sidebar sections beyond "about"
- Responsive sidebar for mobile devices
- Sidebar navigation or interactive elements
- Separate sidebar component file or framework integration

## Decisions

### Sidebar Placement
The sidebar will be positioned on the left side of the page using CSS flexbox or grid layout. This follows common web design conventions and allows the main content to remain prominent.

### Styling Approach
The sidebar will use inline CSS (consistent with the existing approach in `hello-world.html`) with colors that complement the night sky theme. It will have a semi-transparent background to maintain visual harmony with the existing design and allow the cursor lamp effect to shine through subtly.

### Content
The "about" field will contain a brief description of the project: that it's a testbed for demonstrating simple web development concepts and the OpenSpec workflow.

### Layout Structure
- Convert the body to a flex container with horizontal layout
- Sidebar on the left with fixed width (e.g., 250-300px)
- Main content area on the right taking remaining space
- Maintain the cursor lamp overlay across the entire viewport

### ADR Links
<!-- No ADRs required for this simple implementation -->

## Risks / Trade-offs

- Adding a sidebar reduces the space available for the main "Hello World" content, but this is acceptable given the content is minimal
- Fixed-width sidebar may not work well on very small screens, but responsive design is explicitly out of scope
- Inline CSS continues to be used for consistency, though this reduces maintainability if the page grows more complex

## External references (if applicable)

- Current page: `hello-world.html`

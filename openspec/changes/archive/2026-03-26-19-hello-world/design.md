## Context

This is a simple demonstration page with no existing codebase dependencies. The page will be standalone and self-contained.

## Goals / Non-Goals

**Goals:**
- Create a valid HTML5 page with proper structure
- Apply night sky-themed colors (dark blues, purples, and light/white accents)
- Display "Hello World" as the primary content
- Ensure the page is visually appealing and demonstrates basic CSS styling

**Non-Goals:**
- Interactive functionality or JavaScript
- Responsive design for multiple screen sizes
- Accessibility features beyond basic HTML semantics
- External CSS framework integration

## Decisions

### Color Scheme
Use a gradient or solid background with deep blues (#0a192f, #1e3a5f) and purples (#2d1b69, #4a2c7f) to evoke a night sky. Text will be light-colored (white or light yellow #fff9e6) to represent stars or moonlight.

### Structure
- Single HTML file with inline CSS for simplicity
- Centered text layout for the "Hello World" message
- Full viewport height background to maximize visual impact

### ADR Links
<!-- No ADRs required for this simple implementation -->

## Risks / Trade-offs

- Inline CSS makes the file less maintainable if styling grows complex, but appropriate for this simple use case
- Hardcoded colors may not work well in all display environments, but sufficient for demonstration purposes

## External references (if applicable)

<!-- None -->

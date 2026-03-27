## ADDED Requirements

### Requirement: Sidebar container
The page must include a sidebar element positioned on the left side of the page that contains informational content.

### Requirement: About field content
The sidebar must contain an "about" field with text that explains the purpose of this project (that it's a testbed for demonstrating web development concepts and the OpenSpec workflow).

### Requirement: Sidebar width
The sidebar must have a fixed width of 250px.

### Requirement: Visual integration with existing design
The sidebar must use a dark, semi-transparent background in the dark blue/purple family (opacity ≤ 0.8) consistent with the existing gradient, integrating visually with the current page design.

### Requirement: Layout adjustment
The page layout must be adjusted to accommodate the sidebar while keeping the main "Hello World" content visible and properly positioned.

### Requirement: Cursor lamp effect preservation
The existing cursor lamp effect must continue to work across the entire page, including over the sidebar area.

## Scenarios

#### Scenario: User opens the page and sees the sidebar
- **GIVEN** the HTML file has been updated with the sidebar
- **WHEN** a user opens the page in a web browser
- **THEN** they should see a sidebar on the left side of the page
- **AND** the sidebar should contain an "about" section with descriptive text

#### Scenario: Sidebar displays with night sky styling
- **GIVEN** the page is loaded with the sidebar
- **WHEN** the page renders
- **THEN** the sidebar element must have a fixed width of 250px
- **AND** the sidebar background must use a dark, semi-transparent color in the dark blue/purple family (e.g., `rgba(10, 10, 40, 0.7)` or equivalent) with opacity ≤ 0.8

#### Scenario: Main content remains visible alongside sidebar
- **GIVEN** the sidebar is present
- **WHEN** the page is displayed
- **THEN** the "Hello World" heading should still be visible
- **AND** the main content should be positioned to the right of the sidebar
- **AND** the main content should remain properly centered in its available space

#### Scenario: Cursor lamp effect works with sidebar
- **GIVEN** the page with sidebar is loaded
- **WHEN** the user moves their mouse cursor over the page
- **THEN** the cursor lamp effect should illuminate areas under the cursor
- **AND** the effect should work over both the sidebar and main content areas

#### Scenario: About field contains project description
- **GIVEN** the sidebar is visible
- **WHEN** the user reads the "about" section
- **THEN** they should see text explaining this is a testbed project
- **AND** the text should mention it demonstrates web development and the OpenSpec workflow

## Out of scope

- Collapsible or toggleable sidebar functionality
- Multiple sections in the sidebar beyond "about"
- Responsive design for mobile or tablet devices — the sidebar layout is designed for viewports ≥ 1024px wide; narrower viewports are not supported
- Sidebar navigation or interactive elements (links, buttons)
- Separate sidebar component files
- External CSS frameworks or libraries
- Accessibility features beyond basic HTML semantics
- Animation effects specific to the sidebar
- Right-side or alternative sidebar positioning

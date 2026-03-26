## ADDED Requirements

### Requirement: Display Hello World Greeting
The page must display the exact text "Hello World" (no comma, correct capitalisation) as the primary content.

### Requirement: Warm Color Scheme
The page must use warm hues (oranges, reds, yellows) in its background. Text must be legible against the warm background.

### Requirement: Centered Layout
The primary content must be visually centered on the page (both horizontally and vertically).

### Requirement: Self-Contained HTML
The page must be a valid, standalone HTML document that works without external dependencies.

## Scenarios

#### Scenario: User opens the hello world page
- **GIVEN** the index.html file exists in the repository root
- **WHEN** a user opens index.html in a web browser
- **THEN** the page displays the exact text "Hello World"

#### Scenario: Page uses warm color palette
- **GIVEN** the index.html file is rendered in a browser
- **WHEN** the user views the page
- **THEN** the page background uses warm colors (oranges, reds, yellows) and the text is legible against it

#### Scenario: Content is centered on the page
- **GIVEN** the index.html file is rendered in a browser
- **WHEN** the user views the page
- **THEN** the "Hello World" text is centered both horizontally and vertically within the viewport

#### Scenario: Page works without dependencies
- **GIVEN** the index.html file
- **WHEN** the file is opened directly in a browser without a web server
- **THEN** the page renders correctly with all styles applied

## Out of scope

- Interactive elements or JavaScript functionality
- Multi-page navigation
- Responsive design for mobile devices
- Accessibility compliance beyond basic HTML semantics
- External CSS or JavaScript files
- Server-side rendering or dynamic content

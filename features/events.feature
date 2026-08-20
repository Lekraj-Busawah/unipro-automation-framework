Feature: Events page - Content rendering and responsiveness
  The Events page should render its hero and "Join us" section, listing upcoming events the company is exhibiting at or attending.

  Background:
    Given the user navigates to "/events/"

  # ---------------------------------------------------------------------------
  # STRUCTURAL PRESENCE
  # ---------------------------------------------------------------------------

  @events @structure @smoke
  Scenario Outline: Verify key page sections are present in the DOM
    Then the "<section_name>" container should exist

    Examples:
      | section_name |
      | hero         |
      | join us      |
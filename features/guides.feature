Feature: Guides page - Content rendering, search and responsiveness
  The Guides page should render its hero, breadcrumb, search bar,
  topic filters, guide card grid and support responsive hero images.

  Background:
    Given the user navigates to "/guides/"

  # ---------------------------------------------------------------------------
  # STRUCTURAL PRESENCE
  # ---------------------------------------------------------------------------

  @guides @structure @smoke
  Scenario Outline: Verify key page sections are present in the DOM
    Then the "<section_name>" container should exist

    Examples:
      | section_name    |
      | hero            |
      | breadcrumb      |
      | search bar      |
      | topics          |
      | guide card grid |
      | final cta       |

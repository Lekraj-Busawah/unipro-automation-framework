Feature: Success Stories page - Content rendering, search and responsiveness
  The Success Stories page should render its hero, breadcrumb, search bar, success story card grid and support responsive hero images.

  Background:
    Given the user navigates to "/success-stories/"

  # ---------------------------------------------------------------------------
  # STRUCTURAL PRESENCE
  # ---------------------------------------------------------------------------

  @successstories @structure @smoke
  Scenario Outline: Verify key page sections are present in the DOM
    Then the "<section_name>" container should exist

    Examples:
      | section_name            |
      | hero                    |
      | breadcrumb              |
      | search bar              |
      | success story card grid |
      | final cta               |

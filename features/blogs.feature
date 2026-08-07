Feature: Blogs page - Content rendering, search and responsiveness
  The Blogs page should render its hero, breadcrumb, featured post, search bar,
  topic filters, blog card grid and support responsive hero images.

  Background:
    Given the user navigates to "/blogs/"

  # ---------------------------------------------------------------------------
  # STRUCTURAL PRESENCE
  # ---------------------------------------------------------------------------

  @blogs @structure @smoke @wip
  Scenario Outline: Verify key page sections are present in the DOM
    Then the "<section_name>" container should exist

    Examples:
      | section_name     |
      | hero             |
      | breadcrumb       |
      | featured post    |
      | search bar       |
      | topics           |
      | blog card grid   |
      | final cta        |

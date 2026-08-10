Feature: Blogs page - Content rendering, search and responsiveness
  The Blogs page should render its hero, breadcrumb, featured post, search bar,
  topic filters, blog card grid and support responsive hero images.

  Background:
    Given the user navigates to "/blogs/"

  # ---------------------------------------------------------------------------
  # STRUCTURAL PRESENCE
  # ---------------------------------------------------------------------------

  @blogs @structure @smoke 
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

  # ---------------------------------------------------------------------------
  # HERO SECTION
  # ---------------------------------------------------------------------------

  @blogs @hero @content @smoke
  Scenario Outline: Verify hero content presence and partial copy
    When the "hero" container is displayed
    Then the <element_name> is visible and contains "<element_contains>"

    Examples:
      | element_name     | element_contains          |
      | hero heading     | Blogs                     |
      | hero intro text  | latest thoughts           |

  @blogs @hero @responsive 
  Scenario Outline: Verify hero image visibility by breakpoint
    When the <page> is viewed on a <device_type> device
    Then the "<desktop_image>" visibility should be <desktop_visibility>
    And the "<mobile_image>" visibility should be <mobile_visibility>

    Examples:
      | page  | device_type | desktop_image      | desktop_visibility | mobile_image      | mobile_visibility |
      | blogs | desktop     | hero desktop image | visible            | hero mobile image | hidden            |
      | blogs | mobile      | hero desktop image | hidden             | hero mobile image | visible           |

  # ---------------------------------------------------------------------------
  # BREADCRUMB
  # ---------------------------------------------------------------------------

  @blogs @breadcrumb @content @smoke
  Scenario Outline: Verify breadcrumb content presence and partial copy
    When the "breadcrumb" container is displayed
    Then the <element_name> is visible and contains "<element_contains>"

    Examples:
      | element_name                   | element_contains   |
      | breadcrumb home link           | Home               |
      | breadcrumb current page label  | Blogs              |
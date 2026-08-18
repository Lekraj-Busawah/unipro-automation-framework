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

  # ---------------------------------------------------------------------------
  # HERO SECTION
  # ---------------------------------------------------------------------------

  @successstories @hero @content @smoke
  Scenario Outline: Verify hero content presence and partial copy
    When the "hero" container is displayed
    Then the <element_name> is visible and contains "<element_contains>"

    Examples:
      | element_name     | element_contains |
      | hero heading      | Success stories |
      | hero intro text   | latest thoughts |

  @successstories @hero @responsive
  Scenario Outline: Verify hero image visibility by breakpoint
    When the <page> is viewed on a <device_type> device
    Then the "<desktop_image>" visibility should be <desktop_visibility>
    And the "<mobile_image>" visibility should be <mobile_visibility>

    Examples:
      | page             | device_type | desktop_image      | desktop_visibility | mobile_image      | mobile_visibility |
      | success-stories  | desktop     | hero desktop image | visible            | hero mobile image | hidden            |
      | success-stories  | mobile      | hero desktop image | hidden             | hero mobile image | visible           |

  # ---------------------------------------------------------------------------
  # BREADCRUMB
  # ---------------------------------------------------------------------------

  @successstories @breadcrumb @content @smoke
  Scenario Outline: Verify breadcrumb content presence and partial copy
    When the "breadcrumb" container is displayed
    Then the <element_name> is visible and contains "<element_contains>"

    Examples:
      | element_name                   | element_contains |
      | breadcrumb home link           | Home             |
      | breadcrumb current page label  | Success Stories  |

  @successstories @breadcrumb @cta
  Scenario Outline: Sub menu bar contact CTA is present and navigates correctly
    Then the sub menu bar contact us cta is visible and contains "<cta_text>"
    And the sub menu bar contact us cta navigates to "<expected_url>"

    Examples:
      | cta_text   | expected_url                      |
      | Contact Us | https://www.unipro.io/contact-us/ |

  @successstories @search @cta
  Scenario Outline: Submitting a search term navigates to the filtered results
    When the "search bar" container is displayed
    And the user searches the success stories for "<search_term>"
    Then the browser navigates to a URL containing "<expected_query_param>"
    And the <grid_name> has at least "<minimum_count>" cards


    Examples:
      | search_term | expected_query_param   | grid_name          | minimum_count |
      | payroll     | success_story=payroll  | success story card | 1             |

  # ---------------------------------------------------------------------------
  # SUCCESS STORY CARD GRID
  # ---------------------------------------------------------------------------

  @successstories @cardgrid @grid @smoke
  Scenario Outline: Success story card grid renders at least the minimum expected number of cards
    When the "success story card grid" container is displayed
    Then the <grid_name> has at least "<minimum_count>" cards

    Examples:
      | grid_name          | minimum_count |
      | success story card | 15            |

  @successstories @cardgrid @content @smoke
  Scenario Outline: The most recent success story cards have a working "Read more" link
    When the "success story card grid" container is displayed
    Then the success story card at position "<position>" has a working "Read more" link

    Examples:
      | position |
      | 1        |
      | 2        |
      | 3        |

  # ---------------------------------------------------------------------------
  # FINAL CTA
  # ---------------------------------------------------------------------------

  @successstories @finalcta @content @smoke
  Scenario Outline: Verify final CTA content presence and partial copy
    When the "final cta" container is displayed
    Then the <element_name> is visible and contains "<element_contains>"

    Examples:
      | element_name   | element_contains |
      | cta eyebrow    | WORK TOGETHER    |
      | cta heading    | conversation     |
      | cta intro text | No pressure      |

  @successstories @finalcta @cta
  Scenario Outline: Final CTA button navigates to the contact page
    Then the cta button is visible and contains "<button_text>"
    And the cta button navigates to "<expected_url>"

    Examples:
      | button_text | expected_url                      |
      | Contact Us  | https://www.unipro.io/contact-us/ |
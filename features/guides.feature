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

  # ---------------------------------------------------------------------------
  # HERO SECTION
  # ---------------------------------------------------------------------------

  @guides @hero @content @smoke
  Scenario Outline: Verify hero content presence and partial copy
    When the "hero" container is displayed
    Then the <element_name> is visible and contains "<element_contains>"

    Examples:
      | element_name    | element_contains |
      | hero heading    | Guides           |
      | hero intro text | newest guides    |

  @guides @hero @responsive
  Scenario Outline: Verify hero image visibility by breakpoint
    When the <page> is viewed on a <device_type> device
    Then the "<desktop_image>" visibility should be <desktop_visibility>
    And the "<mobile_image>" visibility should be <mobile_visibility>

    Examples:
      | page   | device_type | desktop_image      | desktop_visibility | mobile_image      | mobile_visibility |
      | guides | desktop     | hero desktop image | visible            | hero mobile image | hidden            |
      | guides | mobile      | hero desktop image | hidden             | hero mobile image | visible           |

  # ---------------------------------------------------------------------------
  # BREADCRUMB
  # ---------------------------------------------------------------------------

  @guides @breadcrumb @content @smoke
  Scenario Outline: Verify breadcrumb content presence and partial copy
    When the "breadcrumb" container is displayed
    Then the <element_name> is visible and contains "<element_contains>"

    Examples:
      | element_name                   | element_contains |
      | breadcrumb home link           | Home             |
      | breadcrumb current page label  | Guides           |

  @guides @breadcrumb @cta
  Scenario Outline: Sub menu bar contact CTA is present and navigates correctly
    Then the sub menu bar contact us cta is visible and contains "<cta_text>"
    And the sub menu bar contact us cta navigates to "<expected_url>"

    Examples:
      | cta_text   | expected_url                      |
      | Contact Us | https://www.unipro.io/contact-us/ |

  # ---------------------------------------------------------------------------
  # SEARCH
  # ---------------------------------------------------------------------------

  @guides @search @cta
  Scenario Outline: Submitting a search term navigates to the filtered results
    When the "search bar" container is displayed
    And the user searches the guides for "<search_term>"
    Then the browser navigates to a URL containing "<expected_query_param>"
    Then the <grid_name> has at least "<minimum_count>" cards

    Examples:
      | search_term | expected_query_param | grid_name          | minimum_count |
      | low-code    | guide=low-code       | guide card grid    | 1             |

  # ---------------------------------------------------------------------------
  # TOPICS
  # ---------------------------------------------------------------------------

  @guides @topics @content @smoke
  Scenario Outline: Topics list renders all category filter links
    When the "topics" container is displayed
    Then the "topics" list has exactly "<expected_count>" items
    And the "topics" list item at position "<index>" has title "<title>"
    And the topic link at position "<index>" links to "<expected_url>"

    Examples:
      | expected_count  | index | title                             | expected_url                            |
      | 7               | 1     | Data consolidation and migration  | /category/data-consolidation            |
      | 7               | 2     | Development                       | /category/rapid-application-development |
      | 7               | 3     | Digital Transformation            | /category/digital-transformation        |
      | 7               | 4     | Legacy Modernisation              | /category/legacy-modernisation          |
      | 7               | 5     | Low-Code                          | /category/low-code                      |
      | 7               | 6     | Quality Assurance                 | /category/quality-assurance             |
      | 7               | 7     | UX & UI Design                    | /category/ux                            |

  # ---------------------------------------------------------------------------
  # GUIDE CARD GRID
  # ---------------------------------------------------------------------------

  @guides @cardgrid @grid @smoke
  Scenario Outline: Guide card grid renders at least the minimum expected number of articles
    When the "guide card grid" container is displayed
    Then the <grid_name> has at least "<minimum_count>" cards

    Examples:
      | grid_name  | minimum_count |
      | guide card | 2             |

  @guides @cardgrid @content @smoke
  Scenario Outline: The most recent guide cards have a working "Read more" link
    When the "guide card grid" container is displayed
    Then the guide card at position "<position>" has a working "Read more" link

    Examples:
      | position |
      | 1        |
      | 2        |

  @guides @finalcta @content @smoke
  Scenario Outline: Verify final CTA content presence and partial copy
    When the "final cta" container is displayed
    Then the <element_name> is visible and contains "<element_contains>"

    Examples:
      | element_name   | element_contains |
      | cta eyebrow    | WORK TOGETHER    |
      | cta heading    | conversation     |
      | cta intro text | No pressure      |

  @guides @finalcta @cta
  Scenario Outline: Final CTA button navigates to the contact page
    Then the cta button is visible and contains "<button_text>"
    And the cta button navigates to "<expected_url>"

    Examples:
      | button_text | expected_url                      |
      | Contact Us  | https://www.unipro.io/contact-us/ |
@whowedoitfor @regression
Feature: Who We Do It For page - Content rendering and responsiveness
  The "Who we do it for" page should render its key content and support responsive
  images

  Background:
    Given the user navigates to "/who-we-do-it-for/"

  # ---------------------------------------------------------------------------
  # STRUCTURAL PRESENCE
  # ---------------------------------------------------------------------------

  @whowedoitfor @structure @smoke 
  Scenario Outline: Verify key page sections are present in the DOM
    Then the "<section_name>" container should exist

    Examples:
      | section_name          |
      | hero                  |
      | leaders               |
      | enterprise challenges |
      | client experience     |
      | sector expertise      |
      | strategic advantage   |
      | final cta             |

  # ---------------------------------------------------------------------------
  # HERO SECTION
  # ---------------------------------------------------------------------------

  @whowedoitfor @hero @content @smoke
  Scenario Outline: Verify hero content presence and partial copy
    When the "hero" container is displayed
    Then the <element_name> is visible and contains "<element_contains>"

    Examples:
      | element_name          | element_contains                |
      | hero eyebrow text     | WHO WE DO IT FOR                |
      | hero heading          | BESPOKE SOFTWARE                |
      | hero intro text block | Challenge-Defined Partnership   |

  @whowedoitfor @hero @responsive
  Scenario Outline: Verify hero image visibility by breakpoint
    When the <page> is viewed on a <device_type> device
    Then the "<desktop_image>" visibility should be <desktop_visibility>
    And the "<mobile_image>" visibility should be <mobile_visibility>

    Examples:
      | page             | device_type | desktop_image      | desktop_visibility | mobile_image      | mobile_visibility |
      | who we do it for | desktop     | desktop hero image | visible            | mobile hero image | hidden            |
      | who we do it for | mobile      | desktop hero image | hidden             | mobile hero image | visible           |

  # ---------------------------------------------------------------------------
  # LEADERS SECTION
  # ---------------------------------------------------------------------------

  @whowedoitfor @leaders @content
  Scenario Outline: Verify leaders section content presence and partial copy
    When the "leaders" container is displayed
    Then the <element_name> is visible and contains "<element_contains>"

    Examples:
      | element_name             | element_contains              |
      | leaders eyebrow text     | THE LEADERS WE PARTNER WITH   |
      | leaders heading          | Digital Accountability        |
      | leaders intro text block | Senior Executive              |

  @whowedoitfor @leaders @responsive
  Scenario Outline: Verify leaders image visibility by breakpoint
    When the <page> is viewed on a <device_type> device
    Then the <block_name> desktop image visibility is <desktop_visibility>
    And the <block_name> mobile image visibility is <mobile_visibility>

    Examples:
      | page             | device_type | block_name | desktop_visibility | mobile_visibility |
      | who we do it for | desktop     | leaders    | visible            | hidden            |
      | who we do it for | mobile      | leaders    | hidden             | visible           |

  # ---------------------------------------------------------------------------
  # ENTERPRISE CHALLENGES SECTION
  # ---------------------------------------------------------------------------

  @whowedoitfor @enterprisechallenges @content
  Scenario Outline: Verify enterprise challenges section content presence and partial copy
    When the "enterprise challenges" container is displayed
    Then the <element_name> is visible and contains "<element_contains>"

    Examples:
      | element_name                           | element_contains                  |
      | enterprise challenges eyebrow text     | ENTERPRISE CHALLENGES             |
      | enterprise challenges heading          | True Cost of Compromise           |
      | enterprise challenges intro text block | off the shelf                     |

  @whowedoitfor @enterprisechallenges @list
  Scenario Outline: Enterprise challenges list has the expected items
    When the "enterprise challenges" container is displayed
    Then the "enterprise challenges" list has exactly "<expected_count>" items
    And the "enterprise challenges" list item at position "<index>" has title "<title>"
    And the "enterprise challenges" list item at position "<index>" has copy "<copy>"

    Examples:
      | expected_count | index | title                              | copy                  |
      | 4              | 1     | Crippling Backlogs and Bottlenecks | technical debt        |
      | 4              | 2     | The Burden of Legacy Systems       | legacy systems        |
      | 4              | 3     | Hidden Costs of Compromise         | vendor lock-in        |
      | 4              | 4     | The Demand for ROI                 | return on investment  |

  @whowedoitfor @enterprisechallenges @responsive
  Scenario Outline: Verify enterprise challenges image visibility by breakpoint
    When the <page> is viewed on a <device_type> device
    Then the <block_name> desktop image visibility is <desktop_visibility>
    And the <block_name> mobile image visibility is <mobile_visibility>

    Examples:
      | page             | device_type | block_name            | desktop_visibility | mobile_visibility |
      | who we do it for | desktop     | enterprise challenges | visible            | hidden            |
      | who we do it for | mobile      | enterprise challenges | hidden             | visible           |

  # ---------------------------------------------------------------------------
  # CLIENT EXPERIENCE GRID
  # ---------------------------------------------------------------------------

  @whowedoitfor @clientexperience @content
  Scenario Outline: Verify client experience content presence and partial copy
    When the "client experience" container is displayed
    Then the <element_name> is visible and contains "<element_contains>"

    Examples:
      | element_name                       | element_contains          |
      | client experience eyebrow text     | OUR EXPERIENCE            |
      | client experience heading          | Trusted by the Enterprise |
      | client experience intro text block | recognised                |

  @whowedoitfor @clientexperience @grid 
  Scenario Outline: Client experience grid renders the expected number of brand tiles
    When the "client experience" container is displayed
    Then the image grid has at least <tile_count> client tiles
    And the client tile at position <tile_position> has an associated image

    Examples:
      | tile_count | tile_position |
      | 12         | 1             |
      | 12         | 2             |
      | 12         | 3             |
      | 12         | 4             |
      | 12         | 5             |
      | 12         | 6             |
      | 12         | 7             |
      | 12         | 8             |
      | 12         | 9             |
      | 12         | 10            |
      | 12         | 11            |
      | 12         | 12            |

  @whowedoitfor @clientexperience @responsive
  Scenario Outline: Client image variants are visible at the correct breakpoint
    When the <page> is viewed on a <device_type> device
    Then each client tile desktop image visibility is <desktop_visibility>
    And each client tile mobile image visibility is <mobile_visibility>

    Examples:
      | page             | device_type | desktop_visibility | mobile_visibility |
      | who we do it for | desktop     | visible            | hidden            |
      | who we do it for | mobile      | hidden             | visible           |

  # ---------------------------------------------------------------------------
  # SECTOR EXPERTISE SECTION
  # ---------------------------------------------------------------------------

  @whowedoitfor @sectorexpertise @content
  Scenario Outline: Verify sector expertise content presence and partial copy
    When the "sector expertise" container is displayed
    Then the <element_name> is visible and contains "<element_contains>"

    Examples:
      | element_name                     | element_contains               |
      | sector expertise eyebrow text    | DELIVERED UNRIVALLED ADVANTAGE |
      | sector expertise heading         | Sector-Agnostic Expertise      |
      | sector expertise intro text block| complexity                     |

  @whowedoitfor @sectorexpertise @grid @wip
  Scenario Outline: Sector expertise list renders numbered sector titles
    When the "sector expertise" container is displayed
    Then the "sector expertise" list has exactly "<expected_count>" items
    And the "sector expertise" list item at position "<index>" has number "<number>"
    And the "sector expertise" list item at position "<index>" has title "<title>"

    Examples:
      | expected_count | index | number | title             |
      | 8              | 1     | 1      | Finance & Banking |
      | 8              | 2     | 2      | Retail            |
      | 8              | 3     | 3      | Healthcare        |
      | 8              | 4     | 4      | Civil Engineering |
      | 8              | 5     | 5      | Manufacturing     |
      | 8              | 6     | 6      | Utilities         |
      | 8              | 7     | 7      | Entertainment     |
      | 8              | 8     | 8      | Travel            |

  # ---------------------------------------------------------------------------
  # STRATEGIC ADVANTAGE SECTION
  # ---------------------------------------------------------------------------

  @whowedoitfor @strategicadvantage @content
  Scenario Outline: Verify strategic advantage content presence and partial copy
    When the "strategic advantage" container is displayed
    Then the <element_name> is visible and contains "<element_contains>"

    Examples:
      | element_name                         | element_contains    |
      | strategic advantage eyebrow text     | Strategic Advantage |
      | strategic advantage heading          | Digital Autonomy    |
      | strategic advantage intro text block | precisely tailored  |

  @whowedoitfor @strategicadvantage @list
  Scenario Outline: Strategic advantage list has the expected benefits
    When the "strategic advantage" container is displayed
    Then the "strategic advantage" list has exactly "<expected_count>" items
    And the "strategic advantage" list item at position "<index>" has title "<title>"
    And the "strategic advantage" list item at position "<index>" has copy "<copy>"

    Examples:
      | expected_count | index | title                       | copy              |
      | 3              | 1     | Digital Autonomy            | vendor lock-in    |
      | 3              | 2     | Operational Efficiency      | license fees      |
      | 3              | 3     | Future-Proof Adaptability   | evolving business |

  @whowedoitfor @strategicadvantage @responsive
  Scenario Outline: Verify strategic advantage image visibility by breakpoint
    When the <page> is viewed on a <device_type> device
    Then the <block_name> desktop image visibility is <desktop_visibility>
    And the <block_name> mobile image visibility is <mobile_visibility>

    Examples:
      | page             | device_type | block_name          | desktop_visibility | mobile_visibility |
      | who we do it for | desktop     | strategic advantage | visible            | hidden            |
      | who we do it for | mobile      | strategic advantage | hidden             | visible           |

  # ---------------------------------------------------------------------------
  # FINAL CTA
  # ---------------------------------------------------------------------------

  @whowedoitfor @finalcta @content @smoke
  Scenario Outline: Verify final CTA content presence and partial copy
    When the "final cta" container is displayed
    Then the <element_name> is visible and contains "<element_contains>"

    Examples:
      | element_name              | element_contains           |
      | final cta eyebrow text    | Take Control               |
      | final cta heading         | conversation               |
      | final cta intro text block| No pressure                |

  @whowedoitfor @finalcta @cta
  Scenario Outline: Final CTA provides a working Contact Us call to action
    When the "final cta" container is displayed
    Then the <element_name> is visible and contains "<expected_label>"
    And the <element_name> navigates to "<expected_url>"

    Examples:
      | element_name           | expected_label | expected_url                      |
      | final cta contact CTA  | Contact Us     | https://www.unipro.io/contact-us/ |
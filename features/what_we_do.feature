Feature: What We Do page - Content rendering, responsiveness, CTAs, and accessibility
  The "What we do" page should render all key sections, support responsive imagery, and provide working calls to action.

  Background:
    Given the user navigates to "/what-we-do/"

  # ---------------------------------------------------------------------------
  # STRUCTURAL PRESENCE
  # ---------------------------------------------------------------------------

  @whatwedo @structure @smoke @wip
  Scenario Outline: Verify key page sections are present in the DOM
    When the "<section_name>" container is displayed

    Examples:
      | section_name         |
      | hero                 |
      | build vs buy         |
      | our promise          |
      | unipro difference    |
      | final cta            |

  # ---------------------------------------------------------------------------
  # HERO SECTION
  # ---------------------------------------------------------------------------

  @whatwedo @hero @smoke
  Scenario Outline: Verify hero content presence and partial copy
    When the "hero" container is displayed
    Then the <element_name> is visible and contains "<element_contains>"

    Examples:
      | element_name          | element_contains                |
      | hero eyebrow text     | What we do                      |
      | hero heading          | BESPOKE SOFTWARE                |
      | hero intro text block | agentic AI orchestrated bespoke |

  @whatwedo @hero @responsive @desktop
  Scenario Outline: Verify hero image visibility on desktop
    When the <page> is viewed on a <device_type> device
    Then the "<visible_image>" visibility should be visible
    And the "<hidden_image>" visibility should be hidden

    Examples:
      | page         | device_type | visible_image      | hidden_image       |
      | what we do   | desktop     | desktop hero image | mobile hero image  |

  @whatwedo @hero @responsive @mobile
  Scenario Outline: Verify hero image visibility on mobile
    When the <page> is viewed on a <device_type> device
    Then the "<visible_image>" visibility should be visible
    And the "<hidden_image>" visibility should be hidden

    Examples:
      | page         | device_type | visible_image      | hidden_image       |
      | what we do   | mobile      | mobile hero image  | desktop hero image |

  # ---------------------------------------------------------------------------
  # BUILD VS BUY SECTION
  # ---------------------------------------------------------------------------

  @whatwedo @buildvsbuy @content
  Scenario Outline: Verify Build vs Buy section content presence and partial copy
    When the "build vs buy" container is displayed
    Then the <element_name> is visible and contains "<element_contains>"

    Examples:
      | element_name                    | element_contains                |
      | build vs buy eyebrow text       | Build vs Buy                    |
      | build vs buy heading            | strategic liability             |
      | build vs buy intro text block   | Off-the-Shelf Solutions         |

  @whatwedo @buildvsbuy @cta
  Scenario: Build vs Buy section provides a working Contact Us call to action
    When the "build vs buy" container is displayed
    Then the "build vs buy contact CTA" is visible and contains "Contact Us"
    And the "build vs buy contact CTA" links to "/contact-us/"

  @whatwedo @buildvsbuy @responsive
  Scenario Outline: Build vs Buy image visibility by breakpoint
    When the <page> is viewed on a <device_type> device
    Then the "<visible_image>" visibility should be visible
    And the "<hidden_image>" visibility should be hidden

    Examples:
      | page       | device_type | visible_image             | hidden_image                |
      | what we do | desktop     | build vs buy desktop image | build vs buy mobile image  |
      | what we do | mobile      | build vs buy mobile image  | build vs buy desktop image |

  # ---------------------------------------------------------------------------
  # OUR PROMISE SECTION
  # ---------------------------------------------------------------------------

  @whatwedo @ourpromise @content
  Scenario Outline: Verify Our Promise section content presence and partial copy
    When the "our promise" container is displayed
    Then the <element_name> is visible and contains "<element_contains>"

    Examples:
      | element_name                  | element_contains             |
      | our promise eyebrow text      | Our promise                  |
      | our promise heading           | Strategic Advantage          |
      | our promise intro text block  | gnarly problems              |

  @whatwedo @ourpromise @grid
  Scenario: Our Promise benefit list has exactly 3 items
    When the "our promise" container is displayed
    Then the "our promise" list has exactly "3" items

  @whatwedo @ourpromise @grid
  Scenario Outline: Our Promise benefit list items - titles and copy present
    When the "our promise" container is displayed
    Then the "our promise" list item at position "<index>" has title "<title>"
    Then the "our promise" list item at position "<index>" has copy "<copy>"

    Examples:
      | index | title                             | copy                        |
      | 1     | Unbeatable Competitive Edge        | strategic asset             |
      | 2     | Digital Autonomy and Full Control  | total control               |
      | 3     | Optimised Operational Efficiency   | 100% of your needs          |

  @whatwedo @ourpromise @cta
  Scenario: Our Promise section provides a working Contact Us call to action
    When the "our promise" container is displayed
    Then the "our promise contact CTA" is visible and contains "Contact Us"
    And the "our promise contact CTA" links to "/contact-us/"

  @whatwedo @ourpromise @responsive
  Scenario Outline: Our Promise image visibility by breakpoint
    When the <page> is viewed on a <device_type> device
    Then the "<visible_image>" visibility should be visible
    And the "<hidden_image>" visibility should be hidden

    Examples:
      | page       | device_type | visible_image              | hidden_image                |
      | what we do | desktop     | our promise desktop image  | our promise mobile image    |
      | what we do | mobile      | our promise mobile image   | our promise desktop image   |

  # ---------------------------------------------------------------------------
  # THE UNIPRO DIFFERENCE SECTION
  # ---------------------------------------------------------------------------

  @whatwedo @uniprodifference @content
  Scenario Outline: Verify The Unipro Difference section content presence and partial copy
    When the "unipro difference" container is displayed
    Then the <element_name> is visible and contains "<element_contains>"

    Examples:
      | element_name                        | element_contains        |
      | unipro difference eyebrow text      | Human-Led, AI Accelerated |
      | unipro difference heading           | The Unipro Difference   |
      | unipro difference intro text block  | 4D approach              |

  @whatwedo @uniprodifference @cta
  Scenario: The Unipro Difference section provides a working Contact Us call to action
    When the "unipro difference" container is displayed
    Then the "unipro difference contact CTA" is visible and contains "Contact Us"
    And the "unipro difference contact CTA" links to "/contact-us/"

  @whatwedo @uniprodifference @responsive
  Scenario Outline: The Unipro Difference image visibility by breakpoint
    When the <page> is viewed on a <device_type> device
    Then the "<visible_image>" visibility should be visible
    And the "<hidden_image>" visibility should be hidden

    Examples:
      | page       | device_type | visible_image                        | hidden_image                          |
      | what we do | desktop     | unipro difference desktop image      | unipro difference mobile image        |
      | what we do | mobile      | unipro difference mobile image       | unipro difference desktop image       |

  # ---------------------------------------------------------------------------
  # CTA SECTION
  # ---------------------------------------------------------------------------

  @whatwedo @finalcta @content @smoke
  Scenario Outline: Verify final CTA section content presence and partial copy
    When the "final cta" container is displayed
    Then the <element_name> is visible and contains "<element_contains>"

    Examples:
      | element_name              | element_contains          |
      | final cta eyebrow text    | technical debt             |
      | final cta heading         | complete control           |
      | final cta intro text block| No pressure, no commitment |

  @whatwedo @finalcta @cta
  Scenario: Final CTA section provides a working Contact Us call to action
    When the "final cta" container is displayed
    Then the "final cta button" is visible and contains "Contact Us"
    And the "final cta button" links to "/contact-us/"
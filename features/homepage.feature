Feature: Homepage marketing content and layout
  The homepage should present consistent marketing content, visual layout,
  testimonials, and client imagery across devices.

  Background:
    Given the user navigates to the Home page

  # ---------------------------------------------------------------------------
  # HERO SECTION
  # ---------------------------------------------------------------------------

  @structure
  Scenario Outline: Validate existence of key structural containers in the hero section
    Then the "<element_name>" container should exist

    Examples:
      | element_name       |
      | hero section       |
      | heading            |
      | intro feature text |

  @content
  Scenario Outline: Verify hero headline and feature text are displayed
    Then the hero heading text should equal "<expected_text>"
    And the intro feature text at position <paragraph_index> should equal "<paragraph_text>"

    Examples:
      | expected_text                           | paragraph_index | paragraph_text                                                                                                                                                                                                                                     |
      | BESPOKE SOFTWARE. UNRIVALLED ADVANTAGE. | 1               | We are a custom software studio that replaces outdated systems and technical constraints with lasting competitive advantage.                                                                                                                       |
      | BESPOKE SOFTWARE. UNRIVALLED ADVANTAGE. | 2               | With bespoke systems and Agentic AI, we eliminate the drain of legacy debt and unify your data, building bespoke solutions that seamlessly embed intelligence – anticipating needs, automating decisions, and driving immediate commercial impact. |
      | BESPOKE SOFTWARE. UNRIVALLED ADVANTAGE. | 3               | You define the roadmap. We create the advantage.                                                                                                                                                                                                   |

  @responsive @desktop
  Scenario Outline: Verify hero image visibility on Desktop
    When the homepage is viewed on a <device_type> device
    Then the "<visible_image>" visibility should be visible
    And the "<hidden_image>" visibility should be hidden

    Examples:
      | device_type | visible_image      | hidden_image      |
      | desktop     | desktop hero image | mobile hero image |

  @responsive @mobile
  Scenario Outline: Verify hero image visibility on Mobile
    When the homepage is viewed on a <device_type> device
    Then the "<visible_image>" visibility should be visible
    And the "<hidden_image>" visibility should be hidden

    Examples:
      | device_type | visible_image     | hidden_image       |
      | mobile      | mobile hero image | desktop hero image |

  # ---------------------------------------------------------------------------
  # "WHY" CONTENT BLOCK (The problem & the Guide)
  # ---------------------------------------------------------------------------

  @homepage @why-section @content
  Scenario Outline: Display of "why" content block (presence + partial content)
    When the "why" container is displayed
    Then the <element_name> is visible and contains "<element_contains>"

    Examples:
      | element_name     | element_contains        |
      | why eyebrow text     | PROBLEM                 |
      | why heading          | strategic liability     |
      | why intro text block | bespoke agentic         |
      | why call to action   | keeping you up at night |

  @homepage @why-section @navigation
  Scenario: Verify "why" section CTA redirect
    Then the call to action navigates to "https://www.unipro.io/contact-us/"


  @homepage @why-section @reponsive
  Scenario Outline: Responsive imagery for "why" content block
    When the homepage is viewed on a <device_type> device
    Then the <block_name> desktop image visibility is <desktop_image_visibility>
    And the <block_name> mobile image visibility is <mobile_image_visibility>

    Examples:
      | device_type | block_name | desktop_image_visibility | mobile_image_visibility |
      | desktop     | why        | visible                  | hidden                  |
      | mobile      | why        | hidden                   | visible                 |

  # ---------------------------------------------------------------------------
  # FEATURE BLOCK – "The Unipro advantage"
  # ---------------------------------------------------------------------------

  @homepage @feature-section
  Scenario Outline: Display of feature block content and CTA
    When the "feature" container is displayed
    Then the <element_name> is visible and contains "<element_contains>"
    # And the feature primary call-to-action button navigates to <button_target_url>

    Examples:
      | element_name             | element_contains     |
      | feature eyebrow text     | ADVANTAGE            |
      | feature heading          | Unrivalled Advantage |
      | feature intro text block | Strategic Definition |
      | feature call to action   | Contact Us           |

  @homepage @feature-section
  Scenario: Feature block imagery
    When the "feature" container is displayed
    Then the "feature image" is visible

  @homepage @feature-section @navigation
  Scenario: Verify "feature" section CTA redirect
    Then the call to action navigates to "https://www.unipro.io/contact-us/"
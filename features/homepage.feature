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
    Given I set the homepage viewport width to <viewportWidth>
    Then the "<visible_image>" visibility should be visible
    And the "<hidden_image>" visibility should be hidden

    Examples:
      | viewportWidth | visible_image      | hidden_image      |
      | 1920          | desktop hero image | mobile hero image |

  @responsive @mobile 
  Scenario Outline: Verify hero image visibility on Mobile
    Given I set the homepage viewport width to <viewportWidth>
    Then the "<visible_image>" visibility should be visible
    And the "<hidden_image>" visibility should be hidden

    Examples:
      | viewportWidth | visible_image     | hidden_image       |
      | 375           | mobile hero image | desktop hero image |

  # ---------------------------------------------------------------------------
  # "WHY" CONTENT BLOCK (The problem & the Guide)
  # ---------------------------------------------------------------------------

  @homepage @why-section @content @wip
  Scenario Outline: Display of "why" content block (presence + partial content + CTA)
    When the <block_name> container is displayed
    # Then the <block_name> eyebrow text is visible and contains "<eyebrow_contains>"
    # And the <block_name>" heading is visible and contains "<heading_contains>"
    # And the <block_name> intro text block is visible and contains "<intro_contains>"
    # And the "<block_name> call to action is visible and its text contains "<cta_text_contains>"
    # And the <block_name> call to action navigates to "<cta_target_url>"

    Examples:
      | block_name | eyebrow_contains | heading_contains    | intro_contains  | cta_text_contains       | cta_target_url                    |
      | why        | problem          | strategic liability | bespoke agentic | keeping you up at night | https://www.unipro.io/contact-us/ |

  @homepage @why-section @reponsive
  Scenario Outline: Responsive imagery for "why" content block
    When the homepage is viewed on a <device_type> device
    Then the "why" desktop image visibility is <desktop_image_visibility>
    And the "why" mobile image visibility is <mobile_image_visibility>

    Examples:
      | device_type | desktop_image_visibility | mobile_image_visibility |
      | desktop     | visible                  | hidden                  |
      | mobile      | hidden                   | visible                 |
      | tablet      | visible                  | hidden                  |


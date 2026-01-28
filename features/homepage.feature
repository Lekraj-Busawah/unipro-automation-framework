Feature: Hero Section Content and Rendering
  The hero section should display its heading, paragraphs, and responsive imagery correctly.

  Background:
    Given the user navigates to the Home page

  @structure
  Scenario Outline: Validate existence of key structural containers
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

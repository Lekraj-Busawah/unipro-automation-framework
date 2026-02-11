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
      | element_name            |
      | hero section            |
      | hero heading            |
      | hero intro feature text |

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
      | element_name         | element_contains        |
      | why eyebrow text     | PROBLEM                 |
      | why heading          | strategic liability     |
      | why intro text block | bespoke agentic         |
      | why call to action   | keeping you up at night |

  @homepage @why-section @navigation
  Scenario Outline: Verify "why" section CTA redirect
    Then the <element_name> navigates to "<expected_url>"

    Examples:
      | element_name       | expected_url                      |
      | why call to action | https://www.unipro.io/contact-us/ |

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
  Scenario Outline: Verify "feature" section CTA redirect
    Then the <element_name> navigates to "<expected_url>"
    Examples:
      | element_name           | expected_url                      |
      | feature call to action | https://www.unipro.io/contact-us/ |

  # ---------------------------------------------------------------------------
  # IMAGE GRID – CLIENTS
  # ---------------------------------------------------------------------------

  Scenario Outline: Display of image grid heading content
    When the "clients" container is displayed
    Then the <element_name> is visible and contains "<element_contains>"

    Examples:
      | element_name             | element_contains          |
      | clients eyebrow text     | TRUST                     |
      | clients heading          | demanding sectors         |
      | clients intro text block | custom software solutions |

  Scenario Outline: Image grid client tiles basic content and accessibility
    When the "clients" container is displayed
    Then the image grid has at least <tile_count> client tiles
    And the client tile at position <tile_position> has an associated image
    And the client tile at position <tile_position> link presence is <link_presence>

    Examples:
      | tile_count | tile_position | link_presence |
      | 12         | 1             | present       |
      | 12         | 2             | present       |
      | 12         | 3             | present       |
      | 12         | 4             | present       |
      | 12         | 5             | present       |
      | 12         | 6             | present       |
      | 12         | 7             | present       |
      | 12         | 8             | absent        |
      | 12         | 9             | absent        |
      | 12         | 10            | absent        |
      | 12         | 11            | absent        |
      | 12         | 12            | absent        |

  Scenario Outline: Image grid client tiles link targets for tiles with links
    When the "clients" container is displayed
    Then the client tile at position <tile_position> links to <client_pdf_url> in a new tab

    Examples:
      | tile_position | client_pdf_url                                                                                                                    |
      | 1             | https://www.unipro.io/wp-content/uploads/2025/07/Specsavers-Driving-E-Commerce-Innovation-2025-Stats-Version.pdf                  |
      | 2             | https://www.unipro.io/wp-content/uploads/2025/07/Jacobs-Modernising-Asset-Management-Systems-2025-Stats-Version.pdf               |
      | 3             | https://www.unipro.io/wp-content/uploads/2025/08/IFGL-Defining-and-Designing-a-Future-Ready-Digital-Portal-2025-Stats-Version.pdf |
      | 4             | https://www.unipro.io/wp-content/uploads/2025/07/Peninsula-Streamlining-Global-Payroll-2025-Stats-Version.pdf                     |
      # | 5             | https://www.unipro.io/wp-content/uploads/2025/07/PIAS-Success-Story-2025-Stats-Version.pdf |
      | 6             | https://www.unipro.io/wp-content/uploads/2025/07/PIAS-Success-Story-2025-Stats-Version.pdf                                        |
      | 7             | https://www.unipro.io/wp-content/uploads/2025/07/Montagu-Evans-Modernising-Business-Processes-2025-Stats-Version.pdf              |

  Scenario Outline: Image grid responsive imagery behaviour
    When the homepage is viewed on a <device_type> device
    Then each client tile desktop image visibility is <desktop_image_visibility>
    And each client tile mobile image visibility is <mobile_image_visibility>

    Examples:
      | device_type | desktop_image_visibility | mobile_image_visibility |
      | desktop     | visible                  | hidden                  |
      | mobile      | hidden                   | visible                 |

  # ---------------------------------------------------------------------------
  # TESTIMONIALS
  # ---------------------------------------------------------------------------

  Scenario Outline: Testimonials section heading and intro
    When the "testimonials" container is displayed
    Then the <element_name> is visible and contains "<element_contains>"

    Examples:
      | element_name                 | element_contains         |
      | testimonials eyebrow         | CUSTOMER QUOTES          |
      | testimonials heading         | don’t just take our word |
      | testimonials intro paragraph | Getting great feedback   |

  Scenario Outline: Individual testimonial contents
    When the "testimonials" container is displayed
    Then the testimonial at position <testimonial_position> has quote text <quote_text>
    And the testimonial at position <testimonial_position> has client name <client_name>

    Examples:
      | testimonial_position | quote_text                                                | client_name      |
      | 1                    | The value of working with Unipro                          | CHUCK FRANCESCHI |
      | 2                    | Thank you very much for your excellent and efficient work | LEYLA MENEKSE    |
      | 3                    | Unipro knows what they’re doing — they just get it.       | TAG GUILLORY     |
      | 4                    | Our experience with Unipro has been exceptional           | TOMAS MAAGS      |

  Scenario: Testimonials section decorative icon
    When the "testimonials" container is displayed
    Then the "testimonial decorative icon" is visible

  # ---------------------------------------------------------------------------
  # CTA BLOCK – "Secure your digital autonomy"
  # ---------------------------------------------------------------------------

  Scenario Outline: CTA block content and button behaviour
    When the "CTA" container is displayed
    Then the <element_name> is visible and contains "<element_contains>"

    Examples:
      | element_name         | element_contains           |
      | CTA eyebrow          | BEYOND SOLVING PROBLEMS    |
      | CTA heading          | digital autonomy           |
      | CTA intro text block | No pressure, no commitment |
      | CTA button           | Contact Us                 |
  
  Scenario Outline: Verify "Contact Us" section CTA redirect
    Then the <element_name> navigates to "<expected_url>"

    Examples:
      | element_name | expected_url                      |
      | CTA button   | https://www.unipro.io/contact-us/ |
Feature: Contact Us page - Content rendering and form availability
  The Contact Us page should render its hero, "Get in touch" section and the embedded contact form, with responsive hero images.

  Background:
    Given the user navigates to "/contact-us/"

  # ---------------------------------------------------------------------------
  # STRUCTURAL PRESENCE
  # ---------------------------------------------------------------------------

  @contactus @structure @smoke
  Scenario Outline: Verify key page sections are present in the DOM
    Then the "<section_name>" container should exist

    Examples:
      | section_name  |
      | hero          |
      | get in touch  |
      | contact form  |

  # ---------------------------------------------------------------------------
  # HERO SECTION
  # ---------------------------------------------------------------------------

  @contactus @hero @content @smoke
  Scenario Outline: Verify hero content presence and partial copy
    When the "hero" container is displayed
    Then the <element_name> is visible and contains "<element_contains>"

    Examples:
      | element_name    | element_contains |
      | hero eyebrow    | CONTACT US       |
      | hero heading    | how we can help  |
      | hero intro text | No pressure      |

  @contactus @hero @responsive
  Scenario Outline: Verify hero image visibility by breakpoint
    When the <page> is viewed on a <device_type> device
    Then the "<desktop_image>" visibility should be <desktop_visibility>
    And the "<mobile_image>" visibility should be <mobile_visibility>

    Examples:
      | page        | device_type | desktop_image      | desktop_visibility | mobile_image      | mobile_visibility |
      | contact-us  | desktop     | hero desktop image | visible            | hero mobile image | hidden            |
      | contact-us  | mobile      | hero desktop image | hidden             | hero mobile image | visible           |

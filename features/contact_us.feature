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
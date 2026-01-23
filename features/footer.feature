Feature: Website Footer Content and Navigation
  The footer provides branding, contact information, office addresses,
  social media access, and mandatory policy links.
  It must be consistently visible, accurate, and accessible across the site.

  Background:
    Given the user is viewing any public page on the website
    And the footer container is visible

  Scenario Outline: Footer is visibly rendered with correct branding
    Then the footer displays the company logo
    And the footer displays the company tagline "<expected_tagline>"

    Examples:
      | expected_tagline     |
      | A safe pair of hands |

  Scenario: Company logo navigates to the homepage
    When the user clicks the company logo
    Then the user is navigated to the homepage

  Scenario Outline: Footer displays valid company contact email
    Then the footer contains a contact email link
    And the email address is "<expected_email>"

    Examples:
      | expected_email |
      | info@unipro.io |

  Scenario: Footer displays available office locations
    Then the footer displays the London office section
    And the footer displays the Havant office section

  Scenario Outline: Footer displays complete office details
    Then the "<office>" address displays "<street>", "<city>", "<postcode>" and "<telephone>"

    Examples:
      | office | street                        | city   | postcode | telephone           |
      | Havant | Langstone Gate Solent Road    | Havant | PO9 1TR  | +44 (0) 1243 539412 |
      | London | 167-169 Great Portland Street | London | W1W 5PF  | +44 (0) 2034 439203 |

  Scenario Outline: Social media links open in a new browser tab
    Then the "<social>" link is visible in the footer
    And the "<social>" link opens in a new browser tab

    Examples:
      | social   |
      | LinkedIn |
      | YouTube  |

  Scenario Outline: Footer policy links navigate to the correct destinations
    When the user clicks the "<policy>" link in the footer
    Then the user is navigated to the "<policy>" page

    Examples:
      | policy          |
      | Privacy Policy  |
      | Cookie Policy   |
      | Security Policy |
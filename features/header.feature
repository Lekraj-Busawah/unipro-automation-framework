
Feature: Header navigation and branding
  As a visitor
  I want to see a clear, functional header
  So that I can navigate key sections and return to the homepage

  Background:
    Given I open the homepage


  Scenario: Header exists and logo is visible
    Then the header should be visible
    And the logo in the header should be visible


  Scenario: Header navigation menu is visible
    When the header is displayed
    Then I should see the primary navigation menu


  Scenario Outline: Navigation menu items redirect correctly
    Given I open the homepage
    When I click the "<menuItem>" link in the header
    Then I should be navigated to the "<expectedPath>" URL

    Examples:
      | menuItem         | expectedPath     |
      | who_we_are       | who-we-are       |
      | what_we_do       | what-we-do       |
      | who_we_do_it_for | who-we-do-it-for |
      | contact_us       | contact-us       |
      | careers          | careers          |

  @mobile @wip
  Scenario Outline: Header adapts to responsive breakpoints
    When the header is viewed on a <device_type> device
    Then the header layout should adjust to the <device_type> layout

    Examples:
      | device_type | 
      | mobile      |
      | tablet      |
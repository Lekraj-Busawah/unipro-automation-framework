Feature: Who We Are page - Content rendering, responsiveness, and CTAs
    The "Who we are" page should render all key sections, support responsive imagery,
    and provide working calls to action.

    Background:
        Given the user navigates to "/who-we-are/"

    # ---------------------------------------------------------------------------
    # HERO SECTION
    # ---------------------------------------------------------------------------

    @whoweare @hero @smoke
    Scenario Outline: Verify hero content presence and partial copy
        When the "hero section" container is displayed
        Then the <element_name> is visible and contains "<element_contains>"

        Examples:
            | element_name         | element_contains                         |
            | who eyebrow text     | WHO WE ARE                               |
            | who heading          | BESPOKE SOFTWARE                         |
            | who intro text block | team of inquisitive software specialists |

    @whoweare @hero @responsive @desktop
    Scenario Outline: Verify "Who We Are" hero image visibility on Desktop
        When the <page> is viewed on a <device_type> device
        Then the "<visible_image>" visibility should be visible
        And the "<hidden_image>" visibility should be hidden

        Examples:
            | page       | device_type | visible_image      | hidden_image      |
            | who we are | desktop     | desktop hero image | mobile hero image |

    @whoweare @hero @responsive @mobile
    Scenario Outline: Verify "Who We Are" hero image visibility on Moblie
        When the <page> is viewed on a <device_type> device
        Then the "<visible_image>" visibility should be visible
        And the "<hidden_image>" visibility should be hidden

        Examples:
            | page       | device_type | visible_image     | hidden_image       |
            | who we are | mobile      | mobile hero image | desktop hero image |

    # ---------------------------------------------------------------------------
    # TEAM SECTION
    # ---------------------------------------------------------------------------

    @whoweare @team @content
    Scenario Outline: Team section container, headings, and intro presence
        When the "team" container is displayed
        Then the <element_name> is visible and contains "<element_contains>"

        Examples:
            | element_name          | element_contains               |
            | team eyebrow text     | INQUISITIVE TEAM               |
            | team heading          | strategic partner              |
            | team intro text block | human-led, transparent process |


    @whoweare @team @responsive
    Scenario Outline: Team section image visibility and loading by breakpoint
        When the homepage is viewed on a <device_type> device
        Then the <block_name> desktop image visibility is <desktop_image_visibility>

        Examples:
            | page       | device_type | block_name | desktop_image_visibility |
            | who we are | desktop     | team       | visible                  |
            | who we are | mobile      | team       | hidden                   |

    # ---------------------------------------------------------------------------
    # CULTURE SECTION
    # ---------------------------------------------------------------------------

    @whoweare @culture @content
    Scenario Outline: Culture section container and copy presence
        When the "culture" container is displayed
        Then the <element_name> is visible and contains "<element_contains>"

        Examples:
            | element_name             | element_contains        |
            | culture eyebrow text     | FOUNDATIONAL PRINCIPLES |
            | culture heading          | Autonomy                |
            | culture intro text block | Our culture             |

    @whoweare @culture @grid
    Scenario: Culture grid has exactly 4 principles
        When the "culture" container is displayed
        Then the "culture" grid has exactly "4" items

    @whoweare @culture @grid
    Scenario Outline: Culture grid items - titles present
        When the "culture" container is displayed
        Then the "culture" grid item at position "<index>" has title "<title>"
        Then the "culture" grid item at position "<index>" has copy "<copy>"


        Examples:
            | index | title                   | copy                                          |
            | 1     | Make it Happen          | dissect complex issues                        |
            | 2     | Make it Better          | relentless drive for improvement              |
            | 3     | Accountable Partnership | honesty, respect, listening, and transparency |
            | 4     | Embrace Empowerment     | complete control                              |
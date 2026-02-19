from behave import *
from pages.who_we_are import WhoWeAre

# ---------------------------------------------------------------------------
# HERO SECTION
# ---------------------------------------------------------------------------

@given(u'the user navigates to "{path}"')
def step_impl(context, path):
    context.current_page = WhoWeAre(context.driver)
    context.current_page.navigate_to_url(path)


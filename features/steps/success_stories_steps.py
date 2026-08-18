from behave import *
from selenium.webdriver.common.keys import Keys

# ---------------------------------------------------------------------------
# SEARCH
# ---------------------------------------------------------------------------

@when(u'the user searches the success stories for "{search_term}"')
def step_impl(context, search_term):
    context.current_page.enter_text("search input", search_term)
    context.current_page.get_element("search input").send_keys(Keys.RETURN)

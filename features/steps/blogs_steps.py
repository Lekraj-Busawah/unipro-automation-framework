from behave import *
from selenium.webdriver.common.keys import Keys

# ---------------------------------------------------------------------------
# SEARCH
# ---------------------------------------------------------------------------

@when(u'the user searches the blogs for "{search_term}"')
def step_impl(context, search_term):
    context.current_page.enter_text("search input", search_term)
    context.current_page.get_element("search input").send_keys(Keys.RETURN)

@then(u'the browser navigates to a URL containing "{expected_query_param}"')
def step_impl(context, expected_query_param):
    context.current_page.wait_for_url_to_contain(expected_query_param)
    actual_url = context.current_page.get_url()
    assert expected_query_param in actual_url, f"Expected '{expected_query_param}' to be in URL '{actual_url}'"
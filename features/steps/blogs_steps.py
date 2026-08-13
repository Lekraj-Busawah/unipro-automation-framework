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

# ---------------------------------------------------------------------------
# BLOG CARD GRID
# ---------------------------------------------------------------------------

@then(u'the {grid_name} has at least "{minimum_count}" cards')
def step_impl(context, grid_name, minimum_count):
    minimum_count = int(minimum_count)
    actual_count = context.current_page.get_blog_card_grid_count(grid_name)
    assert actual_count >= minimum_count, f"Expected at least '{minimum_count}' cards, but found '{actual_count}'"


@then(u'the {element_name} at position "{index}" has a working "Read more" link')
def step_impl(context, element_name, index):
    locator_key = f"{element_name} read more link"
    href = context.current_page.get_href_at_position(locator_key, position=index)
    assert href, f"No 'Read more' link found on the {element_name} at position {index}"

    status = context.current_page.get_http_status(href)
    assert status == 200, f"Expected 'Read more' link '{href}' to return 200 but got {status}"
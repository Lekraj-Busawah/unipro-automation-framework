from behave import *
from pages.blogs import Blogs
from pages.homepage import Homepage
from pages.who_we_are import WhoWeAre
from pages.what_we_do import WhatWeDo
from pages.who_we_do_it_for import WhoWeDoItFor

# ---------------------------------------------------------------------------
# SHARED NAVIGATION STEPS
# ---------------------------------------------------------------------------

# Maps URL path to Page Object
PAGE_REGISTRY = {
    "/": Homepage,
    "/who-we-are/": WhoWeAre,
    "/what-we-do/": WhatWeDo,
    "/who-we-do-it-for/": WhoWeDoItFor,
    "/blogs/": Blogs
}

@given(u'the user navigates to "{path}"')
def step_impl(context, path):
    page_class = PAGE_REGISTRY[path]
    context.current_page = page_class(context.driver)
    context.current_page.navigate_to_url(path)

@then(u'the {element_name} is visible and contains "{element_contains}"')
def step_impl(context, element_name, element_contains):
    is_visible = context.current_page.is_element_displayed(element_name)
    assert is_visible is True, f"The {element_name} container was not visible on the page!"
    actual_text = context.current_page.get_element_text(element_name)
    assert element_contains in actual_text, f"Expected text to contain '{element_contains}' but found {actual_text}"

@then(u'the "{section}" list has exactly "{expected_count}" items')
def step_impl(context, section, expected_count):
    locator_key = f"{section} list"
    elements_list = context.current_page.get_elements(locator_key)
    actual_count = len(elements_list)
    assert actual_count == int(expected_count), f"Expected {expected_count} items in the {locator_key} list, but found {actual_count}"

@then(u'the "{section}" list item at position "{index}" has title "{title}"')
def step_impl(context, section, index, title):
    locator_key = f"{section} list item"
    element = context.current_page.get_element_at_position(locator_key, position=index)
    actual_text = element.text.strip()
    assert title in actual_text, f"Expected title to be '{title}' but found '{actual_text}'"

@then(u'the "{section}" list item at position "{index}" has copy "{copy}"')
def step_impl(context, section, index, copy):
    locator_key = f"{section} list item"
    element = context.current_page.get_element_at_position(locator_key, position=index)
    actual_text = element.text.strip()
    assert copy in actual_text, f"Expected copy to be '{copy}' but found '{actual_text}'"

@then(u'the {element_name} navigates to "{expected_url}"')
def step_impl(context, element_name, expected_url):
    context.current_page.click_element(context.current_page.locators[element_name])

    context.current_page.wait_for_url_to_be(expected_url)

    actual_url = context.current_page.get_url()

    assert actual_url == expected_url, f"Expected {expected_url} but got {actual_url}"

    status = context.current_page.get_http_status(expected_url)
    assert status == 200, f"Expected 200 but got {status}"

@then(u'the {element_name} at position "{index}" links to "{expected_url}"')
def step_impl(context, element_name, index, expected_url):
    context.current_page.click_element_at_position(element_name, position=index)

    context.current_page.wait_for_url_to_contain(expected_url)

    actual_url = context.current_page.get_url()

    assert expected_url in actual_url, f"Expected URL to contain '{expected_url}' but got '{actual_url}'"

    status = context.current_page.get_http_status(actual_url)
    assert status == 200, f"Expected 200 but got {status}"
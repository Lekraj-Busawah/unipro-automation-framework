from behave import *
from pages.homepage import Homepage
from pages.who_we_are import WhoWeAre
from pages.what_we_do import WhatWeDo

# ---------------------------------------------------------------------------
# SHARED NAVIGATION STEPS
# ---------------------------------------------------------------------------

# Maps URL path to Page Object
PAGE_REGISTRY = {
    "/who-we-are/": WhoWeAre,
    "/what-we-do/": WhatWeDo,
    "/": Homepage,
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


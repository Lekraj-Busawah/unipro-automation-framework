from behave import *
from pages.who_we_are import WhoWeAre
from pages.what_we_do import WhatWeDo

# ---------------------------------------------------------------------------
# SHARED NAVIGATION STEPS
# ---------------------------------------------------------------------------

# Maps URL path to Page Object
PAGE_REGISTRY = {
    "/who-we-are/": WhoWeAre,
    "/what-we-do/": WhatWeDo,
}

@given(u'the user navigates to "{path}"')
def step_impl(context, path):
    page_class = PAGE_REGISTRY[path]
    context.current_page = page_class(context.driver)
    context.current_page.navigate_to_url(path)

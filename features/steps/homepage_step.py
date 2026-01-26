from behave import *
from pages.footer import Footer
import time

@given(u'the user navigates to the Home page')
def step_impl(context):
    pass


@then(u'the "{element_name}" container should exist')
def step_impl(context):
    pass


@then(u'the hero heading should be visible')
def step_impl(context):
    pass


@then(u'the hero heading text should equal "{heading_text}"')
def step_impl(context):
    pass


@then(u'the intro feature text at position {paragraph_index} should equal "{paragraph_text}"')
def step_impl(context):
    pass


@given(u'the viewport is set to "{viewport}"')
def step_impl(context):
    pass


@then(u'the "{visible_image}" should be visible')
def step_impl(context):
    pass


@then(u'the "{hidden_image}" should not be visible')
def step_impl(context):
    pass

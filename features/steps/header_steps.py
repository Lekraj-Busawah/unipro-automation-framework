from behave import *
from pages.header import Header

# Scenario: Header exists and logo is visible
@given(u'I open the homepage')
def step_impl(context):
    context.driver.get(context.base_url)
    context.header = Header(context.driver)
    context.header.handle_cookie_consent()


@then(u'the header should be visible')
def step_impl(context):
    context.header.check_header_visible()


@then(u'the logo in the header should be visible')
def step_impl(context):
    context.header.check_logo_visible()


# Scenario: Header navigation menu is visible
@when(u'the header is displayed')
def step_impl(context):
    context.header.check_header_visible()


@then(u'I should see the primary navigation menu')
def step_impl(context):
    context.header.check_main_menu_visible()


# Scenario Outline: Navigation menu items redirect correctly
@when(u'I click the "{menu_item}" link in the header')
def step_impl(context, menu_item):
    context.header.check_header_visible()
    context.header.click_menu_item(menu_item)


@then(u'I should be navigated to the "{expected_path}" URL')
def step_impl(context, expected_path):
    context.header.verify_page_navigation_by_url(expected_path)


# Scenario Outline: Header adapts to responsive breakpoints
@when(u'the header is viewed on a {device_type} device')
def step_impl(context, device_type):
    # Delegate to the Page Object
    context.header.set_viewport_size(device_type)


@then(u'the header layout should adjust to the {device_type} layout')
def step_impl(context, device_type):
    if device_type in ['mobile', 'tablet']:
        assert context.header.is_hamburger_visible(), \
            f"Hamburger menu not visible in {device_type} layout"
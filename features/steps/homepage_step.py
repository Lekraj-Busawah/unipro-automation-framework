from behave import *
from pages.homepage import Homepage

# ---------------------------------------------------------------------------
# HERO SECTION
# ---------------------------------------------------------------------------

@given(u'the user navigates to the Home page')
def step_impl(context):
    context.homepage = Homepage(context.driver)
    context.homepage.navigate_to_base_url()


@then(u'the "{element_name}" container should exist')
def step_impl(context, element_name):
    is_visible = context.homepage.is_element_displayed(element_name)
    assert is_visible, f"The {element_name} container was not visible on the page."


@then(u'the hero heading text should equal "{expected_text}"')
def step_impl(context, expected_text):
    actual_text = context.homepage.get_element_text("hero heading")
    
    assert actual_text == expected_text, f"Expected '{expected_text}' but found '{actual_text}'" 

@then(u'the intro feature text at position {paragraph_index} should equal "{paragraph_text}"')
def step_impl(context, paragraph_index, paragraph_text):
    key = int(paragraph_index)
    
    actual_text = context.homepage.get_element_text(key)
    
    assert actual_text == paragraph_text, f"Expected '{paragraph_text}' but found '{actual_text}'"

@given(u'I set the homepage viewport width to {viewportWidth}')
def step_impl(context, viewportWidth):
    context.homepage.set_viewport_size(int(viewportWidth))


@then(u'the "{image_name}" visibility should be {expected_status}')
def step_impl(context, image_name, expected_status):
    # assign should_be_visible either true or false depending on 'expected_status' string
    should_be_visible = (expected_status == "visible")

    is_visible = context.homepage.is_element_displayed(image_name)
    
    assert is_visible == should_be_visible, f"Error: {image_name} was expected to be {expected_status}."
# ---------------------------------------------------------------------------
# "WHY" CONTENT BLOCK (The problem & the Guide)
# ---------------------------------------------------------------------------

@when(u'the "{block_name}" container is displayed')
def step_impl(context, block_name):
    is_visible = context.homepage.is_element_displayed(block_name)
    assert is_visible is True, f"The {block_name} container was not visible on the page!"

@then(u'the {element_name} is visible and contains "{element_contains}"')
def step_impl(context, element_name, element_contains):
    is_visible = context.homepage.is_element_displayed(element_name)
    assert is_visible is True, f"The {element_name} container was not visible on the page!"
    actual_text = context.homepage.get_element_text(element_name)
    assert element_contains in actual_text, f"Expected text to contain '{element_contains}' but found {actual_text}"


@then(u'the call to action navigates to "{expected_url}"')
def step_impl(context, expected_url):
    context.homepage.click_element(context.homepage.locators["call to action"])

    context.homepage.wait_for_url_to_be(expected_url)

    actual_url = context.homepage.get_url()

    assert actual_url == expected_url, f"Expected {expected_url} but got {actual_url}"

    status = context.homepage.get_http_status(expected_url)
    assert status == 200, f"Expected 200 but got {status}"


@when(u'the homepage is viewed on a {device_type} device')
def step_impl(context, device_type):
    context.homepage.set_viewport_size(device_type)
    context.driver.refresh()


@then(u'the {block_name} desktop image visibility is {expected_visibility}')
def step_impl(context, block_name, expected_visibility):
    # Create the key: "why desktop image"
    locator_key = f"{block_name} desktop image"
    
    is_visible = context.homepage.is_element_displayed(locator_key)
    actual = "visible" if is_visible else "hidden"
    
    assert actual == expected_visibility, \
        f"Responsive Error: {locator_key} should be {expected_visibility} on {context.current_device}"


@when(u'the {block_name} mobile image visibility is {mobile_image_visibility}')
def step_impl(context, block_name, mobile_image_visibility):
    # Create the key: "why mobile image"
    locator_key = f"{block_name} mobile image"
    
    is_visible = context.homepage.is_element_displayed(locator_key)
    actual = "visible" if is_visible else "hidden"
    
    assert actual == mobile_image_visibility, \
        f"Responsive Error: {locator_key} should be {mobile_image_visibility} on {context.current_device}"

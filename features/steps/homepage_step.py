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
    is_visible = context.homepage.is_visible(element_name)
    assert is_visible, f"The {element_name} container was not visible on the page."


@then(u'the hero heading text should equal "{expected_text}"')
def step_impl(context, expected_text):
    actual_text = context.homepage.get_element_text("heading")
    
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

    is_visible = context.homepage.is_visible(image_name)
    
    assert is_visible == should_be_visible, f"Error: {image_name} was expected to be {expected_status}."
# ---------------------------------------------------------------------------
# "WHY" CONTENT BLOCK (The problem & the Guide)
# ---------------------------------------------------------------------------

@when(u'the {block_name} container is displayed')
def step_impl(context, block_name):
    is_visible = context.homepage.is_visible(block_name)
    assert is_visible is True, f"The {block_name} container was not visible on the page!"

@then(u'the {block_name} eyebrow text is visible and contains "{eyebrow_contains}"')
def step_impl(context):
    pass


@then(u'the {block_name} heading is visible and contains "{heading_contains}"')
def step_impl(context):
    pass


@then(u'the {block_name} intro text block is visible and contains "{intro_contains}"')
def step_impl(context):
    pass


@then(u'the {block_name} call to action is visible and its text contains "{cta_text_contains}"')
def step_impl(context):
    pass


@then(u'the {block_name} call to action navigates to "{cta_target_url}"')
def step_impl(context):
    pass


@when(u'the homepage is viewed on a {device_type} device')
def step_impl(context):
    pass


@then(u'the {block_name} desktop image visibility is {desktop_image_visibility}')
def step_impl(context):
    pass


@then(u'the {block_name} mobile image visibility is {mobile_image_visibility}')
def step_impl(context):
    pass


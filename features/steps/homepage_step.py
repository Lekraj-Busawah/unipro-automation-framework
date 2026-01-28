from behave import *
from pages.homepage import Homepage

@given(u'the user navigates to the Home page')
def step_impl(context):
    context.homepage = Homepage(context.driver)
    context.homepage.navigate_to_base_url()


@then(u'the "{element_name}" container should exist')
def step_impl(context, element_name):
    is_visible = context.homepage.is_container_visible(element_name)
    assert is_visible, f"The {element_name} container was not visible on the page."


@then(u'the hero heading text should equal "{expected_text}"')
def step_impl(context, expected_text):
    actual_text = context.homepage.get_hero_heading_text()
    assert actual_text == expected_text, f"Expected '{expected_text}' but found '{actual_text}'"
    

@then(u'the intro feature text at position {paragraph_index} should equal "{paragraph_text}"')
def step_impl(context, paragraph_index, paragraph_text):
    actual_text = context.homepage.get_paragraph_text(paragraph_index)
    assert actual_text == paragraph_text, f"Expected '{paragraph_index}' but found '{actual_text}'"


@given(u'I set the homepage viewport width to {viewportWidth}')
def step_impl(context, viewportWidth):
    context.homepage.set_viewport_size(int(viewportWidth))


@then(u'the "{image_name}" visibility should be {expected_status}')
def step_impl(context, image_name, expected_status):
    # assign should_be_visible either true or false depending on 'expected_status' string
    should_be_visible = (expected_status == "visible")

    is_visible = context.homepage.is_image_visible(image_name)
    
    assert is_visible == should_be_visible, f"Error: {image_name} was expected to be {expected_status}."

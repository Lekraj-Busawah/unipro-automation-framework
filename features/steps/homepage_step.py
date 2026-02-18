from behave import *
from pages.homepage import Homepage

# ---------------------------------------------------------------------------
# HERO SECTION
# ---------------------------------------------------------------------------

@given(u'the user navigates to the Home page')
def step_impl(context):
    context.current_page = Homepage(context.driver)
    context.current_page.navigate_to_base_url()


@then(u'the "{element_name}" container should exist')
def step_impl(context, element_name):
    is_visible = context.current_page.is_element_displayed(element_name)
    assert is_visible, f"The {element_name} container was not visible on the page."


@then(u'the hero heading text should equal "{expected_text}"')
def step_impl(context, expected_text):
    actual_text = context.current_page.get_element_text("hero heading")
    
    assert actual_text == expected_text, f"Expected '{expected_text}' but found '{actual_text}'" 

@then(u'the intro feature text at position {paragraph_index} should equal "{paragraph_text}"')
def step_impl(context, paragraph_index, paragraph_text):
    key = int(paragraph_index)
    
    actual_text = context.current_page.get_element_text(key)
    
    assert actual_text == paragraph_text, f"Expected '{paragraph_text}' but found '{actual_text}'"

@given(u'I set the homepage viewport width to {viewportWidth}')
def step_impl(context, viewportWidth):
    context.current_page.set_viewport_size(int(viewportWidth))


@then(u'the "{image_name}" visibility should be {expected_status}')
def step_impl(context, image_name, expected_status):
    # assign should_be_visible either true or false depending on 'expected_status' string
    should_be_visible = (expected_status == "visible")

    is_visible = context.current_page.is_element_displayed(image_name)
    
    assert is_visible == should_be_visible, f"Error: {image_name} was expected to be {expected_status}."
# ---------------------------------------------------------------------------
# "WHY" CONTENT BLOCK (The problem & the Guide)
# ---------------------------------------------------------------------------

@when(u'the "{block_name}" container is displayed')
def step_impl(context, block_name):
    is_visible = context.current_page.is_element_displayed(block_name)
    assert is_visible is True, f"The {block_name} container was not visible on the page!"

@then(u'the {element_name} is visible and contains "{element_contains}"')
def step_impl(context, element_name, element_contains):
    is_visible = context.current_page.is_element_displayed(element_name)
    assert is_visible is True, f"The {element_name} container was not visible on the page!"
    actual_text = context.current_page.get_element_text(element_name)
    assert element_contains in actual_text, f"Expected text to contain '{element_contains}' but found {actual_text}"


@then(u'the {element_name} navigates to "{expected_url}"')
def step_impl(context, element_name, expected_url):
    context.current_page.click_element(context.current_page.locators[element_name])

    context.current_page.wait_for_url_to_be(expected_url)

    actual_url = context.current_page.get_url()

    assert actual_url == expected_url, f"Expected {expected_url} but got {actual_url}"

    status = context.current_page.get_http_status(expected_url)
    assert status == 200, f"Expected 200 but got {status}"


@when(u'the homepage is viewed on a {device_type} device')
def step_impl(context, device_type):
    context.current_page.set_viewport_size(device_type)
    context.driver.refresh()


@then(u'the {block_name} desktop image visibility is {expected_visibility}')
def step_impl(context, block_name, expected_visibility):
    # Create the key: "why desktop image"
    locator_key = f"{block_name} desktop image"
    
    is_visible = context.current_page.is_element_displayed(locator_key)
    actual = "visible" if is_visible else "hidden"
    
    assert actual == expected_visibility, \
        f"Responsive Error: {locator_key} should be {expected_visibility} on {context.current_device}"


@then(u'the {block_name} mobile image visibility is {mobile_image_visibility}')
def step_impl(context, block_name, mobile_image_visibility):
    # Create the key: "why mobile image"
    locator_key = f"{block_name} mobile image"
    
    is_visible = context.current_page.is_element_displayed(locator_key)
    actual = "visible" if is_visible else "hidden"
    
    assert actual == mobile_image_visibility, \
        f"Responsive Error: {locator_key} should be {mobile_image_visibility} on {context.current_device}"
    
# ---------------------------------------------------------------------------
# FEATURE BLOCK – "The Unipro advantage"
# ---------------------------------------------------------------------------

@then(u'the "{element_name}" is visible')
def step_impl(context, element_name):
    is_visible = context.current_page.is_element_displayed(element_name)
    assert is_visible is True, f"The {element_name} container was not visible on the page!"

# ---------------------------------------------------------------------------
# IMAGE GRID – CLIENTS
# ---------------------------------------------------------------------------

@then(u'the image grid has at least {tile_count} client tiles')
def step_impl(context, tile_count):
    count = context.current_page.get_number_tiles()
    assert count == int(tile_count), f"Expected at least {tile_count} client tiles, but found {count}"

@then(u'the client tile at position {tile_position} has an associated image')
def step_impl(context, tile_position):
    tile = context.current_page.get_tile_at_position(tile_position)
    desktop_img = context.current_page.get_desktop_image_from_tile(tile)
    assert desktop_img.get_attribute("src"), f"Tile {tile_position} desktop image has no src"


@then(u'the client tile at position {tile_position} link presence is {link_presence}')
def step_impl(context, tile_position, link_presence):
    tile = context.current_page.get_tile_at_position(tile_position)
    has_link = context.current_page.tile_has_link(tile)

    if link_presence == "present":
            assert has_link, f"Expected link in tile {tile_position}, but none found"
    else:
        assert not has_link, f"Expected no link in tile {tile_position}, but a link was found"

@then(u'the client tile at position {tile_position} links to {client_pdf_url} in a new tab')
def step_impl(context, tile_position, client_pdf_url):

    tile = context.current_page.get_tile_at_position(tile_position)

    actual_href = context.current_page.get_link_href_from_tile(tile)
    actual_target = context.current_page.get_link_target_from_tile(tile)

    assert actual_href == client_pdf_url, "Expected tile {tile_position} to have a link but none was found"
    assert actual_target == "_blank", f"Expected tile {tile_position} to open in a new tab (target=_blank), but target was '{actual_target}'"

@then(u'each client tile desktop image visibility is {expected_state}')
def step_impl(context, expected_state):

    tiles = context.current_page.get_client_tiles()

    for id, tile in enumerate(tiles, start=1):
        desktop_img = context.current_page.get_desktop_image_from_tile(tile)
        is_visible = desktop_img.is_displayed()

        expected = (expected_state == "visible")
        assert is_visible == expected, ( 
            f"Desktop image for tile {id} was "
            f"{'visible' if is_visible else 'hidden'}, "
            f"but expected {expected_state}"
        )

@then("each client tile mobile image visibility is {expected_state}")
def step_impl(context, expected_state):
    tiles = context.current_page.get_client_tiles()

    for id, tile in enumerate(tiles, start=1):
        mobile_img = context.current_page.get_mobile_image_from_tile(tile)
        is_visible = mobile_img.is_displayed()

        expected = (expected_state == "visible")
        assert is_visible == expected, (
            f"Mobile image for tile {id} was "
            f"{'visible' if is_visible else 'hidden'}, "
            f"but expected {expected_state}"
        )

@then(u'the testimonial at position {testimonial_position} has quote text {quote_text}')
def step_impl(context, testimonial_position, quote_text):
    testimonial = context.current_page.get_testimonial_at_position(testimonial_position)
    assert quote_text in testimonial.text, f"Expected testimonial {testimonial_position} to contain '{quote_text}' but found '{testimonial.text}'"
 
@then(u'the testimonial at position {testimonial_position} has client name {client_name}')
def step_impl(context, testimonial_position, client_name):
    client = context.current_page.get_testimonial_client_at_position(testimonial_position)
    assert client_name in client.text, f"Expected client name for testimonial at poition {testimonial_position} to be '{client_name}' but found '{client.text}'"
 
@when(u'each testimonial item includes a decorative icon')
def step_impl(context):
    assert context.current_page.is_element_displayed("testimonial decorative icon"), "Testimonial decorative icons are not visible."
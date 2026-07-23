from behave import *

# ---------------------------------------------------------------------------
# HERO SECTION
# ---------------------------------------------------------------------------

@then(u'the "{culture}" grid has exactly "4" items')
def step_impl(context, culture):

    locator_key = f"{culture} grid item"

    grid_items = context.current_page.get_culture_grid_items(locator_key)
    grid_item_length = len(grid_items)
    assert grid_item_length == 4, f"Expected 4 items in the grid but found {grid_item_length}"

@then(u'the "{culture}" grid item at position "{position_index}" has title "{title}"')
def step_impl(context, culture, position_index, title):

    locator_key = f"{culture} grid item title"

    item = context.current_page.get_culture_grid_items_at_index(locator_key, int(position_index))
    item_title = item.text
    assert item_title == title, f"Expected title at position {position_index} to be {title} but found {item_title}"
    
@then(u'the "{culture}" grid item at position "{position_index}" has copy "{copy}"')
def step_impl(context, culture, position_index, copy):

    locator_key = f"{culture} grid item copy"

    item = context.current_page.get_culture_grid_items_at_index(locator_key, int(position_index))
    item_copy = item.text
    assert copy in item_copy, f"Expected copy at position {position_index} to be {copy} but found {item_copy}"   

@when(u'the {section} image grid is displayed')
def step_impl(context, section):
    locator_key = f"{section} image grid"
    
    is_visible = context.current_page.is_element_displayed(locator_key)
    
    assert is_visible, f"{section} image grid was not visible"

@then(u'the {section} image grid has at least {min_items} items')
def step_impl(context, section, min_items):
    locator_key = f"{section} image grid"

    grid_items = context.current_page.get_section_grid_items(locator_key)
    grid_item_length = len(grid_items)
    min_items = int(min_items)
    assert grid_item_length == min_items, f"Expected {min_items} items in the grid but found {grid_item_length}"


@then(u'the "{section}" has at least {min_items} items')
def step_impl(context, section, min_items):
    locator_key = f"{section} items"

    grid_items = context.current_page.get_section_grid_items(locator_key)
    grid_item_length = len(grid_items)
    min_items = int(min_items)
    assert grid_item_length == min_items, f"Expected {min_items} items in the grid but found {grid_item_length}"


@then(u'each testimonial card has non-empty quote text')
def step_impl(context):
    locator_key = "testimonials copy"

    testimonials_copy = context.current_page.get_elements(locator_key)
    
    text = " ".join(
                p.text.strip() for p in testimonials_copy if p.text.strip()
            )

    assert text != "", f"Card has empty quote text"

@then(u'each testimonial card has at least one attribution field present (name or business)')
def step_impl(context):
    testimonial_name_locator_key = "testimonials name"
    testimonial_business_locator_key = "testimonials business"

    name_elements = context.current_page.get_elements(testimonial_name_locator_key)
    business_elements = context.current_page.get_elements(testimonial_business_locator_key)

    max_len = max(len(name_elements), len(business_elements))

    for i in range(max_len):
        name = name_elements[i].text.strip() if i < len(name_elements) and name_elements[i].text.strip() else ""
        business = business_elements[i].text.strip() if i < len(business_elements) and business_elements[i].text.strip() else ""

        assert (name or business), f"Card {i} has no attribution (name or business)"

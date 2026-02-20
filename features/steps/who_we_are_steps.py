from behave import *
from pages.who_we_are import WhoWeAre

# ---------------------------------------------------------------------------
# HERO SECTION
# ---------------------------------------------------------------------------

@given(u'the user navigates to "{path}"')
def step_impl(context, path):
    context.current_page = WhoWeAre(context.driver)
    context.current_page.navigate_to_url(path)

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
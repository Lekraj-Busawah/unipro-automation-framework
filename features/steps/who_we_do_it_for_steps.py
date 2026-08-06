from behave import *

# ---------------------------------------------------------------------------
# SECTOR EXPERTISE SECTION
# ---------------------------------------------------------------------------

@then(u'the "{section}" list item at position "{position}" has number "{number}"')
def step_impl(context, section, position, number):
    locator = f"{section} list number"
    list_item = context.current_page.get_section_list_item_at_position(locator, int(position))
    actual_number = list_item.text.strip()
    assert actual_number == number, f"Expected number '{number}' at position {position}, but found '{actual_number}'"

    
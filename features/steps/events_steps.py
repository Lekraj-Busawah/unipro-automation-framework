from behave import *

# ---------------------------------------------------------------------------
# JOIN US / EVENT LISTINGS
# ---------------------------------------------------------------------------

@then(u'the {list_name} has at least "{minimum_count}" items')
def step_impl(context, list_name, minimum_count):
    list_items = context.current_page.get_section_list_items(list_name)
    actual_count = len(list_items)
    assert actual_count >= int(minimum_count), f"Expected at least {minimum_count} items in the '{list_name}' list, but found {actual_count}"
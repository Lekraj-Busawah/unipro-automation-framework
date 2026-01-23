from behave import *
from pages.footer import Footer
import time

@given(u'the user is viewing any public page on the website')
def step_impl(context):
    context.driver.get(context.base_url)

    # create a new instance of the Footer page object and save it into context
    context.footer = Footer(context.driver)

    context.footer.handle_cookie_consent()

@given(u'the footer container is visible')
def step_impl(context):
    context.footer.scroll_to_footer()
    assert context.footer.is_footer_visible(), "Footer not found"


@then(u'the footer displays the company logo')
def step_impl(context):
    assert context.footer.is_logo_displayed(), "Unipro logo is not visible"


@then(u'the footer displays the company tagline "{expected_tagline}"')
def step_impl(context, expected_tagline):
    actual_text = context.footer.get_tagline_text()

    assert actual_text == expected_tagline, f"Expected '{expected_tagline}', but found '{actual_text}'"


@when(u'the user clicks the company logo')
def step_impl(context):
    context.footer.click_company_logo()
    

@then(u'the user is navigated to the homepage')
def step_impl(context):
    assert context.footer.wait_for_url_to_be(context.base_url), "Unable to navigate to homepage"


@then(u'the footer contains a contact email link')
def step_impl(context):
    email_element = context.footer.get_footer_email()

    assert email_element, "Email link was not found in the footer"

@then(u'the email address is "{expected_email}"')
def step_impl(context, expected_email):
    email_element = context.footer.get_footer_email()

    actual_email_text = email_element.text

    assert (actual_email_text == expected_email), f"Expected {expected_email} but found {actual_email_text}"


@then(u'the footer displays the London office section')
def step_impl(context):
    london_office_section = context.footer.get_london_office_section()
    assert london_office_section, "London Office section not found in the footer"


@then(u'the footer displays the Havant office section')
def step_impl(context):
    havant_office_section = context.footer.get_havant_office_section()
    assert havant_office_section, "havant Office section not found in the footer"


@then(u'the "{office}" address displays "{street}", "{city}", "{postcode}" and "{phone}"')
def step_impl(context, office, street, city, postcode, phone):
    raw_address_text = (context.footer.get_office_details(office)).text

    flat_address = raw_address_text.replace("\n", " ")

    assert street in flat_address, f"Expected street '{street}' not found in '{flat_address}'"
    assert city in flat_address, f"Expected city '{city}' not found"
    assert postcode in flat_address, f"Expected postcode '{postcode}' not found"
    assert phone in flat_address, f"Expected phone '{phone}' not found"
    

@then(u'the "{social}" link is visible in the footer')
def step_impl(context, social):
    assert context.footer.get_social_link(social), f"{social} link not found"


@then(u'the "{social}" link opens in a new browser tab')
def step_impl(context, social):
    context.footer.click_social_link(social)
    
    actual_title = context.footer.check_title_in_new_tab()
    
    assert social in actual_title, f"Expected title '{social}' not found in '{actual_title}'"


@when(u'the user clicks the "{policy}" link in the footer')
def step_impl(context, policy):
    context.footer.click_policy_link(policy)


@then(u'the user is navigated to the "{policy}" page')
def step_impl(context, policy):
    title = context.footer.get_title(expected_text=policy)
    print(title)

    assert policy in title, f"Expected '{policy}' in title but found in '{title}'"
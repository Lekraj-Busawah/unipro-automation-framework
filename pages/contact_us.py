from selenium.webdriver.common.by import By
from .base_page import BasePage


class ContactUs(BasePage):
    # ---------------------------------------------------------------------------
    # LOCATORS
    # ---------------------------------------------------------------------------

    locators = {

        # Sections
        "hero": (By.CSS_SELECTOR, ".hero-block"),
        "get in touch": (By.CSS_SELECTOR, ".general-grid-block"),
        "contact form": (By.CSS_SELECTOR, "[data-hs-forms-root='true']"),
    }
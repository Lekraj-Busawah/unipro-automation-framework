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

        # Hero section
        "hero eyebrow": (By.CSS_SELECTOR, ".hero-block .typography .eyebrow"),
        "hero heading": (By.CSS_SELECTOR, ".hero-block .typography h2"),
        "hero intro text": (By.CSS_SELECTOR, ".hero-block .intro-feature-text p"),
        "hero desktop image": (By.CSS_SELECTOR, ".hero-block__image.hide-mobile"),
        "hero mobile image": (By.CSS_SELECTOR, ".hero-block__image.hide-desktop"),

    }
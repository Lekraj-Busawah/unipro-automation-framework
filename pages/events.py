from selenium.webdriver.common.by import By
from .base_page import BasePage


class Events(BasePage):
    # ---------------------------------------------------------------------------
    # LOCATORS
    # ---------------------------------------------------------------------------

    locators = {

        # Sections
        "hero": (By.CSS_SELECTOR, ".hero-block"),
        "join us": (By.CSS_SELECTOR, ".content-block"),     

       # Hero section
        "hero heading": (By.CSS_SELECTOR, ".hero-block .typography h1"),
        "hero desktop image": (By.CSS_SELECTOR, ".hero-block__image.hide-mobile"),
        "hero mobile image": (By.CSS_SELECTOR, ".hero-block__image.hide-desktop"),

        # Join us / event listings
        "join us heading": (By.CSS_SELECTOR, ".content-block__typography > .typography h2"),
        "exhibiting at label": (By.CSS_SELECTOR, ".content-block__typography > .columned-text p:nth-of-type(1)"),
        "attending label": (By.CSS_SELECTOR, ".content-block__typography > .columned-text p:nth-of-type(3)"),
    }
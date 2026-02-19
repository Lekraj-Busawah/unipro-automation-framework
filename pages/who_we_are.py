from .base_page import BasePage
from selenium.webdriver.common.by import By


class WhoWeAre(BasePage):
    # ---------------------------------------------------------------------------
    # LOCATORS
    # ---------------------------------------------------------------------------
    locators = {
        # Containers / Sections
        "hero section": (By.CSS_SELECTOR, ".hero-block.block"),
        "who eyebrow text": (By.XPATH , "//p[normalize-space()='WHO WE ARE']"),
        "who heading": (By.CSS_SELECTOR , "div[class='typography'] h1"),
        "who intro text block": (By.XPATH , "//p[contains(text(),'We are a team of inquisitive software specialists ')]"),

        # Hero images
        "desktop hero image": (By.CSS_SELECTOR, ".hero-block__image.hide-mobile"),
        "mobile hero image": (By.CSS_SELECTOR, ".hero-block__image.hide-desktop"),

        # Team block
        "team": (By.CSS_SELECTOR, "#team"),
        "team eyebrow text": (By.CSS_SELECTOR, "div[class='content-block__typography'] p[class='eyebrow']"),
        "team heading": (By.CSS_SELECTOR, "div[class='content-block__typography'] h2"),
        "team intro text block": (By.CSS_SELECTOR, "div[class='content-block__typography'] div[class='intro-feature-text'] p"),
        "team desktop image": (By.CSS_SELECTOR, "img[alt='Unipro Team']"),

    }

    # ---------------------------------------------------------------------------
    # ACTIONS
    # ---------------------------------------------------------------------------
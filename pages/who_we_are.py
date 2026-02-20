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

        # Culture block
        "culture": (By.CSS_SELECTOR, "#culture"),
        "culture eyebrow text": (By.CSS_SELECTOR, "div[id='culture'] p[class='eyebrow']"),
        "culture heading": (By.CSS_SELECTOR, "div[id='culture'] h2"),
        "culture intro text block": (By.CSS_SELECTOR, "div[id='culture'] div[class='intro-feature-text'] p"),
        "culture grid": (By.CSS_SELECTOR, ".text-grid-block__content"),
        "culture grid item": (By.CSS_SELECTOR, ".text-grid-block__item"),
        "culture grid item title": (By.CSS_SELECTOR, ".text-grid-block__item-title"),
        "culture grid item copy": (By.CSS_SELECTOR, ".text-grid-block__item-copy"),
    }

    # ---------------------------------------------------------------------------
    # ACTIONS
    # ---------------------------------------------------------------------------

    def get_culture_grid_items(self, locator):
        return self.get_elements(locator)
    
    def get_culture_grid_items_at_index(self, locator, position):
        items = self.get_elements(locator)
        item = items[position - 1]
        return item